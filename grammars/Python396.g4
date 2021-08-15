parser grammar Python396;

program:
      statement*
    ;

func_type: 
      '(' type_expressions? ')' '->' expression
    ;

type_expressions:
      ','.expression+ ',' '*' expression ',' '**' expression 
    | ','.expression+ ',' '*' expression 
    | ','.expression+ ',' '**' expression 
    | '*' expression ',' '**' expression 
    | '*' expression 
    | '**' expression 
    | ','.expression+
    ;

statements: statement+;

statement: compound_stmt | simple_stmt;

simple_stmt: ';'.small_stmt+;

small_stmt:
      assignment
    | star_expressions 
    | return_stmt
    | import_stmt
    | raise_stmt
    | 'pass' 
    | del_stmt
    | yield_stmt
    | assert_stmt
    | 'break' 
    | 'continue' 
    | global_stmt
    | nonlocal_stmt
    ;

compound_stmt:
      function_def
    | if_stmt
    | class_def
    | with_stmt
    | for_stmt
    | async_for_stmt
    | try_finally_stmt
    | try_except_else_finally_stmt
    | while_stmt
    ;

assignment:
      NAME ':' expression ('=' annotated_rhs)?
    | ('(' single_target ')' | single_subscript_attribute_target) ':' expression ('=' annotated_rhs)?
    | (star_targets '=')+ (yield_expr | star_expressions) TYPE_COMMENT?
    | single_target augassign (yield_expr | star_expressions) 
    ;

augassign:
      '+=' 
    | '-=' 
    | '*=' 
    | '@=' 
    | '/=' 
    | '%=' 
    | '&=' 
    | '|=' 
    | '^=' 
    | '<<=' 
    | '>>=' 
    | '**=' 
    | '//=' 
    ;

global_stmt: 'global' ','.NAME+;

nonlocal_stmt: 'nonlocal' ','.NAME+;

yield_stmt: yield_expr;

assert_stmt: 'assert' expression (',' expression)?;

del_stmt:
      'del' del_targets
    ;

import_stmt: import_name | import_from;

import_name: 'import' dotted_as_names;

import_from:
      'from' ('.' | '...')* dotted_name 'import' import_from_targets 
    | 'from' ('.' | '...')+ 'import' import_from_targets 
    ;

import_from_targets:
      '(' import_from_as_names ','? ')' 
    | import_from_as_names
    | '*' 
    ;

import_from_as_names:
      ','.import_from_as_name+ 
    ;

import_from_as_name:
      NAME ('as' NAME)?
    ;

dotted_as_names:
      (dotted_as_name (',' dotted_as_name)*) 
    ;

dotted_as_name:
      dotted_name ('as' NAME)?
    ;

dotted_name:
      dotted_name '.' NAME 
    | NAME
    ;

if_stmt:
      'if' named_expression ':' NEWLINE INDENT statement+ NEWLINE elif_stmt* NEWLINE else_block?
    ;

elif_stmt:
      'elif' named_expression ':' NEWLINE INDENT statement+
    ;

else_block: 
      'else' ':' NEWLINE INDENT statement+
    ;

while_stmt:
      'while' named_expression ':' NEWLINE INDENT statement+ NEWLINE else_block?
    ;

for_stmt:
      'for' star_targets 'in' star_expressions ':' TYPE_COMMENT? NEWLINE INDENT statement+ NEWLINE else_block?
    | 
    ;

async_for_stmt:
        'async for' star_targets 'in' star_expressions ':' TYPE_COMMENT? NEWLINE INDENT statement+ NEWLINE else_block?
    | 
    ;

with_stmt:
      with_non_braced_stmt
    | with_braced_stmt
    | async_with_non_braced_stmt
    | async_with_braced_stmt
    ;

with_non_braced_stmt:
      'with' ','.with_item+ ':' TYPE_COMMENT? NEWLINE INDENT statement+
    ;

with_braced_stmt:
      'with' '(' ','.with_item+ ','? ')' ':' NEWLINE INDENT statement+
    ;

async_with_non_braced_stmt:
      'async with' ','.with_item+ ':' TYPE_COMMENT? NEWLINE INDENT statement+
    ;

async_with_braced_stmt:
      'async with' '(' ','.with_item+ ','? ')' ':' NEWLINE INDENT statement+
    ;

with_item:
      expression 'as' star_target
    | expression 
    ;

try_finally_stmt:
      'try' ':' NEWLINE INDENT statement+ NEWLINE finally_block 
    ;

try_except_else_finally_stmt:
      'try' ':' NEWLINE INDENT statement+ NEWLINE except_block+ NEWLINE else_block? NEWLINE finally_block?
    ;

except_block:
      except_block_expression_stmts
    | except_block_stmts
    ;

except_block_expression_stmts:
      'except' expression ('as' NAME)? ':' NEWLINE INDENT statement+
    ;

except_block_stmts:
      'except' ':' NEWLINE INDENT statement+
    ;

finally_block:
      'finally' ':' NEWLINE INDENT statement+
    ;

