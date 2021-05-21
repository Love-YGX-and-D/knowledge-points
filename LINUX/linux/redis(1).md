# redis安装
```
Remote Dictionary Server（远程数据服务）
```
1. $sudo apt-get update
2. $sudo apt-get install redis-server
3. 启动服务器 Redis
`$ redis-server`
5. 启动客户端redis
`$ redis-cli -h -p -a`
6. 设置密码
   ```
   config set requirepass pass
   ```
7. 配置文件
```
 /etc/redis/redis.conf
```
# redis字符串常用命令
1. 设置值
```
set key value [EX s] 默认的生命周期
```
2. 获取值
```
get  key
```
3. 设置,获取多个值
```
mset key1 value1 key2 value2 ....
mget key1 key2 ....
```
4. 追加值
```
append  key value
```
5. 删除值
```
del key
```
6. 自增 增减

```
incr key
decr key
```

7. 加减指定的值
```
incrby key num
decrby key num
```
# redis hash常用命令
1. 设置hash值
```
hset mainkey innerkey val .....
```
2. 获取hash值
```
hget mainkey innerkey
```
3. 设置多个hash值
```
hmset mainkey innerkey1 val1  innerkey2 val2
```
4. 获取多个hash值
```
hmget mainkey innerkey1   innerkey2
```
5. 获取所有的hash 键值对

```
hgetall mainkey
```
6. 删除指定的key
```
hdel mainkey innerkey
```
7. 删除所有的值
```
del mainkey
```
8. 自增、自减值
```
hincrby mainkey innerkey num
hdecrby mainkey innerkey num
```
9. 查看某个属性是否存在
```
hexists mainkey innerkey
```
10. 获取个数
```
hlen mainkey
```
11. 获取所有的键
```
hkeys mainkey
```

# redis 列表常用命令
1. 开始(左侧)添加数据
lpush name val1 val2 val3
```
2. 结尾(右侧)添加数据
```
rpush name val1 val2 val3
```
3. 查看数据
```
lrange name start end[支持负数]
```
4. 从左侧删除元素
```
lpop name
```
5. 从右侧删除元素
```
rpop name
```
6. 删除指定个数的元素
```
lrem name num val
```
7. 指定的位置设置值
```
lset name num val
```
8. 在指定的位置之后插入值
```
linsert name after val newval
```
9. 在指定的位置之前插入值
```
linsert name before val newval
```
10. 获取元素的个数
```
llen name
```

# redis set数据的常用命令
**set 中不允许出现重复的元素**

1. 设置值
```
sadd name val1,val2,val3
```
2. 删除值
```
srem name val1,val2,val3
```
3. 查看值
```
smembers name
```
4. 判断某个值是否存在
```
sismember name val
```
5. 差集运算
```
sdiff name1 name2
```
6. 交集运算
```
sinter name1 name2
```
7. 并集运算
```
sunion name1 name2
```
8. 获取成员的数量
```
scard name
```

# redis key的通用操作
1. 查询所有的key
```
keys *
```
2. 查看某些key
```
keys name?
```
3. 删除指定的key
```
del key1 key2 ....
```
4. 查看某个键是否存在
```
exists key
```
5. 重命名key
```
rename key newkey
```
6. 设置一个值过期的时间
```
expire key time
```
7. 查看剩余的时间
```
ttl key
```
8. 获取key的类型
```
type key
```
9. 清空所有的数据
```
flushall
```
10. 选择库
```
select num
```

# redis持久化方式

1. RDB方式 默认
2. AOF

# python 操作redis

1. 安装 redispy
```
sudo pip install redis
```

# django使用redis
1. 安装包：pip install django-redis-cache
2. 设置 setting
    ```

    CACHES = {
        "default": {
            "BACKEND": "redis_cache.cache.RedisCache",
            "LOCATION": "172.16.168.130:6379",
            "OPTIONS":{
                'PASSWORD': '123456'
            },
            'TIMEOUT': 60,
        },
    }
    ```

3. 单个view缓存
    ```
    from django.views.decorators.cache import cache_page

    @cache_page(60 * 15)
    def index(request):
        return HttpResponse('hello1')
        #return HttpResponse('hello2')
    ```

4. 模板片断缓存
    ```
    { % load cache % }
    { % cache 500 hello % }
    hello1
    <!--hello2-->
    { % endcache % }
    ```
5. 调用原生方法
    ```
    from django.core.cache import cache

    设置：cache.set(键,值,有效时间)
    获取：cache.get(键)
    删除：cache.delete(键)
    清空：cache.clear()
    ```

