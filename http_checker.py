#-*- encoding: utf-8 -*-
#!/usr/bin/python3
"""Add a script to check if a website is available"""

import urllib.request
import datetime
import time
import os

def check(url):
    '''Tries to open a site. Takes the url as an argument. If the site was opened returns True else False'''
    try:
        urllib.request.urlopen(url)
        write_log("Site " + url + " was opened")
        return True
    except:
        write_log("Error to open " + url)
        return False

def send_sms(sms_api_id, phone, message):
    '''Sends message to phone using sms.ru api'''
    try:
        url="http://sms.ru/sms/send?api_id=%s&to=%s&text=%s"%(sms_api_id, phone, message)
        urllib.request.urlopen(url)
        write_log("Send sms " + url)
    except:
        write_log("Error to send message " + message)

def write_log(string):
    '''Writes log file'''
    if os.path.exists("./http_checker.log"):
        log_file = open("./http_checker.log", 'a')
        log_file.write(str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()) + '_' + string + '\n')
        log_file.close()
    #print(str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()) + '_' + string + '\n')

def main():
	site_name = 'site'
    site_url = "http://193.93.*.*/"
    sms_api_id = "********-****-****-****-************"
    phone = "8903*******"
    message = "Site_" + site_name +"_is_not_available"
    while True:
        count = 0
        for n in range(3):
            if check(site_url):
                count += 1
                time.sleep(30)
        if count == 0:
            send_sms(sms_api_id, phone, message)

if __name__ == "__main__":
    main()