return_stmt:
      'return' star_expressions?
    ;

raise_stmt:
      'raise' expression ('from' expression)?
    | 'raise' 
    ;

function_def:
      decorator* NEWLINE (function_def_raw | function_async_def_raw)
    ;

function_def_raw:
      'def' NAME '(' parameters? ')' ('->' expression)? ':' func_type_comment? NEWLINE INDENT statement+
    ;

function_async_def_raw:
      'async def' NAME '(' parameters? ')' ('->' expression)? ':' func_type_comment? NEWLINE INDENT statement+
    ;

func_type_comment:
      '#' STRING
    ;

parameters:
      slash_no_default param_no_default* param_with_default* star_etc?
    | slash_with_default param_with_default* star_etc?
    | param_no_default+ param_with_default* star_etc?
    | param_with_default+ star_etc?
    | star_etc 
    ;

slash_no_default:
      param_no_default+ '/' ',' 
    | param_no_default+ '/'
    ;

slash_with_default:
      param_no_default* param_with_default+ '/' ',' 
    | param_no_default* param_with_default+ '/'
    ;

star_etc:
      '*' param_no_default param_maybe_default* kwds?
    | '*' ',' param_maybe_default+ kwds?
    | kwds 
    ;

kwds: '**' param_no_default;

param_no_default:
      param ',' TYPE_COMMENT? 
    | param TYPE_COMMENT?
    ;

param_with_default:
      param default ',' TYPE_COMMENT? 
    | param default TYPE_COMMENT?
    ;

param_maybe_default:
      param default? ',' TYPE_COMMENT? 
    | param default? TYPE_COMMENT?
    ;

param: NAME annotation?;

annotation: ':' expression;

default: '=' expression;

decorator: ('@' named_expression);

class_def:
      decorator* NEWLINE class_def_raw 
    ;

class_def_raw:
      'class' NAME ('(' arguments? ')')? ':' NEWLINE INDENT statement+ 
    ;

star_expressions:
      star_expression (',' star_expression)+ ','? 
    | star_expression ',' 
    | star_expression
    ;

star_expression:
      '*' bitwise_or 
    | expression
    ;

star_named_expressions: ','.star_named_expression+ ','?;

star_named_expression:
      '*' bitwise_or 
    | named_expression
    ;

named_expression:
      NAME ':=' expression 
    | expression
    ;

annotated_rhs: yield_expr | star_expressions;

expressions:
      expression (',' expression)+ ','?
    | expression ',' 
    | expression
    ;

expression:
      disjunction 'if' disjunction 'else' expression 
    | disjunction
    | lambdef
    ;

lambdef:
      'lambda' lambda_parameters? ':' expression 
    ;

lambda_parameters:
      lambda_slash_no_default lambda_param_no_default* lambda_param_with_default* lambda_star_etc?
    | lambda_slash_with_default lambda_param_with_default* lambda_star_etc?
    | lambda_param_no_default+ lambda_param_with_default* lambda_star_etc?
    | lambda_param_with_default+ lambda_star_etc?
    | lambda_star_etc 
    ;

lambda_slash_no_default:
      lambda_param_no_default+ '/' ',' 
    | lambda_param_no_default+ '/'
    ;

lambda_slash_with_default:
      lambda_param_no_default* lambda_param_with_default+ '/' ',' 
    | lambda_param_no_default* lambda_param_with_default+ '/'
    ;

lambda_star_etc:
      '*' lambda_param_no_default lambda_param_maybe_default* lambda_kwds?
    | '*' ',' lambda_param_maybe_default+ lambda_kwds?
    | lambda_kwds 
    ;

lambda_kwds: '**' lambda_param_no_default;

lambda_param_no_default:
      LAMBDA_PARAM ',' 
    | LAMBDA_PARAM
    ;

lambda_param_with_default:
      LAMBDA_PARAM default ',' 
    | LAMBDA_PARAM default
    ;

lambda_param_maybe_default:
      LAMBDA_PARAM default? ',' 
    | LAMBDA_PARAM default?
    ;

disjunction:
      conjunction ('or' conjunction)+ 
    | conjunction
    ;

conjunction:
      inversion ('and' inversion)+ 
    | inversion
    ;

inversion:
      'not' inversion 
    | comparison
    ;

comparison:
      bitwise_or compare_op_bitwise_or_pair+ 
    | bitwise_or
    ;

compare_op_bitwise_or_pair:
      eq_bitwise_or
    | noteq_bitwise_or
    | lte_bitwise_or
    | lt_bitwise_or
    | gte_bitwise_or
    | gt_bitwise_or
    | notin_bitwise_or
    | in_bitwise_or
    | isnot_bitwise_or
    | is_bitwise_or
    ;

eq_bitwise_or: '==' bitwise_or;

noteq_bitwise_or:
      '!=' bitwise_or 
    ;

lte_bitwise_or: '<=' bitwise_or;

lt_bitwise_or: '<' bitwise_or;

