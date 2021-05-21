# 简介

## 特点:

- 开源的
- 支持大型的数据库,可以处理拥有成千上万条记录的大型数据库
- 使用标准的SQL数据语言形式
- 可以运行于多个系统上,并且支持多种语言.[c语言,Perl,PHP,Eiffel,Ruby,Tcl]
- 支持大型数据库,支持5000万条记录的数据仓库,32位系统4TB,64位8Tb
- MySQL是可以定制的，采用了GPL协议，你可以修改源码来开发自己的MySQL系统。

## 主要内容

### DCL:数据控制语言

> 用来设置或这更改角色和权限,关键字:grant,remove

### DDL:数据定义语言

>用来创建数据库,创建表结构,关键字:create,truncate

### DML:数据操纵语言

> 负责数据库的插入(insert),更新(update),删除(delete)

### DQL:数据库查询语言

> 查询数据库,查询(select)

### TCL:事务控制语言

> 事务:一个完整的事件

### 数据库锁

### 主从配置

### 数据库优化操作

# 打开/关闭/重启服务器

> service mysql start/close/restart

# 注释语法

```mysql
-- 注释  #注释
sql注入
    > select * from stu where uname=" " or 1=1; --" and upass="123"
```

# DCL

> 在默认情况下,只有超级管理员才能操作数据库

## 访问控制权限

> mysql实现了复杂的访问控制和权限系统,允许多用户同时操作

## 命令行链接方式

> mysql -u 用户名 -p密码 -h 服务器IP地址 -P 服务器端mysql端口 -D 数据库名

## 当客户端链接到服务器时,mysql访问控制两个阶段

>1.链接
>
>2.验证

## 默认表

>创建mysql的时候就会有

### user表:包含账户和权限列

### db表:哪个用户可以访问哪个数据库

### table_priv和columns_priv表:包含表级和列级操作

### procs_priv:包含存储函数和存储过程的表

## 创建账户:

> create user 用户名(格式:username@访问域名) identified by 密码[必须是明文,字符串]
>
> 用户名:
>
> ​	username@%
>
> ​	username@%.alibaba.com 只能访问alibaba.com 域名下的东西	
>
> ​	省略@,表示%

## 通配符（%）和（-）

> 百分号或者；-表示在任意部位都可以修改

## 删除用户

> drop username@访问域名
>
> drop username@访问域名,username1@访问域名,username2@访问域名
>
> delete from user where user=username

## 查看用户权限

> show grants for username@访问域名

```
点之前的部分表示数据库,(.)之后的部分表示表上的结果,
```

## 设置权限

> grant 权限1，权限2【all：所有】on 库.表/库/表 to user 【 identified by 密码[必须是明文,字符串]】 【require 链接数据的方式】 【with [grant option | resource option]】(一般都写)

grant all on （ * . *） to username@访问域名 with grant option；

### 设置指定权限

> create user rfc indentified  by '密码'

> grant select,update,delete on alibaba.* to rfc

### 执行无权利错误 1142（42000）

## 允许远程链接

> grant all privileges on * . * to 'root'@'%' indentfied by 'mysql' with grant option; 设置权限密码用户名
>
> 8.0版本：
>
> create user 'root'@'%' 

```python
CREATE USER 'root'@'%' IDENTIFIED BY '1002';
 
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '1002';
设置为远程登录

GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'root' WITH GRANT OPTION;

GRANT ALL ON 表示所有权限，% 表示通配所有 host，可以访问远程。
5.刷新权限
所有操作后，应执行
flush privileges;
```



## 刷新权限

> flush privileges；

## 撤销权限

> revoke privilege_type [(column_list)],[privilege_type [(column_list)]] on object_type.privilege_level from user,[user1,user2]

### 示例：

> revoke select on * . * from user

## 修改密码

### 1.登录MySQL

> set password for 用户名@localhost =‘新密码’

### 2.登录MySQL

> update user set password='密码' where user='root' and host='localhost'
>
> 刷新

### 3.用mysqladmin

> mysqladmin -u用户名 -p旧密码 password 新密码

### 4.忘记root密码或者初始化密码

```mysql
在windows上
 1.关闭正在运行的mysql【必须】
 2.打开DOS窗口，转到mysql\bin
 3.输入
 	8.0版本以前：mysqld --skip-grant-tables   【跳过权限检查】
 	8.0版本：mysqld --console --skip-grant-tables --shared-memory
 4.再打开一个DOS窗口，转到mysql\bin目录
 5.输入mysql回车，若成功，将出现mysql提示符
 6.链接数据库： use mysql
 7.改密码
 	update user set password=password('密码') where user='root' and host='localhost'
 8.刷新权限
 	flush privileges;
 9.退出
 10.重启电脑早进入，修改完成
```

## 数据库备份

> mysqldump

> mysqldump -u 用户名 -p 密码 [-h localhost] 数据库名 >  输出的文件.sql

### 仅备份数据库结构

> mysqldump -u 用户名 -p 密码 [-hlocalhost] --no-data 数据库名 >  输出的文件.sql

### 仅备份数据库数据

> mysqldump -u 用户名 -p 密码 [-hlocalhost] --no-create-info  数据库名 >  输出的文件.sql

### 导出多个数据库

> mysqldump -u 用户名 -p 密码 [数据库1,数据库2] > [输出的文件1.sql，输出的文件2.sql]
>
> 所有的：
>
> mysqldump -u 用户名 -p 密码 --all-database > [all_dbs_dump_files.sql]

## 导入数据库

```mysql
1、首先建空数据库
	mysql>create database abc;
2、导入数据库
    方法一：
        （1）选择数据库
            use abc;
        （2）设置数据库编码
            set names utf8;
        （3）导入数据（注意sql文件的路径）
            source /home/abc/abc.sql;
    方法二：
        mysql -u用户名 -p密码 数据库名 < 数据库名.sql
```

## 查询

### 查询数据库

```mysql
show databases；
删除数据库：
	drop database sc；
查询表的结构：desc 表名；
查看基本表：show tables；
```

### 查询列

```mysql
show columns from 表名;
show columns from 表名 like '关键字'；  #关键字查询
show columns from 表名 like '%e%';    #包含e的
show columns from 表名 where Field="关键字"; 
```

### 查询用户

```mysql
select user from mysql;
当前用户：
select user();
select current_user();
```

### 当前登录的用户

```mysql
select user,host,db,command from information_schema.processlist;[临时表]
```

## 数据库维护

> 维护的是表

```mysql
维护结果：
Table：表名；
Op：执行的操作[analyze/....]
Msg_type:信息类型，状态/警告/错误
Msg_text:显示信息
```

### 分析表

```mysql
analyze table 表名，【表名2，...】；
```

### 优化表

```mysql
optimize table 表名；
```

### 检查表

```mysql
check table 表名；
只管检查，不管修复
```

### 修复表

> 尝试修复，不一定能修好

```mys
repair table 表名；
显示表是否修复；
```

# DDL

> 数据库定义语言create，alter，drop

## 数据库

### 创建数据库

```mysql
create database 【if not exists】 库名；
【if not exists】:可选字段，保证库是新的
创建带字符编码的数据库
CREATE DATABASE UAIW1803 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
```

### 删除数据库

```mysql
drop database [if exists] 库名；
```

## 表：

### 查询表

```mysql
show create table 表名；
desc 表名
show full tables;
```

### 创建表

