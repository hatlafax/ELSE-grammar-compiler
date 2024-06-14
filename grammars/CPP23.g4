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
  : '\\N{' n_char '}'
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

universal_character_name
  : '\\u' hex_quad
  | '\\U' hex_quad_quad
  | '\\u{' hexadecimal_digit '}'
  | named_universal_character
  ;

non_whitespace_character_literal
  : '<<<Each non_whitespace character that cannot be one of the above.>>>'
  ;

preprocessing_token
  : header_name
  | import_keyword
  | module_keyword
  | export_keyword
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
  : '<' h_char '>'
  | '"' q_char '"'
  ;

pp_number
  : digit
  | '.' digit
  | pp_number digit
  | pp_number identifier_nondigit
  | pp_number '\'' digit
  | pp_number '\'' nondigit
  | pp_number 'e' sign
  | pp_number 'E' sign
  | pp_number 'p' sign
  | pp_number 'P' sign
  | pp_number '.'
  ;

identifier
  : identifier_start
  | identifier identifier_continue
  ;

identifier_nondigit
  : '<<<Enter an identifier that is not a digit.>>>'
  ;

translation_character_xid_start
  : '<<<Enter an element of the translation character set with the Unicode property XID_Start.>>>'
  ;

translation_character_xid_continue
  : '<<<Enter an element of the translation character set with the Unicode property XID_Continue.>>>'
  ;


identifier_start
  : nondigit
  | translation_character_xid_start
  ;

identifier_continue
  : digit
  | nondigit
  | translation_character_xid_continue
  ;

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
  | 'inline'
  | 'int'
  | 'long'
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
  | import_keyword
  | module_keyword
  | export_keyword
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
  : binary_literal integer_suffix ?
  | octal_literal integer_suffix ?
  | decimal_literal integer_suffix ?
  | hexadecimal_literal integer_suffix ?
  ;

simple_quote_char
  : '\''
  ;

binary_literal
  : '0b' binary_digit
  | '0B' binary_digit
  | binary_literal simple_quote_char ? binary_digit
  ;

octal_literal
  : '0'
  | octal_literal simple_quote_char ? octal_digit
  ;

decimal_literal
  : nonzero_digit
  | decimal_literal simple_quote_char ? digit
  ;

hexadecimal_literal
  : hexadecimal_prefix hexadecimal_digit_sequence
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
  | hexadecimal_digit_sequence simple_quote_char ? hexadecimal_digit
  ;

integer_suffix
  : unsigned_suffix long_suffix ?
  | unsigned_suffix long_long_suffix ?
  | unsigned_suffix size_suffix ?
  | long_suffix unsigned_suffix ?
  | long_long_suffix unsigned_suffix ?
  | size_suffix unsigned_suffix ?
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

character_literal
  : encoding_prefix ? '\'' c_char+ '\''
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

escape_sequence
  : simple_escape_sequence
  | numeric_escape_sequence
  | conditional_escape_sequence
  ;

simple_escape_sequence
  : '\\' simple_escape_sequence_char
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
  : '\\' octal_digit
  | '\\' octal_digit octal_digit
  | '\\' octal_digit octal_digit octal_digit
  | '\\o{' octal_digit+ '}'
  ;

hexadecimal_escape_sequence
  : '\\x' hexadecimal_digit
  | '\\x{' hexadecimal_digit '}'
  ;

conditional_escape_sequence
  : '\\' conditional_escape_sequence_char
  ;

conditional_escape_sequence_char
  : '<<<Enter a basic source character that is not an octal_digit, a simple_escape_sequence_char, or the characters N, o, u, U, or x.>>>'
  ;

floating_point_literal
  : decimal_floating_point_literal
  | hexadecimal_floating_point_literal
  ;

decimal_floating_point_literal
  : fractional_constant exponent_part ? floating_point_suffix ?
  | digit_sequence exponent_part floating_point_suffix ?
  ;

