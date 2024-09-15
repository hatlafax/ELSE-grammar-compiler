from PreProcessListener import PreProcessListener
import re
from enum import Enum
from typing import TypeVar, Generic, List
from ANTLRv4Parser import ANTLRv4Parser

from ProcessListenerBase import ProcessListenerBase, Stack
from ElseTemplateGenerator import ElsePlaceholder

class ProcessListener(ProcessListenerBase):
    """Process the AST.
    """

    #patternRuleSpec = re.compile(r'^\s*(?:public|private|protected|fragment)?([A-Za-z0-9_-]+)\s*:.*$')
    patternRuleSpec = re.compile(r'^\s*(?:public|private|protected|fragment)?([A-Za-z0-9_-]+)(?:(?:annotations\(|locals\[|throws|returns)\s*[^:]+)?\s*:.*$')
    patternSeparator = re.compile(r'^([,;|:]\s*).*$')
    patternMenuPlaceHolder = re.compile(r'^(:?\{.*\}|\[.*\])$')

    def __init__(self, options, output, language) -> None:
        super().__init__(options.print_tokens, options.verbose)

        self._options = options

        self._output = output
        self._language = language

        self._isParserRuleSpec = False

        self._parserRule = None
        self._annotationKey = None

        self._stack_placeholders: Stack[str] = Stack()
        self._stack_alternatives: Stack[List[str]] = Stack()
        self._stack_elements: Stack[List[str]] = Stack()

        self._set_placeholders: Set[str] = set()
        self._dict_placeholders = dict()

        self._dict_placeholders_substitute_type  : dict[str, str] = dict()
        self._dict_placeholders_substitute_count : dict[str, str] = dict()
        self._dict_placeholders_description      : dict[str, str] = dict()
        self._dict_placeholders_duplication_type : dict[str, str] = dict()
        self._dict_placeholders_separators       : dict[str, str] = dict()

    #
    # Helper functions
    #

    def processSuffix(self, ref, suffix) -> str:
        result = ""

        if self._options.read_placeholders:
            if ref in self._options.placeholders_map:
                ref = self._options.placeholders_map[ref]

        if suffix:
            if suffix.getText() == '?':
                result = '[' + ref + ']'
            if suffix.getText() == '*':
                result = '[' + ref + ']...'
            if suffix.getText() == '+':
                result = '{' + ref + '}...'
        else:
            result = '{' + ref + '}'
        return result

    def processAtom(self, atom, suffix) -> str:
        result = ""
        if atom.terminal():
            terminal = atom.terminal().getText()

            if terminal == self._options.indentation_token:
                result = "indentation-token"
            elif terminal == self._options.dedentation_token:
                result = "dedentation-token"
            elif terminal == self._options.newline_token:
                result = "newline-token"
            elif terminal in self._options.quotedLexerRuleSpec:
                terminal = self._options.quotedLexerRuleSpec[terminal]
                result = terminal[1:-1]
            elif terminal in self._options.unquotedLexerRuleSpec:
                self._dict_placeholders[terminal] = None
                result = self.processSuffix(terminal, suffix)
            elif terminal in self._options.quotedTerminals:
                result = terminal[1:-1]
        elif atom.ruleref():
            ruleref = atom.ruleref().getText()
            result = self.processSuffix(ruleref, suffix)
        return result

    def processElements(self, elements) -> str:
        result = ""
        separator = elements.terminal().getText()
        if len(separator) >= 3:
            separator = separator[1:-1]
        ruleref = None
        if elements.atom():
            atom = elements.atom()
            if atom.terminal():
                terminal = atom.terminal().getText()

                if terminal in self._options.unquotedLexerRuleSpec:
                    self._dict_placeholders[terminal] = None
                    ruleref = terminal

            elif atom.ruleref():
                ruleref = atom.ruleref().getText()

        elif elements.block():
            ruleref = elements.block().getText()

        if ruleref is not None:
            if ruleref not in self._dict_placeholders_separators:
                self._dict_placeholders_separators[ruleref] = separator

            result = '{' + ruleref + '}...'

        return result

    def processEbnf(self, ebnf) -> str:
        result = ""
        if ebnf.block():
            result = self.processBlock(ebnf.block(), ebnf.blockSuffix())
        return result

    def processBlock(self, block, suffix) -> str:
        result = ""
        if block:
            ruleref = block.getText()
            result = self.processSuffix(ruleref, suffix)
        return result

    #
    # ELSE placeholder generation
    #

    def createElseTerminalPlaceholder(self, placeholder_name, content = None) -> None:
        if placeholder_name not in self._set_placeholders:
            self._set_placeholders.add(placeholder_name)
            self._options.placeholders.append(placeholder_name)

            separator        = self._dict_placeholders_separators.get(placeholder_name,       "")
            substitute_count = self._dict_placeholders_substitute_count.get(placeholder_name, 1)
            description      = self._dict_placeholders_description.get(placeholder_name,      "")
            duplication_type = self._dict_placeholders_duplication_type.get(placeholder_name, ElsePlaceholder.DuplicationType.CONTEXT_DEPENDENT)
            substitute_type  = self._dict_placeholders_substitute_type.get(placeholder_name,  ElsePlaceholder.SubstituteType.NOAUTO_SUBSTITUTE)

            if self._options.read_placeholders:
                if placeholder_name in self._options.placeholders_map:
                    placeholder_name = self._options.placeholders_map[placeholder_name]

            placeholder: ElsePlaceholder = ElsePlaceholder(self._output, self._language)
            placeholder.set_placeholder_name(placeholder_name)
            placeholder.set_placeholder_type(ElsePlaceholder.PlaceHolderType.TERMINAL)

            if content is not None and content.startswith("<<<") and content.endswith(">>>"):
              content = content.strip('<>')
              placeholder.set_content(content)
            else:
              placeholder.set_content(f"Enter a valid {placeholder_name} terminal.")

            placeholder.set_separator       (separator)
            placeholder.set_substitute_type (substitute_type)
            placeholder.set_substitute_count(substitute_count)
            placeholder.set_description     (description)
            placeholder.set_duplication_type(duplication_type)

            placeholder.write()

            self.log(f"createElseTerminalPlaceholder -> {placeholder_name}", indentation = 2)

    def createElseNonTerminalPlaceholder(self, placeholder_name, content) -> None:
        if placeholder_name not in self._set_placeholders:
            self._set_placeholders.add(placeholder_name)
            self._options.placeholders.append(placeholder_name)

            separator        = self._dict_placeholders_separators.get(placeholder_name,       "")
            substitute_count = self._dict_placeholders_substitute_count.get(placeholder_name, 1)
            description      = self._dict_placeholders_description.get(placeholder_name,      "")
            duplication_type = self._dict_placeholders_duplication_type.get(placeholder_name, ElsePlaceholder.DuplicationType.CONTEXT_DEPENDENT)
            substitute_type  = self._dict_placeholders_substitute_type.get(placeholder_name,  ElsePlaceholder.SubstituteType.NOAUTO_SUBSTITUTE)

            indentation = self._options.indentation * " "

            lines = re.split(r'\s*newline-token\s*', content)

            content = ""
            for idx, line in enumerate(lines):
                line = re.sub(r'\s*indentation-token\s*', indentation, line)
                if idx == 0:
                    content += line
                else:
                    content += "\n" + line

            if self._options.read_placeholders:
                if placeholder_name in self._options.placeholders_map:
                    placeholder_name = self._options.placeholders_map[placeholder_name]

            placeholder: ElsePlaceholder = ElsePlaceholder(self._output, self._language)
            placeholder.set_placeholder_name(placeholder_name)
            placeholder.set_placeholder_type(ElsePlaceholder.PlaceHolderType.NONTERMINAL)
            placeholder.set_content(content)

            if len(separator) == 0:
                m = ProcessListener.patternSeparator.match(content)
                if m and len(separator) == 0:
                    separator = m.group(1)
                    if len(separator) == 1:
                        separator += " "

            placeholder.set_separator       (separator)
            placeholder.set_substitute_type (substitute_type)
            placeholder.set_substitute_count(substitute_count)
            placeholder.set_description     (description)
            placeholder.set_duplication_type(duplication_type)

            placeholder.write()

            self.log(f"createElseNonTerminalPlaceholder -> {placeholder_name} -> {content}", indentation = 2)

    def createElseMenuPlaceholder(self, placeholder_name, alternatives) -> None:
        if placeholder_name not in self._set_placeholders:
            self._set_placeholders.add(placeholder_name)
            self._options.placeholders.append(placeholder_name)

            separator        = self._dict_placeholders_separators.get(placeholder_name,       "")
            substitute_count = self._dict_placeholders_substitute_count.get(placeholder_name, 1)
            description      = self._dict_placeholders_description.get(placeholder_name,      "")
            duplication_type = self._dict_placeholders_duplication_type.get(placeholder_name, ElsePlaceholder.DuplicationType.CONTEXT_DEPENDENT)
            substitute_type  = self._dict_placeholders_substitute_type.get(placeholder_name,  ElsePlaceholder.SubstituteType.NOAUTO_SUBSTITUTE)

            if self._options.read_placeholders:
                if placeholder_name in self._options.placeholders_map:
                    placeholder_name = self._options.placeholders_map[placeholder_name]

            placeholder: ElsePlaceholder = ElsePlaceholder(self._output, self._language)
            placeholder.set_placeholder_name(placeholder_name)
            placeholder.set_placeholder_type(ElsePlaceholder.PlaceHolderType.MENU)

            content = ""
            for idx in range(len(alternatives)):
                alternative = alternatives[idx]

                m = ProcessListener.patternMenuPlaceHolder.match(alternative)
                if m and alternative[1:-1] in self._options.placeholders_set:
                    alternative = alternative[1:-1]
                    placeholder.add_placeholder_attribute(alternative, ElsePlaceholder.PlaceHolderMenuAttribute.PLACEHOLDER)

                if idx == 0:
                    content += alternative
                else:
                    content += "\n" + alternative

            placeholder.set_content         (content)
            placeholder.set_separator       (separator)
            placeholder.set_substitute_type (substitute_type)
            placeholder.set_substitute_count(substitute_count)
            placeholder.set_description     (description)
            placeholder.set_duplication_type(duplication_type)

            placeholder.write()

            self.log(f"createElseMenuPlaceholder -> {placeholder_name} ->", indentation = 2)
            for entry in re.split(r',\s*\n|[\n]', content):
                self.log(f"{entry}", indentation = 3)

    #
    # Antlr listener APIs
    #

    # Enter a parse tree produced by ANTLRv4Parser#parserRuleSpec.
    def enterParserRuleSpec(self, ctx:ANTLRv4Parser.ParserRuleSpecContext):
        super().enterParserRuleSpec(ctx)
        m = ProcessListener.patternRuleSpec.match(ctx.getText())
        if m:
            self._parserRule = m.group(1)
            self._isParserRuleSpec = True

    # Exit a parse tree produced by ANTLRv4Parser#parserRuleSpec.
    def exitParserRuleSpec(self, ctx:ANTLRv4Parser.ParserRuleSpecContext):
        super().exitParserRuleSpec(ctx)
        if self._isParserRuleSpec:
            self._parserRule = None
            self._isParserRuleSpec = False


    # Enter a parse tree produced by ANTLRv4Parser#annotationsSpec.
    def enterAnnotationsSpec(self, ctx:ANTLRv4Parser.AnnotationsSpecContext):
        super().enterAnnotationsSpec(ctx)

    # Exit a parse tree produced by ANTLRv4Parser#annotationsSpec.
    def exitAnnotationsSpec(self, ctx:ANTLRv4Parser.AnnotationsSpecContext):
        super().exitAnnotationsSpec(ctx)

    # Enter a parse tree produced by ANTLRv4Parser#annotationBlockSeq.
    def enterAnnotationBlockSeq(self, ctx:ANTLRv4Parser.AnnotationBlockSeqContext):
        super().enterAnnotationBlockSeq(ctx)

    # Exit a parse tree produced by ANTLRv4Parser#annotationBlockSeq.
    def exitAnnotationBlockSeq(self, ctx:ANTLRv4Parser.AnnotationBlockSeqContext):
        super().exitAnnotationBlockSeq(ctx)

    # Enter a parse tree produced by ANTLRv4Parser#annotationBlock.
    def enterAnnotationBlock(self, ctx:ANTLRv4Parser.AnnotationBlockContext):
        super().enterAnnotationBlock(ctx)

    # Exit a parse tree produced by ANTLRv4Parser#annotationBlock.
    def exitAnnotationBlock(self, ctx:ANTLRv4Parser.AnnotationBlockContext):
        super().exitAnnotationBlock(ctx)

    # Enter a parse tree produced by ANTLRv4Parser#annotationKey.
    def enterAnnotationKey(self, ctx:ANTLRv4Parser.AnnotationKeyContext):
        super().enterAnnotationKey(ctx)
        self._annotationKey = ctx.getText()

    # Exit a parse tree produced by ANTLRv4Parser#annotationKey.
    def exitAnnotationKey(self, ctx:ANTLRv4Parser.AnnotationKeyContext):
        super().exitAnnotationKey(ctx)

    # Enter a parse tree produced by ANTLRv4Parser#annotationValue.
    def enterAnnotationValue(self, ctx:ANTLRv4Parser.AnnotationValueContext):
        super().enterAnnotationValue(ctx)

        if   self._annotationKey.lower() == 'separator':
            separator = ctx.getText()[1:-1]
            self._dict_placeholders_separators[self._parserRule] = separator

        elif self._annotationKey.lower() == 'substitute-count' or self._annotationKey.lower() == 'substitute_count':
            substitute_count = int(ctx.getText()[1:-1])
            self._dict_placeholders_substitute_count[self._parserRule] = substitute_count

        elif self._annotationKey.lower() == 'description':
            description = ctx.getText()[1:-1]
            self._dict_placeholders_description[self._parserRule] = description

        elif self._annotationKey.lower() == 'duplication':
            duplication_type = ctx.getText()[1:-1].lower()
            if   duplication_type == 'context-dependent' or 'context_dependent' or duplication_type == 'context':
                duplication_type = ElsePlaceholder.DuplicationType.CONTEXT_DEPENDENT
            elif duplication_type == 'vertical':
                duplication_type = ElsePlaceholder.DuplicationType.VERTICAL
            elif duplication_type == 'horizontal':
                duplication_type = ElsePlaceholder.DuplicationType.HORIZONTAL
            else:
                duplication_type = ElsePlaceholder.DuplicationType.CONTEXT_DEPENDENT
            self._dict_placeholders_duplication_type[self._parserRule] = duplication_type

        elif self._annotationKey.lower() == 'substitute-type' or self._annotationKey.lower() == 'substitute_type':
            substitute_type = ctx.getText()[1:-1].lower()
            if substitute_type == 'auto':
                substitute_type = ElsePlaceholder.SubstituteType.AUTO_SUBSTITUTE
            else:
                substitute_type = ElsePlaceholder.SubstituteType.NOAUTO_SUBSTITUTE
            self._dict_placeholders_substitute_type[self._parserRule] = substitute_type

        elif self._annotationKey.lower() == 'auto-substitute' or self._annotationKey.lower() == 'auto_substitute':
            auto_substitute = ctx.getText()[1:-1].lower()
            if auto_substitute == '1' or auto_substitute == 'true' or auto_substitute == 'on' or auto_substitute == 'yes':
                substitute_type = ElsePlaceholder.SubstituteType.AUTO_SUBSTITUTE
            else:
                substitute_type = ElsePlaceholder.SubstituteType.NOAUTO_SUBSTITUTE
            self._dict_placeholders_substitute_type[self._parserRule] = substitute_type


    # Exit a parse tree produced by ANTLRv4Parser#annotationValue.
    def exitAnnotationValue(self, ctx:ANTLRv4Parser.AnnotationValueContext):
        super().exitAnnotationValue(ctx)
        self._annotationKey = None

    # Enter a parse tree produced by ANTLRv4Parser#ruleBlock.
    def enterRuleBlock(self, ctx:ANTLRv4Parser.RuleBlockContext):
        super().enterRuleBlock(ctx)
        if self._isParserRuleSpec:
            self._stack_alternatives.push([])
            self._stack_placeholders.push(self._parserRule)

    # Exit a parse tree produced by ANTLRv4Parser#ruleBlock.
    def exitRuleBlock(self, ctx:ANTLRv4Parser.RuleBlockContext):
        super().exitRuleBlock(ctx)
        if self._isParserRuleSpec:
            if not self._stack_alternatives.empty and not self._stack_placeholders.empty:
                alternatives = self._stack_alternatives.pop()
                placeholder_name = self._stack_placeholders.pop()

                if len(alternatives) == 1:
                    self._dict_placeholders[placeholder_name] = alternatives[0]
                elif len(alternatives) > 1:
                    self._dict_placeholders[placeholder_name] = alternatives

    # Enter a parse tree produced by ANTLRv4Parser#ruleAltList.
    def enterRuleAltList(self, ctx:ANTLRv4Parser.RuleAltListContext):
        super().enterRuleAltList(ctx)

    # Exit a parse tree produced by ANTLRv4Parser#ruleAltList.
    def exitRuleAltList(self, ctx:ANTLRv4Parser.RuleAltListContext):
        super().exitRuleAltList(ctx)


    # Enter a parse tree produced by ANTLRv4Parser#labeledAlt.
    def enterLabeledAlt(self, ctx:ANTLRv4Parser.LabeledAltContext):
        super().enterLabeledAlt(ctx)

    # Exit a parse tree produced by ANTLRv4Parser#labeledAlt.
    def exitLabeledAlt(self, ctx:ANTLRv4Parser.LabeledAltContext):
        super().exitLabeledAlt(ctx)


    # Enter a parse tree produced by ANTLRv4Parser#lexerRuleSpec.
    def enterLexerRuleSpec(self, ctx:ANTLRv4Parser.LexerRuleSpecContext):
        super().enterLexerRuleSpec(ctx)

    # Exit a parse tree produced by ANTLRv4Parser#lexerRuleSpec.
    def exitLexerRuleSpec(self, ctx:ANTLRv4Parser.LexerRuleSpecContext):
        super().enterLexerRuleSpec(ctx)


    # Enter a parse tree produced by ANTLRv4Parser#altList.
    def enterAltList(self, ctx:ANTLRv4Parser.AltListContext):
        super().enterAltList(ctx)

    # Exit a parse tree produced by ANTLRv4Parser#altList.
    def exitAltList(self, ctx:ANTLRv4Parser.AltListContext):
        super().exitAltList(ctx)


    # Enter a parse tree produced by ANTLRv4Parser#alternative.
    def enterAlternative(self, ctx:ANTLRv4Parser.AlternativeContext):
        super().enterAlternative(ctx)
        if self._isParserRuleSpec:
            self._stack_elements.push([])

    # Exit a parse tree produced by ANTLRv4Parser#alternative.
    def exitAlternative(self, ctx:ANTLRv4Parser.AlternativeContext):
        super().exitAlternative(ctx)
        if self._isParserRuleSpec:
            elements = self._stack_elements.pop()

            self.log(f"elements -> {elements}")

            alternative = ""
            for element in elements:
                element = element.strip()

                le = len(element)
                la = len(alternative)

                #print(element)
                #print(alternative)

                non_space_sep = self._options.non_space_separated_map

                if le > 0:                      # anything to do
                    if la == 0:                  # first element
                        alternative = element
                    else:
                        found = False

                        for lhs, rhs_list in non_space_sep.items():
                            rhs_str = ''.join(rhs_list)
                            if alternative.endswith(lhs) and rhs_str == '<any>':
                                found = True
                            elif alternative.endswith(lhs) and element == rhs_str:
                                found = True
                            elif lhs.startswith('regex:'):
                                lhs_regex = lhs[6:] + '$'
                                m = re.search(lhs_regex, alternative)
                                if m:
                                    if element == str(rhs_list):
                                        found = True
                                    else:
                                        for rhs in rhs_list:
                                            if element.startswith(rhs):
                                                found = True
                            elif alternative.endswith(lhs):
                                for rhs in rhs_list:
                                    if element.startswith(rhs):
                                        found = True

                        if found:
                            alternative += element
                            print(alternative)
                        else:
                            alternative += " " + element

            self.log(f"alternative -> {alternative}", indentation = 2)

            if len(alternative) > 0:
                self._stack_alternatives.top().append(alternative)


    # Enter a parse tree produced by ANTLRv4Parser#element.
    def enterElement(self, ctx:ANTLRv4Parser.ElementContext):
        super().enterElement(ctx)
        if self._isParserRuleSpec:
            element = ""

            if ctx.labeledElement():
                if ctx.labeledElement().atom():
                    element = self.processAtom(ctx.labeledElement().atom(), ctx.ebnfSuffix())
                elif ctx.labeledElement().block():
                    element = self.processBlock(ctx.labeledElement().block(), ctx.ebnfSuffix())

            elif ctx.elements():
                element = self.processElements(ctx.elements())

            elif ctx.atom():
                element = self.processAtom(ctx.atom(), ctx.ebnfSuffix())

            elif ctx.ebnf():
                element = self.processEbnf(ctx.ebnf())

            self.log(f"element -> {element}", indentation = 1)

            self._stack_elements.top().append(element)

    # Exit a parse tree produced by ANTLRv4Parser#element.
    def exitElement(self, ctx:ANTLRv4Parser.ElementContext):
        super().exitElement(ctx)


    def enterElements(self, ctx:ANTLRv4Parser.ElementsContext):
        super().enterElements(ctx)

    # Exit a parse tree produced by ANTLRv4Parser#elements.
    def exitElements(self, ctx:ANTLRv4Parser.ElementsContext):
        super().exitElements(ctx)


    # Enter a parse tree produced by ANTLRv4Parser#labeledElement.
    def enterLabeledElement(self, ctx:ANTLRv4Parser.LabeledElementContext):
        super().enterLabeledElement(ctx)

    # Exit a parse tree produced by ANTLRv4Parser#labeledElement.
    def exitLabeledElement(self, ctx:ANTLRv4Parser.LabeledElementContext):
        super().exitLabeledElement(ctx)


    # Enter a parse tree produced by ANTLRv4Parser#ebnf.
    def enterEbnf(self, ctx:ANTLRv4Parser.EbnfContext):
        super().enterEbnf(ctx)

    # Exit a parse tree produced by ANTLRv4Parser#ebnf.
    def exitEbnf(self, ctx:ANTLRv4Parser.EbnfContext):
        super().exitEbnf(ctx)


    # Enter a parse tree produced by ANTLRv4Parser#blockSuffix.
    def enterBlockSuffix(self, ctx:ANTLRv4Parser.BlockSuffixContext):
        super().enterBlockSuffix(ctx)

    # Exit a parse tree produced by ANTLRv4Parser#blockSuffix.
    def exitBlockSuffix(self, ctx:ANTLRv4Parser.BlockSuffixContext):
        super().exitBlockSuffix(ctx)


    # Enter a parse tree produced by ANTLRv4Parser#ebnfSuffix.
    def enterEbnfSuffix(self, ctx:ANTLRv4Parser.EbnfSuffixContext):
        super().enterEbnfSuffix(ctx)

    # Exit a parse tree produced by ANTLRv4Parser#ebnfSuffix.
    def exitEbnfSuffix(self, ctx:ANTLRv4Parser.EbnfSuffixContext):
        super().exitEbnfSuffix(ctx)


    # Enter a parse tree produced by ANTLRv4Parser#atom.
    def enterAtom(self, ctx:ANTLRv4Parser.AtomContext):
        super().enterAtom(ctx)

    # Exit a parse tree produced by ANTLRv4Parser#atom.
    def exitAtom(self, ctx:ANTLRv4Parser.AtomContext):
        super().exitAtom(ctx)


    # Enter a parse tree produced by ANTLRv4Parser#block.
    def enterBlock(self, ctx:ANTLRv4Parser.BlockContext):
        super().enterBlock(ctx)
        if self._isParserRuleSpec:
            self._stack_alternatives.push([])
            self._stack_placeholders.push(ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#block.
    def exitBlock(self, ctx:ANTLRv4Parser.BlockContext):
        super().exitBlock(ctx)
        if self._isParserRuleSpec:
            if not self._stack_alternatives.empty and not self._stack_placeholders.empty:
                alternatives = self._stack_alternatives.pop()
                placeholder_name = self._stack_placeholders.pop()

                if len(alternatives) == 1:
                    self._dict_placeholders[placeholder_name] = alternatives[0]
                elif len(alternatives) > 1:
                    self._dict_placeholders[placeholder_name] = alternatives


    # Enter a parse tree produced by ANTLRv4Parser#ruleref.
    def enterRuleref(self, ctx:ANTLRv4Parser.RulerefContext):
        super().enterRuleref(ctx)

    # Exit a parse tree produced by ANTLRv4Parser#ruleref.
    def exitRuleref(self, ctx:ANTLRv4Parser.RulerefContext):
        super().exitRuleref(ctx)


    # Enter a parse tree produced by ANTLRv4Parser#terminal.
    def enterTerminal(self, ctx:ANTLRv4Parser.TerminalContext):
        super().enterTerminal(ctx)

    # Exit a parse tree produced by ANTLRv4Parser#terminal.
    def exitTerminal(self, ctx:ANTLRv4Parser.TerminalContext):
        super().exitTerminal(ctx)


    def write_else_template(self, print_placeholders) -> None:

        if print_placeholders:
          for p, s in self._dict_placeholders_separators.items():
              print(f"{p} -> {s}")

          for placeholder_name, content in self._dict_placeholders.items():
              print(f"placeholder_name: {placeholder_name}")

        for placeholder_name, content in self._dict_placeholders.items():
            if content is not None and isinstance(content, str) and content.startswith("<<<") and content.endswith(">>>"):
                self.createElseTerminalPlaceholder(placeholder_name, content)
            elif content is None:
                self.createElseTerminalPlaceholder(placeholder_name)
            elif isinstance(content, str):
                self.createElseNonTerminalPlaceholder(placeholder_name, content)
            elif isinstance(content, list):
                self.createElseMenuPlaceholder(placeholder_name, content)
