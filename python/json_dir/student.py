
class Student:

    def __init__(self,d):

        self.meno=d['meno']
        self.priezvisko=d['priezvisko']

    def __repr__(self):

        return f'Student("{self.meno}","{self.priezvisko}")'
    
    def to_dict(self):

        return {
            'meno':self.meno,
            'priezvisko':self.priezvisko
            }


