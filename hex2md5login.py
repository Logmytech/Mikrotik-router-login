import hashlib  # For calculation of MD5 hash
import re       # Regex library
import requests # URLlib for Humans
#import time
import sys
from bs4 import BeautifulSoup # For scraping the value.

PY2 = sys.version_info[0] == 2 #Returns True if Python version is 2 

URL = "http://10.110.210.1/"
STATUS_URL= URL + "status"
LOGIN_URL = URL + "login"
USERNAME = "username"
PASSWORD = "password"

headers = {
           'Host': '10.110.210.1',
           'User-Agent': '    Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language': 'en-US,en;q=0.5',
           'Accept-Encoding': 'gzip, deflate',
           'DNT': '1',
           'Referer': LOGIN_URL,
           'Connection': 'keep-alive',
           }


def hexMD5ForPy2(s):
    return hashlib.md5(s).hexdigest()


def loginPy2():
    ss = requests.get(LOGIN_URL)
    s= re.search("hexMD5\(([^)]*?)\)",ss.content)
    
    match1 = s.group(1)
#   print match1
    
    match2 = match1.replace(' + document.login.password.value + ',PASSWORD).replace('\'',"").replace('\n','')
    print(match2)
    match2 = match2.decode('string_escape')
    print(match2)
    print(hexMD5ForPy2(match2))   
    payload = {'user': USERNAME ,'password':hexMD5ForPy2(match2),'dst':"",'popup':'true'}
    r = requests.post(LOGIN_URL,data = payload,headers = headers)

if __name__ == "__main__":
    loginPy2()
