# Simple-Compiler
Simple compiler made with my friend Jean in Python.

<h3> Subject: Linguagem de Programação </h3>

  Activity 01: Create a postfix expression taking as entry an infix expression.

<ul>
  <li> BNF: </li>
  <li> [programa] 		:- [lista_instruções] </li>
  <li> [lista_instruções] 	:- [instrução] ; [lista_instruções] | [instrução] </li>
  <li> [instrução]		:- [expressão] </li>
  <li> [expressão]		:- [var] = [expressão] | [var] + [var] | [var] - [var] | [var] * [var] | [var] / [var] | [var] </li>
  <li> [var]			:- A | B | C | [dígito] </li>
  <li> [dígito]		:- 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | [dígito][dígito] </li>
</ul>

  Acticvity 02: Calculate the postfix expression that you created at Activity 01.
  
<h3> Important: </h3>

We only evaluate expressions of 2 types: A = B + C or A = B.
Where A is always a [var] and B and C can be [var] or [digit]
