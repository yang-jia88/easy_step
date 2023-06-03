import requests
from bs4 import BeautifulSoup
import pandas as pd
res=requests.get("")
soup = BeautifulSoup(res.text,features="html.parser")
print(soup)