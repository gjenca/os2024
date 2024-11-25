
import json
import datadir
from collections import UserDict

class JsonDir(datadir.DataDir):

    def __init__(self,dirname):

        self.dirname=dirname
        self.dd=datadir.DataDir(dirname)

    def __getitem__(self,key):

        return json.loads(self.dd[key])

    def __setitem__(self,key,value):

        self.dd[key]=json.dumps(value)

    

