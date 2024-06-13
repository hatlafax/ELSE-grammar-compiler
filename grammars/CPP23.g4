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

n-char
  : '<<<Enter a n-char sequence, that is translation characters except of { or \\n.>>>'
  ;

named-universal-character
  : '\\N{' n-char '}'
  ;

hexadecimal-digit
  : '<<<Enter a hexadecimal digit, i.e. any number of hex characters [0-9a-fA-F].>>>'
  ;

hex-quad
  : '<<<Enter exactly four hex number characters [0-9a-fA-F], i.e. NNNN.>>>'
  ;

hex-quad-quad
  : '<<<Enter exactly eight hex number characters [0-9a-fA-F], i.e. NNNNNNNN.>>>'
  ;

universal-character-name
  : '\\u' hex-quad
  | '\\U' hex-quad-quad
  | '\\u{' hexadecimal-digit '}'
  | named-universal-character
  ;

non-whitespace-character-literal
  : '<<<Each non-whitespace character that cannot be one of the above.>>>'
  ;

preprocessing-token
  : header-name
  | import-keyword
  | module-keyword
  | export-keyword
  | identifier
  | pp-number
  | character-literal
  | user-defined-character-literal
  | string-literal
  | user-defined-string-literal
  | preprocessing-op-or-punc
  | non-whitespace-character-literal
  ;

token
  : identifier
  | keyword
  | literal
  | operator-or-punctuator
  ;

h-char
  : '<<<Enter a h-char sequence, i.e. source characters except \\n and > characters.>>>'
  ;

q-char
  : '<<<Enter a q-char sequence, i.e. source characters except \\n and quotation mark " characters.>>>'
  ;

header-name
  : '<' h-char '>'
  | '"' q-char '"'
  ;

pp-number
  : digit
  | '.' digit
  | pp-number digit
  | pp-number identifier-nondigit
  | pp-number '\'' digit
  | pp-number '\'' nondigit
  | pp-number 'e' sign
  | pp-number 'E' sign
  | pp-number 'p' sign
  | pp-number 'P' sign
  | pp-number '.'
  ;

identifier
  : identifier-start
  | identifier identifier-continue
  ;

translation-character-xid-start
  : '<<<Enter an element of the translation character set with the Unicode property XID-Start.>>>'
  ;

translation-character-xid-continue
  : '<<<Enter an element of the translation character set with the Unicode property XID-Continue.>>>'
  ;


identifier-start
  : nondigit
  | translation-character-xid-start
  ;


identifier-continue
  : digit
  | nondigit
  | translation-character-xid-continue
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
  | import-keyword
  | module-keyword
  | export-keyword
  ;

preprocessing-op-or-punc
  :
  preprocessing-operator
  |
  operator-or-punctuator
  ;

preprocessing-operator
  : '#'
  | '##'
  | '%:'
  | '%:%:'
  ;

operator-or-punctuator
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
  : integer-literal
  | character-literal
  | floating-point-literal
  | string-literal
  | boolean-literal
  | pointer-literal
  | user-defined-literal
  ;

integer-literal
  : binary-literal integer-suffix ?
  | octal-literal integer-suffix ?
  | decimal-literal integer-suffix ?
  | hexadecimal-literal integer-suffix ?
  ;

simple-quote-char
  : '\''
  ;

binary-literal
  : '0b' binary-digit
  | '0B' binary-digit
  | binary-literal simple-quote-char ? binary-digit
  ;

octal-literal
  : '0'
  | octal-literal simple-quote-char ? octal-digit
  ;

decimal-literal
  : nonzero-digit
  | decimal-literal simple-quote-char ? digit
  ;

hexadecimal-literal
  : hexadecimal-prefix hexadecimal-digit-sequence
  ;

binary-digit
  : '0'
  | '1'
  ;

octal-digit
  : '0'
  | '1'
  | '2'
  | '3'
  | '4'
  | '5'
  | '6'
  | '7'
  ;

nonzero-digit
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

hexadecimal-prefix
  : '0x'
  | '0X'
  ;

hexadecimal-digit-sequence
  : hexadecimal-digit
  | hexadecimal-digit-sequence simple-quote-char ? hexadecimal-digit
  ;

hexadecimal-digit
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
  | 'a'
  | 'b'
  | 'c'
  | 'd'
  | 'e'
  | 'f'
  | 'A'
  | 'B'
  | 'C'
  | 'D'
  | 'E'
  | 'F'
  ;

integer-suffix
  : unsigned-suffix long-suffix ?
  | unsigned-suffix long-long-suffix ?
  | unsigned-suffix size-suffix ?
  | long-suffix unsigned-suffix ?
  | long-long-suffix unsigned-suffix ?
  | size-suffix unsigned-suffix ?
  ;

unsigned-suffix
  : 'u'
  | 'U'
  ;

long-suffix
  : 'l'
  | 'L'
  ;

long-long-suffix
  : 'll'
  | 'LL'
  ;

size-suffix
  : 'z'
  | 'Z'
  ;

character-literal
  : encoding-prefix ? '\'' c-char+ '\''
  ;

encoding-prefix
  : 'u8'
  | 'u'
  | 'U'
  | 'L'
  ;

c-char
  : basic-c-char
  | escape-sequence
  | universal-character-name
  ;

