grammar CPP23;

//
// n4981 working draft
//


//
// A.1 General

//
// A.2 Keywords
//


//
// A.3 Lexical conventions
//
n_char
  : '<<<Enter a n_char sequence, that is translation characters except of { or \\n.>>>'
  ;


named_universal_character
  : '\\N{' NOSPC n_char NOSPC '}'
  ;

hexadecimal_digit
  : '<<<Enter a hexadecimal digit, i.e. any number of hex characters [0-9a-fA-F].>>>'
  ;

hex_quad
  : '<<<Enter exactly four hex number characters [0-9a-fA-F], i.e. NNNN.>>>'
  ;

hex_quad_quad
  : '<<<Enter exactly eight hex number characters [0-9a-fA-F], i.e. NNNNNNNN.>>>'
  ;

//
// Universal character names are formed by a prefix \U followed by an eight-digit Unicode code point, or by a
// prefix \u followed by a four-digit Unicode code point. All eight or four digits, respectively, must be present
// to make a well-formed universal character name.
//
universal_character_name
  : '\\u' NOSPC hex_quad
  | '\\U' NOSPC hex_quad_quad
  | '\\u{' NOSPC hexadecimal_digit NOSPC '}'
  | named_universal_character
  ;

non_whitespace_character_literal
  : '<<<Each non_whitespace character that cannot be one of the above.>>>'
  ;

preprocessing_token
  : header_name
  | 'import'
  | 'module'
  | 'export'
  | identifier
  | pp_number
  | character_literal
  | user_defined_character_literal
  | string_literal
  | user_defined_string_literal
  | preprocessing_op_or_punc
  | non_whitespace_character_literal
  ;

token
  : identifier
  | keyword
  | literal
  | operator_or_punctuator
  ;

h_char
  : '<<<Enter a h_char sequence, i.e. source characters except \\n and > characters.>>>'
  ;

q_char
  : '<<<Enter a q_char sequence, i.e. source characters except \\n and quotation mark " characters.>>>'
  ;

header_name
  : '<' NOSPC h_char NOSPC '>'
  | '"' NOSPC q_char NOSPC '"'
  ;

pp_number
  : digit
  | '.' NOSPC digit
  | pp_number NOSPC digit
  | pp_number NOSPC identifier_nondigit
  | pp_number NOSPC '\'' NOSPC digit
  | pp_number NOSPC '\'' NOSPC nondigit
  | pp_number NOSPC 'e' NOSPC sign
  | pp_number NOSPC 'E' NOSPC sign
  | pp_number NOSPC 'p' NOSPC sign
  | pp_number NOSPC 'P' NOSPC sign
  | pp_number NOSPC '.'
  ;

identifier
  : '<<<Enter a valid C++ identifier.>>>'
  ;

//identifier
//  : identifier_start
//  | identifier identifier_continue
//  ;
//

identifier_nondigit
  : '<<<Enter a valid C++ identifier that is not a digit.>>>'
  ;

//translation_character_xid_start
//  : '<<<Enter an element of the translation character set with the Unicode property XID_Start.>>>'
//  ;
//
//translation_character_xid_continue
//  : '<<<Enter an element of the translation character set with the Unicode property XID_Continue.>>>'
//  ;
//
//identifier_start
//  : nondigit
//  | translation_character_xid_start
//  ;
//
//identifier_continue
//  : digit
//  | nondigit
//  | translation_character_xid_continue
//  ;

nondigit
  : 'a'
  | 'b'
  | 'c'
  | 'd'
  | 'e'
  | 'f'
  | 'g'
  | 'h'
  | 'i'
  | 'j'
  | 'k'
  | 'l'
  | 'm'
  | 'n'
  | 'o'
  | 'p'
  | 'q'
  | 'r'
  | 's'
  | 't'
  | 'u'
  | 'v'
  | 'w'
  | 'x'
  | 'y'
  | 'z'
  | 'A'
  | 'B'
  | 'C'
  | 'D'
  | 'E'
  | 'F'
  | 'G'
  | 'H'
  | 'I'
  | 'J'
  | 'K'
  | 'L'
  | 'M'
  | 'N'
  | 'O'
  | 'P'
  | 'Q'
  | 'R'
  | 'S'
  | 'T'
  | 'U'
  | 'V'
  | 'W'
  | 'X'
  | 'Y'
  | 'Z'
  | '_'
  ;

digit
  : '0'
  | '1'
  | '2'
  | '3'
  | '4'
  | '5'
  | '6'
  | '7'
  | '8'
  | '9'
  ;

keyword
  : 'alignas'
  | 'alignof'
  | 'asm'
  | 'auto'
  | 'bool'
  | 'break'
  | 'case'
  | 'catch'
  | 'char'
  | 'char8_t'
  | 'char16_t'
  | 'char32_t'
  | 'class'
  | 'concept'
  | 'const'
  | 'consteval'
  | 'constexpr'
  | 'constinit'
  | 'const_cast'
  | 'continue'
  | 'co_await'
  | 'co_return'
  | 'co_yield'
  | 'decltype'
  | 'default'
  | 'delete'
  | 'do'
  | 'double'
  | 'dynamic_cast'
  | 'else'
  | 'enum'
  | 'explicit'
  | 'export'
  | 'extern'
  | 'false'
  | 'float'
  | 'for'
  | 'friend'
  | 'goto'
  | 'if'
  | 'import'
  | 'inline'
  | 'int'
  | 'long'
  | 'module'
  | 'mutable'
  | 'namespace'
  | 'new'
  | 'noexcept'
  | 'nullptr'
  | 'operator'
  | 'private'
  | 'protected'
  | 'public'
  | 'register'
  | 'reinterpret_cast'
  | 'requires'
  | 'return'
  | 'short'
  | 'signed'
  | 'sizeof'
  | 'static'
  | 'static_assert'
  | 'static_cast'
  | 'struct'
  | 'switch'
  | 'template'
  | 'this'
  | 'thread_local'
  | 'throw'
  | 'true'
  | 'try'
  | 'typedef'
  | 'typeid'
  | 'typename'
  | 'union'
  | 'unsigned'
  | 'using'
  | 'virtual'
  | 'void'
  | 'volatile'
  | 'wchar_t'
  | 'while'
  ;

import_keyword
  : 'import'
  ;

module_keyword
  : 'module'
  ;

export_keyword
  : 'export'
  ;

preprocessing_op_or_punc
  : preprocessing_operator
  | operator_or_punctuator
  ;

preprocessing_operator
  : '#'
  | '##'
  | '%:'
  | '%:%:'
  ;

operator_or_punctuator
  : '{'
  | '}'
  | '['
  | ']'
  | '('
  | ')'
  | '<:'
  | ':>'
  | '<%'
  | '%>'
  | ';'
  | ':'
  | '...'
  | '?'
  | '::'
  | '.'
  | '.*'
  | '->'
  | '->*'
  | '~'
  | '!'
  | '+'
  | '-'
  | '*'
  | '/'
  | '%'
  | '^'
  | '&'
  | '|'
  | '='
  | '+='
  | '-='
  | '*='
  | '/='
  | '%='
  | '^='
  | '&='
  | '|='
  | '=='
  | '!='
  | '<'
  | '>'
  | '<='
  | '>='
  | '<=>'
  | '&&'
  | '||'
  | '<<'
  | '>>'
  | '<<='
  | '>>='
  | '++'
  | '--'
  | ','
  | 'and'
  | 'or'
  | 'xor'
  | 'not'
  | 'bitand'
  | 'bitor'
  | 'compl'
  | 'and_eq'
  | 'or_eq'
  | 'xor_eq'
  | 'not_eq'
  ;


//
// Literals are fundamental elements used to represent constant values used in C++ programming language.
// These constants can include numbers, characters, strings, and more.
//
literal
  : integer_literal
  | character_literal
  | floating_point_literal
  | string_literal
  | boolean_literal
  | pointer_literal
  | user_defined_literal
  ;

integer_literal
  : binary_literal NOSPC integer_suffix ?
  | octal_literal NOSPC integer_suffix ?
  | decimal_literal NOSPC integer_suffix ?
  | hexadecimal_literal NOSPC integer_suffix ?
  ;

simple_quote_char
  : '\''
  ;

