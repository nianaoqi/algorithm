整体流程:

用例写在excel, 获取前置token--读取用例数据--根据环境&用例执行角色(账号)生成对应的header--获取url&request_data中的依赖参数--先从流转变量文件中取值--若取不到,从环境变量中取--替换url/data中的参数--请求--断言--...(未完成)结果写入excel--调bug平台openapi提bug--bug汇总+测试报告邮件


目录说明：

common：公共类、方法

	assert.py: 断言
	data_util: 操作数据文件的方法, cofig, yaml, json等
	db_util: 操作数据库的方法
	get_testdata: 获取token, 获取case参数, 构建header, 
	functions: 针对项目的特殊方法, 封装请求签名，参数流转、依赖的提取等
	logger: 日志器
	request: 请求方法, 暂只支持Http
	
config: 配置目录

	数据库配置、环境配置, 在此切换环境
data: 数据目录

	env_var.yaml: 环境变量
	flow_var.yaml: 流转变量, 接口关联时,用来存储临时变量

Logs: 日志文件目录, 以日期为分割保存,可在logger模块中自定义

reports: 测试报告目录

