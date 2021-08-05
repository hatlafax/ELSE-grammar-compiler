import re
from ANTLRv4Parser import ANTLRv4Parser
from ANTLRv4ParserListener import ANTLRv4ParserListener

class PreProcessListener(ANTLRv4ParserListener):
    """Listen to terminals. Find start rule.
    """

    patternRuleSpec = re.compile(r'^\s*(?:public|private|protected|fragment)?([A-Za-z0-9_]+)\s*:.*$')
    patternQuotedTerminals = re.compile(r"^\s*'(?:[^']|\\')+'s*$")

    def __init__(self,
                 terminals,
                 quotedTerminals,
                 ruleSpec,
                 lexerRuleSpec,
                 quotedLexerRuleSpec,
                 unquotedLexerRuleSpec ) -> None:
        super().__init__()

        self.terminals = terminals
        self.quotedTerminals = quotedTerminals
        self.ruleSpec = ruleSpec
        self.lexerRuleSpec = lexerRuleSpec
        self.quotedLexerRuleSpec = quotedLexerRuleSpec
        self.unquotedLexerRuleSpec = unquotedLexerRuleSpec
        self.listenRuleSpec = None
        self.listenLexerRuleSpec = None

        self.dictParserRules = {}
        self.listParserRules = []
        self.isParserRuleSpec = False


    def enterTerminal(self, ctx:ANTLRv4Parser.TerminalContext):
        terminal = ctx.getText()
        m = PreProcessListener.patternQuotedTerminals.match(terminal)
        if m:
            self.quotedTerminals.add(terminal)
        else:
            self.terminals.add(terminal)

    def enterRuleSpec(self, ctx:ANTLRv4Parser.RuleSpecContext):
        m = PreProcessListener.patternRuleSpec.match(ctx.getText())
        if m:
            self.listenRuleSpec = m.group(1)

    def exitRuleSpec(self, ctx:ANTLRv4Parser.RuleSpecContext):
        self.listenRuleSpec = None

    def enterLexerRuleSpec(self, ctx:ANTLRv4Parser.LexerRuleSpecContext):
        m = PreProcessListener.patternRuleSpec.match(ctx.getText())
        if m:
            self.listenLexerRuleSpec = m.group(1)

    def exitLexerRuleSpec(self, ctx:ANTLRv4Parser.LexerRuleSpecContext):
        self.listenLexerRuleSpec = None

    def enterLexerRuleBlock(self, ctx:ANTLRv4Parser.LexerRuleBlockContext):
        text = ctx.getText()
        if self.listenRuleSpec is not None:
            self.ruleSpec[self.listenRuleSpec] = text

        if self.listenLexerRuleSpec is not None:
            self.lexerRuleSpec[self.listenLexerRuleSpec] = text
            if PreProcessListener.isQuoted(text):
                self.quotedLexerRuleSpec[self.listenLexerRuleSpec] = text
            else:
                self.unquotedLexerRuleSpec[self.listenLexerRuleSpec] = text

    def enterParserRuleSpec(self, ctx:ANTLRv4Parser.ParserRuleSpecContext):
        self.isParserRuleSpec = True
        m = PreProcessListener.patternRuleSpec.match(ctx.getText())
        if m:
            text = m.group(1)
            self.listParserRules.append(text)
            self.dictParserRules.setdefault(text, 0)

    def exitParserRuleSpec(self, ctx:ANTLRv4Parser.ParserRuleSpecContext):
        self.isParserRuleSpec = False

    def enterRuleref(self, ctx:ANTLRv4Parser.RulerefContext):
        if self.isParserRuleSpec:
            text = ctx.getText()
            value = self.dictParserRules.setdefault(text, 0)
            self.dictParserRules[text] = value + 1

    def getTerminal(self, rule):
        terminal = None
        if rule in self.lexerRuleSpec:
            terminal = self.lexerRuleSpec[rule]
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
        for r, c in self.dictParserRules.items():
            if c == 0 and r.lower() in heuristic:
                start_rule = r
        if start_rule is None:
            for r in self.listParserRules:
                if r in self.dictParserRules:
                    c = self.dictParserRules[r]
                    if c == 0:
                        start_rule =  r
                        break
        return start_rule