gte_bitwise_or: '>=' bitwise_or;

gt_bitwise_or: '>' bitwise_or;

notin_bitwise_or: 'not' 'in' bitwise_or;

in_bitwise_or: 'in' bitwise_or;

isnot_bitwise_or: 'is' 'not' bitwise_or;

is_bitwise_or: 'is' bitwise_or;

bitwise_or:
      bitwise_or '|' bitwise_xor 
    | bitwise_xor
    ;

bitwise_xor:
      bitwise_xor '^' bitwise_and 
    | bitwise_and
    ;

bitwise_and:
      bitwise_and '&' shift_expr 
    | shift_expr
    ;

shift_expr:
      shift_expr '<<' sum 
    | shift_expr '>>' sum 
    | sum
    ;

sum:
      sum '+' term 
    | sum '-' term 
    | term
    ;

term:
      term '*' factor 
    | term '/' factor 
    | term '//' factor 
    | term '%' factor 
    | term '@' factor 
    | factor
    ;

factor:
      '+' factor 
    | '-' factor 
    | '~' factor 
    | power
    ;

power:
      await_primary '**' factor 
    | await_primary
    ;

await_primary:
      'await' primary 
    | primary
    ;

primary:
      invalid_primary
    | primary '.' NAME 
    | primary genexp 
    | primary '(' arguments? ')' 
    | primary '[' slices ']' 
    | atom
    ;

slices:
      slice
    | ','.slice+ ','?
    ;

slice:
      expression? ':' expression? (':' expression?)? 
    | expression 
    ;

atom:
      NAME
    | 'True' 
    | 'False' 
    | 'None' 
    | '__peg_parser__' 
    | strings
    | NUMBER
    | (tuple | group | genexp)
    | (list | listcomp)
    | (dict | set | dictcomp | setcomp)
    | '...' 
    ;

strings: STRING+;

list:
      '[' star_named_expressions? ']' 
    ;

listcomp:
      '[' named_expression for_if_clauses ']' 
    ;

tuple:
      '(' (star_named_expression ',' star_named_expressions?)? ')' 
    ;

group:
      '(' (yield_expr | named_expression) ')' 
    ;

genexp:
      '(' named_expression for_if_clauses ')' 
    ;

set: '{' star_named_expressions '}';

setcomp:
      '{' named_expression for_if_clauses '}' 
    ;

dict:
      '{' double_starred_kvpairs? '}' 
    ;

dictcomp:
      '{' kvpair for_if_clauses '}' 
    ;

double_starred_kvpairs: ','.double_starred_kvpair+ ','?;

double_starred_kvpair:
      '**' bitwise_or 
    | kvpair
    ;

kvpair: expression ':' expression;

for_if_clauses:
      for_if_clause+
    ;

for_if_clause:
      'async' 'for' star_targets 'in' disjunction ('if' disjunction)* 
    | 'for' star_targets 'in' disjunction ('if' disjunction)* 
    ;

yield_expr:
      'yield' 'from' expression 
    | 'yield' star_expressions?
    ;

arguments:
      args ','?
    ;

args:
      ','.(starred_expression | named_expression)+ (',' kwargs)?
    | kwargs 
    ;

kwargs:
      ','.kwarg_or_starred+ ',' ','.kwarg_or_double_starred+ 
    | ','.kwarg_or_starred+
    | ','.kwarg_or_double_starred+
    ;

starred_expression:
      '*' expression 
    ;

kwarg_or_starred:
      NAME '=' expression 
    | starred_expression 
    ;

kwarg_or_double_starred:
      NAME '=' expression 
    | '**' expression 
    ;

star_targets:
      star_target
    | ','.star_target+ ','? 
    ;

star_targets_list_seq: ','.star_target+ ','?;

star_targets_tuple_seq:
      star_target (',' star_target)+ ','?
    | star_target ',' 
    ;

star_target:
      '*' star_target 
    | target_with_star_atom
    ;

target_with_star_atom:
      t_primary '.' NAME
    | t_primary '[' slices ']'
    | star_atom
    ;

star_atom:
      NAME 
    | '(' target_with_star_atom ')' 
    | '(' star_targets_tuple_seq? ')' 
    | '[' star_targets_list_seq? ']' 
    ;

single_target:
      single_subscript_attribute_target
    | NAME 
    | '(' single_target ')' 
    ;

single_subscript_attribute_target:
      t_primary '.' NAME
    | t_primary '[' slices ']'
    ;

del_targets: ','.del_target+ ','?;

del_target:
      t_primary '.' NAME 
    | t_primary '[' slices ']'
    | del_t_atom
    ;

del_t_atom:
      NAME 
    | '(' del_target ')' 
    | '(' del_targets? ')' 
    | '[' del_targets? ']' 
    ;

t_primary:
      t_primary '.' NAME
    | t_primary '[' slices ']' 
    | t_primary genexp 
    | t_primary '(' arguments? ')' 
    | atom 
    ;

LAMBDA_PARAM:
      STRING
    ;
