from ytmusicapi import YTMusic
#c = ":authority: music.youtube.com :method: POST :path: /youtubei/v1/browse?ctoken=4qmFsgLZAhIMRkVtdXNpY19ob21lGsgCQ0FONjdBRkhUekpQZFRacE5UQlFRVU5OYVRCaFN6RktSVkV3ZUVKVGVsWXhaVlk1ZEZSV2JGSlhha3A1VVhwU2FsVXpTbkZSYW1SSFRVWktTV1I2UW5GVVdHTTFVbFk1VmxRd2FHeFJiR3hoWW5kd2RFTm9iRFZrUmpsM1dWZGtiRmd6VG5WWldFSjZZVWM1TUZnelNteGFNbXgyWW0xR2MwVm9PVzVQUlhSclRsUmtkRTVxU2tSWFYxWnVVek5hTW1KNlFsbGhSbWhMWld0S1MxVkliR2xpU0docVIyazRRVUZIVW14QlFVWkZVbEZCUWxKRlZVRkJVVUpIVWxjeE1XTXliR3BZTW1oMllsZFZRVUZSUVVKUmQwRkJRVUZGUVVGUlFVRkJVVVZGUVZwNFRqQjJjV040TnpCS1FXZG5RUSUzRCUzRA%253D%253D&continuation=4qmFsgLZAhIMRkVtdXNpY19ob21lGsgCQ0FONjdBRkhUekpQZFRacE5UQlFRVU5OYVRCaFN6RktSVkV3ZUVKVGVsWXhaVlk1ZEZSV2JGSlhha3A1VVhwU2FsVXpTbkZSYW1SSFRVWktTV1I2UW5GVVdHTTFVbFk1VmxRd2FHeFJiR3hoWW5kd2RFTm9iRFZrUmpsM1dWZGtiRmd6VG5WWldFSjZZVWM1TUZnelNteGFNbXgyWW0xR2MwVm9PVzVQUlhSclRsUmtkRTVxU2tSWFYxWnVVek5hTW1KNlFsbGhSbWhMWld0S1MxVkliR2xpU0docVIyazRRVUZIVW14QlFVWkZVbEZCUWxKRlZVRkJVVUpIVWxjeE1XTXliR3BZTW1oMllsZFZRVUZSUVVKUmQwRkJRVUZGUVVGUlFVRkJVVVZGUVZwNFRqQjJjV040TnpCS1FXZG5RUSUzRCUzRA%253D%253D&type=next&itct=CAMQybcCIhMIoKiOqLnQ8AIVHoF8Ch0ECw_q&alt=json&key=AIzaSyC9XL3ZjWddXya6X74dJoCTL-WEYFDNX30 :scheme: https accept: */* accept-encoding: gzip, deflate, br accept-language: de-DE,de;q=0.9 authorization: SAPISIDHASH 1621245282_24d67b3a2f3c1385e9205a204beaef1f001fc45a content-length: 715 content-type: application/json cookie: YSC=8SPTuF0zhJc; VISITOR_INFO1_LIVE=vNz4mY07s0M; CONSENT=PENDING+031; _gcl_au=1.1.995250531.1621245249; PREF=volume=100; SID=9geu_4zQyeHayKX50AUAG-K4r5oBNTuMazKhUzzXsyijsK6BHHB9-ATZpZXV_Kf7Kie2vw.; __Secure-3PSID=9geu_4zQyeHayKX50AUAG-K4r5oBNTuMazKhUzzXsyijsK6BDXA8QpB-C-fOOFDbfTtCUg.; HSID=AtAO5LuiKUKWZl2YF; SSID=AH92qrKq35IyDJXPx; APISID=f7KHQfdExtZm94SJ/AMqAwci5gaZwbNMBJ; SAPISID=5q-3tZQG16m9CbWn/AW5VVmYe3gVktNB9t; __Secure-3PAPISID=5q-3tZQG16m9CbWn/AW5VVmYe3gVktNB9t; LOGIN_INFO=AFmmF2swRgIhAJxVJpLFpLcaoKnwqD9tRR-Bw4WMV5gqmqw9K82ax_a7AiEAkQsVb83Yi_aGdDSKjaDleRbY2Irjc1NgIJ9Wx99y7Bo:QUQ3MjNmeTJ1T3ZrM0dFU1c4Q0ZWaDJhOTc3SEtYR0dCeElQMGcyQ3o4SUxRNjZ6VlJzUElmNTNvZjNLTDFzbHh6b253RGJQUTNpSHhvMnZYY0pjSmhLNUJDTmVIVm1MWDdpV3FRNXFFbkdLOUdlQWlkeVpWY2tQNGxJYnpVMS1rWjRVZFI0ZGF5cXVjZ0FvdWdDRzhpVTYxNXRDMzAyWUxnXzdBc0JBV0xCR28tMmVfVVcxLVFj; SIDCC=AJi4QfG-_4cZ40F8Pmn8kONzOWyWdrDBN6FANz1Qws1yjOlcGvKpffnnviCdtk-9SFXJoeW3; __Secure-3PSIDCC=AJi4QfEXefJCHdAHmt8i7ec57bjqEWditr5jTV2C8pHWmWpXOM_xJinYNoQWRl_kLL_Jb-Wy-Q origin: https://music.youtube.com referer: https://music.youtube.com/ sec-ch-ua: \"Google Chrome\";v=\"89\", \"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\" sec-ch-ua-mobile: ?0 sec-fetch-dest: empty sec-fetch-mode: cors sec-fetch-site: same-origin user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 x-goog-authuser: 0 x-goog-pageid: undefined x-goog-visitor-id: Cgt2Tno0bVkwN3MwTSjg-oiFBg%3D%3D x-origin: https://music.youtube.com x-youtube-ad-signals: dt=1621245280747&flash=0&frm&u_tz=120&u_his=5&u_java&u_h=900&u_w=1600&u_ah=873&u_aw=1600&u_cd=24&u_nplug=3&u_nmime=4&bc=31&bih=769&biw=861&brdim=0%2C27%2C0%2C27%2C1600%2C27%2C1600%2C873%2C873%2C769&vis=1&wgl=true&ca_type=image x-youtube-client-name: 67 x-youtube-client-version: 0.1 x-youtube-device: cbr=Chrome&cbrver=89.0.4389.114&ceng=WebKit&cengver=537.36&cos=X11&cplatform=DESKTOP x-youtube-identity-token: QUFFLUhqa2g5UEtlR3hJWmVpbmZZck40LTRGWHZUT20zQXw= x-youtube-page-cl: 372150654 x-youtube-page-label: youtube.music.web.client_20210510_00_RC00 x-youtube-time-zone: Europe/Berlin x-youtube-utc-offset: 120"
#c = "cookie: YSC=8SPTuF0zhJc; VISITOR_INFO1_LIVE=vNz4mY07s0M; CONSENT=PENDING+031; _gcl_au=1.1.995250531.1621245249; PREF=volume=100; SID=9geu_4zQyeHayKX50AUAG-K4r5oBNTuMazKhUzzXsyijsK6BHHB9-ATZpZXV_Kf7Kie2vw.; __Secure-3PSID=9geu_4zQyeHayKX50AUAG-K4r5oBNTuMazKhUzzXsyijsK6BDXA8QpB-C-fOOFDbfTtCUg.; HSID=AtAO5LuiKUKWZl2YF; SSID=AH92qrKq35IyDJXPx; APISID=f7KHQfdExtZm94SJ/AMqAwci5gaZwbNMBJ; SAPISID=5q-3tZQG16m9CbWn/AW5VVmYe3gVktNB9t; __Secure-3PAPISID=5q-3tZQG16m9CbWn/AW5VVmYe3gVktNB9t; LOGIN_INFO=AFmmF2swRgIhAJxVJpLFpLcaoKnwqD9tRR-Bw4WMV5gqmqw9K82ax_a7AiEAkQsVb83Yi_aGdDSKjaDleRbY2Irjc1NgIJ9Wx99y7Bo:QUQ3MjNmeTJ1T3ZrM0dFU1c4Q0ZWaDJhOTc3SEtYR0dCeElQMGcyQ3o4SUxRNjZ6VlJzUElmNTNvZjNLTDFzbHh6b253RGJQUTNpSHhvMnZYY0pjSmhLNUJDTmVIVm1MWDdpV3FRNXFFbkdLOUdlQWlkeVpWY2tQNGxJYnpVMS1rWjRVZFI0ZGF5cXVjZ0FvdWdDRzhpVTYxNXRDMzAyWUxnXzdBc0JBV0xCR28tMmVfVVcxLVFj; SIDCC=AJi4QfG-_4cZ40F8Pmn8kONzOWyWdrDBN6FANz1Qws1yjOlcGvKpffnnviCdtk-9SFXJoeW3; __Secure-3PSIDCC=AJi4QfEXefJCHdAHmt8i7ec57bjqEWditr5jTV2C8pHWmWpXOM_xJinYNoQWRl_kLL_Jb-Wy-Q x-goog-authuser: 0 x-goog-pageid: undefined x-goog-visitor-id: Cgt2Tno0bVkwN3MwTSjg-oiFBg%3D%3D"
c = ":authority: music.youtube.com :method: POST :path: /youtubei/v1/browse?ctoken=4qmFsgLZAhIMRkVtdXNpY19ob21lGsgCQ0FONjdBRkhUekpQZFRacE5UQlFRVU5OYVRCaFN6RktSVkV3ZUVKVGVsWXhaVlk1ZEZSV2JGSlhha3A1VVhwU2FsVXpTbkZSYW1SSFRVWktTV1I2UW5GVVdHTTFVbFk1VmxRd2FHeFJiR3hoWW5kd2RFTm9iRFZrUmpsM1dWZGtiRmd6VG5WWldFSjZZVWM1TUZnelNteGFNbXgyWW0xR2MwVm9PVzVQUlhSclRsUmtkRTVxU2tSWFYxWnVVek5hTW1KNlFsbGhSbWhMWld0S1MxVkliR2xpU0docVIyazRRVUZIVW14QlFVWkZVbEZCUWxKRlZVRkJVVUpIVWxjeE1XTXliR3BZTW1oMllsZFZRVUZSUVVKUmQwRkJRVUZGUVVGUlFVRkJVVVZGUVZwNFRqQjJjV040TnpCS1FXZG5RUSUzRCUzRA%253D%253D&continuation=4qmFsgLZAhIMRkVtdXNpY19ob21lGsgCQ0FONjdBRkhUekpQZFRacE5UQlFRVU5OYVRCaFN6RktSVkV3ZUVKVGVsWXhaVlk1ZEZSV2JGSlhha3A1VVhwU2FsVXpTbkZSYW1SSFRVWktTV1I2UW5GVVdHTTFVbFk1VmxRd2FHeFJiR3hoWW5kd2RFTm9iRFZrUmpsM1dWZGtiRmd6VG5WWldFSjZZVWM1TUZnelNteGFNbXgyWW0xR2MwVm9PVzVQUlhSclRsUmtkRTVxU2tSWFYxWnVVek5hTW1KNlFsbGhSbWhMWld0S1MxVkliR2xpU0docVIyazRRVUZIVW14QlFVWkZVbEZCUWxKRlZVRkJVVUpIVWxjeE1XTXliR3BZTW1oMllsZFZRVUZSUVVKUmQwRkJRVUZGUVVGUlFVRkJVVVZGUVZwNFRqQjJjV040TnpCS1FXZG5RUSUzRCUzRA%253D%253D&type=next&itct=CAMQybcCIhMIoKiOqLnQ8AIVHoF8Ch0ECw_q&alt=json&key=AIzaSyC9XL3ZjWddXya6X74dJoCTL-WEYFDNX30 :scheme: https accept: */* accept-encoding: gzip, deflate, br accept-language: de-DE,de;q=0.9 authorization: SAPISIDHASH 1621245282_24d67b3a2f3c1385e9205a204beaef1f001fc45a content-length: 715 content-type: application/json cookie: YSC=8SPTuF0zhJc; VISITOR_INFO1_LIVE=vNz4mY07s0M; CONSENT=PENDING+031; _gcl_au=1.1.995250531.1621245249; PREF=volume=100; SID=9geu_4zQyeHayKX50AUAG-K4r5oBNTuMazKhUzzXsyijsK6BHHB9-ATZpZXV_Kf7Kie2vw.; __Secure-3PSID=9geu_4zQyeHayKX50AUAG-K4r5oBNTuMazKhUzzXsyijsK6BDXA8QpB-C-fOOFDbfTtCUg.; HSID=AtAO5LuiKUKWZl2YF; SSID=AH92qrKq35IyDJXPx; APISID=f7KHQfdExtZm94SJ/AMqAwci5gaZwbNMBJ; SAPISID=5q-3tZQG16m9CbWn/AW5VVmYe3gVktNB9t; __Secure-3PAPISID=5q-3tZQG16m9CbWn/AW5VVmYe3gVktNB9t; LOGIN_INFO=AFmmF2swRgIhAJxVJpLFpLcaoKnwqD9tRR-Bw4WMV5gqmqw9K82ax_a7AiEAkQsVb83Yi_aGdDSKjaDleRbY2Irjc1NgIJ9Wx99y7Bo:QUQ3MjNmeTJ1T3ZrM0dFU1c4Q0ZWaDJhOTc3SEtYR0dCeElQMGcyQ3o4SUxRNjZ6VlJzUElmNTNvZjNLTDFzbHh6b253RGJQUTNpSHhvMnZYY0pjSmhLNUJDTmVIVm1MWDdpV3FRNXFFbkdLOUdlQWlkeVpWY2tQNGxJYnpVMS1rWjRVZFI0ZGF5cXVjZ0FvdWdDRzhpVTYxNXRDMzAyWUxnXzdBc0JBV0xCR28tMmVfVVcxLVFj; SIDCC=AJi4QfG-_4cZ40F8Pmn8kONzOWyWdrDBN6FANz1Qws1yjOlcGvKpffnnviCdtk-9SFXJoeW3; __Secure-3PSIDCC=AJi4QfEXefJCHdAHmt8i7ec57bjqEWditr5jTV2C8pHWmWpXOM_xJinYNoQWRl_kLL_Jb-Wy-Q origin: https://music.youtube.com referer: https://music.youtube.com/ sec-ch-ua: \"Google Chrome\";v=\"89\", \"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\" sec-ch-ua-mobile: ?0 sec-fetch-dest: empty sec-fetch-mode: cors sec-fetch-site: same-origin user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 x-goog-authuser: 0 x-goog-pageid: undefined x-goog-visitor-id: Cgt2Tno0bVkwN3MwTSjg-oiFBg%3D%3D x-origin: https://music.youtube.com x-youtube-ad-signals: dt=1621245280747&flash=0&frm&u_tz=120&u_his=5&u_java&u_h=900&u_w=1600&u_ah=873&u_aw=1600&u_cd=24&u_nplug=3&u_nmime=4&bc=31&bih=769&biw=861&brdim=0%2C27%2C0%2C27%2C1600%2C27%2C1600%2C873%2C873%2C769&vis=1&wgl=true&ca_type=image x-youtube-client-name: 67 x-youtube-client-version: 0.1 x-youtube-device: cbr=Chrome&cbrver=89.0.4389.114&ceng=WebKit&cengver=537.36&cos=X11&cplatform=DESKTOP x-youtube-identity-token: QUFFLUhqa2g5UEtlR3hJWmVpbmZZck40LTRGWHZUT20zQXw= x-youtube-page-cl: 372150654 x-youtube-page-label: youtube.music.web.client_20210510_00_RC00 x-youtube-time-zone: Europe/Berlin x-youtube-utc-offset: 120"
cs = c.split(": ")
key = []
value = []
config = ""
remove_keys = {":authority", ":method", ":path", ":scheme"}
for i in range(0,len(cs)-1):
    k_start = cs[i].rfind(' ')+1
    key.append(cs[i][k_start:])
    value.append(cs[i+1])
    if(i>0):
        value[i-1] = value[i-1].replace(' '+key[i],'')
        if(key[i-1] not in remove_keys):
            config += key[i-1]+": "+value[i-1]+'\n'
    if(i==len(cs)-2):
        config += key[i]+": "+value[i]+'\n'
#print(config)

for i in range(0,len(key)):
    print("["+str(i)+"] "+key[i])

YTMusic.setup(filepath = '/tmp/key', headers_raw = config)
ytmusic = YTMusic('/tmp/key')
s=ytmusic.get_library_playlists()
print(s)