hexadecimal_floating_point_literal
  : hexadecimal_prefix hexadecimal_fractional_constant binary_exponent_part floating_point_suffix ?
  | hexadecimal_prefix hexadecimal_digit_sequence binary_exponent_part floating_point_suffix ?
  ;

fractional_constant
  : digit_sequence ? '.' digit_sequence
  | digit_sequence '.'
  ;

hexadecimal_fractional_constant
  : hexadecimal_digit_sequence ? '.' hexadecimal_digit_sequence
  | hexadecimal_digit_sequence '.'
  ;

exponent_part
  : 'e' sign ? digit_sequence
  | 'E' sign ? digit_sequence
  ;

binary_exponent_part
  : 'p' sign ? digit_sequence
  | 'P' sign ? digit_sequence
  ;

sign
  : '+'
  | '-'
  ;

digit_sequence
  : digit
  | digit_sequence simple_quote_char ? digit
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

string_literal
  : encoding_prefix ? '"' s_char* '"'
  | encoding_prefix ? 'R' raw_string
  ;

s_char
  : basic_s_char
  | escape_sequence
  | universal_character_name
  ;

basic_s_char
  : '<<<Enter a basic source character except the double_quote ", backslash \\, or new_line \\n character.>>>'
  ;

raw_string
  : '"' d_char* '(' r_char* ')' d_char* '"'
  ;

r_char
  : '<<<Enter a sequence of source characters, except a right parenthesis ) followed by the initial d_char sequence (which may be empty) followed by a double quote ".>>>'
  ;

d_char
  : '<<<Enter a sequence of basic source characters except: space, the left parenthesis (, the right parenthesis ), the backslash \\, and the control characters representing horizontal tab, vertical tab, form feed, and newline.>>>'
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
  : decimal_literal ud_suffix
  | octal_literal ud_suffix
  | hexadecimal_literal ud_suffix
  | binary_literal ud_suffix
  ;

user_defined_floating_point_literal
  : fractional_constant exponent_part ? ud_suffix
  | digit_sequence exponent_part ud_suffix
  | hexadecimal_prefix hexadecimal_fractional_constant binary_exponent_part ud_suffix
  | hexadecimal_prefix hexadecimal_digit_sequence binary_exponent_part ud_suffix
  ;

user_defined_string_literal
  : string_literal ud_suffix
  ;

user_defined_character_literal
  : character_literal ud_suffix
  ;

ud_suffix
  : identifier
  ;

//
// A.4 Basics
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
  | '(' expression ')'
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
  | '~' type_name
  | '~' computed_type_specifier
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
  | type_name '::'
  | namespace_name '::'
  | computed_type_specifier '::'
  | nested_name_specifier identifier '::'
  | nested_name_specifier template ? simple_template_id '::'
  ;

pack_index_expression
  : id_expression '... [' constant_expression ']'
  ;

lambda_expression
  : lambda_introducer attribute_specifier* lambda_declarator compound_statement
  | lambda_introducer '<' template_parameter_list '>' requires_clause ? attribute_specifier* lambda_declarator compound_statement
  ;

lambda_introducer
  : '[' lambda_capture ? ']'
  ;

lambda_declarator
  : lambda_specifier+ noexcept_specifier ? attribute_specifier* trailing_return_type ?
  | noexcept_specifier attribute_specifier* trailing_return_type ?
  | trailing_return_type ?
  | '(' parameter_declaration_clause ')' lambda_specifier* noexcept_specifier ? attribute_specifier* trailing_return_type ? requires_clause ?
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
  | capture_default ',' capture_list
  ;

capture_default
  : '&'
  | '='
  ;

capture_list
  : capture
  | capture_list ',' capture
  ;

capture
  : simple_capture
  | init_capture
  ;

simple_capture
  : identifier three_dots ?
  | '&' identifier three_dots ?
  | 'this'
  | '*this'
  ;

and_three_dots
  : '& ...'
  ;

init_capture
  : three_dots ? identifier initializer
  | and_three_dots ? identifier initializer
  ;

