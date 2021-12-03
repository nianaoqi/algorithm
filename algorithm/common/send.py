import json
import requests
# 请求方法，根据不同的请求方法，传不同的参数

def send(host,method, url, data, headers):
    if method == "get":
        res = requests.get(host + url, params=data, headers=headers)
    elif method == "post":
        res = requests.post(host + url, json=data, headers=headers)
    elif method == "put":
        res = requests.put(host + url, json=data, headers=headers)
    elif method == "delete":
        res = requests.delete(host + url + "/" + data, headers=headers)
    return res

