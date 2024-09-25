import sys, re, os
from enum import Enum
from typing import NoReturn
from optparse import OptionParser
from pathlib import Path

from antlr4 import *
from ANTLRv4Lexer import ANTLRv4Lexer
from ANTLRv4Parser import ANTLRv4Parser

from ElseTemplateGenerator import ElseLanguage
from PreProcessListener import PreProcessListener
from ProcessListener import ProcessListener

def main():
    usage = r"""Usage: %(prog_name)s [options] file1 file2 ...

    This program parses Antlrv4 grammer files (*.g4) and writes emacs ELSE lse
    files.
    """
    parser = OptionParser(usage = usage % { 'prog_name' : '%prog' })

    parser.add_option('-i',
                      '--input-directory',
                      dest = 'input_dir',
                      default = os.getcwd(),
                      metavar = 'DIR',
                      help = """Set grammar files input directory."""
                             """Defaults to the current working directory.""")

    parser.add_option('-o',
                      '--output-directory',
                      dest = 'output_dir',
                      default = os.getcwd(),
                      metavar = 'DIR',
                      help = """Set the destination directory for the generated ELSE lse files."""
                             """Defaults to the current working directory.""")

    parser.add_option('-l',
                      '--language',
                      dest = 'language',
                      default = 'python',
                      help = """Set the ELSE language that should be generated: python, c++, rust, java,..."""
                             """Defaults to python.""")

    parser.add_option('-b',
                      '--batch-processing',
                      dest = 'batch_processing',
                      default = False,
                      action="store_true",
                      help = """If True, batch processing is performed on the input-directory."""
                             """The following Antlr v4 grammars are considered:"""
                             """cmake, C++, C, CSharp, Java, JavaScript, Modellica, Php, TypeScript,"""
                             """ECMAScript, Python, Pascal, Rust, Scala, Clojure, Golang, Dot, Erlang,"""
                             """Html, Prolog, RestructuredText, Ruby."""
                             """"""
                             """Only available predefined grammar files are considered."""
                             """Batch processing is only useful for testing, because important information"""
                             """like the set of punctuation characters and the set of valid characters is"""
                             """not defined properly.""")

    parser.add_option('-s',
                      '--indentation',
                      dest = 'indentation',
                      default = 4,
                      metavar = 'NUMBER',
                      help = """Set the ELSE language space indentation parameter."""
                             """Defaults to 4.""")

    parser.add_option('-p',
                      '--punctuation-chars',
                      dest = 'punctuation',
                      default = r"*(),;:",
                      metavar = "'CHARACTERS'",
                      help = """Set the ELSE language punctuation character set."""
                             """Defaults to '*(),;:'.""")

    parser.add_option('-I',
                      '--valid-identifiers',
                      dest = 'valid_identifier',
                      default = r"a-zA-Z_0-9-",
                      metavar = "'CHARACTERS'",
                      help = """Set the ELSE language valid identifier character set."""
                             """Defaults to 'a-zA-Z_0-9-'.""")

    parser.add_option('-V',
                      '--version',
                      dest = 'version',
                      default = "1.0",
                      help = """Set the ELSE language version string."""
                             """Defaults to '1.0'.""")

    parser.add_option('-c',
                      '--copyright-holder',
                      dest = 'copyright_holder',
                      default = "2024 Johannes Brunen",
                      metavar = 'HOLDER',
                      help = """Set the ELSE file copyright holder."""
                             """Defaults to '2021 Johannes Brunen'.""")

    parser.add_option('-a',
                      '--copyright-author',
                      dest = 'copyright_author',
                      metavar = 'AUTHOR',
                      default = "Johannes Brunen <hatlafax@gmx.de>",
                      help = """Set the ELSE file copyright holder."""
                             """Defaults to 'Johannes Brunen <hatlafax@gmx.de>'.""")

    parser.add_option('--indentation-token',
                      dest = 'indentation_token',
                      metavar = 'STRING',
                      default = "INDENT",
                      help = """In order to generate useful ELSE files, additional semantic"""
                             """tokens for indentation can be embedded into the grammar."""
                             """These tokens yield not in placeholders but modify a"""
                             """placeholders content layout."""
                      )

    parser.add_option('--dedentation-token',
                      dest = 'dedentation_token',
                      metavar = 'STRING',
                      default = "DEDENT",
                      help = """In order to generate useful ELSE files, additional semantic"""
                             """tokens for dedentation can be embedded into the grammar."""
                             """These tokens yield not in placeholders but modify a"""
                             """placeholders content layout."""
                      )

    parser.add_option('--newline-token',
                      dest = 'newline_token',
                      metavar = 'STRING',
                      default = "NEWLINE",
                      help = """In order to generate useful ELSE files, additional semantic"""
                             """tokens for dedentation can be embedded into the grammar."""
                             """These tokens yield not in placeholders but modify a"""
                             """placeholders content layout."""
                      )

    parser.add_option('--nospace-token',
                      dest = 'nospace_token',
                      metavar = 'STRING',
                      default = "NOSPC",
                      help = """In order to generate useful ELSE files, additional semantic"""
                             """tokens for dedentation can be embedded into the grammar."""
                             """These tokens yield not in placeholders but modify a"""
                             """placeholders content layout."""
                      )

    copyright = """;; Copyright (C) {copyright_holder}
;;
;; Author: {copyright_author},
;;
;; Keywords: language sensitive abbreviation template placeholder token
;;
;; GNU Emacs is free software; you can redistribute it and/or modify
;; it under the terms of the GNU General Public License as published by
;; the Free Software Foundation; either version 2, or (at your option)
;; any later version.
;;
;; GNU Emacs is distributed in the hope that it will be useful,
;; but WITHOUT ANY WARRANTY; without even the implied warranty of
;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;; GNU General Public License for more details.
;;
;; You should have received a copy of the GNU General Public License
;; along with GNU Emacs; see the file COPYING.  If not, write to the
;; Free Software Foundation, Inc., 59 Temple Place - Suite 330,
;; Boston, MA 02111-1307, USA.
"""

    parser.add_option('-C',
                      '--copyright',
                      dest = 'copyright',
                      default = copyright,
                      help = """Set the ELSE file copyright text."""
                             """Attention: '{copyright_holder}' and '{copyright_author}' are expected"""
                             """           to be embedded literally in the copyright string!"""
                             """Defaults to:""" + "\n" + copyright)

    parser.add_option('-v',
                      '--verbose',
                      dest = 'verbose',
                      default = False,
                      action="store_true",
                      help = """If True the program prints verbose output messages."""
                             """Defaults to False.""")

    print_tokens_str = """RuleSpec,
RuleBlock,
RuleAltList,
LabeledAlt,
Alternative,
Element,
Elements,
LabeledElement,
Ebnf,
EbnfSuffix,
Atom,
Block,
AltList,
RuleSpec,
Ruleref,
AnnotationsSpec,
AnnotationBlockSeq,
AnnotationBlock,
AnnotationKey,
AnnotationValue,
Terminal,
Identifier"""

    parser.add_option('-T',
                      '--print-tokens',
                      dest = 'print_tokens',
                      default = print_tokens_str,
                      metavar = "'token1,token2,...'",
                      help = """Set the listener functions that are printed in verbose printing mode."""
                             """Defaults to: {print_tokens}""")

    parser.add_option('-w',
                      '--write-placeholders',
                      dest = 'write_placeholders',
                      default = False,
                      action="store_true",
                      help = """The compiler will write the file 'language.lst' to the output directory which"""
                             """contains all placeholders that gets written to the '*.lse' output file. The option"""
                             """'read-placeholders' allows to read a mapping file which can easily be generated"""
                             """from this file."""
                             """Defaults to: False""")

    parser.add_option('-r',
                      '--read-placeholders',
                      dest = 'read_placeholders',
                      default = False,
                      action="store_true",
                      help = """The compiler will read a mapping file 'language.lst' that does contain two columns in each line:"""
                             """The first column contains the placeholder string, as written with option 'write-placeholders'."""
                             """The second column contains the mapping used in the ELSE LSE generated file for the"""
                             """placeholder. The two columns are expected to be separated by the following regular"""
                             """expression: '\\s*=> ::\\s*'."""
                             """Defaults to: False""")

    parser.add_option('-E',
                      '--terminal-tokens',
                      dest = 'terminal_tokens',
                      default = "",
                      metavar = "'token1,token2,...'",
                      help = """Set the terminal tokens that leads to ELSE terminal placeholders."""
                             """In case that the grammar does not contain detail lexer specification a comma separated"""
                             """list of terminals can be specified. Other non specified terminals are silently ignored."""
                             """Defaults to empty string""")

    parser.add_option('-x',
                      '--non-space-separated',
                      dest = 'non_space_separated',
                      default = False,
                      action="store_true",
                      help = """The compiler will read the file 'language.spc'. This file provides character pairs,"""
                             """one in each line that specifify token elements that should not be separated by a"""
                             """space character. E.g. a line entry '},' would cause the compiler to omit the default"""
                             """space character between any two parser elements where the first ends with the curly"""
                             """bracket character and the second starts with the comma character."""
                             """This allows to get control over the final ELSE LSE template file layout."""
                             """Defaults to: False""")

    parser.add_option('-P',
                      '--print-placeholders',
                      dest = 'print_placeholders',
                      default = False,
                      action="store_true",
                      help = """If True the program prints the found placeholders to the console."""
                             """Defaults to False.""")


    options, args = parser.parse_args(sys.argv[1:])

    copyright = options.copyright.format(copyright_holder = options.copyright_holder, copyright_author = options.copyright_author)
    options.copyright = copyright

    # check preconditions:
    if not os.path.exists(options.input_dir):
        sys.exit(f"Input directory {options.input_dir} not found!")

    Path(options.output_dir).mkdir(parents=True, exist_ok=True)

    languages = []
    files = []

    if options.batch_processing:
        std_languages = [
                     'cmake',
                     'c++',
                     'c',
                     'csharp',
                     'java',
                     'javascript',
                     'modelica',
                     'php',
                     'typescript',
                     'ecmascript',
                     'python',
                     'pascal',
                     'rust',
                     'scala',
                     'clojure',
                     'golang',
                     'dot',
                     'erlang',
                     'html',
                     'prolog',
                     'restructuredtext',
                     'ruby',
        ]

        std_files = [
            [os.path.join(options.input_dir, "cmake.g4")],
            [os.path.join(options.input_dir, "CPP23.g4")],
            [os.path.join(options.input_dir, "C.g4")],
            [os.path.join(options.input_dir, "CSharpParser.g4"), os.path.join(options.input_dir, "CSharpPreprocessorParser.g4"), os.path.join(options.input_dir, "CSharpLexer.g4")],
            [os.path.join(options.input_dir, "Java9Parser.g4"), os.path.join(options.input_dir, "Java9Lexer.g4")],
            [os.path.join(options.input_dir, "JavaScriptParser.g4"), os.path.join(options.input_dir, "JavaScriptLexer.g4")],
            [os.path.join(options.input_dir, "modellica.g4")],
            [os.path.join(options.input_dir, "PhpParser.g4"), os.path.join(options.input_dir, "PhpLexer.g4")],
            [os.path.join(options.input_dir, "TypescriptParser.g4"), os.path.join(options.input_dir, "TypescriptLexer.g4")],
            [os.path.join(options.input_dir, "ECMAScript.g4")],
            [os.path.join(options.input_dir, "Python3Parser.g4"), os.path.join(options.input_dir, "Python3Lexer.g4")],
            [os.path.join(options.input_dir, "pascal.g4")],
            [os.path.join(options.input_dir, "RustParser.g4"), os.path.join(options.input_dir, "RustLexer.g4")],
            [os.path.join(options.input_dir, "Scala.g4")],
            [os.path.join(options.input_dir, "Clojure.g4")],
            [os.path.join(options.input_dir, "GoParser.g4"), os.path.join(options.input_dir, "GoLexer.g4")],
            [os.path.join(options.input_dir, "DOT.g4")],
            [os.path.join(options.input_dir, "Erlang.g4")],
            [os.path.join(options.input_dir, "HTMLParser.g4"), os.path.join(options.input_dir, "HTMLLexer.g4")],
            [os.path.join(options.input_dir, "prolog.g4")],
            [os.path.join(options.input_dir, "ReStructuredText.g4")],
            [os.path.join(options.input_dir, "Corundum.g4")],
        ]

        for language, language_files in zip(std_languages, std_files):
            valid = True
            for file in language_files:
                if not os.path.exists(file):
                    valid = False
            if valid:
                languages.append(language)
                files.append(language_files)
    else:
        language = options.language

        file_list = []
        for file in args:
            _, f = os.path.split(file)
            file = os.path.join(options.input_dir, f)

            if os.path.exists(file):
                file_list.append(file)
            else:
                sys.exit(f"The input grammar file {file} does not exist!")

        files.append(file_list)
        languages.append(language)

    printTokens = []
    for token in re.split(r',\s*\n|[,\n ]', options.print_tokens):
        printTokens.append('enter' + token)
        printTokens.append('exit' + token)

    options.print_tokens = []

    if options.verbose:
        options.print_tokens = printTokens
        for l, f in zip(languages, files):
            print(l, "->", f)
        print("")

    index_cnt = 0

    terminalTokens = re.split(r',\s*\n|[,\n ]', options.terminal_tokens)

    patternMapping = re.compile(r'^\s*(.*?)\s*=> ::\s*(.*?)\s*$')

    for language, language_files in zip(languages, files):

        options.placeholders = []
        options.placeholders_map = {}
        options.placeholders_set = set()
        options.terminals = set()
        options.quotedTerminals = set()
        options.ruleSpec = {}
        options.lexerRuleSpec = {}
        options.quotedLexerRuleSpec = {}
        options.unquotedLexerRuleSpec = {}
        options.non_space_separated_map: Dict[str, List[str]] = {}

        for t in terminalTokens:
            options.placeholders_set.add(t)

        if options.read_placeholders:
            input_file = language + '.map'
            input_path = os.path.join(options.input_dir, input_file)

            if os.path.exists(input_path):
                with open(input_path, mode='r') as input:
                    for line in input:
                        line = line.rstrip()
                        if not line.startswith('#'):
                            m = patternMapping.match(line)
                            if m:
                                key = m.group(1)
                                val = m.group(2)
                                options.placeholders_map[key] = val
            else:
                options.read_placeholders = False

        if options.verbose and options.read_placeholders:
            print ("---- placeholders --------------------------------------------------------------------------------")
            for key, val in options.placeholders_map.items():
                print(f"{key} => :: {val}")

        if options.non_space_separated:
            input_file = language + '.spc'
            input_path = os.path.join(options.input_dir, input_file)

            if os.path.exists(input_path):
                with open(input_path, mode='r') as input:
                    for line in input:
                        line = line.rstrip()
                        if not line.startswith('#'):
                            m = patternMapping.match(line)
                            if m:
                                lhs = m.group(1)
                                rhs = m.group(2)
                                if lhs in options.non_space_separated_map:
                                    options.non_space_separated_map[lhs].append(rhs)
                                else:
                                    options.non_space_separated_map[lhs] = list(rhs)

        if options.verbose and options.non_space_separated:
            print ("---- non space parser token separation -----------------------------------------------------------")
            for lhs, val in options.non_space_separated_map.items():
                for rhs in val:
                    print(f"'{lhs}' => :: '{rhs}'")

        start_rule = None
        if options.verbose:
            print (f"Working in language {language}.")
        index_cnt += 1

        output_file = language + '.lse'
        output_path = os.path.join(options.output_dir, output_file)

        with open(output_path, mode='w') as output:
            #
            # Pre processing
            #
            for file in language_files:
                input_stream = FileStream(file, encoding = 'utf8')
                lexer = ANTLRv4Lexer(input_stream)
                stream = CommonTokenStream(lexer)
                parser = ANTLRv4Parser(stream)

                tree = parser.grammarSpec()

                preProcessListener = PreProcessListener(options)
                walker = ParseTreeWalker()
                walker.walk(preProcessListener, tree)

                if start_rule is None:
                    start_rule = preProcessListener.startRule()

            #
            # Process any Antlr g4 files provided for the language
            #
            if start_rule is not None:
                #
                # Write the ELSE language construct
                #
                lang: ElseLanguage = ElseLanguage(output, language, options.punctuation, options.valid_identifier, options.indentation, options.version, options.copyright, start_rule)
                lang.write()

                #
                # Main processing
                #
                for file in language_files:
                    if options.verbose:
                        N = len(file)

                        print("")
                        print(f"== {file} ==")
                        print(len(file) * "-" + "------")

                    input_stream = FileStream(file, encoding = 'utf8')
                    lexer = ANTLRv4Lexer(input_stream)
                    stream = CommonTokenStream(lexer)
                    parser = ANTLRv4Parser(stream)

                    tree = parser.grammarSpec()

                    processListener = ProcessListener(options, output, language)
                    walker = ParseTreeWalker()
                    walker.walk(processListener, tree)
                    processListener.write_else_template(options.print_placeholders)

        if options.write_placeholders:
            output_file = language + '.lst'
            output_path = os.path.join(options.output_dir, output_file)

            with open(output_path, mode='w') as out:
                for entry in options.placeholders:
                    out.write(entry + '\n')

        if options.verbose:
            print ("---- quoteTerminals ------------------------------------------------------------------------------")

            out = []

            for t in options.quotedTerminals:
                out.append(t)

            for e in sorted(out):
                print(e)

            print ("---- terminals -----------------------------------------------------------------------------------")

            out = []

            for t in options.terminals:
                out.append(t)

            for e in sorted(out):
                print(e)


            print ("---- lexerRuleSpec -------------------------------------------------------------------------------")

            out = []

            for key, value in options.lexerRuleSpec.items():
                out.append(key + ": " +  value)

            for e in sorted(out):
                print(e)

            print ("---- quotedLexerRuleSpec -------------------------------------------------------------------------")

            out = []

            for key, value in options.quotedLexerRuleSpec.items():
                out.append(key + ": " +  value)

            for e in sorted(out):
                print(e)

            print ("---- unquotedLexerRuleSpec -----------------------------------------------------------------------")

            out = []

            for key, value in options.unquotedLexerRuleSpec.items():
                out.append(key + ": " +  value)

            for e in sorted(out):
                print(e)

            print ("---- ruleSpec ------------------------------------------------------------------------------------")

            out = []

            for key, value in options.ruleSpec.items():
                out.append(key +  ": " + value)

            for e in sorted(out):
                print(e)

            print ("---- placeholders -------------------------------------------------------------------------------")

            out = []

            for t in options.placeholders_set:
                out.append(t)

            for e in sorted(out):
                print(e)

            print("")

if __name__ == '__main__':
    main()
