from Bio import Phylo


class Parser:
    def __init__(self, newick):
        print("Checking format correction...")
        if not self.checkcorrection(newick):
            print ("Wrong format. Please try again.")
        else:
            print("Format ok.")
            Phylo.draw(newick)

    def checkcorrection(self, newick):
        print("found")
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