basic-c-char
  : '<<<Enter a basic source character except the single-quote \', backslash \\, or new-line \\n character.>>>'
  ;

escape-sequence
  : simple-escape-sequence
  | numeric-escape-sequence
  | conditional-escape-sequence
  ;

simple-escape-sequence
  : '\\' simple-escape-sequence-char
  ;

simple-escape-sequence-char
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

numeric-escape-sequence
  : octal-escape-sequence
  | hexadecimal-escape-sequence
  ;

octal-escape-sequence
  : '\\' octal-digit
  | '\\' octal-digit octal-digit
  | '\\' octal-digit octal-digit octal-digit
  | '\\o{' octal-digit+ '}'
  ;

hexadecimal-escape-sequence
  : '\\x' hexadecimal-digit
  | '\\x{' hexadecimal-digit '}'
  ;

conditional-escape-sequence
  : '\\' conditional-escape-sequence-char
  ;

conditional-escape-sequence-char
  : '<<<Enter a basic source character that is not an octal-digit, a simple-escape-sequence-char, or the characters N, o, u, U, or x.>>>'
  ;

floating-point-literal
  : decimal-floating-point-literal
  | hexadecimal-floating-point-literal
  ;

decimal-floating-point-literal
  : fractional-constant exponent-part ? floating-point-suffix ?
  | digit-sequence exponent-part floating-point-suffix ?
  ;

hexadecimal-floating-point-literal
  : hexadecimal-prefix hexadecimal-fractional-constant binary-exponent-part floating-point-suffix ?
  | hexadecimal-prefix hexadecimal-digit-sequence binary-exponent-part floating-point-suffix ?
  ;

fractional-constant
  : digit-sequence ? '.' digit-sequence
  | digit-sequence '.'
  ;

hexadecimal-fractional-constant
  : hexadecimal-digit-sequence ? '.' hexadecimal-digit-sequence
  | hexadecimal-digit-sequence '.'
  ;

exponent-part
  : 'e' sign ? digit-sequence
  | 'E' sign ? digit-sequence
  ;

binary-exponent-part
  : 'p' sign ? digit-sequence
  | 'P' sign ? digit-sequence
  ;

sign
  : '+'
  | '-'
  ;

digit-sequence
  : digit
  | digit-sequence simple-quote-char ? digit
  ;

floating-point-suffix
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

string-literal
  : encoding-prefix ? '"' s-char* '"'
  | encoding-prefix ? 'R' raw-string
  ;

s-char
  : basic-s-char
  | escape-sequence
  | universal-character-name
  ;

basic-s-char
  : '<<<Enter a basic source character except the double-quote ", backslash \\, or new-line \\n character.>>>'
  ;

raw-string
  : '"' d-char* '(' r-char* ')' d-char* '"'
  ;

r-char
  : '<<<Enter a sequence of source characters, except a right parenthesis ) followed by the initial d-char-sequence (which may be empty) followed by a double quote ".>>>'
  ;

d-char
  : '<<<Enter a sequence of basic source characters except: space, the left parenthesis (, the right parenthesis ), the backslash \\, and the control characters representing horizontal tab, vertical tab, form feed, and newline.>>>'
  ;

boolean-literal
  : 'false'
  | 'true'
  ;

pointer-literal
  : 'nullptr'
  ;

user-defined-literal
  : user-defined-integer-literal
  | user-defined-floating-point-literal
  | user-defined-string-literal
  | user-defined-character-literal
  ;

user-defined-integer-literal
  : decimal-literal ud-suffix
  | octal-literal ud-suffix
  | hexadecimal-literal ud-suffix
  | binary-literal ud-suffix
  ;

user-defined-floating-point-literal
  : fractional-constant exponent-part ? ud-suffix
  | digit-sequence exponent-part ud-suffix
  | hexadecimal-prefix hexadecimal-fractional-constant binary-exponent-part ud-suffix
  | hexadecimal-prefix hexadecimal-digit-sequence binary-exponent-part ud-suffix
  ;

user-defined-string-literal
  : string-literal ud-suffix
  ;

user-defined-character-literal
  : character-literal ud-suffix
  ;

ud-suffix
  : identifier
  ;

//
// A.4 Basics
//

translation-unit
  : declaration*
  | global-module-fragment ? module-declaration declaration* private-module-fragment ?
  ;

//
// A.5 Expressions
//

primary-expression
  : literal
  | 'this'
  | '(' expression ')'
  | id-expression
  | lambda-expression
  | fold-expression
  | requires-expression
  ;

id-expression
  : unqualified-id
  | qualified-id
  | pack-index-expression
  ;

unqualified-id
  : identifier
  | operator-function-id
  | conversion-function-id
  | literal-operator-id
  | '~' type-name
  | '~' computed-type-specifier
  | template-id
  ;

template
  : 'template'
  ;

qualified-id
  : nested-name-specifier template ? unqualified-id
  ;

nested-name-specifier
  : '::'
  | type-name '::'
  | namespace-name '::'
  | computed-type-specifier '::'
  | nested-name-specifier identifier '::'
  | nested-name-specifier template ? simple-template-id '::'
  ;

pack-index-expression
  : id-expression '... [' constant-expression ']'
  ;

lambda-expression
  : lambda-introducer attribute-specifier* lambda-declarator compound-statement
  | lambda-introducer '<' template-parameter-list '>' requires-clause ? attribute-specifier* lambda-declarator compound-statement
  ;

