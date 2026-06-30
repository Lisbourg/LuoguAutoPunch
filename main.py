import requests
import os
import sys
cookie_str="_uid=1269138; __client_id=yiczrj3i7byt2nxhkzdbz2c2p6dthokneq5nqsg6gnx3e74y" # 这行自己改
url="https://www.luogu.com.cn/index/ajax_punch"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Cookie":cookie_str,
    "Referer":"https://www.luogu.com.cn/",
    "x-requested-with":"XMLHttpRequest" 
}
if __name__ == "__main__":
    response= requests.get(url,headers=headers,timeout=30)
    print(response)
