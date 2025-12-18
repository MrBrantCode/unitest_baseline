"""
QUESTION:
Introduction
Brainfuck is one of the most well-known esoteric programming languages. But it can be hard to understand any code longer that 5 characters. In this kata you have to solve that problem.

Description

In this kata you have to write a function which will do 3 tasks:

Optimize the given Brainfuck code.
Check it for mistakes.
Translate the given Brainfuck programming code into C programming code.


More formally about each of the tasks:



Your function has to remove from the source code all useless command sequences such as: '+-', '<>', '[]'. Also it must erase all characters except +-<>,.[].
Example:
"++--+." -> "+."
"[][+++]" -> "[+++]"
"<>><" -> ""


If the source code contains unpaired braces, your function should return "Error!" string.


Your function must generate a string of the C programming code as follows:




Sequences of the X commands + or - must be replaced by \*p += X;\n or \*p -= X;\n.
Example:
"++++++++++" -> "\*p += 10;\n"
"------" -> "\*p -= 6;\n"



Sequences of the Y commands > or < must be replaced by p += Y;\n or p -= Y;\n.
Example:
">>>>>>>>>>" -> "p += 10;\n"
"<<<<<<" -> "p -= 6;\n"



. command must be replaced by putchar(\*p);\n.
Example:
".." -> "putchar(\*p);\nputchar(\*p);\n"



, command must be replaced by \*p = getchar();\n.
Example:
"," -> "\*p = getchar();\n"



[ command must be replaced by if (\*p) do {\n. ] command must be replaced by } while (\*p);\n.
Example:
"[>>]" ->
if (\*p) do {\n
  p += 2;\n
} while (\*p);\n



Each command in the code block must be shifted 2 spaces to the right accordingly to the previous code block.
Example:
"[>>[<<]]" ->
if (\*p) do {\n
  p += 2;\n
  if (\*p) do {\n
    p -= 2;\n
  } while (\*p);\n
} while (\*p);\n





Examples

Input:
+++++[>++++.<-]
Output:
*p += 5;
if (*p) do {
  p += 1;
  *p += 4;
  putchar(*p);
  p -= 1;
  *p -= 1;
} while (*p);
"""

import re

def translate_brainfuck_to_c(source):
    # Step 1: Remove all useless command sequences and non-Brainfuck characters
    source = re.sub('[^+-<>,.\[\]]', '', source)
    before = ''
    while source != before:
        before = source
        source = re.sub('\+\-|\-\+|\<\>|\>\<|\[\]', '', source)
    
    # Step 2: Check for unpaired braces
    braces = re.sub('[^[\]]', '', source)
    while braces.count('[]'):
        braces = braces.replace('[]', '')
    if braces:
        return 'Error!'
    
    # Step 3: Translate the Brainfuck code to C code
    commands = re.findall('\++|-+|>+|<+|[.,\[\]]', source)
    output = []
    indent = 0
    for cmd in commands:
        if cmd[0] in '+-<>':
            line = '%sp %s= %s;\n' % ('*' if cmd[0] in '+-' else '', '+' if cmd[0] in '+>' else '-', len(cmd))
        elif cmd == '.':
            line = 'putchar(*p);\n'
        elif cmd == ',':
            line = '*p = getchar();\n'
        elif cmd == '[':
            line = 'if (*p) do {\n'
        elif cmd == ']':
            line = '} while (*p);\n'
            indent -= 1
        output.append('  ' * indent + line)
        if cmd == '[':
            indent += 1
    
    return ''.join(output)