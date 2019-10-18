import requests
from bs4 import BeautifulSoup
import bs4
import json
import os
import time
url = "http://www.youth.sdu.edu.cn/333/list.psp"
urlBase = "http://www.youth.sdu.edu.cn"
file = "data.txt"
SCKEY = "XXXX" # replace your SCKEY here

# save data to file
def save(data,out_file):
    with open(out_file,"w") as f:
        f.write(data)


# read data from file
def read(in_file):
    with open(in_file,"r") as f:
        return f.read()

# send to wechat
def send(title,desp):
    r = requests.post("https://sc.ftqq.com/"+SCKEY+".send",data={"text":title,"desp":desp})
    r.raise_for_status()
    time.sleep(5)

# get content list from url
def get_list(url):
    r= requests.get(url)
    r.raise_for_status()
    if r.status_code != 200:
        print("Please run this in inner network")
        exit(-1)
    soup = BeautifulSoup(r.text,"html.parser")
    list = soup.find("ul",class_="wp_article_list")
    d = dict()
    for li in list.contents:
        if type(li) == bs4.element.Tag:
            a = li.a
            link = urlBase + a["href"]
            d[a["title"]] = link
    if not os.path.exists(file):
        data = json.dumps(d)
        save(data , file)
        for i in d:
            # print(d[i])
            send(i,d[i])
    else:
        data = read(file)
        old_data = json.loads(data)
        old_data = dict(old_data)
        for i in d.keys():
            if i not in old_data:
                # print(d[i])
                send(i,d[i])
        data = json.dumps(d)
        save(data,file)


if __name__ == '__main__':
    get_list(url)