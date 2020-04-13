#!/bin/env python

import sys
import requests
from bs4 import BeautifulSoup

HOST = 'http://ayutexts.dharaonline.org'
URL = 'http://ayutexts.dharaonline.org/frmread.asp' 
HEADERS = {
    'Host': HOST,
    'Origin': 'http://%s' % URL,
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:38.0) Gecko/20100101 Firefox/38.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'
}

session = requests.Session()

r = session.get(URL, headers=HEADERS)

if r.status_code != requests.codes.ok:
    sys.exit()

soup = BeautifulSoup(r.content)

# ASP validation and session fields
view_state = soup.select("#__VIEWSTATE")[0]['value']
view_state_generator = soup.select("#__VIEWSTATEGENERATOR")[0]['value']
event_validation = soup.select("#__EVENTVALIDATION")[0]['value']

"""
possible cboState
1: Andhra Pradesh
3: Assam
4: Bihar
5: Chhattisgarh
6: Delhi
7: Goa
8: Gujarat
9: Haryana
10: Himachal Pradesh
11: Jammu &amp; Kashmir
12: Jharkhand
13: Karnataka
14: Kerala
15: Madhya Pradesh
16: Maharashtra
18: Meghalaya
20: Nagaland
21: Orissa
22: Punjab
23: Rajasthan
24: Sikkim
25: Tamil Nadu
30: Telangana
26: Tripura
27: Uttar Pradesh
28: Uttaranchal
29: West Bengal
"""

FORM_FIELDS = {
    '__EVENTTARGET': 'cboState',
    '__EVENTARGUMENT': '',
    '__LASTFOCUS': '',
    '__VIEWSTATE': view_state,
    '__VIEWSTATEGENERATOR': view_state_generator,
    '__EVENTVALIDATION': event_validation,
    'cboState': '3',
    'hdDealerMaps': 'True',
}

# POST form fields
r = session.post(URL, data=FORM_FIELDS, headers=HEADERS, cookies=r.cookies.get_dict())

if r.status_code != requests.codes.ok:
    print "Failed with status_code %d" % r.status_code
    sys.exit()

soup = BeautifulSoup(r.content)
print soup