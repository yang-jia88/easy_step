import requests
from abc import abstractmethod
import json
class crawler:
    def __init__(self,loc,token):
        self.loc=loc
        self.token=token
    @abstractmethod
    def getinfo():
        pass
class GraberFB(crawler):
    def getinfo(self.loc):
        res=requests.get(self.loc+token)
        return res
    def loadfile(self.res):
        data=json.loads(self.res.text)
        return data

class GraberOther(crawler):
    def getFAKE(self.loc):
        print("haha I am FAKE")
        return 
     
token=11
FBApi=GraberFB.getinfo("https://graph.facebook.com/v16.0/me/posts?access_token=",token)
newdata=FBApi.loadfile(FBApi.loc)

res=requests.get("https://graph.facebook.com/v16.0/me/posts?access_token="+token)
data = json.loads(res.text)
while "next" in data["paging"]: #找的到下一頁
    for i in data["data"]: #印出當前這一頁的內容
            if "message" in i: #有文字的話
                print(i["message"])
    nextk=data["paging"]["next"]  #找下一頁
    nextpage=requests.get(nextk) #更新下一頁
    data=json.loads(nextpage.text) #下載下一頁的內容
    if "paging" not in data: #防止最後一頁報錯
        break