(dap-register-debug-template
  "Python :: Run Antlr4ToElseCompiler"
  (list :type "python"
        :args "-i ./grammars -o ./out -l Python -p \"*(),;:\" -I \"a-zA-Z_0-9-\" -w -r -v -x Python3Parser.g4 Python3Lexer.g4"
        :cwd "~/psimacs/ELSE-grammar-compiler/grammars"
        :module nil
        :program "Antlr4ToElseCompiler.py"
        :request "launch"
        :name "Python :: Run Antlr4ToElseCompiler"))


(dap-register-debug-template
  "Python :: Run Antlr4ToElseCompiler on Python396"
  (list :type "python"
        :args "-i ./grammars -o ./out -l Python -p \"*(),;:\" -I \"a-zA-Z_0-9-\" -w -x -v Python396.g4 Python3Lexer.g4"
        :cwd "~/psimacs/ELSE-grammar-compiler/grammars"
        :module nil
        :program "Antlr4ToElseCompiler.py"
        :request "launch"
        :name "Python :: Run Antlr4ToElseCompiler on Python396"))


(dap-register-debug-template
  "Python :: Run Antlr4ToElseCompiler on CPP23"
  (list :type "python"
        :args "-i ./grammars -o ./out -l c++ -p \"*(){}[].,;\" -I \"a-zA-Z_0-9-\" -x CPP23.g4"
        ;;:cwd "~/psimacs/ELSE-grammar-compiler"
        :cwd "/home/hatlafax/psimacs/ELSE-grammar-compiler"
        :module nil
        :program "Antlr4ToElseCompiler.py"
        :request "launch"
        :name "Python :: Run Antlr4ToElseCompiler on CPP23"))

(provide ' dap-mode.el)
