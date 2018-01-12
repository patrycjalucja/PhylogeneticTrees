from implementation import Parser, FileParser, RandomTreeGenerator

"""BEWARE: if you want to draw a tree, don't forget about ';' at the end of input."""

option = input("Welcome to Phylogenetic Trees project. "
               "Type 'file' if you want to import tree in newick format from file. "
               "Type 'console' if you want to paste it to console.")
newick = ""


def functionality(option):
    if option.lower() == 'file':
        dir = input("Enter directory and name of your file.")
        opt = input(
            "Type 's' if you want only to save your file without displaying. Type whatever if you just want to display the tree.")
        p = FileParser.FileParser(dir, opt)
    elif option.lower() == 'console':
        newick = input("Please enter your input in newick format.")
        p = Parser.Parser(newick)
    elif option.lower() == 'help':
        print("This is help.")
        # TODO
    elif option.lower() == 'r':
        p = RandomTreeGenerator.RandomTreeGenerator()
    else:
        print("Need help? Type 'help'.")
        option = input()
        functionality(option)


functionality(option)
