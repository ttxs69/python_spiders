# 通过微博土拍你获取微博用户id
import re


def idx(c):
    c = ord(c)
    if c>=48 and c<=57:
        return c-48
    if c>=97 and c<=122:
        return c-97+10
    return c-65+36


def getUid(url):
    filename = re.search(".*mw690/(.*).jpg",url).groups()[0]
    if filename is None:
        return ""
    first8 = filename[:8]
    k = 16
    uid = 0
    if first8[0]=='0' and first8[1]=='0':
        k=62
    for i in range(8):
        uid = uid*k + idx(first8[i])
    return "https://weibo.com/u/"+str(uid)


if __name__ == '__main__':
    imgUrl = input("input the url:\n")
    print(getUid(imgUrl))