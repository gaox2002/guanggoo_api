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
* 贴子
* 关注
* 公众号
  * 自动答复（推荐）
  * 周报
  * 新闻
