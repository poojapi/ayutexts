#!/bin/env python3

import sys
import requests
import re
from bs4 import BeautifulSoup

HOST = 'ayutexts.dharaonline.org'
URL = 'http://ayutexts.dharaonline.org/frmread.aspx' 
HEADERS = {
    'Host': HOST,
    'Origin': URL,
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:38.0) Gecko/20100101 Firefox/38.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Cookie': 'ASP.NET_SessionId=3ikackn3wx5ujb5hc2d4y3cx'
}

session = requests.Session()

# r = session.get(URL, headers=HEADERS)
# if r.status_code != requests.codes.ok:
#     sys.exit()

# soup = BeautifulSoup(r.content, features="lxml")

# # ASP validation and session fields
# view_state = soup.select("#__VIEWSTATE")[0]['value']
# view_state_generator = soup.select("#__VIEWSTATEGENERATOR")[0]['value']
# event_validation = soup.select("#__EVENTVALIDATION")[0]['value']


# FORM_FIELDS = {
#             "__EVENTTARGET": "ctl00$ContentPlaceHolder1$ddbook",
#             "__LASTFOCUS":"",
#             "__VIEWSTATE": view_state,
#             "__VIEWSTATEGENERATOR": view_state_generator,
#             "__EVENTVALIDATION": event_validation,
#             "ctl00$ContentPlaceHolder1$ddbook": "1",
#             "__ASYNCPOST": "true"
# }
# # POST form fields
# try:    
#     r = session.post(URL, data=FORM_FIELDS, headers=HEADERS, cookies=r.cookies.get_dict())
# except Error:
#     print('error', Error)

# if r.status_code != requests.codes.ok:
#     print("Failed with status_code %d" % r.status_code)
#     sys.exit()

# soup = BeautifulSoup(r.content, features="lxml")
# paramList = soup.find_all(text=re.compile("|hiddenField|__VIEWSTATE|(\s)+|"))[-1]
# paramList = paramList.split('|')
# VIEWSTATE=''
# VIEWSTATEGENERATOR = ''
# EVENTVALIDATION=''

# for param in paramList:
#     if(param == '__VIEWSTATE'):
#         VIEWSTATE = paramList[paramList.index(param)+1]
#     if(param == '__VIEWSTATEGENERATOR'):
#         VIEWSTATEGENERATOR = paramList[paramList.index(param)+1]
#     if(param == '__EVENTVALIDATION'):
#         EVENTVALIDATION = paramList[paramList.index(param)+1]

# #view_state = soup.select("#__VIEWSTATE")[0]['value']
# #view_state_generator = soup.select("#__VIEWSTATEGENERATOR")[0]['value']
# #event_validation = soup.select("#__EVENTVALIDATION")[0]['value']
# # print(soup)

# script = "ctl00$ContentPlaceHolder1$updatepanelread|ctl00$ContentPlaceHolder1$ddsection"
        
# formdata={
#      # change pages here
#     "ctl00$ContentPlaceHolder1$script": script,
#     "ctl00$ContentPlaceHolder1$ddbook": "1",
#     "ctl00$ContentPlaceHolder1$ddsection": "1",
#     "__EVENTTARGET": "ctl00$ContentPlaceHolder1$ddsection",
#     "__EVENTARGUMENT": "",
#     "__LASTFOCUS": "",
#     "__VIEWSTATE": VIEWSTATE,
#     "__VIEWSTATEGENERATOR": VIEWSTATEGENERATOR,
#     "__EVENTVALIDATION": EVENTVALIDATION,
# #"ctl00$ContentPlaceHolder1$ddchapter":'', 
#     "__ASYNCPOST": "true&"
# #"ScriptManager.SupportsPartialRendering": "true",
# #"ctl00$ContentPlaceHolder1$btnSearch": "Search"
# }
# try:    
#     r = session.post(URL, data=formdata, headers=HEADERS, cookies=r.cookies.get_dict())
# except Error:
#     print('error', Error)

# if r.status_code != requests.codes.ok:
#     print("Failed with status_code %d" % r.status_code)
#     sys.exit()
# print(r.text)

# soup = BeautifulSoup(r.content, features="lxml")

