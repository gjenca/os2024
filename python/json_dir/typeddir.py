
import jsondir

def TypedDirFactory(C):

    class TypedDir(jsondir.JsonDir):

        def __init__(self,dirname):

            self.dirname=dirname
            self.jd=jsondir.JsonDir(dirname)

        def __getitem__(self,key):

            return C(self.jd[key]) 

        def __setitem__(self,key,value):

            self.jd[key]=value.to_dict()

    return TypedDir

    

