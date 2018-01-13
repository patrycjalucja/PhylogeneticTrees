from ete3 import PhyloTree
import tempfile
from Bio import Phylo
from implementation import Phylol


class Parser:
    def __init__(self, newick, option):
        print("Checking format correction...")
        if not self.check_correction(newick):
            print ("Wrong format. Please try again.")
        else:
            print("Format ok.")
            if option == 'p':
                tree = PhyloTree(newick)
                print(tree)
            else:
                self.parse(newick, "none")

    def check_correction(self, newick):
        brackets = 0
        print(newick)
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

    def parse(self, listofnodes, option):
        file = tempfile.TemporaryFile(mode='w+')
        file.write(listofnodes)
        file.seek(0)
        tree = Phylo.read(file, "newick")
        if option == 's':
            Phylol.draw(tree, do_show=False)
            print("File is saved in this directory and its name is tree.png.")
        else:
            Phylol.draw(tree)
        file.close()
