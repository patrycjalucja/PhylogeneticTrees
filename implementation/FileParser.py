from Bio import Phylo
import Phylol

"""Class which is responsible for handling files with newick format"""

class FileParser:
    def __init__(self, location, option):
        try:
            print("Checking format correction...")
            if not self.check_correction(location):
                print("Wrong format. Please try again.")
            else:
                print("Format ok.")
                tree = Phylo.read(location, "newick")
                if option == 's':
                    Phylol.draw(location, tree, do_show=False)
                    print("File is saved in this directory and its name is same as in xml format.")
                else:
                    Phylol.draw(location, tree)
        except FileNotFoundError:
            print("File not found.")

    def check_correction(self, location):
        brackets = 0
        with open(location) as file:
            newick = file.read()
        for i in newick:
            if i == '(':
                brackets = brackets + 1
            elif i == ')':
                if brackets <= 0:
                    return False
                brackets = brackets - 1
        if brackets is not 0 or not newick.strip().replace(" ", "").endswith(';'):
            print(brackets)
            return False
        return True
