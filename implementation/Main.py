from Parser import Parser
from FileParser import FileParser
from RandomTree import RandomTree
import sys
from optparse import OptionParser

"""BEWARE: if you want to draw a tree, don't forget about ';' at the end of input."""

option = ""
option_parser = OptionParser()
option_parser.add_option("-m", "--mode", action="store", type="string", dest="mode")
option_parser.add_option("-a", "--act", action="store", type="string", dest="action")
option_parser.add_option("-f", "--file", action="store", type="string", dest="filename")
option_parser.add_option("-c", "--code", action="store", type="string", dest="code")
(options, args) = option_parser.parse_args()


def functionality(my_option):
    while True:
        if my_option.lower() == 'file':
            dir = input("Enter directory and name of your file.")
            opt = input(
                "Type 's' if you want only to save your file without displaying. "
                "Type whatever if you just want to display the tree.")
            p = FileParser(dir, opt)
            my_option = ""
        elif my_option.lower() == 'console':
            o = input("Type 'p' for primitive console tree, type everything else for normal tree.")
            newick = input("Please enter your input in newick format.")
            p = Parser(newick, o)
            my_option = ""
        elif my_option.lower() == 'help':
            print("- Type 'file' if you want to import tree in newick format from file. "
                  "Then, after pressing enter, you will have to provide the path. \n"
                  "- Type 'console' if you want to paste it to console.\n"
                  "- Type 'r' if you want to generate random tree.\n"
                  "- Press 'q' for exit.\n"
                  "For more information read README.md.")
            my_option = ""
        elif my_option.lower() == 'r':
            opt = input(
                "Type 's' if you want only to save your file without displaying. "
                "Type whatever if you just want to display the tree.")
            p = RandomTree(opt)
            my_option = ""
        elif my_option.lower() == 'q':
            sys.exit()
        else:
            print("Need help? Type 'help'.")
            my_option = input()
            functionality(my_option)


if options.mode == 'console':
    if options.code is not None:
        Parser(options.code, options.action)
    else:
        functionality(options.mode)
elif options.mode == 'file':
    if options.filename is not None:
        FileParser(options.filename, options.action)
    else:
        functionality(options.mode)
elif options.mode == 'r':
    print("RANDOM")
    RandomTree(options.action)

option = input("Welcome to Phylogenetic Trees project. "
               "Type 'file' if you want to import tree in newick format from file. "
               "Type 'console' if you want to paste it to console."
               "Type 'r' if you want to generate random tree."
               "Press 'q' for exit.")
functionality(option)
