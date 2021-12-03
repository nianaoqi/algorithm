import json
import pytest
import common.case as case
import common.send as send
from common.all_function import *
from datetime import datetime

time = datetime.now().strftime("%m%d_%H%M")

env = input("哪个环境？（输入编号）：\n---BOE环境---\t\t|\t\t---线上环境---\n1.国内prod 2.sit \t|\t 3.国内 4.新加坡 5.美东 \n")


class Test:
    # @pytest.mark.parametrize("param", case.readxl(env, "/Users/bytedance/Downloads/testcase.xlsx", "闭环转标注"))
    # def test_common(self, param):  # 公共方法
    #     # print(param[0])
    #     host, headers, biz_line, method, url, data = param
    #     data = json.loads(data)
    #     res = send.send(host, method, url, data, headers).json()
    #     print(res["msg"])
    #     assert res["status"] == 0

# # 上传文件
#     def upload_file(self,):


# 创建根任务
    def test_create_root_task(self, param = readxl("1", "/Users/bytedance/Downloads/testcase.xlsx", "创建根任务")[0]):
        host, headers, biz_line, method, url, data = param
        data = data % ("回测" + time, biz_line, read_yaml("test.yaml","file_id"))
        print(data,type(data))
        data = json.loads(data)
        res = send(host, method, url, data, headers).json()
        print(res)
        data = {"task_id": res["data"]["task_id"]}
        write_yaml("./data/test.yaml", data)