lambda-introducer
  : '[' lambda-capture ? ']'
  ;

lambda-declarator
  : lambda-specifier+ noexcept-specifier ? attribute-specifier* trailing-return-type ?
  | noexcept-specifier attribute-specifier* trailing-return-type ?
  | trailing-return-type ?
  | '(' parameter-declaration-clause ')' lambda-specifier* noexcept-specifier ? attribute-specifier* trailing-return-type ? requires-clause ?
  ;

lambda-specifier
  : 'consteval'
  | 'constexpr'
  | 'mutable'
  | 'static'
  ;

lambda-capture
  : capture-default
  | capture-list
  | capture-default ',' capture-list
  ;

capture-default
  : '&'
  | '='
  ;

capture-list
  : capture
  | capture-list ',' capture
  ;

capture
  : simple-capture
  | init-capture
  ;

simple-capture
  : identifier three-dots ?
  | '&' identifier three-dots ?
  | 'this'
  | '*this'
  ;

and-three-dots
  : '& ...'
  ;

init-capture
  : three-dots ? identifier initializer
  | and-three-dots ? identifier initializer
  ;

fold-expression
  : '(' cast-expression fold-operator '...)'
  | '(...' fold-operator cast-expression ')'
  | '(' cast-expression fold-operator '...' fold-operator cast-expression ')'
  ;

fold-operator
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

requires-expression
  : 'requires' requirement-parameter-list ? requirement-body
  ;

requirement-parameter-list
  : '(' parameter-declaration-clause ')'
  ;

requirement-body
  : '{' requirement+ '}'
  ;

requirement
  : simple-requirement
  | type-requirement
  | compound-requirement
  | nested-requirement
  ;

simple-requirement
  : expression ';'
  ;

type-requirement
  : 'typename' nested-name-specifier ? type-name ';'
  ;

compound-requirement
  : '{' expression '}' noexcept ? return-type-requirement ? ';'
  ;

return-type-requirement
  : '->' type-constraint
  ;

nested-requirement
  : 'requires' constraint-expression ';'
  ;

dot-template
  : '.template'
  ;

arrow-template
  : '->template'
  ;

postfix-expression
  : primary-expression
  | postfix-expression '[' expression-list ? ']'
  | postfix-expression '(' expression-list ? ')'
  | simple-type-specifier '(' expression-list ? ')'
  | typename-specifier '(' expression-list ? ')'
  | simple-type-specifier braced-init-list
  | typename-specifier braced-init-list
  | postfix-expression dot-template ? id-expression
  | postfix-expression arrow-template ? id-expression
  | postfix-expression '++'
  | postfix-expression '--'
  | 'dynamic-cast<' type-id '>(' expression ')'
  | 'static-cast<' type-id '>(' expression ')'
  | 'reinterpret-cast<' type-id '>(' expression ')'
  | 'const-cast<' type-id '>(' expression ')'
  | 'typeid(' expression ')'
  | 'typeid(' type-id ')'
  ;

expression-list
  : initializer-list
  ;

unary-expression
  : postfix-expression
  | unary-operator cast-expression
  | '++' cast-expression
  | '--' cast-expression
  | await-expression
  | 'sizeof' unary-expression
  | 'sizeof(' type-id ')'
  | 'sizeof...(' identifier ')'
  | 'alignof(' type-id ')'
  | noexcept-expression
  | new-expression
  | delete-expression
  ;

unary-operator
  : '*'
  | '&'
  | '+'
  | '-'
  | '!'
  | '~'
  ;

await-expression
  : 'co_await' cast-expression
  ;

noexcept-expression
  : 'noexcept(' expression ')'
  ;

nesting-operator
  : '::'
  ;

new-expression
  : nesting-operator ? 'new' new-placement ? new-type-id new-initializer ?
  | nesting-operator ? 'new' new-placement ? '(' type-id ')' new-initializer ?
  ;

new-placement
  : '(' expression-list ')'
  ;

new-type-id
  : type-specifier-seq new-declarator ?
  ;

new-declarator
  : ptr-operator new-declarator ?
  | noptr-new-declarator
  ;

noptr-new-declarator
  : '[' expression ? ']' attribute-specifier*
  | noptr-new-declarator '[' constant-expression ']' attribute-specifier*
  ;

new-initializer
  : '(' expression-list ? ')'
  | braced-init-list
  ;

delete-expression
  : nesting-operator ? 'delete' cast-expression
  | nesting-operator ? 'delete[]' cast-expression
  ;

cast-expression
  : unary-expression
  | '(' type-id ')' cast-expression
  ;

pm-expression
  : cast-expression
  | pm-expression '.*' cast-expression
  | pm-expression '->*' cast-expression
  ;

multiplicative-expression
  : pm-expression
  | multiplicative-expression '*' pm-expression
  | multiplicative-expression '/' pm-expression
  | multiplicative-expression '%' pm-expression
  ;

additive-expression
  : multiplicative-expression
  | additive-expression '+' multiplicative-expression
  | additive-expression '-' multiplicative-expression
  ;

shift-expression
  : additive-expression
  | shift-expression '<<' additive-expression
  | shift-expression '>>' additive-expression
  ;

compare-expression
  : shift-expression
  | compare-expression '<=>' shift-expression
  ;

