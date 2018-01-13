import numpy as np
import re
from implementation import Parser


class RandomTreeGenerator:
    def length(obj):
        return obj.__len__()

    def retry(exception):
        def wrapper(function):
            def retry_(list_of_nodes):
                while True:
                    try:
                        return function(list_of_nodes)
                    except exception:
                        pass

            return retry_

        return wrapper

    @retry(ValueError)
    def values(l):
        place = np.random.random_integers(0, RandomTreeGenerator.length(l) - 1)
        if place + 1 >= RandomTreeGenerator.length(l) - 1:
            raise ValueError
        end_place = np.random.random_integers(place + 1, RandomTreeGenerator.length(l) - 1)
        return place, end_place

    def check_for_duplicates(self, previous, place, end_place, nodes):
        iter = 0
        while [place, end_place] in previous or place + 1 == end_place or [i[0] + 1 == end_place for i in
                                                                           previous]:
            place, end_place = RandomTreeGenerator.values(nodes)
            iter += 1
            if iter == 3:
                return False
        return True

    def replace(self, list_of_nodes):
        list_of_nodes = re.sub(",+", ",", list_of_nodes)
        list_of_nodes = list_of_nodes.replace("(),", "")
        if list_of_nodes.endswith(','): list_of_nodes = list_of_nodes[:-1]
        list_of_nodes = list_of_nodes + ";"
        list_of_nodes = list_of_nodes.replace("{", '')
        list_of_nodes = list_of_nodes.replace("[", '(')
        list_of_nodes = list_of_nodes.replace("}", '')
        list_of_nodes = list_of_nodes.replace("]", ')')
        list_of_nodes = list_of_nodes.replace("'", "")
        list_of_nodes = ''.join(list_of_nodes.split())
        if re.search(':0.\d+;\Z', list_of_nodes):
            list_of_nodes = re.sub(':0.\d+;\Z', ';', list_of_nodes)
        return list_of_nodes

    def __init__(self, option):
        size = np.random.random_integers(2, 10)
        list_of_nodes = []
        for i in range(0, size):
            distance = np.random.random_sample()
            letter = str(chr(97 + i))
            sign = {letter: distance}
            list_of_nodes.append(sign)
        number_of_brackets = np.random.random_integers(0, size - 2)
        list_of_nodes = str(list_of_nodes)
        previous_place = []
        if number_of_brackets < 0: number_of_brackets = 0
        print("number of brackets: ", number_of_brackets)
        for i in range(0, number_of_brackets):
            l = list_of_nodes.split(',')
            place, end_place = RandomTreeGenerator.values(l)
            if not RandomTreeGenerator.check_for_duplicates(self, previous_place, place, end_place, l):
                break
            previous_place.append([place, end_place])
            l[place] = '(' + l[place] + ','
            if l[end_place].endswith(','): l[end_place] = l[end_place][:-1]
            l[end_place] = l[end_place] + ')'
            list_of_nodes = l[0] + ','
            for j in range(1, l.__len__()):
                if l[j].endswith('}') or l[j].endswith('} '):
                    l[j] += ','
                if l[j].endswith(")"):
                    l[j] += ":" + str(np.random.random_sample())
                    l[j] += ","
                list_of_nodes += l[j]
        list_of_nodes = RandomTreeGenerator.replace(self, list_of_nodes)
        print("list of nodes", list_of_nodes)
        Parser.Parser.parse(self, list_of_nodes, option)
