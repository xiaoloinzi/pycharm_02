# encoding=utf-8
#encode=utf-8
from urllib import request
import time
import os
from bs4 import BeautifulSoup
url="http://www.kugou.com"
result=request.urlopen(url).read().decode("utf-8")
# print(result)
soup=BeautifulSoup(result,'lxml')
for i in soup.find_all("div"):
    if i.get("id")=="SongtabContent":
        s=i.find_all("li")
with open("E://music.txt","w",encoding="utf-8") as f:
    for j in s:
        print("歌曲名称为: %s ;" % j.a.select(".songName")[0].text)
        print("歌曲播放连接为: %s" % j.a.get("href"))
        print("歌曲播放时间为: %s" % j.a.select(".songTime")[0].text)
        f.write("歌曲名称为: %s ;" % j.a.select(".songName")[0].text)
        f.write("歌曲播放连接为: %s" % j.a.get("href"))
        f.write("歌曲播放时间为: %s" % j.a.select(".songTime")[0].text)
        f.write(os.linesep)
