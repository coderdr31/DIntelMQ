<head><meta charset="UTF-8"></head>
## lpush
```
redis 127.0.0.1:6379> LPUSH KEY_NAME VALUE1.. VALUEN

127.0.0.1:6379> LPUSH list1 "foo"
(integer) 1
127.0.0.1:6379> LPUSH list1 "bar"
(integer) 2
127.0.0.1:6379> LRANGE list1 0 -1
1) "bar"
2) "foo"
```

* FLUSHALL    清空所有数据库的所有 key
* SELECT index. 切换到指定的数据库
* DBSIZE         显示指定数据库的 key 数量
* keys *    列出指定数据库的key
* flushdb   清除指定数据库的key
* llen key






