整体流程:

case写在excel（可指定是否执行和case等级）, 获取前置token--读取用例-筛选用例--根据环境&角色(账号)生成对应的header--获取url&request_data中的依赖参数--先从流转变量文件中取值--若取不到,从环境变量中取--替换url/data中的参数--请求--断言--从请求提取需流转的参数到变量池...(未完成)结果写入excel--调bug平台openapi提bug--bug汇总+allure测试报告-测试报告邮件


目录说明：

common：公共类、方法

	assert.py: 断言
	data_tool: 操作数据文件的方法, cofig, yaml, json等
	db_tool: 数据库连接、增删改查方法
	get_testdata: 获取token, 读case, 拼接case, 构建header, 
	privatetools: 针对项目的特殊方法, 封装请求签名，参数流转、依赖的提取等
	logger: 日志器
	request: 请求方法, 暂只支持Http
	
config: 配置目录

	数据库配置、执行环境配置、要执行的用例等级配置等
	
data: 数据目录

	env_var.yaml: 环境变量
	flow_var.yaml: 关联变量池, 接口关联时,用来存储临时变量

Logs: 日志文件目录, 以日期为分割保存,只保存10天,可在logger模块中自定义

reports: allure测试报告目录