> mysql 5.1不安装引擎，需自己安装
>
> charset=utf8  指定字符集
>
> engine=InnoDB  指定引擎
>
> comment="示例1" 添加注释

```mysql
1)	Student表的信息：
属性名	  数据类型	  长度	完整性约束条件
Sno	    varchar	    9	    主码
Sname	varchar	    20	   唯一值
Sage	smallint	6	
Ssex	varchar	    2	
Sdept	varchar	    20	
代码：
create table if not exists Student(
	Sno varchar(9) primary key,
	Sname varchar(20) unique,
	Sage smallint,
	Ssex varchar(2),
	Sdept varchar(20)
)default charset=utf8 engine=InnoDB comment="示例1";
2)	Course表的信息：
属性名	  数据类型	  长度	完整性约束条件
Cno  	varchar	    4	      主码
Cname	varchar	    40	
Cpno	varchar	    4	与Course表中Cno关联
Ccredit	smallint	6	
代码
create table Course(
	Cno varchar(4) primary key,
	Cname varchar(40) ,
	Cpno varchar(4),
	Ccredit smallint,
	foreign key(Cpno) references Course(Cno)
);
3)	SC表的信息
属性名	  数据类型	  长度	完整性约束条件
Sno	    varchar	    9	   非空，主码，与Student表中Sno关联，级联删除
Cno	    varchar	    4	   非空，主码，与Course表中Cno关联
Grade	smallint	6	
代码：
create table SC(
	Sno varchar(9),
	Cno varchar(4) ,
	Grade smallint,
	primary key(Sno,Cno), #联合主键
    `Create Table 表名 (字段名1 Int Not Null,
                   字段名2 nvarchar(13) Not Null Primary Key (字段名1, 字段名2),
                    字段名3…………
                    字段名N………… )
	`
    
	foreign key(Sno) references Student(Sno)on delete cascade on update cascade,          	//删除和更新时级联操作
	foreign key(Cno) references Course(Cno)on delete cascade on update cascade		
);
```

### 定义列

```mysql
字段意义详解：
int(11):11代表显示的宽度
varchar(size):varchar弹性大小，最大的size是65535
not null：不为空；
defalut ‘默认值’：默认值一般为NULL，和not null选择一个用即可
unique：不唯一，指定后，该列只能出现一个一样的信息，比如手机号/身份证号
enum（"1","0"）：枚举类型，当设置默认值是，默认是第一个为默认值
set("吃","喝","玩")：集合类型，设置爱好时常用
插入中文时需要使用 ：set char set ‘gbk’;
```

### 修改表

```mysql
向Student表中添加“Sentrance”列：
	alter table student add Sentrance enum（“男”，“女”） not null [first|after （列明）] date;
将Student表中“Sentrance”的数据类型改为varchar：
	alter table student modify column Sentrance varchar(4);
删除student表中的“Sentrance”列：
	alter table student drop Sentrance;
修改Course表中的“Cname”为“Cnam”：
	alter table course change 【column】Cname Cnam varchar(20)+设置表的列的其他信息;
```

#### 修改特性

##### 主键

```mysql
1. 添加主键
	alter table 表名 add primary key（列名）
2. 删除主键
	alter table 表名 drop primary key
3. 联合主键
	ALTER TABLE 表名 WITH NOCHECK ADD CONSTRAINT [PK_表名] PRIMARY KEY  NONCLUSTERED ([字段名1],[字段名2])
```

##### 索引

```mysql
添加唯一索引
	alter table 表名 add unique(列明)
添加全文索引：
	alter table 表名 add fulltext(列明)	【版本 >=5.7】
添加普通索引:
	alter table 表名 add index(列明)
删除索引：
	alter table 表名 drop index/ fulltext/unique  列名
修改索引
	删了再加
```

##### 引擎

```mysql
修改：
alter table 表名 engine=innodb
显示所有额引擎：
show engines
```

##### 修改自增

```mysql
alter table 表名 auto_increment=1
```

### 删除表

```mysql
drop table 表名；
```

## 数据类型

> 数值，字符，时间

### 数值类型

| 类型        | 大小                                     | 范围（有符号） | 范围（无符号） |
| ----------- | ---------------------------------------- | -------------- | -------------- |
| tinyint     | 1字节                                    | -2^7，2^7-1    | 0,2^8-1        |
| smallint    | 2字节                                    | -2^15,2^15-1   | 0,2^16-1       |
| mediumint   | 3字节                                    | ...            |                |
| int/integer | 4字节                                    | ..             |                |
| bigint      | 8字节                                    | ...            |                |
| float       | 4字节                                    | ..             |                |
| double      | 8字节                                    | ...            |                |
| decimal     | 对于decimal（m，d）,若m>d,则m+2；否则d+2 | 依赖m，d       |                |

> unsigned : 无符号；最小是0
>
> zerofill：数值的位数不足时，用0填充；

### 字符串：

| 类型       | 大小                   |                         |      |      |
| ---------- | ---------------------- | ----------------------- | ---- | ---- |
| char       | 0-255字节              | 定长字符串【唯一定长】  |      |      |
| varchar    | 0-65535字节            | 变长字符串              |      |      |
| tinyblob   | 0-255字节              | 不超过255个字符的二进制 |      |      |
| tinytext   | 0-255字节              | 不超过255个字符的文本   |      |      |
| blob       | 0-65535                |                         |      |      |
| text       | 0-65535                |                         |      |      |
| mediumblob |                        |                         |      |      |
| mediumtext |                        |                         |      |      |
| longblob   |                        |                         |      |      |
| longtext   |                        |                         |      |      |
| enum       | 数据长度为1，值为0,1,2 |                         |      |      |
| set        |                        |                         |      |      |

### 日期类型

| 类型      | 大小 | 范围 | 格式                 |
| --------- | ---- | ---- | -------------------- |
| date      | 3    |      | yyyy-mm-dd           |
| time      |      |      | hh：mm：ss           |
| year      |      |      | yyyy                 |
| datetime  |      |      | yyyy-mm-dd  hh:mm:ss |
| timestamp |      |      | 毫秒数、时间戳       |

> 类型为timestamp，默认为插入数据的事件，更新时，时间也会变【版本>=5.7】

### 空间数据类型

> 略

## 引擎

> 最大限度利用mysql

### 查询所有引擎

```mysql
show engines;   [myisam  innodb]
```

### MyISAM

```mysql
不支持事物，外键。
虽然访问速度快，对事物完整性没有要求
.frm   ：   存储表结构信息【二进制文件信息】
.myd   ：   数据
.myi   ：   索引
```

### InnoDB

> 健壮的事务型存储引擎

```mysql
更新密集的表
事务
自动灾难恢复
外键约束【只有innodb支持外键】
较高的并发读取速度

文件类型包含
.frm    ：   表结构
.opt    ：   数据库选项
数据：        安装目录下的data文件夹

```

## 索引类型

### 主键索引：primary key 

> 一个表只能有1个(字段)，主键的值唯一，==》 查询更快  auto_increment

#### 注意

```mysql
1、数据库的每张表只能有一个主键，不可能有多个主键。
2、所谓的一张表多个主键，我们称之为联合主键。
     注：联合主键：就是用多个字段一起作为一张表的主键。
3、主键的作用是保证数据的唯一性和完整性，同时通过主键检索表能够增加检索速度。
```

### 唯一键索引：unique

> 可以给多个字段设置，字段中的值不能重复，==》 查询更快

### 普通索引：index

> 仅仅是加了一个索引

### 文本索引：fulltext