binary_literal
  : '0b' NOSPC binary_digit
  | '0B' NOSPC binary_digit
  | binary_literal NOSPC simple_quote_char ? NOSPC binary_digit
  ;

octal_literal
  : '0'
  | octal_literal NOSPC simple_quote_char ? NOSPC octal_digit
  ;

decimal_literal
  : nonzero_digit
  | decimal_literal NOSPC simple_quote_char ? NOSPC digit
  ;

hexadecimal_literal
  : hexadecimal_prefix NOSPC hexadecimal_digit_sequence
  ;

binary_digit
  : '0'
  | '1'
  ;

octal_digit
  : '0'
  | '1'
  | '2'
  | '3'
  | '4'
  | '5'
  | '6'
  | '7'
  ;

nonzero_digit
  : '1'
  | '2'
  | '3'
  | '4'
  | '5'
  | '6'
  | '7'
  | '8'
  | '9'
  ;

hexadecimal_prefix
  : '0x'
  | '0X'
  ;

hexadecimal_digit_sequence
  : hexadecimal_digit
  | hexadecimal_digit_sequence NOSPC simple_quote_char ? NOSPC hexadecimal_digit
  ;

integer_suffix
  : unsigned_suffix  NOSPC long_suffix ?
  | unsigned_suffix  NOSPC long_long_suffix ?
  | unsigned_suffix  NOSPC size_suffix ?
  | long_suffix      NOSPC unsigned_suffix ?
  | long_long_suffix NOSPC unsigned_suffix ?
  | size_suffix      NOSPC unsigned_suffix ?
  ;

unsigned_suffix
  : 'u'
  | 'U'
  ;

long_suffix
  : 'l'
  | 'L'
  ;

long_long_suffix
  : 'll'
  | 'LL'
  ;

size_suffix
  : 'z'
  | 'Z'
  ;

//
// Character literals
//    auto c0 =   'A'; // char
//    auto c1 = u8'A'; // char
//    auto c2 =  L'A'; // wchar_t
//    auto c3 =  u'A'; // char16_t
//    auto c4 =  U'A'; // char32_t
//
// Multicharacter literals
//    auto m0 = 'abcd'; // int, value 0x61626364
//
character_literal
  : encoding_prefix ? NOSPC '\'' NOSPC c_char+ NOSPC '\''
  ;

encoding_prefix
  : 'u8'
  | 'u'
  | 'U'
  | 'L'
  ;

c_char
  : basic_c_char
  | escape_sequence
  | universal_character_name
  ;

basic_c_char
  : '<<<Enter a basic source character except the single_quote \', backslash \\, or new_line \\n character.>>>'
  ;


//
// Escape sequences
//    newline            \n
//    backslash          \\
//    horizontal tab     \t
//    question mark      ? or \?
//    vertical tab       \v
//    single quote       \'
//    backspace          \b
//    double quote       \"
//    carriage return    \r
//    the null character \0
//    form feed          \f
//    octal              \ooo
//    alert (bell)       \a
//    hexadecimal        \xhhh
//
escape_sequence
  : simple_escape_sequence
  | numeric_escape_sequence
  | conditional_escape_sequence
  ;

simple_escape_sequence
  : '\\' NOSPC simple_escape_sequence_char
  ;

simple_escape_sequence_char
  : '\''
  | '"'
  | '?'
  | '\\'
  | 'a'
  | 'b'
  | 'f'
  | 'n'
  | 'r'
  | 't'
  | 'v'
  ;

numeric_escape_sequence
  : octal_escape_sequence
  | hexadecimal_escape_sequence
  ;

octal_escape_sequence
  : '\\' NOSPC octal_digit
  | '\\' NOSPC octal_digit NOSPC octal_digit
  | '\\' NOSPC octal_digit NOSPC octal_digit NOSPC octal_digit
  | '\\o{' NOSPC octal_digit+ NOSPC '}'
  ;

hexadecimal_escape_sequence
  : '\\x' NOSPC hexadecimal_digit
  | '\\x{' NOSPC hexadecimal_digit NOSPC '}'
  ;

conditional_escape_sequence
  : '\\' NOSPC conditional_escape_sequence_char
  ;

conditional_escape_sequence_char
  : '<<<Enter a basic source character that is not an octal_digit, a simple_escape_sequence_char, or the characters N, o, u, U, or x.>>>'
  ;

floating_point_literal
  : decimal_floating_point_literal
  | hexadecimal_floating_point_literal
  ;

decimal_floating_point_literal
  : fractional_constant exponent_part ? NOSPC floating_point_suffix ?
  | digit_sequence NOSPC exponent_part  NOSPC floating_point_suffix ?
  ;

hexadecimal_floating_point_literal
  : hexadecimal_prefix NOSPC hexadecimal_fractional_constant NOSPC binary_exponent_part NOSPC floating_point_suffix ?
  | hexadecimal_prefix NOSPC hexadecimal_digit_sequence      NOSPC binary_exponent_part NOSPC floating_point_suffix ?
  ;

fractional_constant
  : digit_sequence ? NOSPC '.' NOSPC digit_sequence
  | digit_sequence   NOSPC '.'
  ;

hexadecimal_fractional_constant
  : hexadecimal_digit_sequence ? NOSPC '.' NOSPC hexadecimal_digit_sequence
  | hexadecimal_digit_sequence   NOSPC '.'
  ;

exponent_part
  : 'e' NOSPC sign ? NOSPC digit_sequence
  | 'E' NOSPC sign ? NOSPC digit_sequence
  ;

binary_exponent_part
  : 'p' NOSPC sign ? NOSPC digit_sequence
  | 'P' NOSPC sign ? NOSPC digit_sequence
  ;

sign
  : '+'
  | '-'
  ;

digit_sequence
  : digit
  | digit_sequence NOSPC simple_quote_char ? NOSPC digit
  ;

floating_point_suffix
  : 'f'
  | 'l'
  | 'f16'
  | 'f32'
  | 'f64'
  | 'f128'
  | 'bf16'
  | 'F'
  | 'L'
  | 'F16'
  | 'F32'
  | 'F64'
  | 'F128'
  | 'BF16'
  ;

//
// String literals
//    auto s0 =   "hello"; // const char*
//    auto s1 = u8"hello"; // const char* before C++20, encoded as UTF-8,
//                         // const char8_t* in C++20
//    auto s2 =  L"hello"; // const wchar_t*
//    auto s3 =  u"hello"; // const char16_t*, encoded as UTF-16
//    auto s4 =  U"hello"; // const char32_t*, encoded as UTF-32
//
string_literal
  : encoding_prefix ? NOSPC '"' NOSPC s_char* NOSPC '"'
  | encoding_prefix ? NOSPC 'R' NOSPC raw_string
  ;

s_char
  : basic_s_char
  | escape_sequence
  | universal_character_name
  ;

basic_s_char
  : '<<<Enter a basic source character except the double_quote ", backslash \\, or new_line \\n character.>>>'
  ;


//
// Raw string literals containing unescaped \ and "
//    auto R0 =   R"("Hello \ world")"; // const char*
//    auto R1 = u8R"("Hello \ world")"; // const char* before C++20, encoded as UTF-8,
//                                      // const char8_t* in C++20
//    auto R2 =  LR"("Hello \ world")"; // const wchar_t*
//    auto R3 =  uR"("Hello \ world")"; // const char16_t*, encoded as UTF-16
//    auto R4 =  UR"("Hello \ world")"; // const char32_t*, encoded as UTF-32
//
//    auto R5 =   R"_abc_("Hello \ world")_abc_"; // const char*
//
raw_string
  : '"' NOSPC d_char* NOSPC '(' NOSPC r_char* NOSPC ')' NOSPC d_char* NOSPC '"'
  ;

r_char
  : '<<<Enter a sequence of source characters, except a right parenthesis ) followed by the initial d_char sequence (which may be empty) followed by a double quote ".>>>'
  ;

d_char
  : '<<<Enter a sequence of basic source characters except: space, the left parenthesis (, the right parenthesis ), the backslash \\, and the control characters representing horizontal tab, vertical tab, form feed, and newline.>>>'
  ;

