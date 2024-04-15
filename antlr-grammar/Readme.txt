MSys2 bash shell

pip install antlr4-python3-runtime

cd antlr-grammar

c:/utils/Antlr/bin/antlr4.bat -o . -Dlanguage=Python3 ANTLRv4Lexer.g4 ANTLRv4Parser.g4
antlr4 -o . -Dlanguage=Python3 ANTLRv4Lexer.g4 ANTLRv4Parser.g4 && cp *.py ../

python TestAntlr.py ./examples/Hello.g4


Copy
  ANTLRv4Parser.py
  ANTLRv4ParserListener.py
  ANTLRv4Lexer.py
  LexerAdaptor.py

to ../