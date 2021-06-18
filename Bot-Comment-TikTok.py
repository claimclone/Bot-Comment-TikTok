try:
    import requests
except:
    print('[-] pip install requests')
import random
import re
import time
done_comment = 0
error_comment = 0
try:
    import colorama
    from colorama import Fore
    colorama.init(autoreset=True)
except:
    print('[-] pip install colorama')
    exit(0)
Bb = Fore.LIGHTYELLOW_EX
print(Bb + """
           __  __ ____   _____  ____  _   _ 
          |  \/  |___ \ / ____|/ __ \| \ | |
          | \  / | __) | |  __| |  | |  \| |
          | |\/| ||__ <| | |_ | |  | | . ` |
          | |  | |___) | |__| | |__| | |\  |
          |_|  |_|____/ \_____|\____/|_| \_|
""", Fore.LIGHTGREEN_EX + "\n                  ( @_m3gon )", Fore.LIGHTBLUE_EX + "\n",
      Fore.LIGHTRED_EX + "            ( Bot Comment TikTok )\n"+Fore.RESET)
def start():
    def get_id_video():
        sessionid = input('[?] Enter Sessionid : ')
        url_get_id_video = input('[?] Enter Url ( Video ) : ')
        text = input('[?] Enter Comment : ')
        headers_get_id_video = {
            'Connection': 'close',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cookie': 'tt_webid_v2=6940688826462406145; tt_webid=6940688826462406145; ttwid=1%7Cbza8rvLOfNRPRwC43Zn3utwgngykYIkkhCtiFchZVMA%7C1616005073%7C1dd5efed4a61e4b1654f08f10a6ff7b85e3d57622a4d6011f6642b1bbf785fcb; passport_csrf_token=bb82884d8da300de0ce4f8508694e635; passport_csrf_token_default=bb82884d8da300de0ce4f8508694e635; store-country-code=sa; tta_attr_id=0.1616499265.6942811476331593729; store-idc=alisg; sid_guard=5c3ba51706c6f27ef59bb4fcaf0d282b%7C1617813999%7C5184000%7CSun%2C+06-Jun-2021+16%3A46%3A39+GMT; uid_tt=9896d319adfbb4f4f7a56b2122e84ef36354da5b7a766c3d93f08771723b2e3f; uid_tt_ss=9896d319adfbb4f4f7a56b2122e84ef36354da5b7a766c3d93f08771723b2e3f; sid_tt=5c3ba51706c6f27ef59bb4fcaf0d282b; sessionid=5c3ba51706c6f27ef59bb4fcaf0d282b; sessionid_ss=5c3ba51706c6f27ef59bb4fcaf0d282b; odin_tt=530994ec29b8076689f2e696e07f7968d74abe62dc6990364400b7b666b98e83afe2d12f34a5c717c851ce41d2368908d1f4c45a8c3974fb4230088b6d230969a128029a783f0ae00352b0d06fa62e0a; R6kq3TV7=AMgpub14AQAASGoycNrCjOkGEeZn3OSfPJcGlZpRyawc4vVW0_K5JN1ScBmQ|1|0|427184ccd78b46f2f1443048844aba7bf6064745; cmpl_token=AgQQAPO_F-RMpY4vzNb-op0_-jPehXJPv4M0YPgasw; tt_csrf_token=Ev5Kwld907oqGN2T1k0HrHWF; ak_bmsc=ED95FE19720A8F91CACBCE8408BFC78E56335E9519250000BF887260FE32B047~pl7zsPkhgfEfP2YwW3Ph6y02EtVXax7QH9oUN1eMfTdDnvOlFJcDXESyLLkFAXRIaueH2qItg4EdfKBI5loXsbdYeZAAy2oCOz7PNDhyQvstusWjR1M6xBMzpFKRcIXuEXMwtrfBx4nQLynJxNr7CJOOKb02W/y1LENhAnX2p+eHB4S6HL5PRUVaJXx6xqRPtjaFzenP3I/+Wx44jRsDjDNlxmlM7krZQs+TzdJApyqZ4=; bm_sz=F1634B2D883BE7F7F8E55AF4D48798F6~YAAQlV4zViahf3R4AQAAIitmvwtx/krEk+BEEQt4CoGeEB0X2JTHtZKLSBFVXxGgh8oLe8VcsrGqbUWhtO2eK/fhU6tdNs4C36OkPBJt7HlGRC07i6coxuZO1bcf0pxWJoJppYUoC9vPHQYh1++jflOXTPVSS0hw/W++SqiceRZkS+Q5SWGwWgWnx6hP4VB1; bm_sv=5AF097FF6E9C14E8BF077EE5BD7D126D~LBiUQfj1jYvhXvESNmEdfPzQcX6s8MGsQ79mJvSVV/OclkEWqotEPinlq8GADZ+tDMWTfCrS+nQ/dH0mG7bwj0L/5a8LC5sn4KJC+CEzqxHnt2JcMCSmRrYV5vO6sJDXY01ZEpWWSdJTGeCbBD7l2DPIFidy9J5ujWVeVBBbY6I=; _abck=494D5CEEE963A444A9BFED1397AE4A1A~-1~YAAQl14zVjHK03V4AQAAfJRovwV3ujEp8mNTnNKx5q6XhLXbDZgBUZwYi8ZS6N3zYCWz6lpsDgFzXfDQT7dKaxDyijowI/MIW0aLuDCIUFU5bw1xBMaKFv4tvXv8QfiThLmgZh3ihOCUJ9xBvVcf9Aw3OQ0YIpDK7oCidJ7WeQkT5jGIhm9yXvB6zUde3/xrOzZyDyxLO6qbSuunOwTmgGN/+qoNcrE82ZJDp3faWXgLMEtgi22ui9gENAV5rnlzEZll3e8AZMn9xZbq+9Aa7SAtgmih3i4WTgyPxwR7DXjPNZ+pnnAb/qJ+JCI+TFIiRW31KVuqy0A6142qz3Whm+XM++sQIWOuThkmXtEh25NeYtyKV3LwWDHMPg7sICqWEjOtgCLPh4lUxLpZaroVbcn0hnVZQ/ab~0~-1~-'
		}
        try:
            req_get_id_video = requests.get(url_get_id_video, headers=headers_get_id_video).text
            id_video0 = re.findall('"video":{"id":"(.*?)"', req_get_id_video)
            id_video = "".join(id_video0)
        except:
            print('[-] Error Url ( Video )')
            time.sleep(5)
        def send_comment():
            while True:
                global done_comment,error_comment
                amount = int(1)
                length = int(5)
                chars = 'qwertyuiopasdfghjklzxcvbnm1234567890'
                for comment_random in range(amount):
                    comment_random = ''
                    for item in range(length):
                        comment_random += random.choice(chars)
                    comment = text + comment_random
                url = 'https://api2.musical.ly/aweme/v1/comment/publish/?language=ar&app_name=musical_ly&vid=ABFB2D70-F55F-442E-8B49-679D37B8682C&carrier_region=SA&is_my_cn=0&channel=App%20Store&mcc_mnc=42001&device_id=6972197272487544325&tz_offset=10800&account_region=&sys_region=SA&aid=1233&screen_width=1125&openudid=56ee03dd877d5f727082385d10756faf9c6d55d1&os_api=18&ac=WIFI&os_version=14.2&app_language=ar&tz_name=Asia/Riyadh&device_platform=iphone&device_type=iPhone10,6&iid=6975164235513923334&idfa=00000000-0000-0000-0000-000000000000&mas=00525fa10689ae627a7cd1e7269d2d6cc2cac782dbc4a3c9812a98&as=a1061c6cc33630d6bc8527&ts=1624032867'
                headers = {
                    'Host': 'api2.musical.ly',
                    'Connection': 'close',
                    'Content-Length': '37',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept-Encoding': 'gzip, deflate',
                    'Cookie': f'sessionid={sessionid}'
                }
                data = f'aweme_id={id_video}&text={comment}'
                req = requests.post(url, data=data, headers=headers).text
                if ('"status_code":0') or (f'"text":"{comment}"') in req:
                    done_comment +=1
                    print(f'\r[+] Done Send Comment <{done_comment}> | Error Send Comment <{error_comment}>', end='')
                    time.sleep(3)
                else:
                    error_comment +=1
                    print(f'\r[+] Done Send Comment <{done_comment}> | Error Send Comment <{error_comment}>', end='')
                    time.sleep(3)
        send_comment()
    get_id_video()
start()