> 版本 >=5.7
>
> 文本编辑器，快速在大批量文本中有序查找内容

### 外键：foreign key

> 让两个表进行关联：副表的非主键和主表的主键
>
> 保持数据的一致性和完整性

#### 作用

- 若在副表中添加一个主键里不存在的数据，插入时则会报错
- 若在主表当中进行修改或者是删除的时候，副表对应的数据，则会有反应

#### 语法

```mysql
创建：
    简单：
    [CONSTRAINT 约束名] foreign key [外键名] (列名) references 主表（列名）
    复杂：
    [CONSTRAINT 约束名] foreign key [外键名] (列名) references 主表（列名）on delete cascade on update cascade；
    	动作：
    	district:严格模式（默认，报错）
    	cascade:关联
    	set null:将关联的设置为null
    	no action:啥都不做
删除外键：
	alter table 表名 drop foreign key "外键名"
添加外键：
	alter table 表名 add [constraint 约束名] foreign key [外键名] (列名) references 主表（列名） on delete cascade on update cascade；
删除约束：
	alter table 表名 drop key 约束名；
修改外键：
	删除外键，再添加
```

# DML

> crud：

## 插入

### 单行插入：

```mysql
insert into 表名 (字段名) values (字段值1);
```

### 多行插入：

```mysql
insert into 表名 (字段名) values (字段值1),(字段值2)，...；
```

### 保障错误：不阻塞程序

```mysql
insert into 表名 (字段名) values (字段值1),(字段值2)，... on duplicate key update aaa.sid=aaa.sid+1[自定义干啥]；
```

### 具有select子句的insert

#### 快速复制/拷贝表结构：create table 表名 like 表名2

```mysql
insert into aaa select * from stu on duplicate key update aaa.sid=aaa.sid+1[自定义干啥];   =>   快速拷贝一个表
```

### 特殊：replace

> 删除以前的，在增加;碰到unique和主键

```mysql
replace into 表名 (字段名) values (字段值1);
```

## 更新

```mysql
update [low_priority] [ignore] 表名 set 字段1=字段值1，字段2=字段值2 where 条件
low_priority：意义： 查询完在更新
ignore :意义： 忽略；忽略键引发的冲突，
```

### 带有select子句的更新

> 从一个表中拿出一些信息放到另一个表

```mysql
update 表名 set attr1=(select 字段 from 表名 order by rand（） limit 1) where 条件（字段 is null）
```

### 关联更新

```mysql
方法一：
	update table1,table2 set table1.字段=值1，table2.字段=值1 where 条件
方法二：
	update t1 inner join t2 on t2.id = t1.tid SET t1.username=值1，t2.uname=值2， where 条件;
	update t1 inner join t2 SET t1.username=值1，t2.uname=值2， where 条件;
```

## 删除

### 简单

```mysql
delete from 表名 where 条件
```

### 排序删除

```mysql
delete from 表名 order by id desc limit 1
```

### 关联删除

```mysql
delete table1,table2 from table1,table2 where 条件
```

## 清空数据

```mysql
方式一：
	delete from 表； 速度慢；保留自增id
方式二：
	truncate [table] 表名;  效率快，不保留自增id
```

## 日志管理

> 日志文件对于一个服务器来说地非常重要的，他记录服务器的运行信息

### 日志种类

- 错误日志：记录启动，运行，或者停止时出现的问题
- 一般查询日志：记录建立的客户端连接和执行的语句
- 慢查询：记录所有执行时间超过一定值
- 二进制日志：引起数据库变化的操作
- 中继日志：从主服务其的二进制日志文件复制而来
- 事务日志:

### mysql全局变量的查询

```mysql
show global variables  [like '%log%']

修改：
set global 变量名=值
```

### 错误日志

#### 文件位置：show global variables  [like 'log_error']

#### 启用警告信息： show global variables  [like 'log_warnings']；1是开启；0是关闭

### 一般查询日志

#### 变量 : general_log=ON|OFF；状态一般是关闭状态

#### general_log_file:日志文件地址

#### log=ON|OFF：

#### log_output=table|file|none:日志的输出格式

### 慢查询日志

#### 查询超时时间：long_query_time；

#### 启动慢查日志：一般用：slow_query_log， [log_slow_queries=yes|no]  

#### 日志记录文件：slow_query_log_file[=文件名]

### 事务日志

> innodb_flush_log_at_trx_commit:
>
> 0：每秒同步，并执行磁盘刷新flush操作
>
> 1：每事务同步，并执行磁盘刷新flush操作
>
> 2：每事务同步，不执行磁盘刷新flush操作

### 二进制日志

> 不记录select、show语句那些不修改数据的SQL语句

#### 开启

> log_bin=二进制存储路劲，给值就开启
>
> 不能更改（静态文件）
>
> 改，在[mysqld]下增加 log_bin=mysql_bin_log，重启mysql（放在安装目录下【datadir】）
>
> %log_bin%

#### 查看

```mysql
show binary logs;
show master logs;
当前使用的二进制：
show master status;
```

#### 删除

> 没有命令单独删除二进制

```mysql
删除某个文件之前的二进制：
	purge binary logs to xxx
清除所有的二进制
	reset master
自动清理
	show variables like 'expire_logs_days'；默认0天（不删除）
	set expire_logs_days=7;单位是天
```



# DQL

## 查询语句

```mysql
select * from 表 where 条件 【inner/left/right join 表1 on 条件】 group by 列名 having 组 order by 列名 limit 开始，长度；【从0开始】
```

### select 字段  as 别名 from 表

### where 后的条件

> select * from 表 where 条件    =》 基本语法

### 运算符：

| 操作符       | 描述                     |
| ------------ | ------------------------ |
| =            | 等于                     |
| <>  或者 ！= | 不等于                   |
| <            | 小于，数字或者日期的比较 |
| >            | 大于                     |
| <=           | 小于等于                 |
| >=           | 大于等于                 |

### 逻辑运算符

| 操作符 | 描述 |
| ------ | ---- |
| or     | 或者 |
| and    | 并且 |
| not    | 非   |

### between：

```mysql
[not] between 条件1 and 条件2  ：=》包含等于

between cast（‘2013-01-01’ as date） and cast（‘2018-05-06’ as date）
cast（）：类型转换函数
```

### like：模糊查询

```mysql
select * from 表 where 字段 like '%条件%'

select * from 表 where 字段 like '%条$%件%' escape "$" :指定$作为转义字符
% ：任意字符长度
_ ：一个字符长度 
\ : 转义字符

查询user表中姓名中有“王”字的：
select * from user where name like '%王%'

mysql模糊查询not like的用法

查询user表中姓名中没有“王”字的：
select * from user where name not like '%王%'

查询user表中地址在上海姓名中没有“王”字和所有姓名为空的：
select * from user where adress =‘上海’ and name not like '%王%' or name is null

查询user表中地址在上海姓名中没有“王”字和地址在上海姓名为空的：
select * from user where adress =‘上海’ and (name not like '%王%' or name is null)

```

### in

> 适合分类

```mysql
select * from 表 where 字段  in("开始位置","结束位置")
```

### find_in_set()函数：不属于where的子句，但是可以连接在where后

> 第一个参数：要查找的字符串
>
> 第二个参数：字段名

### group by：分组,也可以使用聚合函数

> 在筛选的基础上进行分组

