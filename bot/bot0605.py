#需要用的模組
from flask import Flask, request
#定義APP
app=Flask(__name__)
#定義第一種route網址與模式
@app.route("/", methods=['GET'])
def aa():
    print("登錄成功")
    return "登錄OK"#以字串型式在瀏覽器顯示
#定義第二種route網址與模式
@app.route("/minus/YYY=<x>&XXX=<y>", methods=['GET'])
#可以定義自己要做的function
def bb(x,y):
    s2=int(x)-int(y)
    print("你輸入的是：%s"%(s2))
    return str(s2)#以字串型式在瀏覽器顯示
if __name__ == "__main__":
    app.run(port=3500)