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

    patternRuleSpec = re.compile(r'^\s*(?:public|private|protected|fragment)?([A-Za-z0-9_]+)\s*:.*$')
    patternSeparator = re.compile(r'^([,;|:]\s*).*$')
    patternMenuPlaceHolder = re.compile(r'^(:?\{.*\}|\[.*\])$')

    def __init__(self, options, output, language) -> None:
        super().__init__(options.print_tokens, options.verbose)

        self._options = options

        self._output = output
        self._language = language

        self._isParserRuleSpec = False

        self._parserRule = None

        self._stack_placeholders: Stack[str] = Stack()
        self._stack_alternatives: Stack[List[str]] = Stack()
        self._stack_elements: Stack[List[str]] = Stack()

        self._set_placeholders: Set[str] = set()
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
                self.createElseTerminalPlaceholder(terminal)
                result = self.processSuffix(terminal, suffix)
            elif terminal in self._options.quotedTerminals:
                result = terminal[1:-1]
        elif atom.ruleref():
            ruleref = atom.ruleref().getText()
            result = self.processSuffix(ruleref, suffix)
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

    def createElseTerminalPlaceholder(self, placeholder_name) -> None:
        if placeholder_name not in self._set_placeholders:
            self._set_placeholders.add(placeholder_name)
            self._options.placeholders.append(placeholder_name)

            if self._options.read_placeholders:
                if placeholder_name in self._options.placeholders_map:
                    placeholder_name = self._options.placeholders_map[placeholder_name]

            placeholder: ElsePlaceholder = ElsePlaceholder(self._output, self._language)
            placeholder.set_placeholder_name(placeholder_name)
            placeholder.set_placeholder_type(ElsePlaceholder.PlaceHolderType.TERMINAL)
            placeholder.set_content(f"Enter a valid {placeholder_name} terminal.")
            placeholder.write()

            self.log(f"createElseTerminalPlaceholder -> {placeholder_name}", indentation = 2)

    def createElseNonTerminalPlaceholder(self, placeholder_name, content) -> None:
        if placeholder_name not in self._set_placeholders:
            self._set_placeholders.add(placeholder_name)
            self._options.placeholders.append(placeholder_name)

            if self._options.read_placeholders:
                if placeholder_name in self._options.placeholders_map:
                    placeholder_name = self._options.placeholders_map[placeholder_name]

            placeholder: ElsePlaceholder = ElsePlaceholder(self._output, self._language)
            placeholder.set_placeholder_name(placeholder_name)
            placeholder.set_placeholder_type(ElsePlaceholder.PlaceHolderType.NONTERMINAL)
            placeholder.set_content(content)

            m = ProcessListener.patternSeparator.match(content)
            if m:
                separator = m.group(1)
                if len(separator) == 1:
                    separator += " "
                placeholder.set_separator(separator)

            placeholder.write()

            self.log(f"createElseNonTerminalPlaceholder -> {placeholder_name} -> {content}", indentation = 2)

    def createElseMenuPlaceholder(self, placeholder_name, alternatives) -> None:
        if placeholder_name not in self._set_placeholders:
            self._set_placeholders.add(placeholder_name)
            self._options.placeholders.append(placeholder_name)

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

            placeholder.set_content(content)
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
                    self.createElseNonTerminalPlaceholder(placeholder_name, alternatives[0])
                elif len(alternatives) > 1:
                    self.createElseMenuPlaceholder(placeholder_name, alternatives)

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

            alternative = ""
            for element in elements:
                if len(element) > 0:
                    if len(alternative) == 0:
                        alternative = element
                    else:
                        if element in self._options.punctuation or alternative[-1] in self._options.punctuation:
                            alternative += element
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

            elif ctx.atom():
                element = self.processAtom(ctx.atom(), ctx.ebnfSuffix())

            elif ctx.ebnf():
                element = self.processEbnf(ctx.ebnf())

            self.log(f"element -> {element}", indentation = 1)

            self._stack_elements.top().append(element)

    # Exit a parse tree produced by ANTLRv4Parser#element.
    def exitElement(self, ctx:ANTLRv4Parser.ElementContext):
        super().exitElement(ctx)


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
                    self.createElseNonTerminalPlaceholder(placeholder_name, alternatives[0])
                elif len(alternatives) > 1:
                    self.createElseMenuPlaceholder(placeholder_name, alternatives)


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