//
// An unevaluated_string shall have no encoding_prefix.
// Each universal_character_name and each simple_escape_sequence in an unevaluated_string is replaced by the
// member of the translation character set it denotes. An unevaluated_string that contains a numeric_escape_sequence
// or a conditional_escape_sequence is ill-formed.
//
// string_literals can appear in a context where they are not used to initialize a character array, but
// are used at compile time for diagnostic messages, preprocessing, and other implementation-
// defined behaviors.
// A string-literal can appear in _Pragma, asm, extern, static_assert, [[deprecated]] and [[nodiscard]]
// attributes...
// In all of these cases, the strings are exclusively used at compile time by the compiler, and are as such not evaluated.
// This means they should not be converted to the narrow encoding or any literal encoding specified by an encoding
// prefix (L, u, U, u8).
//
unevaluated_string
  : '"' NOSPC s_char* NOSPC '"'
  | 'R' NOSPC raw_string
  ;

boolean_literal
  : 'false'
  | 'true'
  ;

pointer_literal
  : 'nullptr'
  ;

user_defined_literal
  : user_defined_integer_literal
  | user_defined_floating_point_literal
  | user_defined_string_literal
  | user_defined_character_literal
  ;

user_defined_integer_literal
  : decimal_literal     NOSPC ud_suffix
  | octal_literal       NOSPC ud_suffix
  | hexadecimal_literal NOSPC ud_suffix
  | binary_literal      NOSPC ud_suffix
  ;

user_defined_floating_point_literal
  : fractional_constant NOSPC exponent_part ? NOSPC ud_suffix
  | digit_sequence NOSPC exponent_part        NOSPC ud_suffix
  | hexadecimal_prefix NOSPC hexadecimal_fractional_constant NOSPC binary_exponent_part NOSPC ud_suffix
  | hexadecimal_prefix NOSPC hexadecimal_digit_sequence      NOSPC binary_exponent_part NOSPC ud_suffix
  ;

//
// Combining string literals with standard s-suffix
//    auto S0 =   "hello"s; // std::string
//    auto S1 = u8"hello"s; // std::string before C++20, std::u8string in C++20
//    auto S2 =  L"hello"s; // std::wstring
//    auto S3 =  u"hello"s; // std::u16string
//    auto S4 =  U"hello"s; // std::u32string
//
// Combining raw string literals with standard s-suffix
//    auto S5 =   R"("Hello \ world")"s; // std::string from a raw const char*
//    auto S6 = u8R"("Hello \ world")"s; // std::string from a raw const char* before C++20, encoded as UTF-8,
//                                       // std::u8string in C++20
//    auto S7 =  LR"("Hello \ world")"s; // std::wstring from a raw const wchar_t*
//    auto S8 =  uR"("Hello \ world")"s; // std::u16string from a raw const char16_t*, encoded as UTF-16
//    auto S9 =  UR"("Hello \ world")"s; // std::u32string from a raw const char32_t*, encoded as UTF-32
//
user_defined_string_literal
  : string_literal NOSPC ud_suffix
  ;

user_defined_character_literal
  : character_literal NOSPC ud_suffix
  ;

ud_suffix
  : identifier
  ;

//
// A.4 Basics
//

//
// A translation unit is the basic unit of compilation in C++. It consists of the contents of a single source file,
// plus the contents of any header files directly or indirectly included by it, minus those lines that were ignored
// using conditional preprocessing statements.
//
translation_unit
  : declaration*
  | global_module_fragment ? module_declaration declaration* private_module_fragment ?
  ;

//
// A.5 Expressions
//

primary_expression
  : literal
  | 'this'
  | '(' NOSPC expression NOSPC ')'
  | id_expression
  | lambda_expression
  | fold_expression
  | requires_expression
  ;

id_expression
  : unqualified_id
  | qualified_id
  | pack_index_expression
  ;

unqualified_id
  : identifier
  | operator_function_id
  | conversion_function_id
  | literal_operator_id
  | '~' NOSPC type_name
  | '~' NOSPC computed_type_specifier
  | template_id
  ;

template
  : 'template'
  ;

qualified_id
  : nested_name_specifier template ? unqualified_id
  ;

nested_name_specifier
  : '::'
  | type_name NOSPC '::'
  | namespace_name NOSPC '::'
  | computed_type_specifier NOSPC '::'
  | nested_name_specifier identifier NOSPC '::'
  | nested_name_specifier template ? simple_template_id NOSPC '::'
  ;

pack_index_expression
  : id_expression NOSPC '... [' NOSPC constant_expression NOSPC ']'
  ;

lambda_expression
  : lambda_introducer attribute_specifier* lambda_declarator compound_statement
  | lambda_introducer NOSPC '<' NOSPC template_parameter_list NOSPC '>' requires_clause ? attribute_specifier* lambda_declarator compound_statement
  ;

lambda_introducer
  : '[' NOSPC lambda_capture ? NOSPC ']'
  ;

lambda_declarator
  : lambda_specifier+ noexcept_specifier ? attribute_specifier* trailing_return_type ?
  | noexcept_specifier attribute_specifier* trailing_return_type ?
  | trailing_return_type ?
  | '(' NOSPC parameter_declaration_clause NOSPC ')' lambda_specifier* noexcept_specifier ? attribute_specifier* trailing_return_type ? requires_clause ?
  ;

lambda_specifier
  : 'consteval'
  | 'constexpr'
  | 'mutable'
  | 'static'
  ;

lambda_capture
  : capture_default
  | capture_list
  | capture_default NOSPC ',' capture_list
  ;

capture_default
  : '&'
  | '='
  ;

capture_list
  : capture
  | capture_list NOSPC ',' capture
  ;

capture
  : simple_capture
  | init_capture
  ;

simple_capture
  : identifier NOSPC three_dots ?
  | '&' NOSPC identifier NOSPC three_dots ?
  | 'this'
  | '*this'
  ;

and_three_dots
  : '& ...'
  ;

init_capture
  : three_dots ? NOSPC identifier initializer
  | and_three_dots ? NOSPC identifier initializer
  ;

fold_expression
  : '(' NOSPC cast_expression fold_operator NOSPC '...)'
  | '(...' fold_operator cast_expression NOSPC ')'
  | '(' NOSPC cast_expression fold_operator NOSPC '...' fold_operator cast_expression ')'
  ;

fold_operator
  : '+'
  | '-'
  | '*'
  | '/'
  | '%'
  | '^'
  | '&'
  | '|'
  | '<<'
  | '>>'
  | '+='
  | '-='
  | '*='
  | '/='
  | '%='
  | '^='
  | '&='
  | '|='
  | '<<='
  | '>>='
  | '='
  | '=='
  | '!='
  | '<'
  | '>'
  | '<='
  | '>='
  | '&&'
  | '||'
  | ','
  | '.*'
  | '->*'
  ;

requires_expression
  : 'requires' requirement_parameter_list ? requirement_body
  ;

requirement_parameter_list
  : '(' NOSPC parameter_declaration_clause NOSPC ')'
  ;

requirement_body
  : '{' NOSPC requirement+ NOSPC '}'
  ;

requirement
  : simple_requirement
  | type_requirement
  | compound_requirement
  | nested_requirement
  ;

simple_requirement
  : expression NOSPC ';'
  ;

type_requirement
  : 'typename' nested_name_specifier ? type_name NOSPC ';'
  ;

compound_requirement
  : '{' NOSPC expression NOSPC '}' noexcept ? return_type_requirement ? NOSPC ';'
  ;

return_type_requirement
  : '->' type_constraint
  ;

nested_requirement
  : 'requires' constraint_expression NOSPC ';'
  ;

dot_template
  : '.template'
  ;

arrow_template
  : '->template'
  ;

postfix_expression
  : primary_expression
  | postfix_expression NOSPC '[' NOSPC expression_list ? NOSPC ']'
  | postfix_expression NOSPC '(' NOSPC expression_list ? NOSPC ')'
  | simple_type_specifier NOSPC '(' NOSPC expression_list ? NOSPC ')'
  | typename_specifier NOSPC '(' NOSPC expression_list ? NOSPC ')'
  | simple_type_specifier braced_init_list
  | typename_specifier braced_init_list
  | postfix_expression NOSPC dot_template ? id_expression
  | postfix_expression NOSPC arrow_template ? id_expression
  | postfix_expression NOSPC '++'
  | postfix_expression NOSPC '--'
  | 'dynamic_cast<'     NOSPC type_id NOSPC '>(' NOSPC expression NOSPC ')'
  | 'static_cast<'      NOSPC type_id NOSPC '>(' NOSPC expression NOSPC ')'
  | 'reinterpret_cast<' NOSPC type_id NOSPC '>(' NOSPC expression NOSPC ')'
  | 'const_cast<'       NOSPC type_id NOSPC '>(' NOSPC expression NOSPC ')'
  | 'typeid(' NOSPC expression NOSPC ')'
  | 'typeid(' NOSPC type_id NOSPC ')'
  ;

