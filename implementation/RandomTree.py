import numpy as np
import random
from Parser import Parser


class RandomTree:
    def retry(exception):
        def wrapper(function):
            def retry_(self, list_of_nodes):
                while True:
                    try:
                        return function(self, list_of_nodes)
                    except exception:
                        pass

            return retry_

        return wrapper

    def split_list(l, minlen=2):
        if len(l) <= minlen:  # if the list is 2 or smaller,
            return l if len(l) > 1 else l[0]  # return the list, or its only element
        x = random.randint(1, len(l) - 1)  # choose a random split
        return [RandomTree.split_list(l[:x], minlen), RandomTree.split_list(l[x:], minlen)]

    @retry(ValueError)
    def add_lengths(self, list_of_nodes):
        for j in range(0, 10):
            for i in range(0, list_of_nodes.__len__() - 1):
                if list_of_nodes[i] == ")" and list_of_nodes[i + 1] is not ":":
                    list_of_nodes = list_of_nodes[:i + 1] + ":" + str(np.random.random_sample()) + list_of_nodes[i + 1:]
        return list_of_nodes

    def __init__(self, option):
        size = np.random.random_integers(4, 80)
        list_of_nodes = []
        for i in range(0, size):
            distance = np.random.random_sample()
            letter = str(chr(97 + i % 22))
            sign = {letter: distance}
            list_of_nodes.append(sign)
        list_of_nodes = str(RandomTree.split_list(list_of_nodes)).replace("{", "").replace("}", "").replace("[",
                                                                                                            "(").replace(
            "]", ")")
        list_of_nodes = RandomTree.add_lengths(self, list_of_nodes) + ";"
        list_of_nodes = list_of_nodes.replace(" ", "")
        p = Parser(list_of_nodes, option)