```mysql
select * from 表 where 条件 group by 字段1，字段2【分组条件】

例子:
	select fid,sum(nums) as nums from shop group by fid;
	select shop.sname,sum(list.lnum*shop.sper) as '总价' from shop,list where list.sid=shop.sid and list.ltime 
	in('2018-12-02','2018-12-03') group by list.ltime 
```

### having：对分组后的数据进行过滤，使用聚合函数

> select fid,sum(nums) as nums from shop group by fid having nums>100;  

```mysql
聚合函数：
	avg():计算一组值或者表达式的平均值
	count()：计算表中数量的函数
	instr()：返回子字符串中第一次出现的位置
	sum()：计算一组值的和
	min()：最小值
	max()：最大值
```

### order by：排序

> 按照表数据默认位置进行排序，默认升序
>
> 可以指定多列排序，后排序在前排序的基础上[   有相同值的项      ]进行排序
>
> 如果是汉字，则根据转换后的十六进制码排序；转换函数（hex（转换的内容））

```mysql
select 列名 from 表 order by 列 [ASC|DESC],列2 [ASC|DESC],...
```

#### 按照表达式排序

```mysql
select id,pre*num as tos from 表 order by tos
```

#### 自定义排序

```mysql
select * from 表 order by field(gname,"字段值1","字段值2","字段值3"，..)；
asc  默认在表后， desc 默认在表前
```

### limit：行数

```mysql
情况一：
    select * from 表 limit '偏移量，长度'
    偏移量：开始的位置
    长度：返回的最大行数
情况二：
	select * from 表 limit 数量
	要取前几条
select tname from 表 order by esc/desc/rand（）limit 1;


语句1：select * from student limit 9,4   // 语句1和2均返回表student的第10、11、12、13行 
语句2：slect * from student limit 4 offset 9   //语句2中的4表示返回4行，9表示从表的第十行开始
 

```

> limit和order by使用查询最大/最小值

### sql语句的执行顺序 

```mysql
(1)from 
(3) join 
(2) on 
(4) where 
(5)group by(开始使用select中的别名，后面的语句中都可以使用)
(6) avg,sum.... 
(7)having 
(8) select 
(9) distinct 
(10) order by 
```

### 查询时间

```mysql
--不带时分秒 :
	select current_date  
--带时分秒 :
	select sysdate()   或 SELECT NOW();
	date_format(logs.time,'%Y-%m-%d')  as time   :as  别名 
```

| `~   |      |      |      |      |      |
| ---- | ---- | ---- | ---- | ---- | ---- |
| QWR  |      |      |      |      |      |
|      |      |      |      |      |      |
|      |      |      |      |      |      |
|      |      |      |      |      |      |
|      |      |      |      |      |      |
|      |      |      |      |      |      |
|      |      |      |      |      |      |
|      |      |      |      |      |      |



## 关联查询

> 表与表之间有关系，通过关系去查询

```mysql
select * from 表1 [inner/left/right] join 表2 on 条件 where 条件

inner 交集       left:以左边为准         right 以右边为准       cross:交叉连接
```

### cross join交叉连接

> 乘积的方式【笛卡尔积】

```mysql
select ti.id,t2.id from t1 cross join t2 ；
一般不需要条件
```

### inner join:交集

```mysql
select cname,gname from 表 inner join goods on goods.cid=表.字段
```

### left join:以左边为准

```mysql
右边表没有对应的东西，则为Null，左边表全部查出来
```

### right join：以右边为准

```mysql
左边表没有对应的东西，则为Null，右表全部查出来
```

## 联合查询

> 把多个select语句查询的结果合并起来
>
> 列名为第一个查询语句的列名
>
> 默认自动去除重复项，all不会去重
>
> 也可以limit，order by，....

```mysql
select 列  from 表 union 【all】 select 列2 from 表
```

## 子查询

> slect

### 标量子查询：返回单一值的标量，最简单形式

```mysql
select * from 表 where uid=(select uid from 表 where 条件 order by uid desc limit 1)
子查询仅只能返回一个数据
```

### 列子查询：返回的结果集是N行1列

```mysql
select * from 表 where uid in (select uid from 表 where 条件)
子查询得到的一列
```

#### any/some[不常用some]：

> select * from goods where cid < any(2,3)
>
> < any(2,3)  ： <3的都可以查到
>
> 不大于/小于..其中的任何一数据【=，>,<,>=,<=,<>】

#### all：

> select * from goods where cid < all(2,3)
>
> 不大于/小于..其中的全部数据，最值

### 行子查询：返回的结果集是1行N列

> select * from 表 where (列名1，列名2，...)  in/=/.. （子查询语句）

### 表子查询：返回的结果集是N行N列

```css
select * from logs where phone in (select phone from stu where classid in (select id from classes where fid in (9))) 

select * from 表 where （字段1，字段2，字段3） in （select....）

判断条件是否存在：

select * from 表 where 条件1 and exists （子查询语句）
```

## 配合使用

## 常用的函数

### 聚合函数

#### count():统计数据总行数

> 不会忽略null

```mysql
select count(*) from 表名;
select count(*) from 表  group by 字段
```

#### avg()

> 会忽略null

```mysql
select avg(字段) from 表 
```

#### sum()

#### max()

#### GROUP_CONCAT()

```mysql
select group_concat(字段) from 表 order by
select cate.cid,cname,GROUP_CONCAT(step),GROUP_CONCAT(part) from biao1 join biao2 on 条件 group by cname
```

### 字符串函数

#### concat("1","2"): 

```mysql
select concat(first,last) from 表

```

#### concat_ws("连接符")

```mysql
select concat("-",字段1,字段2) from 表
```

#### left("字符串",长度):

> 返回指定长度的字符串的左边的部分

```mysql
select left()
```

#### replace(字符串,被替换的内容,替换的内容):

```mysql
update 表 set 字段=replace(字符串,被替换的内容,替换的内容)
```

#### substring(字符串,位置)/(字符串,开始位置,长度),开始位置为1 : 截取

```mysql
update 表 set 字段=substring(字符串,位置)/(字符串,开始位置,长度)
```

#### trim(both|leading|trailing) [去除的东西]  from "字符串")

```mysql
select trim("     sdfg    "):取出两边额空格
select trim( both/leading/trailing "去除的东西" from 字符串)
```

#### format():格式化

```mysql
format(数字,保留的位数,[locale(数字的表示方式)])
```

### 时间函数

#### 返回当前日期/时间

##### curdate() : 日期

##### now():带有时间(十分秒)[程序执行的那一课的时间]

##### sysdate(): 程序运行的时刻的时间

##### sleep():

#### 返回制定日期/时间函数

##### day(时间) :  几号

##### month(时间):  月

##### year(时间) :年

##### week(时间): 第几周

##### weekday(时间):星期几(0-6:1-7)

##### dayname(时间): 星期几(mondy/.....)

```mysql
set @@lc_time_name='zh_CN'
显示中国的时间星期一/...
```

#### 日期计算

##### datediff('日期1','日期2'): 差几天[时间1-时间2]

##### timediff("时间1","时间2"): 时间1-时间2

##### timestampdiff(相差单位,开始时间,结束时间)

```mysql
时间单位:
    microsecond:毫秒
    second:秒
    minute:分
    hour:小时
    day:天
    week:周
    month:月
    quarter:季度
    year:年
```

##### date_add(开始时间,interval 添加的时间数量 单位):

```mysql
 添加的时间数量 单位  =>   "1:1" "minute_second"
 添加的时间数量 单位  =>   "1"  单位