relational-expression
  : compare-expression
  | relational-expression '<' compare-expression
  | relational-expression '>' compare-expression
  | relational-expression '<=' compare-expression
  | relational-expression '>=' compare-expression
  ;

equality-expression
  : relational-expression
  | equality-expression '==' relational-expression
  | equality-expression '!=' relational-expression
  ;

and-expression
  : equality-expression
  | and-expression '&' equality-expression
  ;

exclusive-or-expression
  : and-expression
  | exclusive-or-expression '^' and-expression
  ;

inclusive-or-expression
  : exclusive-or-expression
  | inclusive-or-expression '|' exclusive-or-expression
  ;

logical-and-expression
  : inclusive-or-expression
  | logical-and-expression '&&' inclusive-or-expression
  ;

logical-or-expression
  : logical-and-expression
  | logical-or-expression '||' logical-and-expression
  ;

conditional-expression
  : logical-or-expression
  | logical-or-expression '?' expression ':' assignment-expression
  ;

yield-expression
  : 'co_yield' assignment-expression
  | 'co_yield' braced-init-list
  ;

throw-expression
  : 'throw' assignment-expression ?
  ;

assignment-expression
  : conditional-expression
  | yield-expression
  | throw-expression
  | logical-or-expression assignment-operator initializer-clause
  ;

assignment-operator
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
  : assignment-expression
  | expression ',' assignment-expression
  ;

constant-expression
  : conditional-expression
  ;

statement
  : labeled-statement
  | attribute-specifier* expression-statement
  | attribute-specifier* compound-statement
  | attribute-specifier* selection-statement
  | attribute-specifier* iteration-statement
  | attribute-specifier* jump-statement
  | declaration-statement
  | attribute-specifier* try-block
  ;

init-statement
  : expression-statement
  | simple-declaration
  | alias-declaration
  ;

condition
  : expression
  | attribute-specifier* decl-specifier-seq declarator brace-or-equal-initializer
  ;

label
  : attribute-specifier* identifier ':'
  | attribute-specifier* 'case' constant-expression ':'
  | attribute-specifier* 'default:'
  ;

labeled-statement
  : label statement
  ;

expression-statement
  : expression ? ';'
  ;

compound-statement
  : '{' statement* label* '}'
  ;

if-constexpr
  : 'if constexpr'
  ;

if-exlamation-mark
  : 'if !'
  ;

selection-statement
  : if-constexpr ? '(' init-statement ? condition ')' statement
  | if-constexpr ? '(' init-statement ? condition ')' statement 'else' statement
  | if-exlamation-mark ? 'consteval' compound-statement
  | if-exlamation-mark ? 'consteval' compound-statement 'else' statement
  | 'switch(' init-statement ? condition ')' statement
  ;

iteration-statement
  : 'while(' condition ')' statement
  | 'do' statement 'while(' expression ');'
  | 'for(' init-statement condition ? ';' expression ? ')' statement
  | 'for(' init-statement ? for-range-declaration ':' for-range-initializer ')' statement
  ;

for-range-declaration
  : attribute-specifier* decl-specifier-seq declarator
  | structured-binding-declaration
  ;

for-range-initializer
  : expr-or-braced-init-list
  ;

jump-statement
  : 'break;'
  | 'continue;'
  | 'return' expr-or-braced-init-list ? ';'
  | coroutine-return-statement
  | 'goto' identifier ';'
  ;

coroutine-return-statement
  : 'co_return' expr-or-braced-init-list ? ';'
  ;

declaration-statement
  : block-declaration
  ;

//
// A.7 Declarations
//

declaration
  : name-declaration
  | special-declaration
  ;

name-declaration
  : block-declaration
  | nodeclspec-function-declaration
  | function-definition
  | friend-type-declaration
  | template-declaration
  | deduction-guide
  | linkage-specification
  | namespace-definition
  | empty-declaration
  | attribute-declaration
  | module-import-declaration
  ;

special-declaration
  : explicit-instantiation
  | explicit-specialization
  | export-declaration
  ;

block-declaration
  : simple-declaration
  | asm-declaration
  | namespace-alias-definition
  | using-declaration
  | using-enum-declaration
  | using-directive
  | static-assert-declaration
  | alias-declaration
  | opaque-enum-declaration
  ;

nodeclspec-function-declaration
  : attribute-specifier* declarator ';'
  ;

alias-declaration
  : 'using' identifier attribute-specifier* '=' defining-type-id ';'
  ;

attributed-identifier
  : identifier attribute-specifier*
  ;

attributed-identifier-list
  : attributed-identifier
  | attributed-identifier-list ',' attributed-identifier
  ;

structured-binding-declaration
  : attribute-specifier* decl-specifier-seq ref-qualifier? '[' attributed-identifier-list ']'
  ;

simple-declaration
  : decl-specifier-seq init-declarator-list? ';'
  | attribute-specifier* decl-specifier-seq init-declarator-list ';'
  | structured-binding-declaration initializer ';'
  ;

static-assert-message
  : unevaluated-string
  | constant-expression
  ;

static-assert-declaration
  : 'static-assert(' constant-expression ');'
  | 'static-assert(' constant-expression ',' static-assert-message ');'
  ;

empty-declaration
  : ';'
  ;

attribute-declaration
  : attribute-specifier+ ';'
  ;

