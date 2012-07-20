#!/usr/bin/env python
import sys
import json
import requests
import csv

data_file = 'data.json'
if len(sys.argv) > 1:
    data_file = sys.argv[1]

try:
    inputf = open(data_file, 'r')
    outputcsv = csv.writer(open('data.csv', 'wb'), delimiter=',', quotechar='\"', quoting=csv.QUOTE_MINIMAL)
    inputs = inputf.read()

    json_data = json.loads(inputs)
    # print json_data
    for item in json_data:
        for url in item:
            payload = {'url': url}
            r = requests.get("http://expandurl.appspot.com/expand", params=payload)
            # print r.url
            end_url = r.json['end_url']
            print end_url
            outputcsv.writerow([url,end_url])
except:
    print 'Oops'