fold_expression
  : '(' cast_expression fold_operator '...)'
  | '(...' fold_operator cast_expression ')'
  | '(' cast_expression fold_operator '...' fold_operator cast_expression ')'
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
  : '(' parameter_declaration_clause ')'
  ;

requirement_body
  : '{' requirement+ '}'
  ;

requirement
  : simple_requirement
  | type_requirement
  | compound_requirement
  | nested_requirement
  ;

simple_requirement
  : expression ';'
  ;

type_requirement
  : 'typename' nested_name_specifier ? type_name ';'
  ;

compound_requirement
  : '{' expression '}' noexcept ? return_type_requirement ? ';'
  ;

return_type_requirement
  : '->' type_constraint
  ;

nested_requirement
  : 'requires' constraint_expression ';'
  ;

dot_template
  : '.template'
  ;

arrow_template
  : '->template'
  ;

postfix_expression
  : primary_expression
  | postfix_expression '[' expression_list ? ']'
  | postfix_expression '(' expression_list ? ')'
  | simple_type_specifier '(' expression_list ? ')'
  | typename_specifier '(' expression_list ? ')'
  | simple_type_specifier braced_init_list
  | typename_specifier braced_init_list
  | postfix_expression dot_template ? id_expression
  | postfix_expression arrow_template ? id_expression
  | postfix_expression '++'
  | postfix_expression '--'
  | 'dynamic_cast<' type_id '>(' expression ')'
  | 'static_cast<' type_id '>(' expression ')'
  | 'reinterpret_cast<' type_id '>(' expression ')'
  | 'const_cast<' type_id '>(' expression ')'
  | 'typeid(' expression ')'
  | 'typeid(' type_id ')'
  ;

expression_list
  : initializer_list
  ;

unary_expression
  : postfix_expression
  | unary_operator cast_expression
  | '++' cast_expression
  | '--' cast_expression
  | await_expression
  | 'sizeof' unary_expression
  | 'sizeof(' type_id ')'
  | 'sizeof...(' identifier ')'
  | 'alignof(' type_id ')'
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
  : 'noexcept(' expression ')'
  ;

nesting_operator
  : '::'
  ;

new_expression
  : nesting_operator ? 'new' new_placement ? new_type_id new_initializer ?
  | nesting_operator ? 'new' new_placement ? '(' type_id ')' new_initializer ?
  ;

new_placement
  : '(' expression_list ')'
  ;

new_type_id
  : type_specifier_seq new_declarator ?
  ;

new_declarator
  : ptr_operator new_declarator ?
  | noptr_new_declarator
  ;

noptr_new_declarator
  : '[' expression ? ']' attribute_specifier*
  | noptr_new_declarator '[' constant_expression ']' attribute_specifier*
  ;

new_initializer
  : '(' expression_list ? ')'
  | braced_init_list
  ;

delete_expression
  : nesting_operator ? 'delete' cast_expression
  | nesting_operator ? 'delete[]' cast_expression
  ;

cast_expression
  : unary_expression
  | '(' type_id ')' cast_expression
  ;

pm_expression
  : cast_expression
  | pm_expression '.*' cast_expression
  | pm_expression '->*' cast_expression
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
  | expression ',' assignment_expression
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
  | attribute_specifier* 'case' constant_expression ':'
  | attribute_specifier* 'default:'
  ;

labeled_statement
  : label statement
  ;

expression_statement
  : expression ? ';'
  ;

compound_statement
  : '{' statement* label* '}'
  ;

if_constexpr
  : 'if constexpr'
  ;

if_exlamation_mark
  : 'if !'
  ;

selection_statement
  : if_constexpr ? '(' init_statement ? condition ')' statement
  | if_constexpr ? '(' init_statement ? condition ')' statement 'else' statement
  | if_exlamation_mark ? 'consteval' compound_statement
  | if_exlamation_mark ? 'consteval' compound_statement 'else' statement
  | 'switch(' init_statement ? condition ')' statement
  ;

