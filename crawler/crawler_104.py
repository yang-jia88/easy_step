import requests
from bs4 import BeautifulSoup
import pandas as pd
res=requests.get("https://www.104.com.tw/jobs/search/?keyword=%E5%A4%A7%E6%95%B8%E6%93%9A&order=1&jobsource=2018indexpoc&ro=0")
soup = BeautifulSoup(res.text,features="html.parser")

# print(soup.select("use")[0]["href="])
# print(soup.article.select("a"))
# print(soup.article.select("a")[0]["href"])
# print(soup.article.select("a")[1].text)
# print(soup.article.select("li")[3].text)
# print(soup.article.select("a")[2].text)
# print(soup.article.select("a")[0]["class"])
# if soup.find_all('article',class_="b-block--top-bord job-list-item b-clearfix js-job-item")[2].find('div',class_="job-list-tag b-content").select('span')==[]:
#     print(soup.find_all('article',class_="b-block--top-bord job-list-item b-clearfix js-job-item")[2].find('div',class_="job-list-tag b-content").a.text)
# else:
#     print(soup.find_all('article',class_="b-block--top-bord job-list-item b-clearfix js-job-item")[2].find('div',class_="job-list-tag b-content").span.text)
# while soup.find_all("article",class_="b-block--top-bord job-list-item b-clearfix js-job-item") != []: 
#     for job in soup.find_all("article",class_="b-block--top-bord job-list-item b-clearfix js-job-item"):
#         print(job.select("a")[0].text)
#         print("https"+job.select("a")[0]["href"])
#         if job.find("div",class_="job-list-tag b-content").select('span')==[]:
#             print(job.select("a")[2].text)
#         else:print(job.select("span")[1].text)
#         print(job.select("li")[3].text)
#         print(job.select("li")[1].text.strip())


df = {"職位":[],"網址":[],"公司":[],"地點":[],"薪水":[]}
n=0
page = 1
while soup.find_all("article",class_="b-block--top-bord job-list-item b-clearfix js-job-item") != []: 
    for job in soup.find_all("article",class_="b-block--top-bord job-list-item b-clearfix js-job-item"):
        print("進行中"+str(n))
        position = job.select("a")[0].text
        df["職位"].append(position)
        net = "https"+job.select("a")[0]["href"]
        df["網址"].append(net)
        if job.find('div',class_="job-list-tag b-content").select('span')!=[] and job.find('div',class_="job-list-tag b-content").select('span')[0].text=="待遇面議":#薪水
            salary = job.select("a")[2].text
        else:salary = job.select("span")[1].text
        df["薪水"].append(salary)
        locate = job.select("li")[3].text
        df["地點"].append(locate)
        company_name = job.select("li")[1].text.strip()
        df["公司"].append(company_name)
        n+=1
        print(n)
    page += 1
    res = requests.get("https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=%E5%A4%A7%E6%95%B8%E6%93%9A&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=15&asc=0&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1&page=" + str(page)) #將"&page=2"放到最後面
    soup = BeautifulSoup(res.text,features="html.parser")
df = pd.DataFrame(df)
df.to_csv("original_data_104.csv", index = False)