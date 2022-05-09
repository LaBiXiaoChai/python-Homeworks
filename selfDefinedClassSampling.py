from dataFactory import dataFactory

class selfDefinedClassSampling(dataFactory):
    """
    DESCRIPTION
    """
    def __init__(self):
        self.__name = "selfDefinedClassSampling"
    def sampling(self,**kwargs):
        result = list()
        if ('num' in kwargs.keys() and 'classname' in kwargs.keys() and 'parameters' in kwargs.keys()):
            for _ in range(0, kwargs.get('num')):
                tmp = eval(kwargs.get('classname'))(kwargs.get('parameters'))
                result.append(tmp)
        else:
            print("The input dictionary should contain 'num' and 'classname' and 'parameters'")
        return result