decl-specifier
  : storage-class-specifier
  | defining-type-specifier
  | function-specifier
  | 'friend'
  | 'typedef'
  | 'constexpr'
  | 'consteval'
  | 'constinit'
  | 'inline'
  ;

decl-specifier-seq
  : decl-specifier attribute-specifier*
  | decl-specifier decl-specifier-seq
  ;

storage-class-specifier
  : 'static'
  | 'thread_local'
  | 'extern'
  | 'mutable'
  ;

function-specifier
  : 'virtual'
  | explicit-specifier
  ;

explicit-specifier
  : 'explicit(' constant-expression ')'
  | 'explicit'
  ;

typedef-name
  : identifier
  | simple-template-id
  ;

type-specifier
  : simple-type-specifier
  | elaborated-type-specifier
  | typename-specifier
  | cv-qualifier
  ;

type-specifier-seq
  : type-specifier attribute-specifier*
  | type-specifier type-specifier-seq
  ;

defining-type-specifier
  : type-specifier
  | class-specifier
  | enum-specifier
  ;

defining-type-specifier-seq
  : defining-type-specifier attribute-specifier*
  | defining-type-specifier defining-type-specifier-seq
  ;

simple-type-specifier
  : nested-name-specifier ? type-name
  | nested-name-specifier 'template' simple-template-id
  | computed-type-specifier
  | placeholder-type-specifier
  | nested-name-specifier ? template-name
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

type-name
  : class-name
  | enum-name
  | typedef-name
  ;

computed-type-specifier
  : decltype-specifier
  | pack-index-specifier
  ;

pack-index-specifier
  : typedef-name '...[' constant-expression ']'
  ;

elaborated-type-specifier
  : class-key attribute-specifier* nested-name-specifier ? identifier
  | class-key simple-template-id
  | class-key nested-name-specifier template ? simple-template-id
  | 'enum' nested-name-specifier ? identifier
  ;

decltype-specifier
  : 'decltype(' expression ')'
  ;

placeholder-type-specifier
  : type-constraint ? 'auto'
  | type-constraint ? 'decltype(auto)'
  ;

init-declarator-list
  : init-declarator
  | init-declarator-list ',' init-declarator
  ;

init-declarator
  : declarator initializer ?
  | declarator requires-clause
  ;

declarator
  : ptr-declarator
  | noptr-declarator parameters-and-qualifiers trailing-return-type
  ;

ptr-declarator
  : noptr-declarator
  | ptr-operator ptr-declarator
  ;

noptr-declarator
  : declarator-id attribute-specifier*
  | noptr-declarator parameters-and-qualifiers
  | noptr-declarator '[' constant-expression ? ']' attribute-specifier*
  | '(' ptr-declarator ')'
  ;

parameters-and-qualifiers
  : '(' parameter-declaration-clause ')' cv-qualifier* ref-qualifier ? noexcept-specifier ? attribute-specifier*
  ;

trailing-return-type
  : '->' type-id
  ;

ptr-operator
  : '*' attribute-specifier* cv-qualifier*
  | '&' attribute-specifier*
  | '&&' attribute-specifier*
  | nested-name-specifier '*' attribute-specifier* cv-qualifier*
  | ms-based-modifier ? '*' attribute-specifier* ms-pointer-modifier* cv-qualifier*
  | ms-based-modifier ? nested-name-specifier '*' attribute-specifier* ms-pointer-modifier* cv-qualifier*
  ;

cv-qualifier
  : 'const'
  | 'volatile'
  ;

ref-qualifier
  : '&'
  | '&&'
  ;

three-dots
  : '...'
  ;

declarator-id
  : three-dots ? id-expression
  ;

type-id
  : type-specifier-seq abstract-declarator ?
  ;

defining-type-id
  : defining-type-specifier-seq abstract-declarator ?
  ;

abstract-declarator
  : ptr-abstract-declarator
  | noptr-abstract-declarator ? parameters-and-qualifiers trailing-return-type
  | abstract-pack-declarator
  ;

ptr-abstract-declarator
  : noptr-abstract-declarator
  | ptr-operator ptr-abstract-declarator ?
  ;

noptr-abstract-declarator
  : noptr-abstract-declarator ? parameters-and-qualifiers
  | noptr-abstract-declarator ? '[' constant-expression ? ']' attribute-specifier*
  | '(' ptr-abstract-declarator ')'
  ;

abstract-pack-declarator
  : noptr-abstract-pack-declarator
  | ptr-operator abstract-pack-declarator
  ;

noptr-abstract-pack-declarator
  : noptr-abstract-pack-declarator parameters-and-qualifiers
  | '...'
  ;

parameter-declaration-clause
  : parameter-declaration-list ?  three-dots ?
  | parameter-declaration-list ', ...'
  ;

parameter-declaration-list
  : parameter-declaration
  | parameter-declaration-list ',' parameter-declaration
  ;

this
  : 'this'
  ;

parameter-declaration
  : attribute-specifier* this ? decl-specifier-seq declarator
  | attribute-specifier* decl-specifier-seq declarator '=' initializer-clause
  | attribute-specifier* this ? decl-specifier-seq abstract-declarator ?
  | attribute-specifier* decl-specifier-seq abstract-declarator ? '=' initializer-clause
  ;

initializer
  : brace-or-equal-initializer
  | '(' expression-list ')'
  ;