expression_list
  : initializer_list
  ;

unary_expression
  : postfix_expression
  | unary_operator cast_expression
  | '++' NOSPC cast_expression
  | '--' NOSPC cast_expression
  | await_expression
  | 'sizeof' unary_expression
  | 'sizeof(' NOSPC type_id NOSPC ')'
  | 'sizeof...(' NOSPC identifier NOSPC ')'
  | 'alignof(' NOSPC type_id NOSPC ')'
  | noexcept_expression
  | new_expression
  | delete_expression
  ;

unary_operator
  : '*'
  | '&'
  | '+'
  | '-'
  | '!'
  | '~'
  ;

await_expression
  : 'co_await' cast_expression
  ;

noexcept_expression
  : 'noexcept(' NOSPC expression NOSPC ')'
  ;

nesting_operator
  : '::'
  ;

new_expression
  : nesting_operator ? 'new' NOSPC new_placement ? NOSPC new_type_id new_initializer ?
  | nesting_operator ? 'new' NOSPC new_placement ? NOSPC '(' NOSPC type_id NOSPC ')' NOSPC new_initializer ?
  ;

new_placement
  : '(' NOSPC expression_list NOSPC ')'
  ;

new_type_id
  : type_specifier_seq new_declarator ?
  ;

new_declarator
  : ptr_operator new_declarator ?
  | noptr_new_declarator
  ;

noptr_new_declarator
  : '[' NOSPC expression ? NOSPC ']' attribute_specifier*
  | noptr_new_declarator NOSPC '[' NOSPC constant_expression NOSPC ']' attribute_specifier*
  ;

new_initializer
  : '(' NOSPC expression_list ? NOSPC ')'
  | braced_init_list
  ;

delete_expression
  : nesting_operator ? 'delete' cast_expression
  | nesting_operator ? 'delete[]' cast_expression
  ;

cast_expression
  : unary_expression
  | '(' NOSPC type_id NOSPC ')' cast_expression
  ;

pm_expression
  : cast_expression
  | pm_expression NOSPC '.*' cast_expression
  | pm_expression NOSPC '->*' cast_expression
  ;

multiplicative_expression
  : pm_expression
  | multiplicative_expression '*' pm_expression
  | multiplicative_expression '/' pm_expression
  | multiplicative_expression '%' pm_expression
  ;

additive_expression
  : multiplicative_expression
  | additive_expression '+' multiplicative_expression
  | additive_expression '-' multiplicative_expression
  ;

shift_expression
  : additive_expression
  | shift_expression '<<' additive_expression
  | shift_expression '>>' additive_expression
  ;

compare_expression
  : shift_expression
  | compare_expression '<=>' shift_expression
  ;

relational_expression
  : compare_expression
  | relational_expression '<' compare_expression
  | relational_expression '>' compare_expression
  | relational_expression '<=' compare_expression
  | relational_expression '>=' compare_expression
  ;

equality_expression
  : relational_expression
  | equality_expression '==' relational_expression
  | equality_expression '!=' relational_expression
  ;

and_expression
  : equality_expression
  | and_expression '&' equality_expression
  ;

exclusive_or_expression
  : and_expression
  | exclusive_or_expression '^' and_expression
  ;

inclusive_or_expression
  : exclusive_or_expression
  | inclusive_or_expression '|' exclusive_or_expression
  ;

logical_and_expression
  : inclusive_or_expression
  | logical_and_expression '&&' inclusive_or_expression
  ;

logical_or_expression
  : logical_and_expression
  | logical_or_expression '||' logical_and_expression
  ;

conditional_expression
  : logical_or_expression
  | logical_or_expression '?' expression ':' assignment_expression
  ;

yield_expression
  : 'co_yield' assignment_expression
  | 'co_yield' braced_init_list
  ;

throw_expression
  : 'throw' assignment_expression ?
  ;

assignment_expression
  : conditional_expression
  | yield_expression
  | throw_expression
  | logical_or_expression assignment_operator initializer_clause
  ;

assignment_operator
  : '='
  | '*='
  | '/='
  | '%='
  | '+='
  | '-='
  | '>>='
  | '<<='
  | '&='
  | '^='
  | '|='
  ;

expression
  : assignment_expression
  | expression NOSPC ',' assignment_expression
  ;

constant_expression
  : conditional_expression
  ;

statement
  : labeled_statement
  | attribute_specifier* expression_statement
  | attribute_specifier* compound_statement
  | attribute_specifier* selection_statement
  | attribute_specifier* iteration_statement
  | attribute_specifier* jump_statement
  | declaration_statement
  | attribute_specifier* try_block
  ;

init_statement
  : expression_statement
  | simple_declaration
  | alias_declaration
  ;

condition
  : expression
  | attribute_specifier* decl_specifier_seq declarator brace_or_equal_initializer
  ;

label
  : attribute_specifier* identifier ':'
  | attribute_specifier* 'case' constant_expression NOSPC ':'
  | attribute_specifier* 'default:'
  ;

labeled_statement
  : label statement
  ;

expression_statement
  : expression ? NOSPC ';'
  ;

compound_statement
  : '{' NOSPC statement* label* NOSPC '}'
  ;

if_constexpr
  : 'if constexpr'
  ;

if_exlamation_mark
  : 'if !'
  ;

selection_statement
  : if_constexpr ? '(' NOSPC init_statement ? condition NOSPC ')' statement
  | if_constexpr ? '(' NOSPC init_statement ? condition NOSPC ')' statement 'else' statement
  | if_exlamation_mark ? 'consteval' compound_statement
  | if_exlamation_mark ? 'consteval' compound_statement 'else' statement
  | 'switch(' NOSPC init_statement ? condition NOSPC ')' statement
  ;

iteration_statement
  : 'while(' NOSPC condition NOSPC ')' statement
  | 'do' statement 'while(' NOSPC expression NOSPC ');'
  | 'for(' NOSPC init_statement condition ? NOSPC ';' expression ? NOSPC ')' statement
  | 'for(' NOSPC init_statement ? for_range_declaration ':' for_range_initializer NOSPC ')' statement
  ;

for_range_declaration
  : attribute_specifier* decl_specifier_seq declarator
  | structured_binding_declaration
  ;

for_range_initializer
  : expr_or_braced_init_list
  ;

jump_statement
  : 'break;'
  | 'continue;'
  | 'return' expr_or_braced_init_list ? NOSPC ';'
  | coroutine_return_statement
  | 'goto' identifier NOSPC ';'
  ;

coroutine_return_statement
  : 'co_return' expr_or_braced_init_list ? NOSPC ';'
  ;

declaration_statement
  : block_declaration
  ;

//
// A.7 Declarations
//

//
// Declarations are how names are introduced (or re-introduced) into the C++ program. Not all declarations actually
// declare anything, and each kind of entity is declared differently.
//
// Definitions are declarations that are sufficient to use the entity identified by the name.
//
declaration
  : name_declaration
  | special_declaration
  | special_declaration_flat
  ;

name_declaration
  : block_declaration
  | nodeclspec_function_declaration
  | function_definition
  | friend_type_declaration
  | template_declaration
  | deduction_guide
  | linkage_specification
  | namespace_definition
  | empty_declaration
  | attribute_declaration
  | module_import_declaration
  ;

special_declaration
  : explicit_instantiation      // 'extern' ? 'template' declaration
  | explicit_specialization     // 'template<>' declaration
  | export_declaration          // 'export' ...
  ;

special_declaration_flat
  : 'extern template' declaration       // explicit_instantiation
  | 'template' declaration              // explicit_instantiation
  | 'template<>' declaration            // explicit_specialization
  | 'export' name_declaration           // export_declaration
  | 'export {' NOSPC declaration* NOSPC '}'         // export_declaration
  | 'export' module_import_declaration  // export_declaration

