from Bio import Phylo
from implementation import Phylol


class FileParser:
    def __init__(self, newick, option):
        print("Checking format correction...")
        if not self.checkcorrection(newick):
            print("Wrong format. Please try again.")
        else:
            print("Format ok.")
            tree = Phylo.read(newick, "newick")
            if option == 's':
                Phylol.draw(tree, do_show=False)
                print("File is saved in this directory and its name is tree.png.")
            else:
                Phylol.draw(tree)

    def checkcorrection(self, location):
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
        if brackets is not 0 or not newick.strip().endswith(';'):
            print(brackets)
            return False
        return True
