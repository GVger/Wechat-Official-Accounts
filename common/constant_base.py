# coding=utf-8
import re


class ConstantBaseBase(object):
    class ConstError(TypeError):
        pass

    def __init__(self):
        pass

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise self.ConstError("Constant cannot be changed")
        self.__dict__[key] = value


class ConstantBase(ConstantBaseBase):
    class ConstError(TypeError):
        pass

    def __init__(self, constants):
        ConstantBaseBase.__init__(self)
        array = re.split(r'\s*,\s*', constants)
        for key in array:
            self.__dict__[key.upper()] = key

    def __setattr__(self, key, value):
        ConstantBaseBase.__setattr__(self, key, value)
