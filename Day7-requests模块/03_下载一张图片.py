import requests

url = "https://img.yituyu.com/pic/1405/01_5biwvm9v.jpg"
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "cookie": "Path=/; yituyu_lailu=cn.bing.com%2F; yituyu_rukou=www.yituyu.com%2Ftag%2F105%2F; yituyu_fr=; yituyu_first_time=1780912528000; __51uvsct__KfoPIZ9YEA9qUdVj=1; __51vcke__KfoPIZ9YEA9qUdVj=0f902d38-a9f1-5046-a85f-35402296e9cc; __51vuft__KfoPIZ9YEA9qUdVj=1780912528268; yituyu_os=Windows%20NT%2010.0%3B%20Win64%3B%20x64; Hm_lvt_9714eb07ec1e2c497aefe3d4dfded3ed=1780912528; HMACCOUNT=74ED4E40E6CB58EE; __vtins__KfoPIZ9YEA9qUdVj=%7B%22sid%22%3A%20%223fc1ec55-b45f-505f-b817-5193150d9745%22%2C%20%22vd%22%3A%203%2C%20%22stt%22%3A%2058724%2C%20%22dr%22%3A%204806%2C%20%22expires%22%3A%201780914386986%2C%20%22ct%22%3A%201780912586986%7D; Hm_lpvt_9714eb07ec1e2c497aefe3d4dfded3ed=1780912587",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://www.yituyu.com/tag/105/",
    "sec-ch-ua": "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
with open('yituyu.jpg', 'wb') as f:
    f.write(response.content)