iteration_statement
  : 'while(' condition ')' statement
  | 'do' statement 'while(' expression ');'
  | 'for(' init_statement condition ? ';' expression ? ')' statement
  | 'for(' init_statement ? for_range_declaration ':' for_range_initializer ')' statement
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
  | 'return' expr_or_braced_init_list ? ';'
  | coroutine_return_statement
  | 'goto' identifier ';'
  ;

coroutine_return_statement
  : 'co_return' expr_or_braced_init_list ? ';'
  ;

declaration_statement
  : block_declaration
  ;

//
// A.7 Declarations
//

declaration
  : name_declaration
  | special_declaration
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
  : explicit_instantiation
  | explicit_specialization
  | export_declaration
  ;

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
  : attribute_specifier* declarator ';'
  ;

alias_declaration
  : 'using' identifier attribute_specifier* '=' defining_type_id ';'
  ;

attributed_identifier
  : identifier attribute_specifier*
  ;

attributed_identifier_list
  : attributed_identifier
  | attributed_identifier_list ',' attributed_identifier
  ;

structured_binding_declaration
  : attribute_specifier* decl_specifier_seq ref_qualifier? '[' attributed_identifier_list ']'
  ;

simple_declaration
  : decl_specifier_seq init_declarator_list? ';'
  | attribute_specifier* decl_specifier_seq init_declarator_list ';'
  | structured_binding_declaration initializer ';'
  ;

static_assert_message
  : unevaluated_string
  | constant_expression
  ;

static_assert_declaration
  : 'static_assert(' constant_expression ');'
  | 'static_assert(' constant_expression ',' static_assert_message ');'
  ;

empty_declaration
  : ';'
  ;

attribute_declaration
  : attribute_specifier+ ';'
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
  : 'explicit(' constant_expression ')'
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
  : typedef_name '...[' constant_expression ']'
  ;

elaborated_type_specifier
  : class_key attribute_specifier* nested_name_specifier ? identifier
  | class_key simple_template_id
  | class_key nested_name_specifier template ? simple_template_id
  | 'enum' nested_name_specifier ? identifier
  ;

decltype_specifier
  : 'decltype(' expression ')'
  ;

placeholder_type_specifier
  : type_constraint ? 'auto'
  | type_constraint ? 'decltype(auto)'
  ;

init_declarator_list
  : init_declarator
  | init_declarator_list ',' init_declarator
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
  | noptr_declarator '[' constant_expression ? ']' attribute_specifier*
  | '(' ptr_declarator ')'
  ;

parameters_and_qualifiers
  : '(' parameter_declaration_clause ')' cv_qualifier* ref_qualifier ? noexcept_specifier ? attribute_specifier*
  ;

trailing_return_type
  : '->' type_id
  ;

ptr_operator
  : '*' attribute_specifier* cv_qualifier*
  | '&' attribute_specifier*
  | '&&' attribute_specifier*
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
  : three_dots ? id_expression
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
  | noptr_abstract_declarator ? '[' constant_expression ? ']' attribute_specifier*
  | '(' ptr_abstract_declarator ')'
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
  : parameter_declaration_list ?  three_dots ?
  | parameter_declaration_list ', ...'
  ;

parameter_declaration_list
  : parameter_declaration
  | parameter_declaration_list ',' parameter_declaration
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
  | '(' expression_list ')'
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
  : '{' initializer_list comma ? '}'
  | '{' designated_initializer_list comma ? '}'
  | '{}'
  ;

initializer_list
  : initializer_clause  three_dots ?
  | initializer_list ',' initializer_clause  three_dots ?
  ;

designated_initializer_list
  : designated_initializer_clause
  | designated_initializer_list ',' designated_initializer_clause
  ;

designated_initializer_clause
  : designator brace_or_equal_initializer
  ;

designator
  : '.' identifier
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
  | '= delete(' unevaluated_string ');'
  ;

enum_name
  : identifier
  ;

enum_specifier
  : enum_head '{' enumerator_list ? '}'
  | enum_head '{' enumerator_list ', }'
  ;

enum_head
  : enum_key attribute_specifier* enum_head_name ? enum_base ?
  ;

enum_head_name
  : nested_name_specifier ? identifier
  ;

