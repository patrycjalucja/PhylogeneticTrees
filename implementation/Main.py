from Parser import Parser
from FileParser import FileParser
from RandomTreeGenerator import RandomTreeGenerator
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


class Main:
    def __init__(self):
        if options.mode == 'console':
            if options.code is not None:
                Parser(options.code, options.act)
            else:
                self.functionality(options.mode)
        elif options.mode == 'file':
            if options.file is not None:
                FileParser(options.file, options.act)
            else:
                self.functionality(options.mode)
        elif options.mode == 'r':
            RandomTreeGenerator(options.act)
        else:
            option = input("Welcome to Phylogenetic Trees project. "
                           "Type 'file' if you want to import tree in newick format from file. "
                           "Type 'console' if you want to paste it to console."
                           "Type 'r' if you want to generate random tree."
                           "Press 'q' for exit.")
            self.functionality(option)

    def functionality(self, option):
        while True:
            if option.lower() == 'file':
                dir = input("Enter directory and name of your file.")
                opt = input(
                    "Type 's' if you want only to save your file without displaying. "
                    "Type whatever if you just want to display the tree.")
                p = FileParser(dir, opt)
                option = ""
            elif option.lower() == 'console':
                o = input("Type 'p' for primitive console tree, type everything else for normal tree.")
                newick = input("Please enter your input in newick format.")
                p = Parser(newick, o)
                option = ""
            elif option.lower() == 'help':
                print("This is help.")
                # TODO
            elif option.lower() == 'r':
                opt = input(
                    "Type 's' if you want only to save your file without displaying. "
                    "Type whatever if you just want to display the tree.")
                p = RandomTreeGenerator(opt)
                option = ""
            elif option.lower() == 'q':
                sys.exit()
            else:
                print("Need help? Type 'help'.")
                option = input()
                Main.functionality(self, option)


m = Main()