```

##### date_sub(开始时间,interval 减少的时间数量 单位):

## 视图

> 加快性能

```mysql
create view 视图名 as select sno,sname,sage,sdept from student;
create view bt_c(sno,sname,sbir) as select sno,sname,2017-sage from student;
```

### 插入数据里

```mysql
alter view 视图名

create or replace view 视图名 as...
```

### 删除视图

```mysql
drop [if exists]视图名
```

### show create view 视图名

### 查询视图

```mysql
select sno,sage from 试图名 where sage>20;
```

### 插入数据

```mysql
insert into is_student values('201216101','赵婷','20','is');
```

## 临时表

> 访问时在,不访问消失;
>
> 多表查询
>
> 生命周期:mysql开启--mysql关闭

### 创建临时表

> 看不见

```mysql
create temporary table 表名 select ...
```

## 触发器

### 创建

```mysql
create trigger delete_sm after delete on student for each row delete from sc where sno=old.sno;
```

### 删除数据

```mysql
delete from student where sno='201215122';
```

## 事务

> 事务是数据库处理操作，其中执行就好像它是一个单一的一组有序的工作单元，换言之在组内每个单独的操作是成功的，那么一个事务才是完整的。如果事务中的任何操作失败，整个事务将失败
>
> 一个完整的事务

### 事务性质

#### 原子性：

> 确保了工作单位中的所有操作都成功；否则，事务被终止，在失败时会被回滚到事务操作以前的状态

#### 一致性【目的】

> 可确保数据库在正确的更改状态在一个成功提交事务

#### 隔离

> 使事务相互独立地操作【谁先执行听谁的】

#### 持久性

> 确保了提交事务的结果或系统故障情况下仍然存在作用

### 事务控制语言

- BEGIN或START TRANSACTION：显式开启一个事务

  > begin;开始事务
  >
  > 事务操作
  >
  > commit;提交
  >
  > rollback;回滚

- set autocommit=0   禁止自动提交   ：执行操作暂存在内存中；commit；时在数据库中执行

- set autocommit=1  开启自动提交   ：

```python
try：
	执行的语句
execpt:
    出错
else：
	不出错的执行语句
```

### 事务支持的表类型

- 目前最流行的一种：innodb
- 

### 事务并发的问题

#### 脏读

> 如有事务A和B，A读取了B未提交的数据
>
> 事务A读取了事务B更新的数据，然后B回滚操作，那么A读取到的数据就是脏数据

#### 不可重复读

> 如有事务A和B，A负责读取，B负责写入，A连续读的过程中B写入了一次，A前后两次读出来的数据不一样
>
> 事务A多次读取统一数据，事务B在事务A多次读取的过程中。对数据做了更新，导致事务A多次读取到同一数据时，结果不一致

#### 丢失更新

> 如有事务A和B，AB均写入数据，A写入的数据被B覆盖

#### 幻读

> 如有事务A和B，A修改表内数据的过程中，B向表内插入了一条数据，A修改完后发现数据并没有被全部修改完

## 隔离

> 事务级别越高，数据安全行最高；可重复读> 串行化
>
> 由低到高依次为Read uncommitted(未授权读取、读未提交)、Read committed（授权读取、读提交）、Repeatable read（可重复读取）、Serializable（序列化），这四个级别可以逐个解决脏读、不可重复读、幻读这几类问题。

| 事务隔离级别               | 脏读 | 不可重复读 | 幻读 | 描述                                                         |
| -------------------------- | ---- | ---------- | ---- | ------------------------------------------------------------ |
| read uncommitted(读不提交) | 是   | 是         | 是   | 1）其他事务读未提交数据，出现脏读；
2）如果一个事务已经开始写数据，则另外一个事务则不允许同时进行写操作，但允许其他事务读此行数据。该隔离级别可以通过“排他写锁”实现。
3）避免了更新丢失，却可能出现脏读。也就是说事务B读取到了事务A未提交的数据。
（读未提交：一个事务写数据时，只允许其他事务对这行数据进行读，所以会出现脏读，事务T1读取T2未提交的数据） |
| read committed(不可重复读) |      | 是         | 是   | 1）允许写事务，所以会出现不可重复读
2）读取数据的事务允许其他事务继续访问该行数据，但是未提交的写事务将会禁止其他事务访问该行。
3）该隔离级别避免了脏读，但是却可能出现不可重复读。事务A事先读取了数据，事务B紧接了更新了数据，并提交了事务，而事务A再次读取该数据时，数据已经发生了改变。
（读已提交：读取数据的事务允许其他事务进行操作，避免了脏读，但是会出现不可重复读，事务T1读取数据，T2紧接着更新数据并提交数据，事务T1再次读取数据的时候，和第一次读的不一样。即虚读） |
| repeatable read(可重复读)  |      |            | 是   | 1）禁止写事务；
2）读取数据的事务将会禁止写事务（但允许读事务），写事务则禁止任何其他事务。
3）避免了不可重复读取和脏读，但是有时可能出现幻读。这可以通过“共享读锁”和“排他写锁”实现。
（可重复读：读事务会禁止所有的写事务，但是允许读事务，避免了不可重复读和脏读，但是会出现幻读，即第二次查询数据时会包含第一次查询中未出现的数据） |
| Serializable(串行化)       |      |            |      |                                                              |

### 查隔离级别

```mysql
select @@session.tx_isolation;
```

### 设置隔离级别

```mysql
set session transaction isolation level 分离级别
```

### 读未提交



#### repeatable read(可重复读)

> mvcc机制：多版本并发控制
>
> 每一行数据都有一个版本
>
> 新版本依据上一个版本计算
>
> 最终读取最后一个版本
>
>

## MySQL锁

> 锁是计算机协调多个进程或线程并发访问某一资源的机制

### 特点

> 显著特点是不同的存储引擎支持不同的锁机制

- #### 表级锁：开销小，加锁快；不会出现死锁；锁定粒度大，发生锁冲突的概率最高，并发度最低

- #### 行级锁：开销大，加锁慢；会出现死锁；锁定粒度小，发生锁冲突的概率最小，并发度最高

### 表级锁：

> 两种模式：表 共享锁【读锁】（级别） >     表 独占锁【排他锁/写锁】​	
>
> 表级锁的存储引擎：
>
> MyISAM：引擎
>
> MEMORY：引擎
>
> 不能访问别的表

#### 特点

- 作用范围：表级别
- 如果加了读锁，对MyISAM表的`读操作`，不会阻塞其他用户对同一表的读请求，但会阻塞对同一表的 `写` 请求
- 如果加了读锁，可以查询锁定表中的记录，但是更新或者访问其他表都会提示错误【对自己】
- 如果加了写锁，对MyISAM表的`写操作`，会阻塞其他用户对同一表的` 读 和 写` 请求
- 如果加了写锁，可以读取表中的记录，但是更新或者访问其他表都会提示错误，可以写表中的数据【加锁表】【对自己】

#### 如何加锁

> MyISAM在执行查询语句（select）前，会自动给涉及的所有表加读锁，在执行更新操作
>
> 在执行（update、delete、insert）前，会自动给表加写锁

##### 加锁

```mysql
lock table 表名 read [local],
Lock table 表名 write [local]

多表加锁：
lock table 表名1，表名2 read/write [local]
```

##### 解锁

```mysql
unlock tables;
```

#### 查看锁的情况

```mysql
show status like 'table%'

	table_locks_immediate:加锁次数
	table_locks_waited : 等待次数

