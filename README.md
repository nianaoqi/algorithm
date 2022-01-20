整体流程:

1.用例写在excel, 可定义是否执行,用例级别(执行时可选),多种断言,多个流转参数,依赖参数

2.获取全部角色的token, 根据[环境&menu&执行角色(账号)]，生成对应的header(此步骤为业务特殊需要(累计100多种header,无法写死)

3.正则匹配和替换url&request_data中的依赖参数(取值顺序为流转变量池 → 全局环境变量)

4.None

5.需流转供后续接口依赖的参数, key:value 形式保存至变量池yaml文件, 支持多个

6.请求, 断言, 测试结果写入excel

7.调bug平台openapi提bug, bug汇总(暂无需)

8.带详细测试步骤的Allure测试报告

9.钉钉、飞书、邮件等发送测试报告

![img_1.png](imgs/img_1.png)

目录说明：

--common：公共类、方法

    assert.py: 断言
    data_util: 操作数据文件的方法, cofig, yaml, json等
    db_util: 操作数据库的方法
    get_testdata: 获取token, 获取case参数, 构建header, 
    functions: 针对项目的特殊方法, 封装请求签名，参数流转、依赖的提取等
    logger: 日志器
    request: 请求方法, 暂只支持Http
    
--config: 配置目录

    数据库配置、环境配置、用例执行级别
    
--imgs: 图片文件

    图片基准目录
    
--data: 数据目录

    env_var.yaml: 环境变量
    flow_var.yaml: 流转变量, 接口关联时,用来存储临时变量
    
--logs: 日志文件目录

    以日期为分割保存,可在logger模块中自定义

reports: 测试报告

    Allure报告,包含步骤等信息
    
报告示例

    pass

报告通知
![image](https://user-images.githubusercontent.com/75521205/150306248-fa2f8228-f6a2-49dc-ba23-49af8f99297e.png)


流程图
![XemaAp3oBv](https://user-images.githubusercontent.com/75521205/150306697-54bdc641-8598-4501-9dd0-5d7d95163663.png)


    pass
