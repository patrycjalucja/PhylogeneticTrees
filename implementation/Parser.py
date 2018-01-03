class Parser:
    def __init__(self, newick):
        print("Checking format correction...")
        if not self.checkCorrection(newick):
            print ("Wrong format. Please try again.")
        else:
            print("Format ok.")

    def checkCorrection(self, newick):
        brackets = 0
        for i in newick:
            if i == '(':
                brackets = brackets + 1
            elif i == ')':
                if brackets <= 0:
                    return False
                brackets = brackets - 1
        if brackets is not 0 or not newick.strip().endswith(';'):
            return False
        return True