opaque_enum_declaration
  : enum_key attribute_specifier* enum_head_name enum_base ? ';'
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
  | enumerator_list ',' enumerator_definition
  ;

enumerator_definition
  : enumerator
  | enumerator '=' constant_expression
  ;

enumerator
  : identifier attribute_specifier*
  ;

using_enum_declaration
  : 'using enum' using_enum_declarator ';'
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
  : inline ? 'namespace' attribute_specifier* identifier '{' namespace_body '}'
  ;

unnamed_namespace_definition
  : inline ? 'namespace' attribute_specifier* '{' namespace_body '}'
  ;

nested_namespace_definition
  : 'namespace' enclosing_namespace_specifier '::' inline ? identifier '{' namespace_body '}'
  ;

enclosing_namespace_specifier
  : identifier
  | enclosing_namespace_specifier '::' inline ? identifier
  ;

namespace_body
  : declaration*
  ;

namespace_alias
  : identifier
  ;

namespace_alias_definition
  : 'namespace' identifier '=' qualified_namespace_specifier ';'
  ;

qualified_namespace_specifier
  : nested_name_specifier ? namespace_name
  ;

using_directive
  : attribute_specifier* 'using namespace' nested_name_specifier ? namespace_name ';'
  ;

using_declaration
  : 'using' using_declarator_list ';'
  ;

using_declarator_list
  : using_declarator three_dots ?
  | using_declarator_list ',' using_declarator three_dots ?
  ;

typename
  : 'typename'
  ;

using_declarator
  : typename ? nested_name_specifier unqualified_id
  ;

asm_declaration
  : attribute_specifier* 'asm(' balanced_token_seq ');'
  ;

linkage_specification
  : 'extern' unevaluated_string '{' declaration* '}'
  | 'extern' unevaluated_string name_declaration
  ;

attribute_specifier
  : '[[' attribute_using_prefix ? attribute_list ']]'
  | alignment_specifier
  ;

alignment_specifier
  annotations (separator = ', ', substitute_count='10', description='Some text', dublication='vertical', auto_substitute='yes')
  : 'alignas(' type_id three_dots ? ')'
  | 'alignas(' constant_expression three_dots ? ')'
  ;

attribute_using_prefix
  : 'using' attribute_namespace ':'
  ;

attribute_list
  : attribute ?
  | attribute_list ',' attribute ?
  | attribute '...'
  | attribute_list ',' attribute '...'
  ;

attribute
  : attribute_token attribute_argument_clause ?
  ;

attribute_token
  : identifier
  | attribute_scoped_token
  ;

attribute_scoped_token
  : attribute_namespace '::' identifier
  ;

attribute_namespace
  : identifier
  ;

attribute_argument_clause
  : '(' balanced_token_seq ? ')'
  ;

balanced_token_seq
  : balanced_token
  | balanced_token_seq balanced_token
  ;

non_balanced_token
  : '<<<Enter any token other than a parenthesis (), a bracket [], or a brace {}.>>>'
  ;

balanced_token
  : '(' balanced_token_seq ? ')'
  | '[' balanced_token_seq ? ']'
  | '{' balanced_token_seq ? '}'
  | non_balanced_token
  ;

//
// A.8 Modules
//

module_declaration
  : export_keyword ? module_keyword module_name module_partition ? attribute_specifier* ';'
  ;

module_name
  : module_name_qualifier ? identifier
  ;

module_partition
  : ':' module_name_qualifier ? identifier
  ;

module_name_qualifier
  : identifier '.'
  | module_name_qualifier identifier '.'
  ;

export_declaration
  : 'export' name_declaration
  | 'export {' declaration* '}'
  | export_keyword module_import_declaration
  ;

module_import_declaration
  : import_keyword module_name attribute_specifier* ';'
  | import_keyword module_partition attribute_specifier* ';'
  | import_keyword header_name attribute_specifier* ';'
  ;

global_module_fragment
  : module_keyword ';' declaration*
  ;

private_module_fragment
  : module_keyword ': private;' declaration*
  ;

