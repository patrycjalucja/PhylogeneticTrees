import numpy as np
from implementation import Parser


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
        if numberofbrackets < 0: numberofbrackets = 0
        print("nob", numberofbrackets)
        for i in range(0, numberofbrackets):
            l = listofnodes.split(',')
            place, endplace = RandomTreeGenerator.values(l)
            l[place] = '(' + l[place] + ','
            if l[endplace].endswith(','): l[endplace] = l[endplace][:-1]
            l[endplace] = l[endplace] + '),'
            listofnodes = l[0] + ','
            for j in range(1, l.__len__()):
                if l[j].endswith('}') or l[j].endswith('} ') or l[j].endswith(')'):
                    l[j] += ','
                listofnodes += l[j]
            listofnodes.replace("[,+]", ",")
            listofnodes.replace("(),", "")

        if listofnodes.endswith(','): listofnodes = listofnodes[:-1]
        listofnodes = listofnodes + ";"
        listofnodes = listofnodes.replace("{", '(')
        listofnodes = listofnodes.replace("[", '(')
        listofnodes = listofnodes.replace("}", ')')
        listofnodes = listofnodes.replace("]", ')')
        print("listofnodes", listofnodes)
        z = Parser.Parser(listofnodes)