brace-or-equal-initializer
  : '=' initializer-clause
  | braced-init-list
  ;

initializer-clause
  : assignment-expression
  | braced-init-list
  ;

comma
  : ','
  ;

braced-init-list
  : '{' initializer-list comma ? '}'
  | '{' designated-initializer-list comma ? '}'
  | '{}'
  ;

initializer-list
  : initializer-clause  three-dots ?
  | initializer-list ',' initializer-clause  three-dots ?
  ;

designated-initializer-list
  : designated-initializer-clause
  | designated-initializer-list ',' designated-initializer-clause
  ;

designated-initializer-clause
  : designator brace-or-equal-initializer
  ;

designator
  : '.' identifier
  ;

expr-or-braced-init-list
  : expression
  | braced-init-list
  ;

function-definition
  : attribute-specifier* decl-specifier-seq ? declarator virt-specifier-seq ? function-body
  | attribute-specifier* decl-specifier-seq ? declarator requires-clause function-body
  ;

function-body
  : ctor-initializer ? compound-statement
  | function-try-block
  | '= default;'
  | deleted-function-body
  ;

deleted-function-body
  : '= delete;'
  | '= delete(' unevaluated-string ');'
  ;

enum-name
  : identifier
  ;

enum-specifier
  : enum-head '{' enumerator-list ? '}'
  | enum-head '{' enumerator-list ', }'
  ;

enum-head
  : enum-key attribute-specifier* enum-head-name ? enum-base ?
  ;

enum-head-name
  : nested-name-specifier ? identifier
  ;

opaque-enum-declaration
  : enum-key attribute-specifier* enum-head-name enum-base ? ';'
  ;

enum-key
  : 'enum'
  | 'enum class'
  | 'enum struct'
  ;

enum-base
  : ':' type-specifier-seq
  ;

enumerator-list
  : enumerator-definition
  | enumerator-list ',' enumerator-definition
  ;

enumerator-definition
  : enumerator
  | enumerator '=' constant-expression
  ;

enumerator
  : identifier attribute-specifier*
  ;

using-enum-declaration
  : 'using enum' using-enum-declarator ';'
  ;

using-enum-declarator
  : nested-name-specifier ? identifier
  | nested-name-specifier ? simple-template-id
  ;

namespace-name
  : identifier
  | namespace-alias
  ;

namespace-definition
  : named-namespace-definition
  | unnamed-namespace-definition
  | nested-namespace-definition
  ;

inline
  : 'inline'
  ;

nested-inline
  : ':: inline'
  ;

named-namespace-definition
  : inline ? 'namespace' attribute-specifier* identifier '{' namespace-body '}'
  ;

unnamed-namespace-definition
  : inline ? 'namespace' attribute-specifier* '{' namespace-body '}'
  ;

nested-namespace-definition
  : 'namespace' enclosing-namespace-specifier '::' inline ? identifier '{' namespace-body '}'
  ;

enclosing-namespace-specifier
  : identifier
  | enclosing-namespace-specifier '::' inline ? identifier
  ;

namespace-body
  : declaration*
  ;

namespace-alias
  : identifier
  ;

namespace-alias-definition
  : 'namespace' identifier '=' qualified-namespace-specifier ';'
  ;

qualified-namespace-specifier
  : nested-name-specifier ? namespace-name
  ;

using-directive
  : attribute-specifier* 'using namespace' nested-name-specifier ? namespace-name ';'
  ;

using-declaration
  : 'using' using-declarator-list ';'
  ;

using-declarator-list
  : using-declarator three-dots ?
  | using-declarator-list ',' using-declarator three-dots ?
  ;

typename
  : 'typename'
  ;

using-declarator
  : typename ? nested-name-specifier unqualified-id
  ;

asm-declaration
  : attribute-specifier* 'asm(' balanced-token-seq ');'
  ;

linkage-specification
  : 'extern' unevaluated-string '{' declaration* '}'
  | 'extern' unevaluated-string name-declaration
  ;

attribute-specifier
  annotations (separator = ', ', substitute_count='10', description='Some text', dublication='vertical', auto_substitute='yes')
  : '[[' attribute-using-prefix ? attribute-list ']]'
  | alignment-specifier
  ;

alignment-specifier
  : 'alignas(' type-id three-dots ? ')'
  | 'alignas(' constant-expression three-dots ? ')'
  ;

attribute-using-prefix
  : 'using' attribute-namespace ':'
  ;

attribute-list
  : attribute ?
  | attribute-list ',' attribute ?
  | attribute '...'
  | attribute-list ',' attribute '...'
  ;

attribute
  : attribute-token attribute-argument-clause ?
  ;

attribute-token
  : identifier
  | attribute-scoped-token
  ;

attribute-scoped-token
  : attribute-namespace '::' identifier
  ;

attribute-namespace
  : identifier
  ;

attribute-argument-clause
  : '(' balanced-token-seq ? ')'
  ;

balanced-token-seq
  : balanced-token
  | balanced-token-seq balanced-token
  ;

non_balanced_token
  : '<<<Enter any token other than a parenthesis (), a bracket [], or a brace {}.>>>'
  ;

balanced-token
  : '(' balanced-token-seq ? ')'
  | '[' balanced-token-seq ? ']'
  | '{' balanced-token-seq ? '}'
  | non_balanced_token
  ;

//
// A.8 Modules
//

