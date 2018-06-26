#!/usr/bin/python  
# -*- coding: utf-8 -*-

import os
import requests
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm"

def output(file, value):
    f = open(file, 'a')
    f.write(value)
    f.close()

def getAera(phone):
    tel = {'tel': phone}
    r = requests.get(url, params=tel)
    if (r.status_code == requests.codes.ok):
        response = r.text
        if response.find(",") > 0:
            provice = ((response.split(",")[1]).split(":")[1]).strip('\'')
            return phone + "," + provice + "\n"
        else:
            return phone + ",\n"
    else:
        return phone + ",\n"



if __name__ == "__main__":

    with open("ebook-phone", "rb") as f:
        for line in f:
            output("phone2area", getAera(line.strip()))