show status like '%lock%'   # 看到的更全面

show processlist #此命令可以查看那些sql在等待锁 
show open tables #当前被锁住的表以及锁的次数

```

#### 并发插入：由读锁带来的问题解决办法

> 加锁带来的问题
>
> myisam有一个系统变量concurrent_insert，专门用以控制其并发插入的行为，其值分别对应为0，1，2

##### concurrent_insert=0，不允许并发插入【NEVER】

##### concurrent_insert=1，如果myisam没有空洞（即表的中间没有被删除的行），myisam允许在一个进程读表的同时，另一个进程从表尾插入记录，【默认设置】【AUTO】

##### concurrent_insert=2，无论有没有空洞，都在表尾插入【ALWAYS】

> 会产生碎片，用optimize table 表名；解决（优化）

####  读写锁优先级

> 默认情况下，写 >  读 

##### 设置写锁的最多次数

```mysql
设置：
	max_write_lock_count=次数
锁次数=次数值时，执行读操作
有了这样的设置，当系统处理一个写操作后，就会暂停写操作，给读操作执行的机会。
```

##### 降低写操作的优先级，给读操作更高的优先级

```mysql
low_priority_updates=1  降低写的优先级
sql_low_priority_updates=1 
默认值为0
写语句变更为：
update/insert/delete/...  low_priority
再用
```

#### 设置写内存

```mysql
max_allowed_packet=1M  #限制接受的数据包的大小，大的插入和更新会被限制掉，导致失败

net_buffer_length=2K-16M  #设置insert语句缓存值，多数据同时插入（），（），（）。。。

bulk_insert_buffer_size=8M  # 一次性insert语句插入的大小

```

#### 优化办法

- concurrent_insert=2
- 用`optimize table 表名`整理碎片
- 设置优先级
- 设置写内存/写的数量次数

#### 使用场景

```mysql
第一种情况是：事务需要更新大部分或全部数据，表又比较大，如果使用默认的行锁，不仅这个事务执行效率低，而且可能造成其他事务长时间锁等待和锁冲突，这种情况下可以考虑使用表锁来提高该事务的执行速度。

第二种情况是：事务涉及多个表，比较复杂，很可能引起死锁，造成大量事务回滚。这种情况也可以考虑一次性锁定事务涉及的表，从而避免死锁、减少数据库因事务回滚带来的开销。
```

### 行级锁/事务锁

> 行级锁模式
>
> 读锁/共享锁(S):允许一个事务去读一行，组织其他事务获得相同数据集的排他锁;
>
> ​	允许其他线程上读锁，但是不允许上写锁。
>
> 写锁/排他锁（X）：允许获得排他锁的事务更新数据，组织其他事务取得相同数据集的共享读锁和排他锁
>
> ​	不允许其他线程上任何锁。
>
> 意向共享锁（IS）：事务打算给数据行加行共享锁，事务在给一个数据行加锁前必须先取得该表的IS锁；为防止形成死锁
>
> 意向排他锁（IX）：事务打算给数据加行排他锁，事务在给一个数据行加排他锁前必须取得该表的IX锁；为防止形成死锁【不主张用】

| 兼容 |  X   |  IX  |  S   |  IS  |
| :--: | :--: | :--: | :--: | :--: |
|  X   |  ×   |  ×   |  ×   |  ×   |
|  IX  |  ×   | 兼容 |  ×   | 兼容 |
|  S   |  ×   |  ×   | 兼容 | 兼容 |
|  IS  |  ×   | 兼容 | 兼容 | 兼容 |

#### 如果一个事务请求的锁模式与当前锁兼容，InnoDB就将请求的锁授予该事务；

#### 反之。不兼容，该事务就要等待锁释放

#### 行级锁的存储引擎：InnoDB

#### 特点

- InnoDB行锁时通过给`索引上的索引项`加锁来实现的，只有通过索引条件检索数据，InnoDB才使用行级锁，否则，InnoDB将行锁升级为表锁  【操作的行必须有索引】
- 意向锁是InnoDB自动加的，不需要用户干预。
- 对于update、delete、insert，自动给涉及数据集加排他锁；对于普通的select【没有 `显示加锁`的情况】，不加任何锁
- 研究行锁时，需要将自动提交关闭，默认开启：set autocommit=0;
- 多个客户端都要设置 set autocommit=0;

#### select语句加行锁

```mysql
意向共享锁/读锁：select ***** lock in share mode
意向排他锁/写锁：select ***** for update
```

#### 释放锁

```mysql
commit
rollback
```

#### innodb注意事项

```mysql
当我们给某一条数据上了排他锁:
	其他人操作不了这条数据；想操作。排队，等其他人释放（commit；）

	其他人对这条数据没有任何权限，但是并不影响其他客户修改其他数据

	能查询，但是查不到最新的【隔离】

	即使字段加了索引，但是你在使用偷换了数据类型，那么索引失效，最终加上表锁【0   》   ‘0 ’】
```

#### 间隙锁

> 操作的数据的自增值中间有间隙的时候，将间隙（缺的部分）自动锁起来
>
> 也能锁住不存在的条件（一般为子增值）
>
> 锁住范围内的所有数据    =》   指定条件的时候给一个确定的范围
>
> 造成阻塞

#### 查询行级锁征用情况

```mysql
show status like 'innobd_row_lock%'
innobd_row_lock_waits   innobd_row_lock_time_
```

#### 优化行级锁

- 尽量用较低的隔离级别，精心设置索引，并尽量使用索引当问数据，使加锁更精确，从而减少锁冲突的机会
- 选择合理的事务大小，小事务发生锁冲突的几率也更小
- 给记录集显示【手动】加锁时，最好一次性请求足够级别的锁，比如要修改数据的话，最好直接申请排他锁，而不是先申请共享锁，修改时在申请排他锁，这样容易产生死锁
- 尽量用相等条件访问数据，可以避免间隙锁对并发插入的影响
- 对于特定的事务，可以使用`表锁`来提高处理速度或减少死锁的可能

# 主从复制

> 在实际生产环境中，单台mysql数据库是完全不能满足实际需求，无论安全，高可用性，高并发等各个方面的要求。mysql主从复制是满足这些要求的基础，主要用于实时备份，高可用，读写分离的场景

## 原理

- master服务器将数据的改变记录二进制日志，当master上的数据发生改变时，则将其改变写入二进制日志中。
- salve服务器会在一定时间间隔内对master二进制日志进行探测其是否发生改变，如果发生改变，则开始一个I/OThread请求master二进制事件
- 同时主节点为每个I/O线程启动一个dump线程，用于向其发送二进制事件，从节点保存至中继日志。
- 从节点将启动SQL线程从中继日志中读取二进制日志，在本地重放，使得其数据和主节点的保持一致。
- 最后I/OThread和SQLThread将进入睡眠状态，等待下一次被唤醒。

## 过程

### 基本要求

- 两台服务器
- 两台服务器版本一致（主节点低于从节点）
- 两台服务器防火墙关闭
- 双方数据库用户的用户，要具有远程访问的权限【参考远程】

### 主服务器

修改主服务器的mysql配置文件 （wind：my.ini,linux(my.cnf)），放在mysqld下面

```mysql
[mysqld]
有重复的选项，将设置的字段保证不会被覆盖
#mysql唯一id
server-id = 1
#二进制日志文件，此项为必填项，否则不能同步数据；
log-bin = "mysql-bin"
#指定二进制错误文件
log-error="mysql-error"
#需要同步的数据库，如果需要同步多个数据库；
binlog-do-db = 库名
#binlog-do-db = 库名
#binlog-do-db = 库名
#不需要同步的数据库
binlog-ignore-db = mysql
```

#### 给从数据库授权

##### 8.0版本以下

```mysql
GRANT REPLICATION SLAVE ON *.* to 'root'@'172.16.168.142' identified     by '123456';