//
// A.9 Classes
//

class_name
  : identifier
  | simple_template_id
  ;

class_specifier
  : class_head '{' member_specification ? '}'
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
  | access_specifier ':' member_specification ?
  ;

member_declaration
  : attribute_specifier* decl_specifier_seq ? member_declarator_list ? ';'
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
  | member_declarator_list ',' member_declarator
  ;

member_declarator
  : declarator virt_specifier_seq ? pure_specifier ?
  | declarator requires_clause
  | declarator brace_or_equal_initializer ?
  | identifier ? attribute_specifier* ':' constant_expression brace_or_equal_initializer ?
  ;

virt_specifier_seq
  : virt_specifier
  | virt_specifier_seq virt_specifier
  ;

virt_specifier
  : 'override'
  | 'final'
  ;

pure_specifier
  : '= 0'
  ;

friend_type_declaration
  : 'friend' friend_type_specifier_list ';'
  ;

friend_type_specifier_list
  : friend_type_specifier three_dots ?
  | friend_type_specifier_list ',' friend_type_specifier three_dots ?
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
  : base_specifier three_dots ?
  | base_specifier_list ',' base_specifier three_dots ?
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
  : mem_initializer three_dots ?
  | mem_initializer_list ',' mem_initializer three_dots ?
  ;

mem_initializer
  : mem_initializer_id '(' expression_list ? ')'
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
  : 'template<' template_parameter_list '>' requires_clause ?
  ;

template_parameter_list
  : template_parameter
  | template_parameter_list ',' template_parameter
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
  : type_parameter_key three_dots ? identifier ?
  | type_parameter_key identifier ? '=' type_id
  | type_constraint three_dots ? identifier ?
  | type_constraint identifier ? '=' type_id
  | template_head type_parameter_key three_dots ? identifier ?
  | template_head type_parameter_key identifier ? '=' id_expression
  ;

type_parameter_key
  : 'class'
  | 'typename'
  ;

type_constraint
  : nested_name_specifier ? concept_name
  | nested_name_specifier ? concept_name '<' template_argument_list ? '>'
  ;

//
// A.11
//

simple_template_id
  : template_name '<' template_argument_list ? '>'
  ;

template_id
  : simple_template_id
  | operator_function_id '<' template_argument_list ? '>'
  | literal_operator_id '<' template_argument_list ? '>'
  ;

template_name
  : identifier
  ;

template_argument_list
  : template_argument three_dots ?
  | template_argument_list ',' template_argument three_dots ?
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
  : explicit_specifier ? template_name '(' parameter_declaration_clause ')->' simple_template_id ';'
  ;

concept_definition
  : concept concept_name attribute_specifier* '=' constraint_expression ';'
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
  : 'catch(' exception_declaration ')' compound_statement
  ;

exception_declaration
  : attribute_specifier* type_specifier_seq declarator
  | attribute_specifier* type_specifier_seq abstract_declarator ?
  | '...'
  ;

noexcept_specifier
  : 'noexcept(' constant_expression ')'
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
  | '#' conditionally_supported_directive
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
  | 'defined(' identifier ')'
  ;

h_preprocessing_token
  : '<<<Enter any preprocessing_token other than >.>>>'
  ;

header_name_tokens
  : string_literal
  | '<' h_preprocessing_token+ '>'
  ;

has_include_expression
  : '__has_include(' header_name ')'
  | '__has_include(' header_name_tokens ')'
  ;

has_attribute_expression
  : '__has_cpp_attribute(' preprocessing_token+ ')'
  ;

export
  : 'export'
  ;

pp_module
  : export ? 'module' preprocessing_token* ';' new_line
  ;

pp_import
  : export ? 'import' header_name preprocessing_token* ';' new_line
  | export ? 'import' header_name_tokens preprocessing_token* ';' new_line
  | export ? 'import' preprocessing_token+ ';' new_line
  ;

va_replacement
  : '__VA_OPT__(' preprocessing_token* ')'
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
  : '__declspec(' identifier ')'
  ;
