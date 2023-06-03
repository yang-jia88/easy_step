from bs4 import BeautifulSoup
path="web.html"
with open (path,"r",encoding = "utf - 8") as file:
    # print(file.read())
    soup = BeautifulSoup(file.read(),'html')
# print(soup.prettify()) 
# print(soup.head.title.text)
# print(soup.find ("h1",class_="abc"))
print(soup.find_all("h2"))
print(soup.select(".abc"))
print(soup.h2.text)