
from collections import UserDict
import os

class DataDir(UserDict):

    def __init__(self,dirname):

        self.dirname=dirname

    def __getitem__(self,key):

        path=f'{self.dirname}/{key}'

        with open(path) as f:
            return f.read()

    def __setitem__(self,key,value):

        path=f'{self.dirname}/{key}'

        with open(path,'w') as f:
            f.write(value)

    def __iter__(self):

        for filename in os.listdir(self.dirname):
            yield filename


