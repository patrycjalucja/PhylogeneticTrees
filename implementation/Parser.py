class Parser:
    def __init__(self, newick):
        print("Checking format correction...")
        if not self.checkCorrection(newick):
            print ("Wrong format. Please try again.")

    def checkCorrection(self, newick):
        print("#TODO")
        return True