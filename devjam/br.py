import os
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import json
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from qtconsole.qt import QtGui

chromedriver = "E:\Softwares\chromedriver\chromedriver_win32\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://google.com")
cur = driver.current_url
blocked=["Internet and Telecom","Shopping","Games","Arts and Entertainment","Beauty and Fitness",""]
while True:
    now = driver.current_url
    if cur != now:
        #print(now)
        s         cur=now
= "https://website-categorization-api.whoisxmlapi.com/api/v1?apiKey=at_lR7zccIvY6AQ4IrEzJMVlZiTOijlU&domainName="+str(now)
        content = str(urllib.request.urlopen(s).read())
        cc = content[17:-2]
        cat = cc.split("]")
        cat[0]=cat[0].split(",")
        for i in range(len(cat[0])):
            cat[0][i]=cat[0][i][1:-1]
        cat[1] = cat[1].split(":")
        #cat[2] = cat[2].split(":")
        category = cat[0][0]
        print(cat[0])