block_declaration
  : simple_declaration
  | asm_declaration
  | namespace_alias_definition
  | using_declaration
  | using_enum_declaration
  | using_directive
  | static_assert_declaration
  | alias_declaration
  | opaque_enum_declaration
  ;

nodeclspec_function_declaration
  : attribute_specifier* declarator NOSPC ';'
  ;

alias_declaration
  : 'using' identifier attribute_specifier* '=' defining_type_id NOSPC ';'
  ;

attributed_identifier
  : identifier attribute_specifier*
  ;

attributed_identifier_list
  : attributed_identifier
  | attributed_identifier_list NOSPC ',' attributed_identifier
  ;

structured_binding_declaration
  : attribute_specifier* decl_specifier_seq ref_qualifier? '[' NOSPC attributed_identifier_list NOSPC ']'
  ;

simple_declaration
  : decl_specifier_seq init_declarator_list? NOSPC ';'
  | attribute_specifier* decl_specifier_seq init_declarator_list NOSPC ';'
  | structured_binding_declaration initializer NOSPC ';'
  ;

static_assert_message
  : unevaluated_string
  | constant_expression
  ;

static_assert_declaration
  : 'static_assert(' NOSPC constant_expression NOSPC ');'
  | 'static_assert(' NOSPC constant_expression NOSPC ',' static_assert_message NOSPC ');'
  ;

empty_declaration
  : ';'
  ;

attribute_declaration
  : attribute_specifier+ NOSPC ';'
  ;

decl_specifier
  : storage_class_specifier
  | defining_type_specifier
  | function_specifier
  | 'friend'
  | 'typedef'
  | 'constexpr'
  | 'consteval'
  | 'constinit'
  | 'inline'
  ;

decl_specifier_seq
  : decl_specifier attribute_specifier*
  | decl_specifier decl_specifier_seq
  ;

storage_class_specifier
  : 'static'
  | 'thread_local'
  | 'extern'
  | 'mutable'
  ;

function_specifier
  : 'virtual'
  | explicit_specifier
  ;

explicit_specifier
  : 'explicit(' NOSPC constant_expression NOSPC ')'
  | 'explicit'
  ;

typedef_name
  : identifier
  | simple_template_id
  ;

type_specifier
  : simple_type_specifier
  | elaborated_type_specifier
  | typename_specifier
  | cv_qualifier
  ;

type_specifier_seq
  : type_specifier attribute_specifier*
  | type_specifier type_specifier_seq
  ;

defining_type_specifier
  : type_specifier
  | class_specifier
  | enum_specifier
  ;

defining_type_specifier_seq
  : defining_type_specifier attribute_specifier*
  | defining_type_specifier defining_type_specifier_seq
  ;

simple_type_specifier
  : nested_name_specifier ? type_name
  | nested_name_specifier 'template' simple_template_id
  | computed_type_specifier
  | placeholder_type_specifier
  | nested_name_specifier ? template_name
  | 'char'
  | 'char8_t'
  | 'char16_t'
  | 'char32_t'
  | 'wchar_t'
  | 'bool'
  | 'short'
  | 'int'
  | 'long'
  | 'signed'
  | 'unsigned'
  | 'float'
  | 'double'
  | 'void'
  ;

type_name
  : class_name
  | enum_name
  | typedef_name
  ;

computed_type_specifier
  : decltype_specifier
  | pack_index_specifier
  ;

pack_index_specifier
  : typedef_name '...[' NOSPC constant_expression NOSPC ']'
  ;

elaborated_type_specifier
  : class_key attribute_specifier* nested_name_specifier ? identifier
  | class_key simple_template_id
  | class_key nested_name_specifier template ? simple_template_id
  | 'enum' nested_name_specifier ? identifier
  ;

decltype_specifier
  : 'decltype(' NOSPC expression NOSPC ')'
  ;

placeholder_type_specifier
  : type_constraint ? 'auto'
  | type_constraint ? 'decltype(auto)'
  ;

init_declarator_list
  : init_declarator
  | init_declarator_list NOSPC ',' init_declarator
  ;

init_declarator
  : declarator initializer ?
  | declarator requires_clause
  ;

declarator
  : ptr_declarator
  | noptr_declarator parameters_and_qualifiers trailing_return_type
  ;

ptr_declarator
  : noptr_declarator
  | ptr_operator ptr_declarator
  ;

noptr_declarator
  : declarator_id attribute_specifier*
  | noptr_declarator parameters_and_qualifiers
  | noptr_declarator '[' NOSPC constant_expression ? NOSPC ']' attribute_specifier*
  | '(' NOSPC ptr_declarator NOSPC ')'
  ;

parameters_and_qualifiers
  : '(' NOSPC parameter_declaration_clause NOSPC ')' cv_qualifier* ref_qualifier ? noexcept_specifier ? attribute_specifier*
  ;

trailing_return_type
  : '->' type_id
  ;

ptr_operator
  : '*' NOSPC attribute_specifier* cv_qualifier*
  | '&' NOSPC attribute_specifier*
  | '&&' NOSPC attribute_specifier*
  | nested_name_specifier '*' attribute_specifier* cv_qualifier*
  | ms_based_modifier ? '*' attribute_specifier* ms_pointer_modifier* cv_qualifier*
  | ms_based_modifier ? nested_name_specifier '*' attribute_specifier* ms_pointer_modifier* cv_qualifier*
  ;

cv_qualifier
  : 'const'
  | 'volatile'
  ;

ref_qualifier
  : '&'
  | '&&'
  ;

three_dots
  : '...'
  ;

declarator_id
  : three_dots ? NOSPC id_expression
  ;

type_id
  : type_specifier_seq abstract_declarator ?
  ;

defining_type_id
  : defining_type_specifier_seq abstract_declarator ?
  ;

abstract_declarator
  : ptr_abstract_declarator
  | noptr_abstract_declarator ? parameters_and_qualifiers trailing_return_type
  | abstract_pack_declarator
  ;

ptr_abstract_declarator
  : noptr_abstract_declarator
  | ptr_operator ptr_abstract_declarator ?
  ;

noptr_abstract_declarator
  : noptr_abstract_declarator ? parameters_and_qualifiers
  | noptr_abstract_declarator ? '[' NOSPC constant_expression ? NOSPC ']' attribute_specifier*
  | '(' NOSPC ptr_abstract_declarator NOSPC ')'
  ;

abstract_pack_declarator
  : noptr_abstract_pack_declarator
  | ptr_operator abstract_pack_declarator
  ;

noptr_abstract_pack_declarator
  : noptr_abstract_pack_declarator parameters_and_qualifiers
  | '...'
  ;

parameter_declaration_clause
  : parameter_declaration_list ?  NOSPC three_dots ?
  | parameter_declaration_list NOSPC ', ...'
  ;

parameter_declaration_list
  : parameter_declaration
  | parameter_declaration_list NOSPC ',' parameter_declaration
  ;

this
  : 'this'
  ;

parameter_declaration
  : attribute_specifier* this ? decl_specifier_seq declarator
  | attribute_specifier* decl_specifier_seq declarator '=' initializer_clause
  | attribute_specifier* this ? decl_specifier_seq abstract_declarator ?
  | attribute_specifier* decl_specifier_seq abstract_declarator ? '=' initializer_clause
  ;

initializer
  : brace_or_equal_initializer
  | '(' NOSPC expression_list NOSPC ')'
  ;

brace_or_equal_initializer
  : '=' initializer_clause
  | braced_init_list
  ;

initializer_clause
  : assignment_expression
  | braced_init_list
  ;

comma
  : ','
  ;

braced_init_list
  : '{' NOSPC initializer_list NOSPC comma ? NOSPC '}'
  | '{' NOSPC designated_initializer_list NOSPC comma ? NOSPC '}'
  | '{}'
  ;

initializer_list
  : initializer_clause  NOSPC three_dots ?
  | initializer_list NOSPC ',' initializer_clause  NOSPC three_dots ?
  ;

designated_initializer_list
  : designated_initializer_clause
  | designated_initializer_list NOSPC ',' designated_initializer_clause
  ;

designated_initializer_clause
  : designator brace_or_equal_initializer
  ;

designator
  : '.' NOSPC identifier
  ;

expr_or_braced_init_list
  : expression
  | braced_init_list
  ;

