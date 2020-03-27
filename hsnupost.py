import requests
import socket
from selenium import webdriver 
import time 
import datetime

hsnuurl='http://140.131.149.225/auth/index.html/u'
url = 'https://wl110.cc.ntu.edu.tw/auth/loginnw.html'
'''
# 建立一個socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立連線:
s.connect(('140.131.149.225', 80))
'''
params = {
    'user' : '810178',
    'password' : 'hsnu131532252'
}
while True:
    try:
        if(requests.get(hsnuurl).status_code!=302):
            html = requests.post(hsnuurl,data=params)
            html.encoding = html.apparent_encoding
            print("sucessful login",datetime.datetime.now())
    except:
        pass
    time.sleep(5)
