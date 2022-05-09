import random
from dataFactory import dataFactory

class strSampling(dataFactory):
    """
    DESCRIPTION
    """
    def __init__(self):
        self.__name = "srtSampling"

    def sampling(self, **kwargs):
        result = list()
        if ('num' in kwargs.keys() and 'datarange' in kwargs.keys()):
            for _ in range(0, kwargs.get('num')):
                it = iter(kwargs.get('datarange'))
                tmp = ''.join(random.SystemRandom().choice(kwargs.get('datarange'))for _ in range(kwargs.get('strlen')))
                result.append(tmp)
        else:
            print("The input dictionary should contain 'num' and 'datarange'")
        return result