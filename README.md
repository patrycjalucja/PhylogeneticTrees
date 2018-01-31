# PhylogeneticTrees
Phylogenetic trees: Newick to .png converter. Student project 2017/2018.

## 1. Introduction
Main aim of the project was to create Newick format to .png converter. It was achieved in many ways - the user can paste the text to the console, read it from the file or even generate random phylogenetic tree. There are few options of tree's visualisation: it can either be displayed as Matplotlib image, saved in the folder or displayed in the console using PhyloTree library. 

## 2. System requirements
Working Python 3 interpreter. The project uses following libraries: Bio, numpy, ete3, optparse, random, matplotlib. 

## 3. Project structure
### 3.1. Implementation part
Implementation part is situated in <i> implementation </i> folder. It consists of the following classes:
- Main.py - Initializer of the project. It provides as well Option Parser, which allows to run project with arguments from the console, as interactive menu. Firstly user has to choose one of the following possibilities: <b><i> file </b></i> for running file mode (available only for .xml files), <b><i> console </b></i> for running from the console, <b><i> r </b></i> for initializing RandomTree class, <b><i> help </b></i> for help and <b><i> q </b></i> for terminating the program. 

  In the <i> file </i> case, user is asked to provide a path with name of the file (or only name if the file is in implementation folder). Then he has to choose if he wants to save file ('s') or only to display it. The FileParser class is initialized.
  While choosing <i> console </i> option, program needs mode specification: by pressing 'p' there will be primitive variant selected, 's' for default visualisation but only saving; in any other case there will be default mode run. Then it's time for newick format (ending by semicolon) provided. The Parser object is created.
  
  When pressing 'r', the user has only to choose between saving and displaying mode. Then there is RandomTree class started. 
  
  Main.py runs again and again until pressing 'q'.
- Parser.py - class which contains two functions besides the __init__ definition. The constructor has three arguments: self, newick (text pasted previously to the console) and option (primitive/saving/default). First there is format correction checked; if it is ok, next steps depend on the chosen mode: for 'p' it uses PhyloTree (from ete3) and draws primitive phylogenetic trees; in 's' case user is asked for naming the figure which has to be created, then 'parse' function starts; in other cases there is also 'parse' function run but without name argument. 

    <i> check_correction(self, newick) </i> function checks if there is semicolon at the end of the text. It also supervises brackets correction.
    
    <i> parse(self, listofnodes, option, title="tree") </i> creates temporary file where the newick format is pasted. This operation was inevitable due to problems with Phylo functions in Python 3. The text is read, then Phylol function <i> draw </i> is initialized and temporary file is closed and deleted.

#TODO: to be continued
