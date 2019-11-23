#-*- encoding: utf-8 -*-
#!/usr/bin/python3

"""
Script for checking if an HTTP resource is available
"""

import urllib.request
import datetime, time
import os
import argparse

def check(url):
    # Try to open an HTTP resource. Take the url as an argument. If the resource was opened then return True else False
    try:
        urllib.request.urlopen(url)
        write_log('resource ' + url + ' was opened')
        return True
    except:
        write_log('Error to open ' + url)
        return False

def send_sms(sms_api_id, phone, message):
    # Send message to phone using sms.ru api
    try:
        url=f'http://sms.ru/sms/send?api_id={sms_api_id}&to={phone}&text={message}'
        urllib.request.urlopen(url)
        write_log('Send sms ' + url)
    except:
        write_log('Error to send message ' + message)

def write_log(string):
    # Write log file
    log_file = open('./http_checker.log', 'a')
    log_file.write(str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()) + '_' + string + '\n')
    log_file.close()

def main():
    # Construct the argument parser and parse command line arguments
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-n', '--resource-name', type=str, required=True, help='HTTP resource name')
    arg_parser.add_argument('-u', '--url', type=str, required=True, help='HTTP resource url')
    arg_parser.add_argument('-i', '--api-id', type=str, required=True, help='Api id from sms.ru')
    arg_parser.add_argument('-p', '--phone', type=str, required=True, help='Phone')
    arg_parser.add_argument('-c', '--count', type=int, default=3, help='Count of checking before sending a message. Default value is 3')
    args = vars(arg_parser.parse_args())

    # Run a checking
    message = 'Site_' + args['resource_name'] + '_is_not_available'
    while True:
        count = args['count']
        for n in range(count):
            if not check(args['url']):
                count -= 1
            time.sleep(30)
        if count == 0:
            send_sms(args['api_id'], args['phone'], message)

if __name__ == '__main__':
    main()
