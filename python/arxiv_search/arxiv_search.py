#!/usr/bin/env python3
import sys

import requests
from bs4 import BeautifulSoup as BS 

URL="https://arxiv.org/search/"

def find_preprints(query):

    params={'query':query,'searchtype':'all','source':'header'}
    response=requests.get(URL,params)
    soup=BS(response.text,'html.parser')
    results=soup.find_all('li',class_='arxiv-result')
    ret=[]
    for result in results:
        for link in result.find_all('a'):
            if link.text.startswith('arXiv:'):
                ret.append(link.text.split(':',1)[1])

    return ret

query='+'.join(sys.argv[1:])
for code in find_preprints(query):
    print(code)

