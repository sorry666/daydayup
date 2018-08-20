import requests  # package

req = requests.get(
    'http://www.sina.com.cn/',  # url, as you like
    params={"wd": "find", "rn": "100"},
    headers={'user-agent': 'Mozilla/5.0'}
)
req.encoding = "utf-8"
print(req.text)