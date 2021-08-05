import sys, re, os
from enum import Enum

class ElseLanguage:
    def __init__(self, output, language: str, punctuation: str, valid_identifier: str, indentation: int, version: str, copyright: str, start_rule: str) -> None:
        self.output: str = output
        self.language: str = language
        self.punctuation: str = punctuation
        self.valid_identifier: str = valid_identifier
        self.indentation: int = indentation
        self.version: str = version
        self.copyright: str = copyright
        self.start_rule = start_rule

    def write(self) -> None:
        if self.start_rule is not None:
            self.output.write(self.copyright)
            self.output.write('\n')
            self.output.write(f'DELETE LANGUAGE {self.language}\n')
            self.output.write(f'DEFINE LANGUAGE {self.language}\n')
            self.output.write(f'    /INITIAL_STRING="{{{self.start_rule}}}"\n')
            self.output.write(f'    /PUNCTUATION_CHARACTERS="{self.punctuation}"\n')
            self.output.write(f'    /VALID_IDENTIFIER_CHARACTERS="{self.valid_identifier}"\n')
            self.output.write(f'    /INDENT_SIZE={self.indentation}\n')
            self.output.write(f'    /VERSION={self.version}\n')
            self.output.write( 'END DEFINE\n\n')


class ElsePlaceholder:
    patternPlaceholder = re.compile(r'^[A-Za-z0-9_]+$')

    SubstituteType = Enum("SubstituteType", "AUTO_SUBSTITUTE NOAUTO_SUBSTITUTE")
    DuplicationType = Enum("DuplicationType", "CONTEXT_DEPENDENT VERTICAL HORIZONTAL")
    PlaceHolderType = Enum("PlaceHolderType", "TERMINAL NONTERMINAL MENU")

    def __init__(self, output, language: str) -> None:
        self.output: str = output
        self.language: str = language
        self.initialize()

    def initialize(self) -> None:
        self.placeholder_name: str = None
        self.placeholder_type: PlaceHolderType = ElsePlaceholder.PlaceHolderType.NONTERMINAL
        self.substitute_type: SubstituteType = ElsePlaceholder.SubstituteType.NOAUTO_SUBSTITUTE
        self.substitute_count: int = 1
        self.description = ""
        self.duplication_type: DuplicationType = ElsePlaceholder.DuplicationType.CONTEXT_DEPENDENT
        self.separator: str = ""
        self.content: str = ""


    def set_placeholder_name(self, placeholder_name: str) -> None:
        self.placeholder_name: str = placeholder_name

    def set_placeholder_type(self, placeholder_type: PlaceHolderType) -> None:
        self.placeholder_type: str = placeholder_type

    def set_substitute_type(self, substitute_type: SubstituteType) -> None:
        self.substitute_type: SubstituteType = substitute_type

    def set_substitute_count(self, substitute_count: int) -> None:
        self.substitute_count: int = substitute_count

    def set_content(self, content: str) -> None:
        self.content: str = content

    def set_description(self, description: str) -> None:
        self.description: str = description

    def set_duplication_type(self, duplication_type: DuplicationType) -> None:
        self.duplication_type: DuplicationType = duplication_type

    def set_separator(self, separator: str) -> None:
        self.separator: str = separator

    def write(self) -> None:
        if self.placeholder_name is None:
            return

        #name = self.placeholder_name.upper()
        name = self.placeholder_name

        m = ElsePlaceholder.patternPlaceholder.match(self.placeholder_name)
        if m:
            self.output.write(f'DELETE PLACEHOLDER {name}\n')
            self.output.write(f'    /LANGUAGE="{self.language}"\n')
            self.output.write(f'DEFINE PLACEHOLDER {name}\n')
            self.output.write(f'    /LANGUAGE="{self.language}"\n')
        else:
            self.output.write(f'DELETE PLACEHOLDER "{name}"\n')
            self.output.write(f'    /LANGUAGE="{self.language}"\n')
            self.output.write(f'DEFINE PLACEHOLDER "{name}"\n')
            self.output.write(f'    /LANGUAGE="{self.language}"\n')

        self.output.write(    f'    /{self.substitute_type.name}\n')
        self.output.write(    f'    /SUBSTITUTE_COUNT={self.substitute_count}\n')
        self.output.write(    f'    /DESCRIPTION="{self.description}"\n')
        self.output.write(    f'    /DUPLICATION={self.duplication_type.name}\n')
        self.output.write(    f'    /SEPARATOR="{self.separator}"\n')
        self.output.write(    f'    /TYPE={self.placeholder_type.name}\n')

        #self.output.write('\n')
        for s in self.content.split('\n'):
            self.output.write(f'    "{s}"\n')
        #self.output.write('\n')
        self.output.write(     'END DEFINE\n\n')

        self.initialize()
