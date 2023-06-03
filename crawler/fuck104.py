import requests
from bs4 import BeautifulSoup
res=requests.get("https://www.104.com.tw/jobs/search/?keyword=%E5%A4%A7%E6%95%B8%E6%93%9A&order=1&jobsource=2018indexpoc&ro=0")
soup = BeautifulSoup(res.text,'html')
print(soup.article.a.prettify())
# for article in soup("article"):
#     print(article("a")[1].text)#公司
#     print(soup.article("li")[2].text)#地址
#     print(soup.article.find("a",class_="js-job-link").text)#職位
#     print(soup.article.select("a[class=b-tag--default]")[0].text)#薪水
#     print(soup.article("a")[2]["href"])#網址

# for job in soup.find_all("article",class_="b-block--top-bord job-list-item b-clearfix js-job-item"):
# #     # print(job)
#     print(job["data-cust-name"])
#     print(job.find("a",class_="js-job-link").text)
#     print("https:"+job.find("a",class_="js-job-link")["href"])
#     print(job("li")[3].text)