from jsondir import JsonDir
import random

jd=JsonDir('data_numlists')
for n in range(10):
    # zoznam nahodnych cisel
    zoz=[]
    for i in range(5):
        zoz.append(random.randrange(0,10))
    jd[f'numlist{n}']=zoz


