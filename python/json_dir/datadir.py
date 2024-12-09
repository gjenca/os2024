
from collections.abc import MutableMapping
import os

class DataDir(MutableMapping):

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

    def __delitem__(self,key):
        
        path=f'{self.dirname}/{key}'
        try:
            os.remove(path)
        except IOError:
            raise KeyError(f'{key}')

    def __len__(self):

        return len(os.listdir(self.dirname))