script = "ctl00$ContentPlaceHolder1$updatepanelread|ctl00$ContentPlaceHolder1$btnSearch"
view_state = '/wEPDwUKMTczMTU1NTc0Nw9kFgJmD2QWAgIDD2QWCGYPDxYGHglGb3JlQ29sb3IJVOHm/x4HRW5hYmxlZGgeBF8hU0ICBGRkAgIPDxYCHgdWaXNpYmxlaGRkAgMPDxYCHgRUZXh0ZWRkAgUPZBYCAgMPZBYCZg9kFhYCAw8QDxYGHg1EYXRhVGV4dEZpZWxkBQl0ZXh0X25hbWUeDkRhdGFWYWx1ZUZpZWxkBQd0ZXh0X2lkHgtfIURhdGFCb3VuZGdkEBUICC1zZWxlY3QtDmNhcmFrYSBzYW1oaXRBD3N1Q3J1dGEgc2FtaGl0QQ5hU1RBR2dhIGhSZGF5YRBhU1RBR2dhIHNhTWdyYWhhDm1BZGhhdmEgbmlkQW5hE0NBckdnYWRoYXJhIHNhTWhpdEENYmhlbGEgc2FNaGl0QRUIAAExATIBMwE0ATcBOAIxMBQrAwhnZ2dnZ2dnZxYBAgFkAgcPEA8WBh8FBQdTZWN0aW9uHwYFAklkHwdnZBAVCQgtc2VsZWN0LQxzVXRyYXN0aEFuYW0NbmlkQW5hc3RoQW5hbQ12aW1BbmFzdGhBbmFtDUNhcklyYXN0aEFuYW0OaW5kcml5YXN0aEFuYW0OY2lraXRzQXN0aEFuYW0Ma2FscGFzdGhBbmFtDXNpZGRoaXN0aEFuYW0VCQABMQEyATMBNAE1ATYBNwE4FCsDCWdnZ2dnZ2dnZxYBAgFkAgsPEA8WCB8FBQdDaGFwdGVyHwFnHwYFAklkHwdnZBAVHwgtc2VsZWN0LRdkSXJnaGFKakl2aXRJeW8vZGh5QXlhSBlhcEFtQXJnYXRhTkR1bEl5by9kaHlBeWFIE0FyYWd2YWRoSXlvL2RoeUF5YUgeU2FEdmlyZWNhbmFDYXRBQ3JpdEl5by9kaHlBeWFIE21BdHJBQ2l0SXlvL2RoeUF5YUgTdGFzeUFDaXRJeW8vZGh5QXlhSBhuYXZlZ0FuZGhBcmFOSXlvL2RoeUF5YUgaaW5kcml5b3Bha3JhbWFOSXlvL2RoeUF5YUgZa2h1RERBa2FjYXR1U3BBZG8vZGh5QXlhSBVtYWhBY2F0dVNwQWRvL2RoeUF5YUgUdGlzcmFpU2FOSXlvL2RoeUF5YUgWdkF0YWthbEFrYWxJeW8vZGh5QXlhSAxzbmVoQWRoeUF5YUgMc3ZlZEFkaHlBeWFIFHVwYWthbHBhbkl5by9kaHlBeWFIGmNpa2l0c0FwckFiaFJ1dEl5by9kaHlBeWFIGGtpeWFudGFIQ2lyYXNJeW8vZGh5QXlhSBJ0cmlDb3RoSXlvL2RoeUF5YUgSYVNUb2Rhckl5by9kaHlBeWFID21haEFyb2dBZGh5QXlhSBZhU1RhdW5pbmRpdEl5by9kaHlBeWFIGmxhR2doYW5hYlJ1TWhhTkl5by9kaHlBeWFIFHNhbnRhcnBhTkl5by9kaHlBeWFIFXZpZGhpQ29OaXRJeW8vZGh5QXlhSBZ5YWpqYUhwdXJ1U0l5by9kaHlBeWFIG0F0cmV5YWJoYWRyYWtBcHlJeW8vZGh5QXlhSBVhbm5hcEFuYXZpZGh5YWRoeUF5YUgZdml2aWRoQUNpdGFwSXRJeW8vZGh5QXlhSBlkYUNhcHJBTkF5YXRhbkl5by9kaHlBeWFIG2FydGhlZGFDYW1haEFtVWxJeW8vZGh5QXlhSBUfAAExATIBMwE0ATUBNgE3ATgBOQIxMAIxMQIxMgIxMwIxNAIxNQIxNgIxNwIxOAIxOQIyMAIyMQIyMgIyMwIyNAIyNQIyNgIyNwIyOAIyOQIzMBQrAx9nZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnFgECAWQCEQ8QDxYCHwFnZBAVjgEILXNlbGVjdC0BMAExATIBMwE0ATUBNgE3ATgBOQIxMAIxMQIxMgIxMwIxNAIxNQIxNgIxNwIxOAIxOQIyMAIyMQIyMgIyMwIyNAIyNQIyNgIyNwIyOAIyOQIzMAIzMQIzMgIzMwIzNAIzNQIzNgIzNwIzOAIzOQI0MAI0MQI0MgI0MwI0NAI0NQI0NgI0NwI0OAI0OQI1MAI1MQI1MgI1MwI1NAI1NQI1NgI1NwI1OAI1OQI2MAI2MQI2MgI2MwI2NAI2NQI2NgI2NwI2OAI2OQI3MAI3MQI3MgI3MwI3NAI3NQI3NgI3NwI3OAI3OQI4MAI4MQI4MgI4MwI4NAI4NQI4NgI4NwI4OAI4OQI5MAI5MQI5MgI5MwI5NAI5NQI5NgI5NwI5OAI5OQMxMDADMTAxAzEwMgMxMDMDMTA0AzEwNQMxMDYDMTA3AzEwOAMxMDkDMTEwAzExMQMxMTIDMTEzAzExNAMxMTUDMTE2AzExNwMxMTgDMTE5AzEyMAMxMjEDMTIyAzEyMwMxMjQDMTI1AzEyNgMxMjcDMTI4AzEyOQMxMzADMTMxAzEzMgMxMzMDMTM0AzEzNQMxMzYDMTM3AzEzOAMxMzkDMTQwFY4BAAEwATEBMgEzATQBNQE2ATcBOAE5AjEwAjExAjEyAjEzAjE0AjE1AjE2AjE3AjE4AjE5AjIwAjIxAjIyAjIzAjI0AjI1AjI2AjI3AjI4AjI5AjMwAjMxAjMyAjMzAjM0AjM1AjM2AjM3AjM4AjM5AjQwAjQxAjQyAjQzAjQ0AjQ1AjQ2AjQ3AjQ4AjQ5AjUwAjUxAjUyAjUzAjU0AjU1AjU2AjU3AjU4AjU5AjYwAjYxAjYyAjYzAjY0AjY1AjY2AjY3AjY4AjY5AjcwAjcxAjcyAjczAjc0Ajc1Ajc2Ajc3Ajc4Ajc5AjgwAjgxAjgyAjgzAjg0Ajg1Ajg2Ajg3Ajg4Ajg5AjkwAjkxAjkyAjkzAjk0Ajk1Ajk2Ajk3Ajk4Ajk5AzEwMAMxMDEDMTAyAzEwMwMxMDQDMTA1AzEwNgMxMDcDMTA4AzEwOQMxMTADMTExAzExMgMxMTMDMTE0AzExNQMxMTYDMTE3AzExOAMxMTkDMTIwAzEyMQMxMjIDMTIzAzEyNAMxMjUDMTI2AzEyNwMxMjgDMTI5AzEzMAMxMzEDMTMyAzEzMwMxMzQDMTM1AzEzNgMxMzcDMTM4AzEzOQMxNDAUKwOOAWdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2cWAQIBZAIVDxAPFgIfAWdkEBWOAQgtc2VsZWN0LQEwATEBMgEzATQBNQE2ATcBOAE5AjEwAjExAjEyAjEzAjE0AjE1AjE2AjE3AjE4AjE5AjIwAjIxAjIyAjIzAjI0AjI1AjI2AjI3AjI4AjI5AjMwAjMxAjMyAjMzAjM0AjM1AjM2AjM3AjM4AjM5AjQwAjQxAjQyAjQzAjQ0AjQ1AjQ2AjQ3AjQ4AjQ5AjUwAjUxAjUyAjUzAjU0AjU1AjU2AjU3AjU4AjU5AjYwAjYxAjYyAjYzAjY0AjY1AjY2AjY3AjY4AjY5AjcwAjcxAjcyAjczAjc0Ajc1Ajc2Ajc3Ajc4Ajc5AjgwAjgxAjgyAjgzAjg0Ajg1Ajg2Ajg3Ajg4Ajg5AjkwAjkxAjkyAjkzAjk0Ajk1Ajk2Ajk3Ajk4Ajk5AzEwMAMxMDEDMTAyAzEwMwMxMDQDMTA1AzEwNgMxMDcDMTA4AzEwOQMxMTADMTExAzExMgMxMTMDMTE0AzExNQMxMTYDMTE3AzExOAMxMTkDMTIwAzEyMQMxMjIDMTIzAzEyNAMxMjUDMTI2AzEyNwMxMjgDMTI5AzEzMAMxMzEDMTMyAzEzMwMxMzQDMTM1AzEzNgMxMzcDMTM4AzEzOQMxNDAVjgEAATABMQEyATMBNAE1ATYBNwE4ATkCMTACMTECMTICMTMCMTQCMTUCMTYCMTcCMTgCMTkCMjACMjECMjICMjMCMjQCMjUCMjYCMjcCMjgCMjkCMzACMzECMzICMzMCMzQCMzUCMzYCMzcCMzgCMzkCNDACNDECNDICNDMCNDQCNDUCNDYCNDcCNDgCNDkCNTACNTECNTICNTMCNTQCNTUCNTYCNTcCNTgCNTkCNjACNjECNjICNjMCNjQCNjUCNjYCNjcCNjgCNjkCNzACNzECNzICNzMCNzQCNzUCNzYCNzcCNzgCNzkCODACODECODICODMCODQCODUCODYCODcCODgCODkCOTACOTECOTICOTMCOTQCOTUCOTYCOTcCOTgCOTkDMTAwAzEwMQMxMDIDMTAzAzEwNAMxMDUDMTA2AzEwNwMxMDgDMTA5AzExMAMxMTEDMTEyAzExMwMxMTQDMTE1AzExNgMxMTcDMTE4AzExOQMxMjADMTIxAzEyMgMxMjMDMTI0AzEyNQMxMjYDMTI3AzEyOAMxMjkDMTMwAzEzMQMxMzIDMTMzAzEzNAMxMzUDMTM2AzEzNwMxMzgDMTM5AzE0MBQrA44BZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZxYBAo0BZAIXDw8WBB8DaB8EBRxDaG9vc2UgVE8gR3JlYXRlciB0aGFuIEZST00gZGQCIw8PFgIfA2hkZAIlDw8WAh8DaGRkAicPDxYCHwNoZGQCKQ8PFgIfA2hkZAItDzwrAAsBAA8WAh8DaGRkZC1skdJi2PYcdzgK1loAzG0KIb207twkGuaJUqdejuBT'
view_state_generator = '1FDFD683'
event_validation = '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'


FORM_FIELDS = {
    "ctl00$ContentPlaceHolder1$script": script,
    "ctl00$ContentPlaceHolder1$ddbook": "1",
    "ctl00$ContentPlaceHolder1$ddsection": "1",
    "ctl00$ContentPlaceHolder1$ddchapter":"1",
    "ctl00$ContentPlaceHolder1$ddfrom": "0",
    "ctl00$ContentPlaceHolder1$ddto": "140",
    "__EVENTTARGET": "",
    "__EVENTARGUMENT": "",
    "__LASTFOCUS": "",
    "__VIEWSTATE": view_state,
    "__VIEWSTATEGENERATOR": view_state_generator,
    "__EVENTVALIDATION": event_validation,
#"ctl00$ContentPlaceHolder1$ddchapter":'', 
    "__ASYNCPOST": "true"
}
# POST form fields

try:    
    r = session.post(URL, data=FORM_FIELDS, headers=HEADERS)
except Error:
    print('error', Error)

if r.status_code != requests.codes.ok:
    print("Failed with status_code %d" % r.status_code)
    sys.exit()

soup = BeautifulSoup(r.content, features="lxml")

print(soup)




