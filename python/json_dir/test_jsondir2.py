from jsondir import JsonDir

jd=JsonDir('data_numlists')
for key in jd:
    print(key,'má súčet',sum(jd[key]))


