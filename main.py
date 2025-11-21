import requests
import os
import sys
# from dotenv import load_dotenv

# load_dotenv()

def luogu_punch():
    # ---------------------------------------------------------
    # 1. 获取 Cookie
    # ---------------------------------------------------------
    # ⚠️ 这里填入你的真实 Cookie 字符串
    # cookie_str = os.getenv("LUOGU_COOKIE")

    cookie_str=os.getenv("LUOGU_COOKIE")

    # 如果你是在本地测试，直接把 cookie 写在这里覆盖上面的变量
    # cookie_str = "__client_id=xxxx; _uid=xxxx; ..." 

    if not cookie_str:
        print("❌ 错误：没有 Cookie")
        return

    # ---------------------------------------------------------
    # 2. 设置请求信息 (修正版)
    # ---------------------------------------------------------
    url = "https://www.luogu.com.cn/index/ajax_punch"
    
    # 修正后的 Headers：去掉了 Content-Type，保留了 x-requested-with
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Cookie": cookie_str,
        "Referer": "https://www.luogu.com.cn/",
        "x-requested-with": "XMLHttpRequest" 
    }

    # ---------------------------------------------------------
    # 3. 发送打卡请求
    # ---------------------------------------------------------
    try:
        print("🚀 正在尝试连接洛谷服务器...")
        
        response = requests.get(url, headers=headers, timeout=10)
        try:
            data = response.json()
        except:
            print("❌ 解析 JSON 失败，可能 Cookie 失效或服务器拦截")
            return

        # 调试打印，确认这次返回了什么
        print(f"🔍 服务器返回: {data}")

        if response.status_code == 200:
            code = data.get('code')
            if code == 200:
                print(f"✅ 打卡成功！运势: {data.get('more', {}).get('html', '未获取')}")
            elif code == 201:
                print("✅ 今天已经打过卡了")
            else:
                print(f"⚠️ 失败: {data.get('message')}")
        else:
            print(f"❌ HTTP 状态码错误: {response.status_code}")

    except Exception as e:
        print(f"❌ 发生异常: {e}")

if __name__ == "__main__":

    luogu_punch()

