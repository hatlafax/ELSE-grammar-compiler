(dap-register-debug-template
  "Python :: Run Antlr4ToElseCompiler"
  (list :type "python"
        :args "-i ./grammars -o ./out -l Python -p \"*(),;:\" -I \"a-zA-Z_0-9-\" -w -r -v -x Python3Parser.g4 Python3Lexer.g4"
        :cwd "d:/work/ELSE-grammar-compiler"
        :module nil
        :program "Antlr4ToElseCompiler.py"
        :request "launch"
        :name "Python :: Run Antlr4ToElseCompiler"))


(dap-register-debug-template
  "Python :: Run Antlr4ToElseCompiler on Python396"
  (list :type "python"
        :args "-i ./grammars -o ./out -l Python -p \"*(),;:\" -I \"a-zA-Z_0-9-\" -w -x -v Python396.g4 Python3Lexer.g4"
        :cwd "d:/work/ELSE-grammar-compiler"
        :module nil
        :program "Antlr4ToElseCompiler.py"
        :request "launch"
        :name "Python :: Run Antlr4ToElseCompiler on Python396"))
