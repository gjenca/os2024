
import datadir


dd=datadir.DataDir('data')
print('pes',dd['pes'])
nohy=int(dd['pes'])+1
dd['pes']=str(nohy)
print('pes',dd['pes'])
for zviera,nohy in dd.items():
    print(zviera,'ma',nohy,'noh')
