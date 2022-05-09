import random
from dataFactory import dataFactory

class intSampling(dataFactory):
    """
    DESCRIPTION
    """
    def __init__(self):
        self.__name = "intSampling"

    def sampling(self, **kwargs):
        result = list()
        if ('num' in kwargs.keys() and 'datarange' in kwargs.keys()):
            for _ in range(0, kwargs.get('num')):
                it = iter(kwargs.get('datarange'))
                tmp = random.randint(next(it), next(it))
                result.append(tmp)
        else:
            print("The input dictionary should contain 'num' and 'datarange'")
        return result