```

##### 8.0版本

```mysql
CREATE USER 'root'@'192.168.43.152' IDENTIFIED WITH
mysql_native_password BY '123456';
GRANT REPLICATION SLAVE ON *.* TO 'root'@'192.168.43.152';
```

#### 最后几步

```mysql
#刷新权限
flush privileges；
#重启服务
service mysql restart;重启 （linux上： /etc/init.d/mysql restart）
#查询二进制信息
show master status 查询主服务器二进制信息
```

### 从服务器配置

```mysql	
[mysqld]
server-id=2    #默认是1改成2
log-bin="mysql-bin"    #这行本身有
replicate-do-db=uek_demo    #需要同步的数据库
replicate-ignore-db=mysql    #不同步系统数据库
read_only     #设只读权限，一般不写
```

#### 重启mysql服务

#### 执行同步sql语句

```mysql
[mysqld]
change master to
master_host='主机域名'
master_user='root'
master_password='密码'
master_log_first='主服务器的二进制地址'
master_log_pos='主服务器的pos'

#实例
change master to master_host='192.168.43.192',master_user='root',master_password='lz1022',master_log_file='mysql-bin.000008',master_log_pos=154;
```

### 开启同步

```mysql
start slave
```

### 判断是否成功

```mysql
show slave status\G;
i/o    sql值是否为yes
```

#### 没有表/库，手动创建***

> 其中Slave_IO_Running 与 Slave_SQL_Running 的值都必须为YES，才表明状态正常



# 优化数据库（概率优化）

> 数据库优化维度有四个: 硬件、系统配置、数据库表结构、SQL及索引 
>
> 优化成本: 硬件>系统配置>数据库表结构>SQL及索引 
>
> 优化效果: 硬件<系统配置<数据库表结构<SQL及索引

## MySQL组成模块

```mysql
1. Connectors
指的是不同语言中与SQL的交互的接口,包括python,php,nodejs,java

2. Management Serveices & Utilities
系统管理和控制工具,包括mysql的配置，权限，日志处理等

3. Connection Pool: 连接池
管理缓冲用户连接，线程处理等需要缓存的需求,。每一个连接上 MySQL Server 的客户端请求都会被分配（或创建）一个连接线程为其单独服务。而连接线程的主要工作就是负责 MySQL Server 与客户端的通信

4. SQL Interface: SQL接口
接受用户的SQL命令，并且返回用户需要查询的结果。比如select from就是调用SQL Interface

5. Parser: 解析器
SQL命令传递到解析器的时候会被解析器验证和解析,将SQL语句进行语义和语法的分析，分解成数据结构，然后按照不同的操作类型进行分类，然后做出针对性的转发到后续步骤,如果在分解构成中遇到错误，那么就说明这个sql语句是不合理的

6. Optimizer: 查询优化器
SQL语句在查询之前会使用查询优化器对查询进行优化。就是优化客户端请求的 query（sql语句） ，根据客户端请求的 query 语句，和数据库中的一些统计信息，在一系列算法的基础上进行分析，得出一个最优的策略，告诉后面的程序如何取得这个 query 语句的结果

7. Cache和Buffer： 查询缓存
他的主要功能是将客户端提交 给MySQL 的 Select 类 query 请求的返回结果集 cache 到内存中，在解析查询之前，要查询缓存，这个缓存只能保存查询信息以及结果数据。如果请求一个查询在缓存 中存在，就不需要解析，优化和执行查询了。直接返回缓存中所存放的这个查询的结果

8. 存储引擎接口
存储引擎接口模块可以说是 MySQL 数据库中最有特色的一点了。目前各种数据库产品中，基本上只有 MySQL 可以实现其底层数据存储引擎的插件式管理
```

## SQL语句编写流程

```mysql
SELECT DISTINCT
  < select_list >
FROM
  < left_table > < join_type >
JOIN < right_table > ON < join_condition >
WHERE
  < where_condition >
GROUP BY
  < group_by_list >
HAVING
  < having_condition >
ORDER BY
  < order_by_condition >
LIMIT < limit_number >
```

## SQL语句执行流程

```mysql
FROM <left_table>
ON <join_condition>
<join_type> JOIN <right_table>
WHERE <where_condition>
GROUP BY <group_by_list>
HAVING <having_condition>
SELECT
DISTINCT <select_list>
ORDER BY <order_by_condition>
LIMIT <limit_number>
```

## 案例代码

```mysql
# 信息表
create table if not exists info(
id int(10) auto_increment primary key,
con varchar(100) not null)default charset=utf8;

# 老师表
create table if not exists teach(
id int(10) auto_increment primary key,
tname varchar(20) not null,
iid int(10),
CONSTRAINT infoid foreign key (iid) REFERENCES info(id)
)default charset=utf8;

