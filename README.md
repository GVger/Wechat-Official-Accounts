# Wechat-Official-Accounts
**微信公众号后台框架 python版<br/>**
<br/>
启动程序之前需要配置好`common/wx_system.template.conf`并且将其改名为`wx_system.conf`;
同样的`wx/Wechat-Official-Accounts.template.conf`需要同样类似的操作。
<br/>
程序的入口 `wx/wx_main.py` 启动命令 `python wx_main.py 9633` (9633为启动的端口)。
<br/>
【2019.7.12】打算利用百度AI来解析用户发送的语句并做自动回答 。
<br/>
【2019.7.17】一些配置独立到配置文件当中。
<br/>
【2019.7.19】添加了微信公众号全局异常代码以及对应，添加了客服文字消息的发送，
一些接口的配置化处理。引入redis库，编写redis的一些操作。
打算利用redis来处理公众号的access_token。
<br/>
【2019.7.23】使用redis处理access_token，图片处理返回百度ai的结果和图片本身。
redis添加密码，配置添加redis密码。
<br/>
【2019.7.29】接入百度语言识别功能。尝试添加.gitignore过滤掉敏感信息。
