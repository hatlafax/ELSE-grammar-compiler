ebnf-onvert - Grammar Converter

Converts foreign grammars to W3C-style EBNF as suitable for REx and RR.

  version v0.67
  released Jan 17, 2024
  from https://www.bottlecaps.de/ebnf-convert

Usage: java -jar ebnf-convert.war [-xml|-f FACTORING|-r KIND|-noinline|-noepsilon|-v]... GRAMMAR

  -xml             create output grammar in XML, rather than EBNF
  -f FACTORING     apply factoring (any of "full-left" (default), "left-only", "full-right", "right-only", or "none")
  -r KIND          remove direct recursion, where KIND is any of "full" (default), "left", "right", or "none"
  -noinline        do not inline nonterminals that derive to a single string literal
  -noepsilon       do not keep nonterminal referemces, that derive to epsilon only
  -v               verbose output

  GRAMMAR          path of foreign grammar

ebnf-convert.war is an executable war file. It can be run with "java -jar" as shown
above, but it can also be deployed in servlet containers like Tomcat or Jetty.
