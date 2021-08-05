
from __future__ import annotations
from typing import TypeVar, Generic, List

from ANTLRv4Parser import ANTLRv4Parser
from ANTLRv4ParserListener import ANTLRv4ParserListener

T = TypeVar('T')


from ANTLRv4ParserListener import ANTLRv4ParserListener

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container  # not is true for empty container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()  # LIFO

    def top(self) -> T:
        return self._container[-1]

    def __repr__(self) -> str:
        return repr(self._container)


class ProcessListenerBase(ANTLRv4ParserListener):
    """Process the AST.
    """

    def __init__(self, printTokens) -> None:
        super().__init__()

        self.printTokens = printTokens

        self._spaces_stack: Stack[str] = Stack()
        self._spaces_stack.push("")

    def _spaces(self) -> str:
        return self._spaces_stack.top()

    def _indent(self) -> None:
        self._spaces_stack.push(self._spaces_stack.top() + "  ")

    def _unindent(self) -> None:
        self._spaces_stack.pop()

    # Enter a parse tree produced by ANTLRv4Parser#grammarSpec.
    def enterGrammarSpec(self, ctx:ANTLRv4Parser.GrammarSpecContext):
        if "enterGrammarSpec" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterGrammarSpec: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#grammarSpec.
    def exitGrammarSpec(self, ctx:ANTLRv4Parser.GrammarSpecContext):
        if "exitGrammarSpec" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitGrammarSpec: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#grammarDecl.
    def enterGrammarDecl(self, ctx:ANTLRv4Parser.GrammarDeclContext):
        if "enterGrammarDecl" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterGrammarDecl: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#grammarDecl.
    def exitGrammarDecl(self, ctx:ANTLRv4Parser.GrammarDeclContext):
        if "exitGrammarDecl" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitGrammarDecl: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#grammarType.
    def enterGrammarType(self, ctx:ANTLRv4Parser.GrammarTypeContext):
        if "enterGrammarType" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterGrammarType: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#grammarType.
    def exitGrammarType(self, ctx:ANTLRv4Parser.GrammarTypeContext):
        if "exitGrammarType" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitGrammarType: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#prequelConstruct.
    def enterPrequelConstruct(self, ctx:ANTLRv4Parser.PrequelConstructContext):
        if "enterPrequelConstruct" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterPrequelConstruct: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#prequelConstruct.
    def exitPrequelConstruct(self, ctx:ANTLRv4Parser.PrequelConstructContext):
        if "exitPrequelConstruct" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitPrequelConstruct: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#optionsSpec.
    def enterOptionsSpec(self, ctx:ANTLRv4Parser.OptionsSpecContext):
        if "enterOptionsSpec" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterOptionsSpec: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#optionsSpec.
    def exitOptionsSpec(self, ctx:ANTLRv4Parser.OptionsSpecContext):
        if "exitOptionsSpec" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitOptionsSpec: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#option.
    def enterOption(self, ctx:ANTLRv4Parser.OptionContext):
        if "enterOption" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterOption: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#option.
    def exitOption(self, ctx:ANTLRv4Parser.OptionContext):
        if "exitOption" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitOption: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#optionValue.
    def enterOptionValue(self, ctx:ANTLRv4Parser.OptionValueContext):
        if "enterOptionValue" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterOptionValue: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#optionValue.
    def exitOptionValue(self, ctx:ANTLRv4Parser.OptionValueContext):
        if "exitOptionValue" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitOptionValue: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#delegateGrammars.
    def enterDelegateGrammars(self, ctx:ANTLRv4Parser.DelegateGrammarsContext):
        if "enterDelegateGrammars" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterDelegateGrammars: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#delegateGrammars.
    def exitDelegateGrammars(self, ctx:ANTLRv4Parser.DelegateGrammarsContext):
        if "exitDelegateGrammars" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitDelegateGrammars: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#delegateGrammar.
    def enterDelegateGrammar(self, ctx:ANTLRv4Parser.DelegateGrammarContext):
        if "enterDelegateGrammar" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterDelegateGrammar: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#delegateGrammar.
    def exitDelegateGrammar(self, ctx:ANTLRv4Parser.DelegateGrammarContext):
        if "exitDelegateGrammar" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitDelegateGrammar: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#tokensSpec.
    def enterTokensSpec(self, ctx:ANTLRv4Parser.TokensSpecContext):
        if "enterTokensSpec" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterTokensSpec: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#tokensSpec.
    def exitTokensSpec(self, ctx:ANTLRv4Parser.TokensSpecContext):
        if "exitTokensSpec" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitTokensSpec: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#channelsSpec.
    def enterChannelsSpec(self, ctx:ANTLRv4Parser.ChannelsSpecContext):
        if "enterChannelsSpec" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterChannelsSpec: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#channelsSpec.
    def exitChannelsSpec(self, ctx:ANTLRv4Parser.ChannelsSpecContext):
        if "exitChannelsSpec" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitChannelsSpec: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#idList.
    def enterIdList(self, ctx:ANTLRv4Parser.IdListContext):
        if "enterIdList" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterIdList: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#idList.
    def exitIdList(self, ctx:ANTLRv4Parser.IdListContext):
        if "exitIdList" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitIdList: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#action_.
    def enterAction_(self, ctx:ANTLRv4Parser.Action_Context):
        if "enterAction" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterAction: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#action_.
    def exitAction_(self, ctx:ANTLRv4Parser.Action_Context):
        if "exitAction" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitAction: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#actionScopeName.
    def enterActionScopeName(self, ctx:ANTLRv4Parser.ActionScopeNameContext):
        if "enterActionScopeName" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterActionScopeName: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#actionScopeName.
    def exitActionScopeName(self, ctx:ANTLRv4Parser.ActionScopeNameContext):
        if "exitActionScopeName" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitActionScopeName: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#actionBlock.
    def enterActionBlock(self, ctx:ANTLRv4Parser.ActionBlockContext):
        if "enterActionBlock" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterActionBlock: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#actionBlock.
    def exitActionBlock(self, ctx:ANTLRv4Parser.ActionBlockContext):
        if "exitActionBlock" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitActionBlock: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#argActionBlock.
    def enterArgActionBlock(self, ctx:ANTLRv4Parser.ArgActionBlockContext):
        if "enterArgActionBlock" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterArgActionBlock: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#argActionBlock.
    def exitArgActionBlock(self, ctx:ANTLRv4Parser.ArgActionBlockContext):
        if "exitArgActionBlock" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitArgActionBlock: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#modeSpec.
    def enterModeSpec(self, ctx:ANTLRv4Parser.ModeSpecContext):
        if "enterModeSpec" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterModeSpec: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#modeSpec.
    def exitModeSpec(self, ctx:ANTLRv4Parser.ModeSpecContext):
        if "exitModeSpec" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitModeSpec: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#rules.
    def enterRules(self, ctx:ANTLRv4Parser.RulesContext):
        if "enterRules" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterRules: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#rules.
    def exitRules(self, ctx:ANTLRv4Parser.RulesContext):
        if "exitRules" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitRules: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#ruleSpec.
    def enterRuleSpec(self, ctx:ANTLRv4Parser.RuleSpecContext):
        if "enterRuleSpec" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterRuleSpec: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#ruleSpec.
    def exitRuleSpec(self, ctx:ANTLRv4Parser.RuleSpecContext):
        if "exitRuleSpec" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitRuleSpec: " + ctx.getText() + '\n')
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#parserRuleSpec.
    def enterParserRuleSpec(self, ctx:ANTLRv4Parser.ParserRuleSpecContext):
        if "enterParserRuleSpec" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterParserRuleSpec: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#parserRuleSpec.
    def exitParserRuleSpec(self, ctx:ANTLRv4Parser.ParserRuleSpecContext):
        if "exitParserRuleSpec" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitParserRuleSpec: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#exceptionGroup.
    def enterExceptionGroup(self, ctx:ANTLRv4Parser.ExceptionGroupContext):
        if "enterExceptionGroup" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterExceptionGroup: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#exceptionGroup.
    def exitExceptionGroup(self, ctx:ANTLRv4Parser.ExceptionGroupContext):
        if "exitExceptionGroup" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitExceptionGroup: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#exceptionHandler.
    def enterExceptionHandler(self, ctx:ANTLRv4Parser.ExceptionHandlerContext):
        if "enterExceptionHandler" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterExceptionHandler: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#exceptionHandler.
    def exitExceptionHandler(self, ctx:ANTLRv4Parser.ExceptionHandlerContext):
        if "exitExceptionHandler" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitExceptionHandler: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#finallyClause.
    def enterFinallyClause(self, ctx:ANTLRv4Parser.FinallyClauseContext):
        if "enterFinallyClause" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterFinallyClause: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#finallyClause.
    def exitFinallyClause(self, ctx:ANTLRv4Parser.FinallyClauseContext):
        if "exitFinallyClause" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitFinallyClause: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#rulePrequel.
    def enterRulePrequel(self, ctx:ANTLRv4Parser.RulePrequelContext):
        if "enterRulePrequel" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterRulePrequel: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#rulePrequel.
    def exitRulePrequel(self, ctx:ANTLRv4Parser.RulePrequelContext):
        if "exitRulePrequel" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitRulePrequel: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#ruleReturns.
    def enterRuleReturns(self, ctx:ANTLRv4Parser.RuleReturnsContext):
        if "enterRuleReturns" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterRuleReturns: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#ruleReturns.
    def exitRuleReturns(self, ctx:ANTLRv4Parser.RuleReturnsContext):
        if "exitRuleReturns" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitRuleReturns: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#throwsSpec.
    def enterThrowsSpec(self, ctx:ANTLRv4Parser.ThrowsSpecContext):
        if "enterThrowsSpec" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterThrowsSpec: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#throwsSpec.
    def exitThrowsSpec(self, ctx:ANTLRv4Parser.ThrowsSpecContext):
        if "exitThrowsSpec" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitThrowsSpec: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#localsSpec.
    def enterLocalsSpec(self, ctx:ANTLRv4Parser.LocalsSpecContext):
        if "enterLocalsSpec" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterLocalsSpec: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#localsSpec.
    def exitLocalsSpec(self, ctx:ANTLRv4Parser.LocalsSpecContext):
        if "exitLocalsSpec" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitLocalsSpec: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#ruleAction.
    def enterRuleAction(self, ctx:ANTLRv4Parser.RuleActionContext):
        if "enterRuleAction" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterRuleAction: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#ruleAction.
    def exitRuleAction(self, ctx:ANTLRv4Parser.RuleActionContext):
        if "exitRuleAction" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitRuleAction: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#ruleModifiers.
    def enterRuleModifiers(self, ctx:ANTLRv4Parser.RuleModifiersContext):
        if "enterRuleModifiers" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterRuleModifiers: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#ruleModifiers.
    def exitRuleModifiers(self, ctx:ANTLRv4Parser.RuleModifiersContext):
        if "exitRuleModifiers" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitRuleModifiers: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#ruleModifier.
    def enterRuleModifier(self, ctx:ANTLRv4Parser.RuleModifierContext):
        if "enterRuleModifier" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterRuleModifier: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#ruleModifier.
    def exitRuleModifier(self, ctx:ANTLRv4Parser.RuleModifierContext):
        if "exitRuleModifier" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitRuleModifier: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#ruleBlock.
    def enterRuleBlock(self, ctx:ANTLRv4Parser.RuleBlockContext):
        if "enterRuleBlock" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterRuleBlock: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#ruleBlock.
    def exitRuleBlock(self, ctx:ANTLRv4Parser.RuleBlockContext):
        if "exitRuleBlock" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitRuleBlock: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#ruleAltList.
    def enterRuleAltList(self, ctx:ANTLRv4Parser.RuleAltListContext):
        if "enterRuleAltList" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterRuleAltList: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#ruleAltList.
    def exitRuleAltList(self, ctx:ANTLRv4Parser.RuleAltListContext):
        if "exitRuleAltList" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitRuleAltList: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#labeledAlt.
    def enterLabeledAlt(self, ctx:ANTLRv4Parser.LabeledAltContext):
        if "enterLabeledAlt" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterLabeledAlt: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#labeledAlt.
    def exitLabeledAlt(self, ctx:ANTLRv4Parser.LabeledAltContext):
        if "exitLabeledAlt" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitLabeledAlt: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#lexerRuleSpec.
    def enterLexerRuleSpec(self, ctx:ANTLRv4Parser.LexerRuleSpecContext):
        if "enterLexerRuleSpec" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterLexerRuleSpec: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#lexerRuleSpec.
    def exitLexerRuleSpec(self, ctx:ANTLRv4Parser.LexerRuleSpecContext):
        if "exitLexerRuleSpec" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitLexerRuleSpec: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#lexerRuleBlock.
    def enterLexerRuleBlock(self, ctx:ANTLRv4Parser.LexerRuleBlockContext):
        if "enterLexerRuleBlock" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterLexerRuleBlock: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#lexerRuleBlock.
    def exitLexerRuleBlock(self, ctx:ANTLRv4Parser.LexerRuleBlockContext):
        if "exitLexerRuleBlock" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitLexerRuleBlock: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#lexerAltList.
    def enterLexerAltList(self, ctx:ANTLRv4Parser.LexerAltListContext):
        if "enterLexerAltList" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterLexerAltList: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#lexerAltList.
    def exitLexerAltList(self, ctx:ANTLRv4Parser.LexerAltListContext):
        if "exitLexerAltList" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitLexerAltList: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#lexerAlt.
    def enterLexerAlt(self, ctx:ANTLRv4Parser.LexerAltContext):
        if "enterLexerAlt" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterLexerAlt: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#lexerAlt.
    def exitLexerAlt(self, ctx:ANTLRv4Parser.LexerAltContext):
        if "exitLexerAlt" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitLexerAlt: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#lexerElements.
    def enterLexerElements(self, ctx:ANTLRv4Parser.LexerElementsContext):
        if "enterLexerElements" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterLexerElements: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#lexerElements.
    def exitLexerElements(self, ctx:ANTLRv4Parser.LexerElementsContext):
        if "exitLexerElements" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitLexerElements: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#lexerElement.
    def enterLexerElement(self, ctx:ANTLRv4Parser.LexerElementContext):
        if "enterLexerElement" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterLexerElement: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#lexerElement.
    def exitLexerElement(self, ctx:ANTLRv4Parser.LexerElementContext):
        if "exitLexerElement" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitLexerElement: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#labeledLexerElement.
    def enterLabeledLexerElement(self, ctx:ANTLRv4Parser.LabeledLexerElementContext):
        if "enterLabeledLexerElement" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterLabeledLexerElement: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#labeledLexerElement.
    def exitLabeledLexerElement(self, ctx:ANTLRv4Parser.LabeledLexerElementContext):
        if "exitLabeledLexerElement" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitLabeledLexerElement: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#lexerBlock.
    def enterLexerBlock(self, ctx:ANTLRv4Parser.LexerBlockContext):
        if "enterLexerBlock" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterLexerBlock: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#lexerBlock.
    def exitLexerBlock(self, ctx:ANTLRv4Parser.LexerBlockContext):
        if "exitLexerBlock" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitLexerBlock: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#lexerCommands.
    def enterLexerCommands(self, ctx:ANTLRv4Parser.LexerCommandsContext):
        if "enterLexerCommands" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterLexerCommands: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#lexerCommands.
    def exitLexerCommands(self, ctx:ANTLRv4Parser.LexerCommandsContext):
        if "exitLexerCommands" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitLexerCommands: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#lexerCommand.
    def enterLexerCommand(self, ctx:ANTLRv4Parser.LexerCommandContext):
        if "enterLexerCommand" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterLexerCommand: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#lexerCommand.
    def exitLexerCommand(self, ctx:ANTLRv4Parser.LexerCommandContext):
        if "exitLexerCommand" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitLexerCommand: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#lexerCommandName.
    def enterLexerCommandName(self, ctx:ANTLRv4Parser.LexerCommandNameContext):
        if "enterLexerCommandName" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterLexerCommandName: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#lexerCommandName.
    def exitLexerCommandName(self, ctx:ANTLRv4Parser.LexerCommandNameContext):
        if "exitLexerCommandName" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitLexerCommandName: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#lexerCommandExpr.
    def enterLexerCommandExpr(self, ctx:ANTLRv4Parser.LexerCommandExprContext):
        if "enterLexerCommandExpr" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterLexerCommandExpr: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#lexerCommandExpr.
    def exitLexerCommandExpr(self, ctx:ANTLRv4Parser.LexerCommandExprContext):
        if "exitLexerCommandExpr" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitLexerCommandExpr: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#altList.
    def enterAltList(self, ctx:ANTLRv4Parser.AltListContext):
        if "enterAltList" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterAltList: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#altList.
    def exitAltList(self, ctx:ANTLRv4Parser.AltListContext):
        if "exitAltList" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitAltList: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#alternative.
    def enterAlternative(self, ctx:ANTLRv4Parser.AlternativeContext):
        if "enterAlternative" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterAlternative: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#alternative.
    def exitAlternative(self, ctx:ANTLRv4Parser.AlternativeContext):
        if "exitAlternative" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitAlternative: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#element.
    def enterElement(self, ctx:ANTLRv4Parser.ElementContext):
        if "enterElement" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterElement: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#element.
    def exitElement(self, ctx:ANTLRv4Parser.ElementContext):
        if "exitElement" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitElement: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#labeledElement.
    def enterLabeledElement(self, ctx:ANTLRv4Parser.LabeledElementContext):
        if "enterLabeledElement" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterLabeledElement: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#labeledElement.
    def exitLabeledElement(self, ctx:ANTLRv4Parser.LabeledElementContext):
        if "exitLabeledElement" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitLabeledElement: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#ebnf.
    def enterEbnf(self, ctx:ANTLRv4Parser.EbnfContext):
        if "enterEbnf" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterEbnf: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#ebnf.
    def exitEbnf(self, ctx:ANTLRv4Parser.EbnfContext):
        if "exitEbnf" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitEbnf: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#blockSuffix.
    def enterBlockSuffix(self, ctx:ANTLRv4Parser.BlockSuffixContext):
        if "enterBlockSuffix" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterBlockSuffix: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#blockSuffix.
    def exitBlockSuffix(self, ctx:ANTLRv4Parser.BlockSuffixContext):
        if "exitBlockSuffix" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitBlockSuffix: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#ebnfSuffix.
    def enterEbnfSuffix(self, ctx:ANTLRv4Parser.EbnfSuffixContext):
        if "enterEbnfSuffix" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterEbnfSuffix: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#ebnfSuffix.
    def exitEbnfSuffix(self, ctx:ANTLRv4Parser.EbnfSuffixContext):
        if "exitEbnfSuffix" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitEbnfSuffix: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#lexerAtom.
    def enterLexerAtom(self, ctx:ANTLRv4Parser.LexerAtomContext):
        if "enterLexerAtom" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterLexerAtom: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#lexerAtom.
    def exitLexerAtom(self, ctx:ANTLRv4Parser.LexerAtomContext):
        if "exitLexerAtom" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitLexerAtom: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#atom.
    def enterAtom(self, ctx:ANTLRv4Parser.AtomContext):
        if "enterAtom" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterAtom: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#atom.
    def exitAtom(self, ctx:ANTLRv4Parser.AtomContext):
        if "exitAtom" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitAtom: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#notSet.
    def enterNotSet(self, ctx:ANTLRv4Parser.NotSetContext):
        if "enterNotSet" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterNotSet: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#notSet.
    def exitNotSet(self, ctx:ANTLRv4Parser.NotSetContext):
        if "exitNotSet" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitNotSet: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#blockSet.
    def enterBlockSet(self, ctx:ANTLRv4Parser.BlockSetContext):
        if "enterBlockSet" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterBlockSet: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#blockSet.
    def exitBlockSet(self, ctx:ANTLRv4Parser.BlockSetContext):
        if "exitBlockSet" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitBlockSet: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#setElement.
    def enterSetElement(self, ctx:ANTLRv4Parser.SetElementContext):
        if "enterSetElement" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterSetElement: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#setElement.
    def exitSetElement(self, ctx:ANTLRv4Parser.SetElementContext):
        if "exitSetElement" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitSetElement: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#block.
    def enterBlock(self, ctx:ANTLRv4Parser.BlockContext):
        if "enterBlock" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterBlock: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#block.
    def exitBlock(self, ctx:ANTLRv4Parser.BlockContext):
        if "exitBlock" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitBlock: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#ruleref.
    def enterRuleref(self, ctx:ANTLRv4Parser.RulerefContext):
        if "enterRuleref" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterRuleref: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#ruleref.
    def exitRuleref(self, ctx:ANTLRv4Parser.RulerefContext):
        if "exitRuleref" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitRuleref: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#characterRange.
    def enterCharacterRange(self, ctx:ANTLRv4Parser.CharacterRangeContext):
        if "enterCharacterRange" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterCharacterRange: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#characterRange.
    def exitCharacterRange(self, ctx:ANTLRv4Parser.CharacterRangeContext):
        if "exitCharacterRange" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitCharacterRange: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#terminal.
    def enterTerminal(self, ctx:ANTLRv4Parser.TerminalContext):
        if "enterTerminal" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterTerminal: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#terminal.
    def exitTerminal(self, ctx:ANTLRv4Parser.TerminalContext):
        if "exitTerminal" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitTerminal: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#elementOptions.
    def enterElementOptions(self, ctx:ANTLRv4Parser.ElementOptionsContext):
        if "enterElementOptions" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterElementOptions: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#elementOptions.
    def exitElementOptions(self, ctx:ANTLRv4Parser.ElementOptionsContext):
        if "exitElementOptions" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitElementOptions: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#elementOption.
    def enterElementOption(self, ctx:ANTLRv4Parser.ElementOptionContext):
        if "enterElementOption" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterElementOption: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#elementOption.
    def exitElementOption(self, ctx:ANTLRv4Parser.ElementOptionContext):
        if "exitElementOption" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitElementOption: " + ctx.getText())
            self._unindent()

    # Enter a parse tree produced by ANTLRv4Parser#identifier.
    def enterIdentifier(self, ctx:ANTLRv4Parser.IdentifierContext):
        if "enterIdentifier" in self.printTokens or "ALL" in self.printTokens:
            self._indent()
            print (self._spaces() + "enterIdentifier: " + ctx.getText())

    # Exit a parse tree produced by ANTLRv4Parser#identifier.
    def exitIdentifier(self, ctx:ANTLRv4Parser.IdentifierContext):
        if "exitIdentifier" in self.printTokens or "ALL" in self.printTokens:
            print (self._spaces() + "exitIdentifier: " + ctx.getText())
            self._unindent()