function_definition
  : attribute_specifier* decl_specifier_seq ? declarator virt_specifier_seq ? function_body
  | attribute_specifier* decl_specifier_seq ? declarator requires_clause function_body
  ;

function_body
  : ctor_initializer ? compound_statement
  | function_try_block
  | '= default;'
  | deleted_function_body
  ;

deleted_function_body
  : '= delete;'
  | '= delete(' NOSPC unevaluated_string NOSPC ');'
  ;

enum_name
  : identifier
  ;

enum_specifier
  : enum_head '{' NOSPC enumerator_list ? NOSPC '}'
  | enum_head '{' NOSPC enumerator_list NOSPC ', }'
  ;

enum_head
  : enum_key attribute_specifier* enum_head_name ? enum_base ?
  ;

enum_head_name
  : nested_name_specifier ? identifier
  ;

opaque_enum_declaration
  : enum_key attribute_specifier* enum_head_name enum_base ? NOSPC ';'
  ;

enum_key
  : 'enum'
  | 'enum class'
  | 'enum struct'
  ;

enum_base
  : ':' type_specifier_seq
  ;

enumerator_list
  : enumerator_definition
  | enumerator_list NOSPC ',' enumerator_definition
  ;

enumerator_definition
  : enumerator
  | enumerator '=' constant_expression
  ;

enumerator
  : identifier attribute_specifier*
  ;

using_enum_declaration
  : 'using enum' using_enum_declarator NOSPC ';'
  ;

using_enum_declarator
  : nested_name_specifier ? identifier
  | nested_name_specifier ? simple_template_id
  ;

namespace_name
  : identifier
  | namespace_alias
  ;

namespace_definition
  : named_namespace_definition
  | unnamed_namespace_definition
  | nested_namespace_definition
  ;

inline
  : 'inline'
  ;

nested_inline
  : ':: inline'
  ;

named_namespace_definition
  : inline ? 'namespace' attribute_specifier* identifier '{' NOSPC namespace_body NOSPC '}'
  ;

unnamed_namespace_definition
  : inline ? 'namespace' attribute_specifier* '{' NOSPC namespace_body NOSPC '}'
  ;

nested_namespace_definition
  : 'namespace' enclosing_namespace_specifier NOSPC '::' inline ? identifier '{' NOSPC namespace_body NOSPC '}'
  ;

enclosing_namespace_specifier
  : identifier
  | enclosing_namespace_specifier NOSPC '::' inline ? identifier
  ;

namespace_body
  : declaration*
  ;

namespace_alias
  : identifier
  ;

namespace_alias_definition
  : 'namespace' identifier '=' qualified_namespace_specifier NOSPC ';'
  ;

qualified_namespace_specifier
  : nested_name_specifier ? namespace_name
  ;

using_directive
  : attribute_specifier* 'using namespace' nested_name_specifier ? namespace_name NOSPC ';'
  ;

using_declaration
  : 'using' using_declarator_list NOSPC ';'
  ;

using_declarator_list
  : using_declarator NOSPC three_dots ?
  | using_declarator_list NOSPC ',' using_declarator NOSPC three_dots ?
  ;

typename
  : 'typename'
  ;

using_declarator
  : typename ? nested_name_specifier unqualified_id
  ;

asm_declaration
  : attribute_specifier* 'asm(' NOSPC balanced_token_seq NOSPC ');'
  ;

linkage_specification
  : 'extern' unevaluated_string '{' NOSPC declaration* NOSPC '}'
  | 'extern' unevaluated_string name_declaration
  ;


//
// Introduces implementation-defined attributes for types, objects, code, etc.
//
// Attributes provide the unified standard syntax for implementation-defined language extensions, such as the
// GNU and IBM language extensions __attribute__((...)), Microsoft extension __declspec(), etc.
//
// An attribute can be used almost everywhere in the C++ program, and can be applied to almost everything:
// to types, to variables, to functions, to names, to code blocks, to entire translation units, although each
// particular attribute is only valid where it is permitted by the implementation.
//
// In declarations, attributes may appear both before the whole declaration and directly after the name of the
// entity that is declared, in which case they are combined. In most other situations, attributes apply to the
// directly preceding entity.
//
// Besides the standard attributes listed below, implementations may support arbitrary non-standard attributes
// with implementation-defined behavior. All attributes unknown to an implementation are ignored without causing
// an error.
//
//    [[ attribute-list ]]
//    [[ using attribute-namespace : attribute-list ]]
//
//    where attribute-list is a comma-separated sequence of zero or more attributes
//    (possibly ending with an ellipsis ... indicating a pack expansion)
//
//    [[noreturn]]
//    [[gnu::unused]]
//    [[deprecated("because")]]
//    [[CC::opt(1), CC::debug]]
//    [[using CC: opt(1), debug]]
//
// For some __declspec parameters such as dllimport and dllexport, so far there's no attribute equivalent, so you must
// continue to use __declspec syntax.
//
// Attributes don't affect the type system, and they don't change the meaning of a program. Compilers ignore attribute
// values they don't recognize.
//
attribute_specifier
  : '[[' NOSPC attribute_using_prefix ? attribute_list NOSPC ']]'
  | alignment_specifier
  | standard_attribute_specifier
  | msvc_attribute_specifier
  ;

standard_attribute_specifier
  : '[[noreturn]]'                   // Indicates that the function does not return
                                     // Indicates that the function will not return control flow to the calling function
                                     //  after it finishes (e.g. functions that terminate the application, throw
                                     // exceptions, loop indefinitely, etc.).
                                     // This attribute applies to the name of the function being declared in function
                                     // declarations only. The behavior is undefined if the function with this attribute
                                     // actually returns.
                                     //
                                     // [[noreturn]] void f() {  throw "error"; // OK }
                                     //
  | '[[carries_dependency]]'         // Indicates that dependency chain in release-consume std::memory_order propagates
                                     // in and out of the function
  | '[[deprecated]]'                 // Indicates that the use of the name or entity declared with this attribute is
  | '[[deprecated("reason")]]'       // allowed, but discouraged for some reason.
                                     //
                                     // [[deprecated]] void TriassicPeriod() {
                                     //     std::clog << "Triassic Period: [251.9 - 208.5] million ears ago.\n";
                                     // }
  | '[[fallthrough]]'                // Indicates that the fall through from the previous case label is intentional and
                                     // should not be diagnosed by a compiler that warns on fall-through
                                     //
                                     // switch (n) {
                                     //     case 1:
                                     //         g();
                                     //         [[fallthrough]];
                                     //     case 2:
                                     //     ...
                                     //
  | '[[maybe_unused]]'               // Suppresses compiler warnings on unused entities, if any
  | '[[nodiscard]]'                  // Encourages the compiler to issue a warning if the return value is discarded
  | '[[nodiscard("reason")]]'
  | '[[likely]]'                     // Indicates that the compiler should optimize for the case where a path of execution
  | '[[unlikely]]'                   // through a statement is more or less likely than any other path of execution
  | '[[no_unique_address]]'          // Indicates that a non-static data member need not have an address distinct from all
                                     // other non-static data members of its class. For MSVC us [[msvc::no_unique_address]]
                                     // instead.
  | '[assume(expression)]]'          // Specifies that the expression will always evaluate to true at a given point
  | '[[indeterminate]]'              // Specifies that an object has an indeterminate value if it is not initialized
  | '[[optimize_for_synchronized]]'  // Indicates that the function definition should be optimized for invocation from a
                                     // synchronized statement
  ;