# 课程表
create table if not exists course(
id int(10) auto_increment primary key,
cname varchar(20) not null,
tid int(10),
CONSTRAINT teachid foreign key (tid) REFERENCES teach(id)
)default charset=utf8;
```

## explain字段内容详解

> 执行关键字顺序
>
> where  ->  group by   ->   having  ->   select   -> distint    -> order by  -> limit 

```mysql
+----+-------------+---------+------+---------------+------+---------+------+------+-------+
| id | select_type | table     | type | possible_keys | key  | key_len | ref  | rows | Extra |
+----+-------------+---------+------+---------------+------+---------+------+------+-------+
|  1 | SIMPLE      | uek_table | ALL  | NULL          | NULL | NULL    | NULL |    1 | NULL  |
+----+-------------+---------+------+---------------+------+---------+------+------+-------+
row in set (0.03 sec)
```

### 派生

>  select aa.cname from  (select cname,tid from course ) as aa
>
> ​							 派生表

### 1. id

> id是SQL执行的顺序的标识

- id相同时，执行顺序由上至下(由于表的数据量的大小决定执行顺序)
- 如果是子查询，id的序号会递增，id值越大优先级越高，越先被执行
- id如果相同，可以认为是一组，从上往下顺序执行；在所有组中，id值越大，优先级越高，越先执行

### 2. select_type

> 查询中每个select子句的类型

1. SIMPLE(简单SELECT,不使用UNION或子查询等)

2. PRIMARY(查询中若包含任何复杂的子部分,最外层的select被标记为PRIMARY)

3. UNION(UNION中的第二个或后面的SELECT语句)

4. DEPENDENT UNION(UNION中的第二个或后面的SELECT语句，取决于外面的查询)

5. UNION RESULT(UNION的结果)

6. SUBQUERY(子查询中的第一个SELECT)

7. DEPENDENT SUBQUERY(子查询中的第一个SELECT，取决于外面的查询)

8. DERIVED(派生表的SELECT, FROM子句的子查询)

   ```
   select form.cname from (select * from course where tid in (1,2)) as form
   ```

### 3. table

> 显示这一行的数据是关于哪张表的，看到的是derivedx的，说明这个结果是派生表的结果

### 4. type

> 表示MySQL在表中找到所需行的方式，又称“访问类型”,代表性能的优劣 常用的类型有： ALL<index<range<ref<eq_ref<const<system<NULL

- ALL：Full Table Scan， MySQL将遍历全表以找到匹配的行,并且查找的内容不带索引

- index: Full Index Scan，index与ALL区别为index类型只遍历索引树,也就是查找有索引的列

- range:只检索给定范围的行，查找的内容不带索引，选择的行带索引，可以用between,>,<,但是不要用in，用in索引失效

- ref: 表示上述表的连接匹配条件，即哪些列或常量被用于查找索引列上的值，使用普通索引

- eq_ref: 类似ref，区别就在使用的索引是唯一引，对于每个索引键值，表中只有一条记录匹配，简单来说，就是多表连接中使用primary key或者 unique key作为关联条件

- const、system: 当MySQL对查询某部分进行优化，并转换为一个常量时，使用这些类型访问。如将主键置于where列表中，MySQL就能将该查询转换为一个常量。

- system: 在衍生/派生查询中只有一条数据

- null：

  ```
  select form.cname from (select cname from course where id=1) as form
  ```

### 5. possible_keys

> MySQL预测使用哪个索引在表中查找记录，如果是NULL说明MySQL找不到要使用的索引

### 6. Key

> key列显示MySQL实际决定使用的键（索引），如果键是NULL，说明该语句性能堪忧，根据实际使用场景要添加索引，经常用来判断复合索引是否完整使用

### 7. key_len

> 表示索引中使用的字节数，可通过该列计算查询中使用的索引的长度，不损失精确性的情况下，长度越短越好,尤其是使用InnoDB引擎

### 8. ref

> 表示上述表的连接匹配条件，即哪些列或常量被用于查找索引列上的值，如果是 const的话说明效率较高

```
​```
select cname from course where id=1
​```
```

### 9. rows

> 表示MySQL根据表统计信息及索引选用情况，估算的找到所需的记录所需要读取的行数

### 10. Extra

> 该列包含MySQL解决查询的详细信息,有以下几种情况：

- Using index:指定索引的索引全部覆盖，代表性能不错

- Using where:代表语句性能一般，仅仅从where指定的索引不能找到全部信息，需要回表查询

- Using temporary：表示MySQL需要使用临时表来存储结果集，常见于排序和分组查询，说明在查询中需要用临时表存储，性能消耗较大，常见于在一个没有索引的表中进行运算

  ```
    explain select distinct name from abc;
  ```

- Using filesort：MySQL进行了多次排序，没有利用索引进行排序，说明性能很低

  ```
    创建一个复合索引的表
    create table demo(
    id int(10) auto_increment primary key,
    one varchar(100),
    two varchar(100),
    three varchar(100),
    index one (one),
    index two (two),
    index three (three)
    )
  
    创建sql语句
    select * from demo where one="" order by one
    select * from demo where one="" order by two
  ```

  **1. 对于单索引查找，排序不是同一个索引会出现重新排序。2.对于复合索引要遵循最佳左前缀，不要跨列**

- Using join buffer：改值强调了在获取连接条件时没有使用索引，并且需要连接缓冲区来存储中间结果。如果出现了这个值，那应该注意，说明你的sql语句写的太差了，需要mysql给你进行优化了，常见多表关联。

- Impossible where：这个值强调了where语句会导致没有符合条件的行。

  ```
    select * from demo where id=1 and id=2;
  ```

## 优化方法

> 工具： explain + sql:测试sql语句的快慢等信息
>
> ​	    开启慢查询（位置：安装目录下的）

### 1.开启慢查询

### 2. 索引优化

> 索引是我们提升sql查询效率的重要手段，同时索引的使用不当也会带来性能的问题，在使用索引的时候，应该注意一下问题

1. 不能将索引用作表达式的一部分，也不能是函数的参数

   ```
     select * from demo where id+1=2
   
     select max(id) from demo where id=1;
   ```

2. 索引不要进行类型转化，否则索引失效

   ```
     select * from demo where name=2
     # 如果name是字符串类型，就存在类型转换
   ```

3. 复合索引应该遵循左前缀策略，不要交叉使用

   ```
     alter table table_name add index a_b_c (a,b,c)
   
     select c from table_name where id=a order by b
   ```

4. 复合索引如果用"or"关键字，索引失效

   ```
     select * from table_name where a="" or b=""
   ```

5. 复合索引不要使用 != <> 或 is null (is not null)

   ```
     select * from table_name where a!=""
   ```

6. 尽量不要和in在一起使用，导致索引失效

   ```
     select * from table_name where id in ("","")
   ```

7. 及时删除冗余的和长期不使用的索引

8. like 查询时候尽量不要出现左 "%",否则索引失效，如果非得使用，请用索引覆盖提高性能,要使用独立索引，不要使用复合索引

   ```
     select * from table_name where con like "%内容%"
   ```

### 3. 单、多表SQL优化手段

1. 单表案例

   > 有一个表用来记录书籍的名字(bookname)，出版号(publicid)，作者(authorid)，类型(typeid)。 然后查询其中两种类型并且属于同一个作者，然后按照出版号来进行排序

   ```
     create table book(
     id int(10) auto_increment primary key,
     bookname varchar(100) not null,
     authorid varchar(20) not null,
     publicid int(10) default 11111,
     typeid int(10)) default charset=utf8;
     select * from book where typeid in(1,2) and authorid=1 order by publicid;
   ```

   - 加索引(并且加在频繁使用的字段上)
   - 调整索引顺序(遵循最佳左前缀)
   - 删除多于(干扰)索引
   - 调整查询条件，对索引有干扰的语句放到条件的最后

2. 多表案例

   > 有一个试题类型表(testtype)记录了试题的类型，字段包含 tid ,试题类型名称 (name) 有一个试题内容表(testcon)记录了试题的题目(title)，选项(opts)，答案(result)和类型(tid)

   ```
     # 类型表
     create table testtype(
     tid int(5) auto_increment primary key,
     name varchar(100))default charset=utf8;
     # 内容表
     create table testcon(
     id int(5) auto_increment primary key,
     title varchar(100) not null,
     opts varchar(200) not null,
     result varchar(100) not null,
     tid int(5),
     CONSTRAINT testid foreign key (tid) REFERENCES testtype(tid))default charset=utf8;
   ```

   - 多表索引添加原则，小表驱动大表(小表在左边 where 小表.x=大表.y)
   - left join 给左表加索引，right join 给右边加索引

### 4. 表级别锁优化(查阅锁章节)

### 5. 系统级别优化

1. 主从复制
2. 读写分离
3. 负载均衡

### 6. 其他优化总结

1. 通常来说把可为NULL的列改为NOT NULL不会对性能提升有多少帮助，只是如果计划在列上创建索引，就应该将该列设置为NOT NULL
2. 对于数据类型，一定要根据业务需求选择尽可能小的存储数据类型
3. UNSIGNED表示不允许负值，大致可以使正数的上限提高一倍，如果表示的是正数，那么要用非符号
4. 通常来讲，没有太大的必要使用DECIMAL数据类型。即使是在需要存储财务数据时，仍然可以使用BIGINT。
5. TIMESTAMP使用4个字节存储空间，DATETIME使用8个字节存储空间
6. 大多数情况下没有使用枚举类型的必要
7. 表的列不要太多，如果列太多而实际使用的列又很少的话，有可能会导致CPU占用过高 **选择数据类型只要遵循小而简单的原则就好，越小的数据类型通常会更快，占用更少的磁盘、内存，处理时需要的CPU周期也更少**