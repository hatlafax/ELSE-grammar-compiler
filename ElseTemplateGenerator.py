import sys, re, os
from enum import Enum

from typing import Literal, Optional, TextIO

class ElseLanguage:
    def __init__(self, output: TextIO, language: str, punctuation: str, valid_identifier: str, indentation: int, version: str, copyright: str, start_rule: str) -> None:
        self.output: TextIO = output
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
            self.output.write( 'END DEFINE\n\n\n')


class ElsePlaceholder:
    patternPlaceholder = re.compile(r'^[A-Za-z0-9_]+$')

    SubstituteType  = Enum("SubstituteType", "AUTO_SUBSTITUTE NOAUTO_SUBSTITUTE")
    DuplicationType = Enum("DuplicationType", "CONTEXT_DEPENDENT VERTICAL HORIZONTAL")
    PlaceHolderType = Enum("PlaceHolderType", "TERMINAL NONTERMINAL MENU")
    PlaceHolderMenuAttribute = Enum("PlaceHolderMenuAttribute", "PLACEHOLDER NOFOLLOW FOLLOW DESCRIPTION")

    def __init__(self, output, language: str) -> None:
        self.output: str = output
        self.language: str = language
        self.initialize()

    def initialize(self) -> None:
        self.placeholder_name: str|None = None
        self.placeholder_type: ElsePlaceholder.PlaceHolderType = ElsePlaceholder.PlaceHolderType.NONTERMINAL
        self.substitute_type: SubstituteType = ElsePlaceholder.SubstituteType.NOAUTO_SUBSTITUTE
        self.substitute_count: int = 1
        self.description = ""
        self.duplication_type: DuplicationType = ElsePlaceholder.DuplicationType.CONTEXT_DEPENDENT
        self.placeholder_menu_attributes: Dict[str, Set[PlaceHolderMenuAttribute]] = {}
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

    def add_placeholder_attribute(self, entry: str, placeholder_attribute: PlaceHolderMenuAttribute) -> None:
        if entry not in self.placeholder_menu_attributes:
            self.placeholder_menu_attributes[entry] = set()

        self.placeholder_menu_attributes[entry].add(placeholder_attribute)

    def remove_placeholder_attribute(self, entry: str, placeholder_attribute: PlaceHolderMenuAttribute) -> None:
        if entry in self.placeholder_menu_attributes:
            if placeholder_attribute in self.placeholder_menu_attributes[entry]:
                self.placeholder_menu_attributes[entry].remove(placeholder_attribute)

    def has_placeholder_attribute(self, entry, placeholder_attribute: PlaceHolderMenuAttribute) -> bool:
        if entry in self.placeholder_menu_attributes:
            if placeholder_attribute in self.placeholder_menu_attributes[entry]:
                return True
        return False

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

        for s in self.content.split('\n'):
            if self.placeholder_type is ElsePlaceholder.PlaceHolderType.MENU:
                menu_attributes = ""
                if s in self.placeholder_menu_attributes:
                    for attribute in self.placeholder_menu_attributes[s]:
                        menu_attributes += f"/{attribute.name}"
                self.output.write(f'    "{s}"{menu_attributes}\n')
            else:
                self.output.write(f'    "{s}"\n')

        self.output.write(     'END DEFINE\n\n\n')

        self.initialize()
