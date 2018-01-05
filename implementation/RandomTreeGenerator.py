import numpy as np


class RandomTreeGenerator:
    def __init__(self):
        size = np.random.random_integers(2, 10)
        list = []
        for i in range(0, size):
            distance = np.random.random_sample()
            letter = str(chr(97 + i))
            t = {letter: distance}
            list.append(t)
        numberofbrackets = np.random.random_integers(0, size - 2)
        if numberofbrackets < 0: numberofbrackets = 0  # TODO
        list = str(list)
        list = list + ";"
        print(list)
