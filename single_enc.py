import requests
import os
import re
import time
from requests.exceptions import RequestException

# Terminal screen ko clear karne ka function
def clear_screen():
    os.system("clear")

# Cookies set up karne ka function
def set_cookies():
    cookies = []
    num_cookies = int(input("\033[92mKitni cookies dalni hain? :: "))
    for i in range(num_cookies):
        cookie = input(f"\033[92mCookie {i+1} enter karein: ")
        cookies.append(cookie)
    return cookies

# Commenter ka naam lekar aane ka function
def get_commenter_name():
    return input("\033[92mHater ka Naam :: ")

# Password enter karne ka function
def get_password():
    return input("\033[92mPassword :: ")

# Network requests handle karne ka function
def make_request(url, headers, cookies):
    try:
        response = requests.get(url, headers=headers, cookies=cookies).text
        return response
    except RequestException as e:
        print("\033[91m[!] Request mein galti aayi:", e)
        return None

# Author details
author_info = """
                                     Author :: DEVIL
"""

print(author_info)

# Start time
print("\033[92mStart Time:", time.strftime("%Y-%m-%d %H:%M:%S"))

# Login System
password = "Devil 789"
while True:
    user_pass = get_password()
    if user_pass == password:
        print("\n\033[92mLogin Successful!\n")
        break
    else:
        print("\n\033[91mGalt Password! Dubara try karein.\n")

while True:
    try:
        print()
        cookies = set_cookies()

        # Loop through each cookie and make requests
        for cookie in cookies:
            response = make_request('https://business.facebook.com/business_locations', headers={
                'Cookie': cookie,
                'User-Agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]'
            }, cookies={'Cookie': cookie})

            if response is None:
                break

            token_eaag = re.search('(EAAG\w+)', str(response)).group(1)
            id_post = int(input("\033[92mPost Id :: "))
            commenter_name = get_commenter_name()
            delay = int(input("\033[92mDelay (Second) :: "))
            comment_file_path = input("\033[92mAapka Comment File Path :: ")

            with open(comment_file_path, 'r') as file:
                comments = file.readlines()

            x, y = 0, 0
            print()

            while True:
                try:
                    time.sleep(delay)
                    teks = comments[x].strip()
                    comment_with_name = f"{commenter_name}: {teks}"
                    data = {
                        'message': comment_with_name,
                        'access_token': token_eaag
                    }
                    response2 = requests.post(f'https://graph.facebook.com/{id_post}/comments/', data=data, cookies={'Cookie': cookie}).json()
                    if '\'id\':' in str(response2):
                        print("\033[92mPost Id ::", id_post)
                        print("\033[92mDate time ::", time.strftime("%Y-%m-%d %H:%M:%S"))
                        print("\033[92mComment bheja gaya ::", comment_with_name)
                        print("\033[92mCookie ka istemal ::", cookie)
                        print('\033[97m' + '──────────────────────────────────────────────────────────────')
                        x = (x + 1) % len(comments)
                    else:
                        y += 1
                        print("\033[91m[{}] Status : Asafalta".format(y))
                        print("\033[91m[/]Link : https://m.basic.facebook.com//{}".format(id_post))
                        print("\033[91m[/]Comments : {}\n".format(comment_with_name))
                        continue

                except RequestException as e:
                    print("\033[91m[!] Request mein galti aayi:", e)
                    time.sleep(5.5)
                    continue

    except Exception as e:
        print("\033[91m[!] Koi anjaan galti aayi:", e)
        break
