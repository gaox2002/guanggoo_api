# guanggoo_api
REST APIs for content management

## Start

### initialize database
init database by 
```shell
./manage.py db init 
```
it generates migrate folder as migrations, then run
```perl
./manage.py db upgrade
```
to create/update the tables

### Start server
```python
./manage.py runserver
```


### Roadmap
* 用户
  * 注册
  * 登录
  * email确认
  * 密码找回
  * 第三方
  * -- 短信确认
* 贴子
  * 回贴
  * 搜索
* 关注
  * 分享
* 公众号
  * 自动答复（推荐）
  * 周报
  * 新闻