msvc_attribute_specifier
  : '[[gsl::suppress(rules)]]'       // Used to suppress warnings from checkers that enforce Guidelines Support Library
                                     // (https://github.com/Microsoft/GSL) rules in code.
                                     //
                                     // int main()
                                     // {
                                     //     int arr[10]; // GSL warning C26494 will be fired
                                     //     int* p = arr; // GSL warning C26485 will be fired
                                     //     [[gsl::suppress(bounds.1)]] // This attribute suppresses Bounds rule #1
                                     //     {
                                     //         int* q = p + 1; // GSL warning C26481 suppressed
                                     //         p = q--; // GSL warning C26481 suppressed
                                     //     }
                                     // }
  | '[[msvc::flatten]]'              // Is very similar to [[msvc::forceinline_calls]]. It will [[msvc::forceinline_calls]]
                                     // all calls in the scope it's applied to recursively, until no calls are left.
  | '[[msvc::forceinline]]'          // Has the same meaning as __forceinline
  | '[[msvc::forceinline_calls]]'    // can be placed on or before a statement or a block. It causes the inline heuristic
                                     // to attempt to [[msvc::forceinline]] all calls in that statement or block.
                                     //
                                     // void f() {
                                     //     [[msvc::forceinline_calls]]
                                     //     {
                                     //         foo();
                                     //         bar();
                                     //     }
                                     //
  | '[[msvc::intrinsic]]'            // Tells the compiler to inline a metafunction that acts as a named cast from the
                                     // parameter type to the return type. When the attribute is present on a function
                                     // definition, the compiler replaces all calls to that function with a simple cast.
                                     //
                                     // template <typename T>
                                     // [[msvc::intrinsic]] T&& my_move(T&& t) { return static_cast<T&&>(t); }
                                     //
                                     // void f() {
                                     //     int i = 0;
                                     //     i = my_move(i);
                                     // }
                                     //
  | '[[msvc::noinline]]'             // Has the same meaning as __declspec(noinline).
  | '[[msvc::noinline_calls]]'       // Can be placed before any statement or block, turning off any inlining.
  | '[[msvc::no_tls_guard]]'         // Disables checks for initialization on first access to thread-local variables in DLLs.
  | '[[msvc::no_unique_address]]'    // For MSVC to be used instead of [[no_unique_address]]
  ;

//
// Specifies the alignment requirement of a type or an object.
//    alignas( expression)
//    alignas( type-id   )  // equiva;emt to alignas(alignof( type-id ))
//    alignas( pack ...  )
//
//  struct alignas(float) struct_float { /* your definition here */ };
//  struct alignas(32) sse_t { float sse_data[4]; };
//
alignment_specifier
  annotations (separator = ', ', substitute_count='10', description='Some text', duplication='vertical', substitute_type='auto')
  : 'alignas(' NOSPC type_id NOSPC three_dots ? NOSPC ')'
  | 'alignas(' NOSPC constant_expression NOSPC three_dots ? NOSPC ')'
  ;

//
// In the scope of an attribute list, you can specify the namespace for all names with a single using introducer:
//
//    void g() {
//        [[using rpr: kernel, target(cpu,gpu)]] // equivalent to [[ rpr::kernel, rpr::target(cpu,gpu) ]]
//        do task();
//    }
//
attribute_using_prefix
  : 'using' attribute_namespace NOSPC ':'
  ;

attribute_list
  : attribute ?
  | attribute_list NOSPC ',' attribute ?
  | attribute NOSPC '...'
  | attribute_list NOSPC ',' attribute NOSPC '...'
  ;

attribute
  : attribute_token attribute_argument_clause ?
  ;

attribute_token
  : identifier
  | attribute_scoped_token
  ;

attribute_scoped_token
  : attribute_namespace NOSPC '::' NOSPC identifier
  ;

attribute_namespace
  : identifier
  ;

attribute_argument_clause
  : '(' NOSPC balanced_token_seq ? NOSPC ')'
  ;

balanced_token_seq
  : balanced_token
  | balanced_token_seq balanced_token
  ;

non_balanced_token
  : '<<<Enter any token other than a parenthesis (), a bracket [], or a brace {}.>>>'
  ;

balanced_token
  : '(' NOSPC balanced_token_seq ? NOSPC ')'
  | '[' NOSPC balanced_token_seq ? NOSPC ']'
  | '{' NOSPC balanced_token_seq ? NOSPC '}'
  | non_balanced_token
  ;

//
// A.8 Modules
//

module_declaration
  : export_keyword ? 'module' module_name module_partition ? attribute_specifier* NOSPC ';'
  ;

module_name
  : module_name_qualifier ? identifier
  ;

module_partition
  : ':' module_name_qualifier ? identifier
  ;

module_name_qualifier
  : identifier NOSPC '.'
  | module_name_qualifier identifier NOSPC '.'
  ;

export_declaration
  : 'export' name_declaration
  | 'export {' NOSPC declaration* NOSPC '}'
  | 'export' module_import_declaration
  ;

module_import_declaration
  : 'import' module_name attribute_specifier* NOSPC ';'
  | 'import' module_partition attribute_specifier* NOSPC ';'
  | 'import' header_name attribute_specifier* NOSPC ';'
  ;

global_module_fragment
  : 'module;' NEWLINE declaration*
  ;

private_module_fragment
  : 'module: private;' NEWLINE declaration*
  ;

//
// A.9 Classes
//

class_name
  : identifier
  | simple_template_id
  ;

class_specifier
  : class_head '{' NOSPC member_specification ? NOSPC '}'
  ;

class_head
  : class_key attribute_specifier* class_head_name class_virt_specifier ? base_clause ?
  | class_key attribute_specifier* base_clause ?
  ;

class_head_name
  : nested_name_specifier ? class_name
  ;

class_virt_specifier
  : 'final'
  ;

class_key
  : 'class'
  | 'struct'
  | 'union'
  ;

member_specification
  : member_declaration member_specification ?
  | access_specifier NOSPC ':' member_specification ?
  ;

member_declaration
  : attribute_specifier* decl_specifier_seq ? member_declarator_list ? NOSPC ';'
  | function_definition
  | friend_type_declaration
  | using_declaration
  | using_enum_declaration
  | static_assert_declaration
  | template_declaration
  | explicit_specialization
  | deduction_guide
  | alias_declaration
  | opaque_enum_declaration
  | empty_declaration
  ;

member_declarator_list
  : member_declarator
  | member_declarator_list NOSPC ',' member_declarator
  ;

member_declarator
  : declarator virt_specifier_seq ? pure_specifier ?
  | declarator requires_clause
  | declarator brace_or_equal_initializer ?
  | identifier ? attribute_specifier* NOSPC ':' constant_expression brace_or_equal_initializer ?
  ;

virt_specifier_seq
  : virt_specifier
  | virt_specifier_seq virt_specifier
  ;

test_aaa
  :
  | b1 NEWLINE b2 NEWLINE b3
  | c1 NEWLINE c2 NEWLINE c3
  | d1 NOSPC d2 NOSPC d3
  ;

b1
 : '<<<This is b1>>>'
 ;

b2
 : '<<<This is b2>>>'
 ;

b3
 : '<<<This is b3>>>'
 ;

c1
 : '<<<This is c1>>>'
 ;

c2
 : '<<<This is c2>>>'
 ;

c3
 : '<<<This is c3>>>'
 ;

d1
 : '<<<This is d1>>>'
 ;

d2
 : '<<<This is d2>>>'
 ;

d3
 : '<<<This is d3>>>'
 ;

virt_specifier
  : 'override'
  | 'final'
  ;

pure_specifier
  : '= 0'
  ;

friend_type_declaration
  : 'friend' friend_type_specifier_list NOSPC ';'
  ;

friend_type_specifier_list
  : friend_type_specifier NOSPC three_dots ?
  | friend_type_specifier_list NOSPC ',' friend_type_specifier NOSPC three_dots ?
  ;

friend_type_specifier
  : simple_type_specifier
  | elaborated_type_specifier
  | typename_specifier
  ;

conversion_function_id
  : 'operator' conversion_type_id
  ;

conversion_type_id
  : type_specifier_seq conversion_declarator ?
  ;

conversion_declarator
  : ptr_operator conversion_declarator ?
  ;

base_clause
  : ':' base_specifier_list
  ;

base_specifier_list
  : base_specifier NOSPC three_dots ?
  | base_specifier_list NOSPC ',' base_specifier NOSPC three_dots ?
  ;

virtual
  : 'virtual'
  ;

base_specifier
  : attribute_specifier* class_or_decltype
  | attribute_specifier* 'virtual' access_specifier ? class_or_decltype
  | attribute_specifier* access_specifier virtual ? class_or_decltype
  ;

class_or_decltype
  : nested_name_specifier ? type_name
  | nested_name_specifier 'template' simple_template_id
  | decltype_specifier
  ;

access_specifier
  : 'private'
  | 'protected'
  | 'public'
  ;

ctor_initializer
  : ':' mem_initializer_list
  ;

