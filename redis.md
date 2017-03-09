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

1. SELECT index. 切换到指定的数据库
2. llen key






