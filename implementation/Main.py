from implementation import Parser, FileParser

"""BEWARE: if you want to draw a tree, don't forget about ';' at the end of input."""

option = input("Welcome to Phylogenetic Trees project. "
               "Type 'file' if you want to import tree in newick format from file. "
               "Type 'console' if you want to paste it to console.")
newick = ""


def functionality(option):
    if option.lower() == 'file':
        dir = input("Enter directory and name of your file.")
        p = FileParser.FileParser(dir)
    elif option.lower() == 'console':
        newick = input("Please enter your input in newick format.")
        p = Parser.Parser(newick)
    elif option.lower() == 'help':
        # todo
        print("This is help.")
    else:
        print("Need help? Type 'help'.")
        option = input()
        functionality(option)


functionality(option)
