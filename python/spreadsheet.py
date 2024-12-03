
class SpreadSheet(dict):

    def __getitem__(self,key):
        
        val=dict.__getitem__(self,key)
        if type(val)==str:
            return eval(val,self)
        else:
            return val


