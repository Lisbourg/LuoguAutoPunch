import requests
import os
import sys

def luogu_punch():
    cookie_str="_uid=1269138; __client_id=0223036fd9265a6cd59b14d3c378b8df814e2a7e; _cfuvid=pv2pv2Qa88m7yktQEtwfjeLNweGmCwgi0QDu4HK0TUc-1767869481377-0.0.1.1-604800000" # 这行自己改
    url="https://www.luogu.com.cn/index/ajax_punch"
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Cookie":cookie_str,
        "Referer":"https://www.luogu.com.cn/",
        "x-requested-with":"XMLHttpRequest" 
    }
    try:
        print("正在尝试连接洛谷服务器...")
        response= requests.get(url,headers=headers,timeout=10)
        # print(response)
        try:
            data=response.json()
        except:
            print("解析 JSON 失败")
            return
        if response.status_code==200:
            code=data.get('code')
            if code==200:
                print(f"打卡成功，运势: {data}")
            elif code==201:
                print("今天已经打过卡了")
            else:
                print(f"失败: {data.get('message')}")
        else:
            print(f"状态码错误: {response.status_code}")
    except Exception as e:
        print(f"发生异常: {e}")

if __name__=="__main__":
    luogu_punch()