mem_initializer_list
  : mem_initializer NOSPC three_dots ?
  | mem_initializer_list NOSPC ',' mem_initializer NOSPC three_dots ?
  ;

mem_initializer
  : mem_initializer_id NOSPC '(' NOSPC expression_list ? NOSPC ')'
  | mem_initializer_id braced_init_list
  ;

mem_initializer_id
  : class_or_decltype
  | identifier
  ;

//
// A.10 Overloading
//

operator_function_id
  : 'operator' operator
  ;

operator
  : 'new'
  | 'delete'
  | 'new[]'
  | 'delete[]'
  | 'co_await'
  | '()'
  | '[]'
  | '->'
  | '->*'
  | '~'
  | '!'
  | '+'
  | '-'
  | '*'
  | '/'
  | '%'
  | '^'
  | '&'
  | '|'
  | '='
  | '+='
  | '-='
  | '*='
  | '/='
  | '%='
  | '^='
  | '&='
  | '|='
  | '=='
  | '!='
  | '<'
  | '>'
  | '<='
  | '>='
  | '<=>'
  | '&&'
  | '||'
  | '<<'
  | '>>'
  | '<<='
  | '>>='
  | '++'
  | '--'
  | ','
  ;

literal_operator_id
  : 'operator' unevaluated_string identifier
  | 'operator' user_defined_string_literal
  ;

//
// A.11 Templates
//

template_declaration
  : template_head declaration
  | template_head concept_definition
  ;

template_head
  : 'template<' NOSPC template_parameter_list NOSPC '>' requires_clause ?
  ;

template_parameter_list
  : template_parameter
  | template_parameter_list NOSPC ',' template_parameter
  ;

requires_clause
  : 'requires' constraint_logical_or_expression
  ;

constraint_logical_or_expression
  : constraint_logical_and_expression
  | constraint_logical_or_expression '||' constraint_logical_and_expression
  ;

constraint_logical_and_expression
  : primary_expression
  | constraint_logical_and_expression '&&' primary_expression
  ;

template_parameter
  : type_parameter
  | parameter_declaration
  ;

type_parameter
  : type_parameter_key NOSPC three_dots ? identifier ?
  | type_parameter_key identifier ? '=' type_id
  | type_constraint NOSPC three_dots ? identifier ?
  | type_constraint identifier ? '=' type_id
  | template_head type_parameter_key NOSPC three_dots ? identifier ?
  | template_head type_parameter_key identifier ? '=' id_expression
  ;

type_parameter_key
  : 'class'
  | 'typename'
  ;

type_constraint
  : nested_name_specifier ? concept_name
  | nested_name_specifier ? concept_name NOSPC '<' NOSPC template_argument_list ? NOSPC '>'
  ;

//
// A.11
//

simple_template_id
  : template_name NOSPC '<' NOSPC template_argument_list ? NOSPC '>'
  ;

template_id
  : simple_template_id
  | operator_function_id NOSPC '<' NOSPC template_argument_list ? NOSPC '>'
  | literal_operator_id NOSPC '<' NOSPC template_argument_list ? NOSPC '>'
  ;

template_name
  : identifier
  ;

template_argument_list
  : template_argument NOSPC three_dots ?
  | template_argument_list NOSPC ',' template_argument NOSPC three_dots ?
  ;

template_argument
  : constant_expression
  | type_id
  | id_expression
  | braced_init_list
  ;

constraint_expression
  : logical_or_expression
  ;

deduction_guide
  : explicit_specifier ? template_name NOSPC '(' NOSPC parameter_declaration_clause NOSPC ')->' simple_template_id NOSPC ';'
  ;

concept_definition
  : concept concept_name attribute_specifier* '=' constraint_expression NOSPC ';'
  ;

concept_name
  : identifier
  ;

typename_specifier
  : 'typename' nested_name_specifier identifier
  | 'typename' nested_name_specifier template ? simple_template_id
  ;

extern
  : 'extern'
  ;

explicit_instantiation
  : extern ? 'template' declaration
  ;

explicit_specialization
  : 'template<>' declaration
  ;

//
// A.12 Exception handling
//

try_block
  : 'try' compound_statement handler_seq
  ;

function_try_block
  : 'try' ctor_initializer ? compound_statement handler_seq
  ;

handler_seq
  : handler handler_seq ?
  ;

handler
  : 'catch(' NOSPC exception_declaration NOSPC ')' compound_statement
  ;

exception_declaration
  : attribute_specifier* type_specifier_seq declarator
  | attribute_specifier* type_specifier_seq abstract_declarator ?
  | '...'
  ;

noexcept_specifier
  : 'noexcept(' NOSPC constant_expression NOSPC ')'
  | 'noexcept'
  ;

//
// A.13 Preprocessing directives
//

preprocessing_file
  : group ?
  | module_file
  ;

module_file
  : pp_global_module_fragment ? pp_module group ? pp_private_module_fragment ?
  ;

pp_global_module_fragment
  : 'module;' new_line group ?
  ;

pp_private_module_fragment
  : 'module : private;' new_line group ?
  ;

group
  : group_part
  | group group_part
  ;

group_part
  : control_line
  | if_section
  | text_line
  | '#' NOSPC conditionally_supported_directive
  ;

control_line
  : '#include' preprocessing_token+ new_line
  | pp_import
  | '#define' identifier replacement_list new_line
  | '#define' identifier lparen identifier* ')' preprocessing_token* new_line
  | '#define' identifier lparen '...)' preprocessing_token* new_line
  | '#define' identifier lparen identifier+ ',...)' preprocessing_token* new_line
  | '#undef' identifier new_line
  | '#line' preprocessing_token+ new_line
  | '#error' preprocessing_token* new_line
  | '#warning' preprocessing_token* new_line
  | '#pragma' preprocessing_token* new_line
  | '#' new_line
  ;

if_section
  : if_group elif_groups ? else_group ? endif_line
  ;

if_group
  : '#if' constant_expression new_line group ?
  | '#ifdef' identifier new_line group ?
  | '#ifndef' identifier new_line group ?
  ;

elif_groups
  : elif_group
  | elif_groups elif_group
  ;

elif_group
  : '#elif' constant_expression new_line group ?
  | '#elifdef' identifier new_line group ?
  | '#elifndef' identifier new_line group ?
  ;

else_group
  : '#else' new_line group ?
  ;

endif_line
  : '#endif' new_line
  ;

text_line
  : preprocessing_token* new_line
  ;

conditionally_supported_directive
  : preprocessing_token+ new_line
  ;

lparen
  : '<<<Enter a ( character not immediately preceded by whitespace.>>>'
  ;

new_line
  : '<<<Enter the new_line \\n character.>>>'
  ;

defined_macro_expression
  : 'defined' identifier
  | 'defined(' NOSPC identifier NOSPC ')'
  ;

h_preprocessing_token
  : '<<<Enter any preprocessing_token other than >.>>>'
  ;

header_name_tokens
  : string_literal
  | '<' NOSPC h_preprocessing_token+ NOSPC '>'
  ;

has_include_expression
  : '__has_include(' NOSPC header_name NOSPC ')'
  | '__has_include(' NOSPC header_name_tokens NOSPC ')'
  ;

has_attribute_expression
  : '__has_cpp_attribute(' NOSPC preprocessing_token+ NOSPC ')'
  ;

export
  : 'export'
  ;

pp_module
  : export ? 'module' preprocessing_token* NOSPC ';' new_line
  ;

pp_import
  : export ? 'import' header_name preprocessing_token* NOSPC ';' new_line
  | export ? 'import' header_name_tokens preprocessing_token* NOSPC ';' new_line
  | export ? 'import' preprocessing_token+ NOSPC ';' new_line
  ;

va_replacement
  : '__VA_OPT__(' NOSPC preprocessing_token* NOSPC ')'
  ;

ms_call_modifier
  : '__cdecl'
  | '__clrcall'
  | '__stdcall'
  | '__fastcall'
  | '__thiscall'
  | '__vectorcall'
  ;

ms_call_modifier_seq
  : ms_call_modifier ms_call_modifier_seq ?
  ;

ms_pointer_modifier
  : '__restrict'
  | '__uptr'
  | '__sptr'
  | '_unaligned'
  | '__unaligned'
  ;

ms_declspec_modifier
  : '__declspec(' NOSPC identifier NOSPC ')'
  ;
