import sys
"""
This script prints the command-line arguments passed to it.
Usage:
    python comand-line-inpute.py [arg1] [arg2] ...
Arguments:
    arg1, arg2, ... : Optional command-line arguments.
Example:
    python comand-line-inpute.py hello world
    Output: ['comand-line-inpute.py', 'hello', 'world']
"""

print(sys.argv) 
# sys.agrv is a list in python which contains the comando-line arguments passed to the script.
# The first argument is always the script name.
# The command-line arguments are separated by spaces.
# Loop through the command-line arguments and print each one

for i, arg in enumerate(sys.argv):
    print(f"Argument {i}: {arg}")

    
# Run this script from the command-line as follows:
# python comand-line-inpute.py 1 2 3 4 abc
# Output:
# ['comand-line-inpute.py', '1', '2', '3', '4', 'abc']
# Argument 0: comand-line-inpute.py
# Argument 1: 1
# Argument 2: 2
# Argument 3: 3
# Argument 4: 4
# Argument 5: abc