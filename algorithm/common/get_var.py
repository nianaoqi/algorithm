# 从yaml文件读取环境变量信息，根据不同的环境或模块，获取对应的host,space_id,biz_line,menu_id 生成对应的host，token, 和最终headers

import yaml
import requests
import pytest

# 获取json格式的环境变量参数
yml = open(r"E:\pythonProjects\Learn\data\env_var.yaml", "r", encoding="utf-8")
yml = yml.read()
yaml = yaml.safe_load(yml)

# 定义登录账号的请求体,BOE环境和PPE环境, 白名单账号可以直接用用户名登录
data = {
    "username": None,
    "password": "123456",
    "code_id": "QSoYuUzE2s7f7cQDShVh",
    "code_value": "80"
}


# @pytest.mark.parametrize("username",["年奥齐","881","882"])
def var(env, module, username):  # 提供环境，模块，角色，生成对应header和space
    host = yaml[env]["host"]
    space_id = yaml[env]["space_id"]
    menu_id = yaml[env][module]
    headers = {
        "Algorithm-Space": space_id,
        "Content-Type": "application/json"
    }
    # 生成token，boe、ppe8种，线上6种，共存在14种结果
    if env == "1" or "2":
        if username == "扫码用户":
            token = yaml[env]["token"]
        else:
            data["username"] = username
            res = requests.post(host + "/arule/api/v1/user/login", json=data, headers=headers).json()
            # print(data)
            token = res["data"]["token"]
    else:
        if username != "年奥齐":
            token = yaml[env]["token"]
        else:
            token = yaml[env]["token1"]

    # 生成ppe和非ppe的header
    if env == 2:
        headers = {
            "Algorithm-Space": space_id,
            "Content-Type": "application/json",
            "algorithm-menu": menu_id,
            "token": token,
            "X-TT-ENV": "ppe_evaluation",
            "x-use-ppe": "1"
        }
    else:
        headers = {
            "Algorithm-Space": space_id,
            "Content-Type": "application/json",
            "algorithm-menu": menu_id,
            "token": token
        }

    return [host, headers]




if __name__ == "__main__":
    try:
        var("1", "annotate", "881")
    except Exception as e:
        print("--错误信息：", e, "\n--错误行号:", e.__traceback__.tb_lineno)
