整体流程:

1.用例用excel管理, 可定义是否执行, 执行级别, 4种断言, 依赖参数, 流转参数

2.获取前置token, 根据环境&menu&执行角色(账号)，生成对应的header

3.获取url和request_data中需依赖参数的字段

4.先从临时变量池文件中取值,若取不到,从全局环境变量中取,替换掉url/data中的依赖参数

5.发起请求, 请求成功后进行断言

    断言失败,则调bug平台openapi提bug(暂无需,拦截bug不多)

6.jsonpath提取需供后续接口依赖的参数, key:value形式保存至变量池,支持多个

8.带详细测试步骤的Allure测试报告+群消息通知(也可选邮件)

![img_1.png](imgs/case_sample.png)

目录说明：

--common：公共类、方法

    assert.py: 断言
    BASE_PATH: 项目基准路径, 不随导包而变化
    clear_file: 清除文件或目录, 日志或报告超过10个则清空
    data_tool: 数据文件操作, config, yaml, json等
    da_tool: 数据库相关操作
    get_testdata: 获取token, 获取case参数, 构建header等 
    logger: 日志器二次封装
    notice: 发邮件、飞书、钉钉群通知, 通过fixture调用, 附带执行情况和测试报告
    PrivateTools: 针对项目的特殊方法, md5加密获取sign，依赖参数替换、流转参数提取等
    request: 请求方法, 暂只支持Http
    
    
--config: 配置目录

    db_ini: 数据库配置、环境配置、用例执行级别
    setting_ini: 执行环境、用例执行等级、群/邮箱账号配置

--imgs: 图片文件

    执行过程产生的图片、UI自动化才需要
    
--data: 数据目录

    env_var.yaml: 环境变量
    var_pool.yaml: 流转变量, 接口关联时,用来存储临时变量, 执行前会清空
    
--logs: 日志目录

    以日期为分割保存,仅保留10天,可在logger模块中自定义

reports: 测试报告

    Allure测试报告,包含详细执行步骤信息
    
报告示例

![img_1.png](imgs/report.png)

通知示例:
![img_1.png](img_1.png)
流程图

    pass