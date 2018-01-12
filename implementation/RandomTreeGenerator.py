import numpy as np
import re
import tempfile
from Bio import Phylo


class RandomTreeGenerator:
    def length(obj):
        return obj.__len__()

    def retry(exception):
        def wrapper(function):
            def retry_(listofnodes):
                while True:
                    try:
                        return function(listofnodes)
                    except exception:
                        pass

            return retry_

        return wrapper

    @retry(ValueError)
    def values(l):
        place = np.random.random_integers(0, RandomTreeGenerator.length(l) - 1)
        if place + 1 >= RandomTreeGenerator.length(l) - 1:
            raise ValueError
        endplace = np.random.random_integers(place + 1, RandomTreeGenerator.length(l) - 1)
        return place, endplace

    def __init__(self):
        size = np.random.random_integers(2, 10)
        listofnodes = []
        for i in range(0, size):
            distance = np.random.random_sample()
            letter = str(chr(97 + i))
            t = {letter: distance}
            listofnodes.append(t)
        numberofbrackets = np.random.random_integers(0, size - 2)
        listofnodes = str(listofnodes)
        previousplace = []
        if numberofbrackets < 0: numberofbrackets = 0
        print("number of brackets: ", numberofbrackets)
        for i in range(0, numberofbrackets):
            l = listofnodes.split(',')
            place, endplace = RandomTreeGenerator.values(l)
            iter = 0
            while [place, endplace] in previousplace or place + 1 == endplace or [i[0] + 1 == endplace for i in
                                                                                  previousplace]:
                place, endplace = RandomTreeGenerator.values(l)
                iter += 1
                if iter == 3:
                    break
            if iter < 3:
                previousplace.append([place, endplace])
                l[place] = '(' + l[place] + ','
                if l[endplace].endswith(','): l[endplace] = l[endplace][:-1]
                l[endplace] = l[endplace] + ')'
                listofnodes = l[0] + ','
                for j in range(1, l.__len__()):
                    if l[j].endswith('}') or l[j].endswith('} '):
                        l[j] += ','
                    if l[j].endswith(")"):
                        l[j] += ":" + str(np.random.random_sample())
                        l[j] += ","
                    listofnodes += l[j]
                listofnodes = re.sub(",+", ",", listofnodes)
                listofnodes = listofnodes.replace("(),", "")

        if listofnodes.endswith(','): listofnodes = listofnodes[:-1]
        listofnodes = listofnodes + ";"
        listofnodes = listofnodes.replace("{", '')
        listofnodes = listofnodes.replace("[", '(')
        listofnodes = listofnodes.replace("}", '')
        listofnodes = listofnodes.replace("]", ')')
        listofnodes = listofnodes.replace("'", "")
        listofnodes = ''.join(listofnodes.split())
        if re.search(':0.\d+;\Z', listofnodes):
            listofnodes = re.sub(':0.\d+;\Z', ';', listofnodes)
        print("listofnodes", listofnodes)
        file = tempfile.TemporaryFile(mode='w+')
        file.write(listofnodes)
        file.seek(0)
        tree = Phylo.read(file, "newick")
        Phylo.draw(tree)
        file.close()
