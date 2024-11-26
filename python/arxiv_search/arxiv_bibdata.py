#!/usr/bin/env python3
import sys

import requests
from bs4 import BeautifulSoup as BS 


def bibdata(code):

    ret=[]
    URL='https://arxiv.org/abs/'+code
    response=requests.get(URL)
    soup=BS(response.text,'html.parser')
    results=soup.find_all('meta')
    for result in results:
        name=result.get('name')
        content=result.get('content')
        if name!=None and \
           content!=None and name.startswith('citation_'):
            key=name.split('_',1)[1]
            ret.append((key,content))
    return ret

for arg in sys.argv[1:]:
    for key,content in bibdata(arg):
        print(f'{key}:{content}')
    print('-----')

