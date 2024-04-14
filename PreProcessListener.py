import re
from ANTLRv4Parser import ANTLRv4Parser
from ANTLRv4ParserListener import ANTLRv4ParserListener

class PreProcessListener(ANTLRv4ParserListener):
    """Listen to terminals. Find start rule.
    """

    patternRuleSpec = re.compile(r'^\s*(?:public|private|protected|fragment)?([A-Za-z0-9_-]+)\s*:.*$')
    patternQuotedTerminals = re.compile(r"^\s*'(?:[^']|\\')+'s*$")

    def __init__(self, options) -> None:
        super().__init__()

        self._options = options

        self._listenRuleSpec = None
        self._listenLexerRuleSpec = None

        self._dictParserRules = {}
        self._listParserRules = []
        self._isParserRuleSpec = False


    def enterTerminal(self, ctx:ANTLRv4Parser.TerminalContext):
        terminal = ctx.getText()
        m = PreProcessListener.patternQuotedTerminals.match(terminal)
        if m:
            self._options.quotedTerminals.add(terminal)
        else:
            self._options.terminals.add(terminal)

    def enterRuleSpec(self, ctx:ANTLRv4Parser.RuleSpecContext):
        m = PreProcessListener.patternRuleSpec.match(ctx.getText())
        if m:
            self._listenRuleSpec = m.group(1)

    def exitRuleSpec(self, ctx:ANTLRv4Parser.RuleSpecContext):
        self._listenRuleSpec = None

    def enterLexerRuleSpec(self, ctx:ANTLRv4Parser.LexerRuleSpecContext):
        m = PreProcessListener.patternRuleSpec.match(ctx.getText())
        if m:
            self._listenLexerRuleSpec = m.group(1)

    def exitLexerRuleSpec(self, ctx:ANTLRv4Parser.LexerRuleSpecContext):
        self._listenLexerRuleSpec = None

    def enterLexerRuleBlock(self, ctx:ANTLRv4Parser.LexerRuleBlockContext):
        text = ctx.getText()
        if self._listenRuleSpec is not None:
            self._options.ruleSpec[self._listenRuleSpec] = text

        if self._listenLexerRuleSpec is not None:
            self._options.lexerRuleSpec[self._listenLexerRuleSpec] = text
            if PreProcessListener.isQuoted(text):
                self._options.quotedLexerRuleSpec[self._listenLexerRuleSpec] = text
            else:
                self._options.unquotedLexerRuleSpec[self._listenLexerRuleSpec] = text

    def enterParserRuleSpec(self, ctx:ANTLRv4Parser.ParserRuleSpecContext):
        self._isParserRuleSpec = True
        m = PreProcessListener.patternRuleSpec.match(ctx.getText())
        if m:
            text = m.group(1)
            self._listParserRules.append(text)
            self._dictParserRules.setdefault(text, 0)
            self._options.placeholders_set.add(text)

    def exitParserRuleSpec(self, ctx:ANTLRv4Parser.ParserRuleSpecContext):
        self._isParserRuleSpec = False

    def enterRuleref(self, ctx:ANTLRv4Parser.RulerefContext):
        if self._isParserRuleSpec:
            text = ctx.getText()
            value = self._dictParserRules.setdefault(text, 0)
            self._dictParserRules[text] = value + 1

    def enterBlock(self, ctx:ANTLRv4Parser.BlockContext):
        if self._isParserRuleSpec:
            self._options.placeholders_set.add(ctx.getText())

    def getTerminal(self, rule):
        terminal = None
        if rule in self._options.lexerRuleSpec:
            terminal = self._options.lexerRuleSpec[rule]
        return terminal

    def isQuoted(terminal):
        m = PreProcessListener.patternQuotedTerminals.match(terminal)
        if m:
            return True
        else:
            return False

    def startRule(self) -> str:
        start_rule = None
        heuristic = ['program', 'translationunit', 'translation_unit', 'compilation_unit', 'compilationunit']
        for r, c in self._dictParserRules.items():
            if c == 0 and r.lower() in heuristic:
                start_rule = r
        if start_rule is None:
            for r in self._listParserRules:
                if r in self._dictParserRules:
                    c = self._dictParserRules[r]
                    if c == 0:
                        start_rule =  r
                        break
        return start_rule
