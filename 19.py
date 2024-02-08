
# Q-19: How Do You Handle Exceptions With Try/Except/Finally In Python?
# Explain with coding snippets.

# ans:

a = 10
b = 0

try:
    c = a / b
    print(c)
except ZeroDivisionError as error:
    print(error)
finally:
    print('Finishing up.')

# coding snippets:

# "Code Snippet" is a term used to describe a small portion of re-usable source code, machine code, or text.
# They allow a programmer to avoid typing repetitive code during the course of routine programming.
# Most modern text editing programs possess some form of Snippet creation and management
# (I say most because I do not know of every single editor that exists).
# While the exact way you manage Code Snippets does vary slightly from editor to editor, the basic concept is the same.
# For examples I will be using Visual Studio Code.
# Comprises a Code Snippet: Name, Prefix, Body, Description..