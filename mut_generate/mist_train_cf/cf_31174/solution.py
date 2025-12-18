"""
QUESTION:
Write a function `generate_makefile` that takes a list of C source files as input and returns a string representing the content of a Makefile that can be used to compile and link the source files into an executable. The Makefile should include rules to compile each source file into an object file, link the object files into an executable named "executable", and clean up the generated object files and executable. The compiler should be gcc and the flags should be -Wall.
"""

def generate_makefile(source_files):
    makefile_content = f'''
CC = gcc
CFLAGS = -Wall

all: executable

{' '.join([file.replace('.c', '.o') for file in source_files])}: %.o: %.c
\t$(CC) $(CFLAGS) -c $< -o $@

executable: {' '.join([file.replace('.c', '.o') for file in source_files])}
\t$(CC) $(CFLAGS) $^ -o $@

clean:
\trm -f {' '.join([file.replace('.c', '.o') for file in source_files])} executable
'''

    return makefile_content