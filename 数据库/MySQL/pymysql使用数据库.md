# 安装不成功时使用命令建立依赖关系

```linux
sudo apt-get install python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev 
```

# 导入pymysql模块

```python
import pymysql
```

# 连接database
```mysql
db = pymysql.connect(host=“你的数据库地址”, user=“用户名”,password=“密码”,database=“数据库名”,charset=“utf8”)
```

# 得到一个可以执行SQL语句的光标对象
```mysql
cursor = db.cursor()
```

# 定义要执行的SQL语句
```mysql
sql = """
CREATE TABLE USER1 (
id INT auto_increment PRIMARY KEY ,
name CHAR(10) NOT NULL UNIQUE,
age TINYINT NOT NULL
)ENGINE=innodb DEFAULT CHARSET=utf8;
"""
```

# 执行SQL语句
```mysql
cursor.execute(sql)
```

# 关闭光标对象
```mysql
cursor.close()
```

# 关闭数据库连接
```mysql
conn.close()
```

