
class Obdlznik:
    """TRieda obmmm
    """

    def __init__(self,a,b):

        self.a=a
        self.b=b

    def plocha(self):

        return self.a*self.b

class Stvorec(Obdlznik):

    def __init__(self,a):
        
        self.a=a
        self.b=a