module-declaration
  : export-keyword ? module-keyword module-name module-partition ? attribute-specifier* ';'
  ;

module-name
  : module-name-qualifier ? identifier
  ;

module-partition
  : ':' module-name-qualifier ? identifier
  ;

module-name-qualifier
  : identifier '.'
  | module-name-qualifier identifier '.'
  ;

export-declaration
  : 'export' name-declaration
  | 'export {' declaration* '}'
  | export-keyword module-import-declaration
  ;

module-import-declaration
  : import-keyword module-name attribute-specifier* ';'
  | import-keyword module-partition attribute-specifier* ';'
  | import-keyword header-name attribute-specifier* ';'
  ;

global-module-fragment
  : module-keyword ';' declaration*
  ;

private-module-fragment
  : module-keyword ': private;' declaration*
  ;

//
// A.9 Classes
//

class-name
  : identifier
  | simple-template-id
  ;

class-specifier
  : class-head '{' member-specification ? '}'
  ;

class-head
  : class-key attribute-specifier* class-head-name class-virt-specifier ? base-clause ?
  | class-key attribute-specifier* base-clause ?
  ;

class-head-name
  : nested-name-specifier ? class-name
  ;

class-virt-specifier
  : 'final'
  ;

class-key
  : 'class'
  | 'struct'
  | 'union'
  ;

member-specification
  : member-declaration member-specification ?
  | access-specifier ':' member-specification ?
  ;

member-declaration
  : attribute-specifier* decl-specifier-seq ? member-declarator-list ? ';'
  | function-definition
  | friend-type-declaration
  | using-declaration
  | using-enum-declaration
  | static-assert-declaration
  | template-declaration
  | explicit-specialization
  | deduction-guide
  | alias-declaration
  | opaque-enum-declaration
  | empty-declaration
  ;

member-declarator-list
  : member-declarator
  | member-declarator-list ',' member-declarator
  ;

member-declarator
  : declarator virt-specifier-seq ? pure-specifier ?
  | declarator requires-clause
  | declarator brace-or-equal-initializer ?
  | identifier ? attribute-specifier* ':' constant-expression brace-or-equal-initializer ?
  ;

virt-specifier-seq
  : virt-specifier
  | virt-specifier-seq virt-specifier
  ;

virt-specifier
  : 'override'
  | 'final'
  ;

pure-specifier
  : '= 0'
  ;

friend-type-declaration
  : 'friend' friend-type-specifier-list ';'
  ;

friend-type-specifier-list
  : friend-type-specifier three-dots ?
  | friend-type-specifier-list ',' friend-type-specifier three-dots ?
  ;

friend-type-specifier
  : simple-type-specifier
  | elaborated-type-specifier
  | typename-specifier
  ;

conversion-function-id
  : 'operator' conversion-type-id
  ;

conversion-type-id
  : type-specifier-seq conversion-declarator ?
  ;

conversion-declarator
  : ptr-operator conversion-declarator ?
  ;

base-clause
  : ':' base-specifier-list
  ;

base-specifier-list
  : base-specifier three-dots ?
  | base-specifier-list ',' base-specifier three-dots ?
  ;

virtual
  : 'virtual'
  ;

base-specifier
  : attribute-specifier* class-or-decltype
  | attribute-specifier* 'virtual' access-specifier ? class-or-decltype
  | attribute-specifier* access-specifier virtual ? class-or-decltype
  ;

class-or-decltype
  : nested-name-specifier ? type-name
  | nested-name-specifier 'template' simple-template-id
  | decltype-specifier
  ;

access-specifier
  : 'private'
  | 'protected'
  | 'public'
  ;

ctor-initializer
  : ':' mem-initializer-list
  ;

mem-initializer-list
  : mem-initializer three-dots ?
  | mem-initializer-list ',' mem-initializer three-dots ?
  ;

mem-initializer
  : mem-initializer-id '(' expression-list ? ')'
  | mem-initializer-id braced-init-list
  ;

mem-initializer-id
  : class-or-decltype
  | identifier
  ;

//
// A.10 Overloading
//

operator-function-id
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

literal-operator-id
  : 'operator' unevaluated-string identifier
  | 'operator' user-defined-string-literal
  ;

//
// A.11 Templates
//

template-declaration
  : template-head declaration
  | template-head concept-definition
  ;

template-head
  : 'template<' template-parameter-list '>' requires-clause ?
  ;

template-parameter-list
  : template-parameter
  | template-parameter-list ',' template-parameter
  ;

requires-clause
  : 'requires' constraint-logical-or-expression
  ;

constraint-logical-or-expression
  : constraint-logical-and-expression
  | constraint-logical-or-expression '||' constraint-logical-and-expression
  ;

constraint-logical-and-expression
  : primary-expression
  | constraint-logical-and-expression '&&' primary-expression
  ;

template-parameter
  : type-parameter
  | parameter-declaration
  ;

type-parameter
  : type-parameter-key three-dots ? identifier ?
  | type-parameter-key identifier ? '=' type-id
  | type-constraint three-dots ? identifier ?
  | type-constraint identifier ? '=' type-id
  | template-head type-parameter-key three-dots ? identifier ?
  | template-head type-parameter-key identifier ? '=' id-expression
  ;

type-parameter-key
  : 'class'
  | 'typename'
  ;

