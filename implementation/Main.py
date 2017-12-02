from implementation import Parser

option = input("Welcome to Phylogenetic Trees project. Type 'file' if you want to import tree in newick format from file. Type 'console' if you want to paste it to console.")
newick = ""
if option.lower() == 'file':
    dir = input ("Enter directory and name of your file.")
    with open (dir) as file:
        newick = file.read()
elif option.lower() == 'console':
    newick = input ("Please enter your input in newick format.")
else:
    option = ""

if option is not None:
    p = Parser.Parser(newick)