type-constraint
  : nested-name-specifier ? concept-name
  | nested-name-specifier ? concept-name '<' template-argument-list ? '>'
  ;

//
// A.11
//

simple-template-id
  : template-name '<' template-argument-list ? '>'
  ;

template-id
  : simple-template-id
  | operator-function-id '<' template-argument-list ? '>'
  | literal-operator-id '<' template-argument-list ? '>'
  ;

template-name
  : identifier
  ;

template-argument-list
  : template-argument three-dots ?
  | template-argument-list ',' template-argument three-dots ?
  ;

template-argument
  : constant-expression
  | type-id
  | id-expression
  | braced-init-list
  ;

constraint-expression
  : logical-or-expression
  ;

deduction-guide
  : explicit-specifier ? template-name '(' parameter-declaration-clause ')->' simple-template-id ';'
  ;

concept-definition
  : concept concept-name attribute-specifier* '=' constraint-expression ';'
  ;

concept-name
  : identifier
  ;

typename-specifier
  : 'typename' nested-name-specifier identifier
  | 'typename' nested-name-specifier template ? simple-template-id
  ;

extern
  : 'extern'
  ;

explicit-instantiation
  : extern ? 'template' declaration
  ;

explicit-specialization
  : 'template<>' declaration
  ;

//
// A.12 Exception handling
//

try-block
  : 'try' compound-statement handler-seq
  ;

function-try-block
  : 'try' ctor-initializer ? compound-statement handler-seq
  ;

handler-seq
  : handler handler-seq ?
  ;

handler
  : 'catch(' exception-declaration ')' compound-statement
  ;

exception-declaration
  : attribute-specifier* type-specifier-seq declarator
  | attribute-specifier* type-specifier-seq abstract-declarator ?
  | '...'
  ;

noexcept-specifier
  : 'noexcept(' constant-expression ')'
  | 'noexcept'
  ;

//
// A.13 Preprocessing directives
//

preprocessing-file
  : group ?
  | module-file
  ;

module-file
  : pp-global-module-fragment ? pp-module group ? pp-private-module-fragment ?
  ;

pp-global-module-fragment
  : 'module;' new-line group ?
  ;

pp-private-module-fragment
  : 'module : private;' new-line group ?
  ;

group
  : group-part
  | group group-part
  ;

group-part
  : control-line
  | if-section
  | text-line
  | '#' conditionally-supported-directive
  ;

control-line
  : '#include' preprocessing-token+ new-line
  | pp-import
  | '#define' identifier replacement-list new-line
  | '#define' identifier lparen identifier* ')' preprocessing-token* new-line
  | '#define' identifier lparen '...)' preprocessing-token* new-line
  | '#define' identifier lparen identifier+ ',...)' preprocessing-token* new-line
  | '#undef' identifier new-line
  | '#line' preprocessing-token+ new-line
  | '#error' preprocessing-token* new-line
  | '#warning' preprocessing-token* new-line
  | '#pragma' preprocessing-token* new-line
  | '#' new-line
  ;

if-section
  : if-group elif-groups ? else-group ? endif-line
  ;

if-group
  : '#if' constant-expression new-line group ?
  | '#ifdef' identifier new-line group ?
  | '#ifndef' identifier new-line group ?
  ;

elif-groups
  : elif-group
  | elif-groups elif-group
  ;

elif-group
  : '#elif' constant-expression new-line group ?
  | '#elifdef' identifier new-line group ?
  | '#elifndef' identifier new-line group ?
  ;

else-group
  : '#else' new-line group ?
  ;

endif-line
  : '#endif' new-line
  ;

text-line
  : preprocessing-token* new-line
  ;

conditionally-supported-directive
  : preprocessing-token+ new-line
  ;

lparen
  : '<<<Enter a ( character not immediately preceded by whitespace.>>>'
  ;

new-line
  : '<<<Enter the new-line \\n character.>>>'
  ;

defined-macro-expression
  : 'defined' identifier
  | 'defined(' identifier ')'
  ;

h-preprocessing-token
  : '<<<Enter any preprocessing-token other than >.>>>'
  ;

header-name-tokens
  : string-literal
  | '<' h-preprocessing-token+ '>'
  ;

has-include-expression
  : '__has_include(' header-name ')'
  | '__has_include(' header-name-tokens ')'
  ;

has-attribute-expression
  : '__has_cpp_attribute(' preprocessing-token+ ')'
  ;

export
  : 'export'
  ;

pp-module
  : export ? 'module' preprocessing-token* ';' new-line
  ;

pp-import
  : export ? 'import' header-name preprocessing-token* ';' new-line
  | export ? 'import' header-name-tokens preprocessing-token* ';' new-line
  | export ? 'import' preprocessing-token+ ';' new-line
  ;

va-replacement
  : '__VA-OPT__(' preprocessing-token* ')'
  ;

ms-call-modifier
  : '__cdecl'
  | '__clrcall'
  | '__stdcall'
  | '__fastcall'
  | '__thiscall'
  | '__vectorcall'
  ;

ms-call-modifier-seq
  : ms-call-modifier ms-call-modifier-seq ?
  ;

ms-pointer-modifier
  : '__restrict'
  | '__uptr'
  | '__sptr'
  | '_unaligned'
  | '__unaligned'
  ;

ms-declspec-modifier
  : '__declspec(' identifier ')'
  ;
