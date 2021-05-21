# 运行shell的方式

1. 作为可执行程序=>将代码保存为xx.sh，cd到对应目录：

   ```linux
   chmod +x ./xx.sh  #使脚本具有执行权限
   ./xx.sh  # 执行脚本
   ```

2. 作为解释器参数 => 运行解释器，参数是shell脚本文件

   ```python
   /bin/sh xx.sh
   /bin/php xx.php
   ```

# shell变量

## 定义变量

1. 定义变量时，变量名不加美元符($,php语言需要)

   `your_name='ygx'`

2. 变量名和等号之间**不能有空格**

3. 命名只能使用英文字母、数字、下划线；首个字符不能以数字开头

4. 不能不能有空格，可以使用下划线（_）连接

5. 不能使用标点符号

6. 不能使用bash里的关键字（可以用help命令查看保留关键字）

## 变量赋值

1. `变量名=变量值`

2. 语句

   ```shell
   for file in 'ls /etc'
   或者
   for file in $(ls /etc)
   ```

3. 重复赋值

   ```shell
   your='tom'
   echo $your
   your='si'
   echo $your
   ```

## 使用变量

1. $变量名

2. ${变量名}

   > 花括号是可选的，目的是为了帮助解释器识别变量的边界

   ```shell
   for shill in A B C;do
   	echo "I am good at ${skill} Script"
   done
   # 是双引号，而不是单引号，单引号表示仅仅是字符串
   ```

## 只读变量

> 用readonly声明

```shell
myurl='39.96.201.103'
readonly muurl
如果执行：myurl='39.96.201.103:5000'
报错：This variable is read only.
```

## 删除变量

> **unset** 关键字
>
> 变量被删除后不能在使用；
>
> unset不能删除只读变量

```shell
aaa=123
unset aaa
```

## 变量类型

### 作用域

1. 局部变量

   在脚本或者命令中定义，**仅在当前shell实例中有效，其他shell脚本不能访问到**

2. 环境变量

   所有的程序，包括shell启动程序，都能访问环境变量；有些程序需要环境变量来保证其正常运行。必要时shell脚本也可以定义环境变量

3. shell变量

   shell变量是由shell程序设置的特殊变量；

   包含环境变量和局部变量，这些变量保证了shell的正常运行

### 类型

#### 字符串

> 字符串可以用单引号，也可以用双引号，也可以不用引号

##### 单引号定义

```shell
str1='this is string'
```

* 单引号里的任何字符都会原样输出，单引号字符串中的变量是无效的
* 单引号字符串不能出现单独一个的单引号(对单引号使用转义字符后也不行),但是可以成都一出现，作为字符串拼接使用

##### 双引号定义

```powershell
name="ygx"
str="hello, my name is \"${name}\""."
echo -e ${str}
```

* 双引号里可以有变量
* 双引号里可以出现转义字符

##### 字符串拼接

1. 双引号拼接

   ```shell
   name='ygx'
   myname="hello, "${name}" !"
   myname1="hello, ${name}!"
   echo $myname $myname1  =>效果一样
   ```

2. 单引号拼接

   ```shell
   name='ygx'
   myname='hello, '${name}' !'
   echo $myname
   ```

##### 获取字符串长度

```shell
name='ygx'
echo ${#name}  #输出3
```

##### 提取子字符串

```shell
myname='YangGuoXuan'
echo ${myname:1:4}  => 从第二个开始截取4个字符
```

##### 查找子字符串

```shell
myname='YangGuoXuan'
echo `expr index "${myname}" an`
# 查找字符a或者n的位置（那个字母先出现就计算那个）
```

#### 数组

> 支持一维数组，不支持多维数组

##### 定义

```shell
数组名=(值0 值1 ... 值n-1)
# 数组元素用 空格 分隔开

#或者
数组名=(
值0
值1
...
值n-1
)

# 或者
数组名[0]=值0
数组名[1]=值1
...
可以不使用连续的下标；而且下标的范围没有限制
```

##### 读取数组元素

```shell
${数组名[下标]}
${数组名[@]} #获取所有元素
```

##### 获取数组长度

```shell
${#数组名[@]}  #获取数组长度
${#数组名[*]}  #获取数组长度
${#数组名[n]}  #获取数组单个元素的长度
```

# 运算符

## 算术运算符

> **expr是一款表达式计算工具，使用它能够完成表达式的求值操作**
>
> 在 MAC 中 shell 的 expr 语法是：**$((表达式))**，此处表达式中的 "*" 不需要转义符号 "\" 。

```shell
add=`expr 2 + 2`
# + 号前后要有空格
```

| 运算符 | 说明               | 举例            |
| ------ | ------------------ | --------------- |
| +      | 加                 | `expr $a + $b`  |
| -      | 减                 | `expr $a - $b`  |
| *      | 乘                 | `expr $a \* $b` |
| /      | 除                 | `expr $a / $b`  |
| %      | 取余               | `expr $a % $b`  |
| =      | 赋值               | a=$b            |
| ==     | 等于，true/false   | [ $a == $b ]    |
| !=     | 不等于，true/false | [ $a != $b ]    |

**条件表达式要放在方括号之间，并且要有空格，例如: [$a==$b] 是错误的，必须写成 **[ $a == $b ]。

## 关系运算符

> 关系运算符只支持数字，不支持字符串，除非字符串是数字
>
> 返回true/false

| 运算符 | 说明               | 举例          |
| ------ | ------------------ | ------------- |
| -eq    | 检测两个数是否相等 | [ $a -eq $b ] |
| -ne    | 检测两个数是否不能 | [ $a -ne $b ] |
| -gt    | 大于               | [ $a -gt $b ] |
| -lt    | 小于               | [ $a -lt $b ] |
| -ge    | 大于等于           | [ $a -ge $b ] |
| -le    | 小于等于           | [ $a -le $b ] |



## 布尔运算符

| 运算符 | 说明 | 举例        |
| ------ | ---- | ----------- |
| !      | 非   | [ ! false ] |
| -o     | 或   | [ a -o b ]  |
| -a     | 与   | [ a -a b ]  |



## 逻辑运算符

| 运算符 | 说明    | 举例           |
| ------ | ------- | -------------- |
| &&     | 逻辑and | [[ a && b ]]   |
| \|\|   | 逻辑 or | [[ a \|\| b ]] |



## 字符串运算符

| 运算符 | 说明                    | 举例         |
| ------ | ----------------------- | ------------ |
| =      | 检测两个字符串是否相等  | [ $a = $b ]  |
| !=     | 检测两个字符串是否不等  | [ $a != $b ] |
| -z     | 检测字符串长度是否为0   | [ -z $b ]    |
| -n     | 检测字符串长度是否不为0 | [ -n "$a"]   |
| $      | 检测字符串是否不为空    | [ $a ]       |



## 文件测试运算符

> 文件测试运算符用于检测 Unix 文件的各种属性

| 操作符  | 说明                                                         | 举例                      |
| :------ | :----------------------------------------------------------- | :------------------------ |
| -b file | 检测文件是否是块设备文件，如果是，则返回 true。              | [ -b $file ] 返回 false。 |
| -c file | 检测文件是否是字符设备文件，如果是，则返回 true。            | [ -c $file ] 返回 false。 |
| -d file | 检测文件是否是目录，如果是，则返回 true。                    | [ -d $file ] 返回 false。 |
| -f file | 检测文件是否是普通文件（既不是目录，也不是设备文件），如果是，则返回 true。 | [ -f $file ] 返回 true。  |
| -g file | 检测文件是否设置了 SGID 位，如果是，则返回 true。            | [ -g $file ] 返回 false。 |
| -k file | 检测文件是否设置了粘着位(Sticky Bit)，如果是，则返回 true。  | [ -k $file ] 返回 false。 |
| -p file | 检测文件是否是有名管道，如果是，则返回 true。                | [ -p $file ] 返回 false。 |
| -u file | 检测文件是否设置了 SUID 位，如果是，则返回 true。            | [ -u $file ] 返回 false。 |
| -r file | 检测文件是否可读，如果是，则返回 true。                      | [ -r $file ] 返回 true。  |
| -w file | 检测文件是否可写，如果是，则返回 true。                      | [ -w $file ] 返回 true。  |
| -x file | 检测文件是否可执行，如果是，则返回 true。                    | [ -x $file ] 返回 true。  |
| -s file | 检测文件是否为空（文件大小是否大于0），不为空返回 true。     | [ -s $file ] 返回 true。  |
| -e file | 检测文件（包括目录）是否存在，如果是，则返回 true。          | [ -e $file ] 返回 true。  |

# 注释

## 单行注释

> 以`#`开头的每一行都是注释，会被解释器忽略

## 多行注释

```shell
:<< EOF
注释内容..
注释内容..
注释内容..
EOF
```

```shell
:<<'
注释内容..
注释内容..
注释内容..
'
```

```shell
:<<!
注释内容..
注释内容..
注释内容..
!
```

# shell参数传递

> 脚本内获取参数的格式为：**$n**。**n** 代表一个数字，1 为执行脚本的第一个参数，2 为执行脚本的第二个参数，以此类推……

```shell
echo "执行的文件名：$0"
echo "第一个参数：$1"
echo "第二个参数：$2"
echo "第三个参数：$3"
```

```shell
./sh.sh 1 2 3
执行的文件名：./sh.sh
第一个参数：1
第二个参数：2
第三个参数：3
```

## 特殊字符

| 参数处理 | 说明                                                         | 运用                                |
| -------- | ------------------------------------------------------------ | ----------------------------------- |
| $#       | 传递到脚本的参数个数                                         | "参数个数为：$#";                   |
| $*       | 以一个单字符串显示所有向脚本传递的参数；如果'$*'用「"」括起来，以“$1 $2 ...$n”的形式输出所有参数 | "传递的参数作为一个字符串显示：$*"; |
| $$       | 脚本运行的当前进程id号                                       |                                     |
| $!       | 后台运行的最后一个进程的id号                                 |                                     |
| $@       | 与$*相同，但是使用时加引号，并在引号中返回每个参数。<br/>如"$@"用「"」括起来的情况、以"$1" "$2" … "$n" 的形式输出所有参数 |                                     |
| $-       | 显示shell使用的当前选项                                      |                                     |
| $?       | 显示最后命令的退出状态，0表示没有错误，其他任何值表明有错误  |                                     |

## $*与$@的区别

1. 都是引用所有参数
2. 不同点：
   * 在双引号中体现出来
   * 在本运行时谢了三个参数1 2 3；
   * $*  => “1 2 3”
   * $@ => "1" "2" "3"

```shell
for i in "$*"; do
    echo $i   => 1 2 3
done

echo "-- \$@ 演示 ---"
for i in "$@"; do
    echo $i    => 1 \n 2 \n 3
done
```

# echo命令

> 输出
>
> echo 字符串

## 1. 显示普通字符串

```shell
echo "my name is ygx"
echo my name is ygx
```

## 2. 显示转义字符

```shell
echo "\" my name is ygx \""
```

## 3. 显示变量

> read 从标准输入中读取一行，并把内容给到变量

```shell
read name
echo "my name is ${name}"
```

## 4. 换行显示

```shell
echo -e "ok! \n"
echo "my name is ygx"
```

## 5. 显示不换行

```shell
echo -e "ok! \c"
echo "my name is ygx"
```

## 6. 显示结果定向至文件

```shell
echo "my name is ygx !" > 文件
```

## 7. 原样输出字符串(单引号)

```shell
echo '${name}\"'
```

## 8. 显示命令执行结果

```shell
echo `date`
```

# printf

> 由于POSIX标准所定义，因此使用printf的脚本比使用echo移植性好
>
> **使用引用文本或空格分割参数，外边可以再print中使用格式化字符串，还可以制定字符串的宽度、左右对齐方式等**
>
> 默认不换行

```shell
printf format-string [arguments...]
format-string:格式控制字符串
arguments：参数列表
```

## 格式化输出

* %s %c %d %f都是格式替代符
  * **d: Decimal 十进制整数** -- 对应位置参数必须是十进制整数，否则报错！
  * **s: String 字符串** -- 对应位置参数必须是字符串或者字符型，否则报错！
  * **c: Char 字符** -- 对应位置参数必须是字符串或者字符型，否则报错
  * **f: Float 浮点** -- 对应位置参数必须是数字型，否则报错！
* %-10s 指一个宽度为10个字符（-表示左对齐，没有则表示右对齐），任何字符都会被显示在10个字符宽的字符内，如果不足则自动以空格填充，超过也会将内容全部显示出来
* %-4.2f 指格式化为小数，其中.2指保留2位小数。

```shell
printf "%-10s %-8s %-4s\n" 姓名 性别 体重kg  
printf "%-10s %-8s %-4.2f\n" 郭靖 男 66.1234 
printf "%-10s %-8s %-4.2f\n" 杨过 男 48.6543 
printf "%-10s %-8s %-4.2f\n" 郭芙 女 47.9876

姓名     性别   体重kg
郭靖     男      66.12
杨过     男      48.65
郭芙     女      47.99

```

## 单引号、双引号效果一样

```shell
# format-string为双引号
printf "%d %s\n" 1 "abc"

# 单引号与双引号效果一样 
printf '%d %s\n' 1 "abc" 
```

## 没有引号也可以

```shell
printf %s abcdef
```

## 指定一个参数

> 格式只指定了一个参数，但多出的参数仍然会按照该格式输出，format-string 被重用

```shell
printf %s abc def

printf "%s\n" abc def

printf "%s %s %s\n" a b c d e f g h i j
```

## 没有 arguments

> 如果没有 arguments，那么 %s 用NULL代替，%d 用 0 代替

```
printf "%s and %d \n"
```

## printf的转义

| 序列  | 说明                                                         |
| :---- | :----------------------------------------------------------- |
| \a    | 警告字符，通常为ASCII的BEL字符                               |
| \b    | 后退                                                         |
| \c    | 抑制（不显示）输出结果中任何结尾的换行字符（只在%b格式指示符控制下的参数字符串中有效），而且，任何留在参数里的字符、任何接下来的参数以及任何留在格式字符串中的字符，都被忽略 |
| \f    | 换页（formfeed）                                             |
| \n    | 换行                                                         |
| \r    | 回车（Carriage return）                                      |
| \t    | 水平制表符                                                   |
| \v    | 垂直制表符                                                   |
| \\    | 一个字面上的反斜杠字符                                       |
| \ddd  | 表示1到3位数八进制值的字符。仅在格式字符串中有效             |
| \0ddd | 表示1到3位的八进制值字符                                     |

# test测试

> test命令 用于检查某个条件是否成立，他可以进行数值、字符、文件三个方面的测试

## 数值测试

| 参数 | 说明           |
| :--- | :------------- |
| -eq  | 等于则为真     |
| -ne  | 不等于则为真   |
| -gt  | 大于则为真     |
| -ge  | 大于等于则为真 |
| -lt  | 小于则为真     |
| -le  | 小于等于则为真 |

```shell
num1=100
num2=100
if test $[num1 + 1] -eq $[num2+ 1]
then
	echo '相等'
else
	echo '不等'
fi
=>相等
```

**[]中执行算术运算**

## 字符串测试

| 参数      | 说明                     |
| :-------- | :----------------------- |
| =         | 等于则为真               |
| !=        | 不相等则为真             |
| -z 字符串 | 字符串的长度为零则为真   |
| -n 字符串 | 字符串的长度不为零则为真 |

```shell
num1="ygx1"
num2="ygx2"
if test $num1 = $num2
then
    echo '两个字符串相等!'
else
    echo '两个字符串不相等!'
fi
=》两个字符串不相等!
```

## 文件测试

| 参数      | 说明                                 |
| :-------- | :----------------------------------- |
| -e 文件名 | 如果文件存在则为真                   |
| -r 文件名 | 如果文件存在且可读则为真             |
| -w 文件名 | 如果文件存在且可写则为真             |
| -x 文件名 | 如果文件存在且可执行则为真           |
| -s 文件名 | 如果文件存在且至少有一个字符则为真   |
| -d 文件名 | 如果文件存在且为目录则为真           |
| -f 文件名 | 如果文件存在且为普通文件则为真       |
| -c 文件名 | 如果文件存在且为字符型特殊文件则为真 |
| -b 文件名 | 如果文件存在且为块特殊文件则为真     |

```shell
cd /bin
if test -e ./bash
then
    echo '文件已存在!'
else
    echo '文件不存在!'
fi
```

### 与或非（-a -o !）

**另外，Shell还提供了与( -a )、或( -o )、非( ! )三个逻辑操作符用于将测试条件连接起来，其优先级为："!"最高，"-a"次之，"-o"最低。**

```shell
cd /bin
if test -e ./notFile -o -e ./bash
then
    echo '至少有一个文件存在!'
else
    echo '两个文件都不存在'
fi
```

# 流程控制

> sh的流程控制不可为空， 即 不执行任何操作就不写

## if

```shell
if 条件
then
    结果.. 
fi
```

```shell
if [ $(ps -ef | grep -c "ssh") -gt 1 ]; then echo "true"; fi
```

## if ... else

```shell
if 条件
then
    结果..
else
    结果...
fi
```

## if ... else-if ... else

```shell
if 条件1
then
    结果1
elif 条件2 
then 
    结果2
else
    结果...
fi
```

## for

```shel
for var in item1 item2 ... itemN
do
    var的相关操作
done
```

```shell
for var in item1 item2 ... itemN; do command1; command2… done;
```

1. ```shell
   for loop in 1 2 3 4 5
   do
       echo "The value is: $loop"
   done
   ```

2. ```shell
   aa=(1 2 3 4 5)
   for i in ${aa[@]}
   do
       echo "The value is: $i"
   done
   ```

3. ```shell
   aa=(1 2 3 4 5)
   for i in ${aa[*]}
   do
       echo "The value is: $i"
   done
   ```

4. ```shell
   for str in 'This is a string'
   do
       echo $str
   done
   =》  This is a string
   ```

## while

```shell
while condition
do
    command
done
```

```shell
int=1
while(( $int<=5 ))
do
    echo $int
    let "int++"
done
# let 命令，它用于执行一个或多个表达式，变量计算中不需要加上 $ 来表示变量，
```

读取键盘信息

```shell
echo '按下 <CTRL-D> 退出'
echo -n '输入你最喜欢的网站名: '
while read FILM
do
    echo "是的！$FILM 是一个好网站"
done
# 可以无限读取下去
```

## 无限循环

1. ```shell
   while :
   do
       command
   done
   ```

2. ```shell
   while true
   do
       command
   done
   ```

3. ```shell
   for (( ; ; ))
   ```

## until循环

> until 循环执行一系列命令直至条件为 true 时停止。
>
> until 循环与 while 循环在处理方式上刚好相反。
>
> 一般 while 循环优于 until 循环，但在某些时候—也只是极少数情况下，until 循环更加有用。

```shell
until 条件
do
    command
done
```



```shell
a=0
until [ ! $a -lt 10 ]
do
   echo $a
   a=`expr $a + 1`
done
```

## case多语句

```shell
case 值 in
模式1)
    command1
    command2
    ...
    commandN
    ;;
模式2）
    command1
    command2
    ...
    commandN
    ;;
esac
```

```shell
echo '输入 1 到 4 之间的数字:'
echo '你输入的数字为:'
read aNum
case $aNum in
    1)  echo '你选择了 1'
    ;;
    2)  echo '你选择了 2'
    ;;
    3)  echo '你选择了 3'
    ;;
    4)  echo '你选择了 4'
    ;;
    *)  echo '你没有输入 1 到 4 之间的数字'
    ;;
esac
```

## break

> break命令允许跳出所有循环（终止执行后面的所有循环）

```shell
while :
do
    echo -n "输入 1 到 5 之间的数字:"
    read aNum
    case $aNum in
        1|2|3|4|5) echo "你输入的数字为 $aNum!"
        ;;
        *) echo "你输入的数字不是 1 到 5 之间的! 游戏结束"
            break
        ;;
    esac
done

```

## continue

> 仅仅跳出当前循环

```shell
while :
do
    echo -n "输入 1 到 5 之间的数字: "
    read aNum
    case $aNum in
        1|2|3|4|5) echo "你输入的数字为 $aNum!"
        ;;
        *) echo "你输入的数字不是 1 到 5 之间的!"
            continue
            echo "游戏结束"
        ;;
    esac
done
```

# 函数

```shell
[ function ] funname [()]
{
    action;
    [return int;]
}
[]为可选项
# 参数返回，可以显示加：return 返回，如果不加，将以最后一条命令运行结果，作为返回值。 return后跟数值n(0-255)
```

```shell
funWithReturn(){
    echo "这个函数会对输入的两个数字进行相加运算..."
    echo "输入第一个数字: "
    read aNum
    echo "输入第二个数字: "
    read anotherNum
    echo "两个数字分别为 $aNum 和 $anotherNum !"
    return $(($aNum+$anotherNum))
}
funWithReturn
echo "输入的两个数字之和为 $? !"
```

## 参数

```shell
funWithParam(){
    echo "第一个参数为 $1 !"
    echo "第二个参数为 $2 !"
    echo "第十个参数为 $10 !"    # =>10
    echo "第十个参数为 ${10} !"  # =>34
    echo "第十一个参数为 ${11} !"
    echo "参数总数有 $# 个!"
    echo "作为一个字符串输出所有参数 $* !"
}
funWithParam 1 2 3 4 5 6 7 8 9 34 73
#$10 不能获取第十个参数，获取第十个参数需要${10}。当n>=10时，需要使用${n}来获取参数
```

## 特殊参数

| 参数处理 | 说明                                                         |
| :------- | :----------------------------------------------------------- |
| $#       | 传递到脚本的参数个数                                         |
| $*       | 以一个单字符串显示所有向脚本传递的参数                       |
| $$       | 脚本运行的当前进程ID号                                       |
| $!       | 后台运行的最后一个进程的ID号                                 |
| $@       | 与$*相同，但是使用时加引号，并在引号中返回每个参数。         |
| $-       | 显示Shell使用的当前选项，与set命令功能相同。                 |
| $?       | 显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。 |

# 写入/写出

| 命令            | 说明                                               |
| :-------------- | :------------------------------------------------- |
| command > file  | 将输出重定向到 file。                              |
| command < file  | 将输入重定向到 file。                              |
| command >> file | 将输出以追加的方式重定向到 file。                  |
| n > file        | 将文件描述符为 n 的文件重定向到 file。             |
| n >> file       | 将文件描述符为 n 的文件以追加的方式重定向到 file。 |
| n >& m          | 将输出文件 m 和 n 合并。                           |
| n <& m          | 将输入文件 m 和 n 合并。                           |
| << tag          | 将开始标记 tag 和结束标记 tag 之间的内容作为输入。 |

**需要注意的是文件描述符 0 通常是标准输入（STDIN），1 是标准输出（STDOUT），2 是标准错误输出（STDERR）。**

## 输出重定向

```shell
command1 > file1
# who > users
# 这个命令执行command1然后将输出的内容存入file1。
# 没有文件就会创建文件
# 会覆盖文件内容
# 不希望覆盖，写 >>   
# echo "菜鸟教程：www.runoob.com" >> users
```

## 输入重定向

```shell
command1 < file1

```

```shell
wc -l users  #2 users
```

```shell
wc -l < users  #2
```

## command1 < infile > outfile

> 同时替换输入和输出，执行command1，从文件infile读取内容，然后将输出写入到outfile中。

## 重定向

一般情况下，每个Linux命令运行时都会打开三个文件：

* 标准输入文件(stdin):stdin的文件描述符为 0 ，程序默认从stdin读取数据
* 标准输出文件(stdout):stdout的文件描述符为 1 ，程序默认项stdout输出数据
* 标准错误文件(stderr):stderr的文件描述符为 2 ，程序默认向stderr流中写入错误信息

### stderr重定向到file

```shell
command 2 > file
# 追加
command 2 >> file
```

### stdout和stderr合并后重定向到file

```shell
command > file 2>&1
# 追加
command >> file 2>&1
```

### 对stdin和stdout都重定向

```shell
command < file1 > file2
# command 命令将 stdin 重定向到 file1，将 stdout 重定向到 file2。
```

### 特殊的重定向(Here Document )

Here Document 是 Shell 中的一种特殊的重定向方式，用来将输入重定向到一个交互式 Shell 脚本或程序。

```shell
command << delimiter
    document
delimiter
```

#### 它的作用是将两个 delimiter 之间的内容(document) 作为输入传递给 command。

注意：

* 结尾的delimiter 一定要顶格写，前面不能有任何字符，后面也不能有任何字符，包括空格和 tab 缩进。

* 开始的delimiter前后的空格会被忽略掉。

```shell
wc -l << EOF
    欢迎来到
    www.百度.com
EOF
2         # 输出结果为 2 行
```



```shell
cat << EOF
	欢迎来到
    www.百度.com
EOF
```

### /dev/null 文件

如果希望执行某个命令，但又不希望在屏幕上显示输出结果，那么可以将输出重定向到 /dev/null：

```shell
command > /dev/null
```

/dev/null 是一个特殊的文件，写入到它的内容都会被丢弃；如果尝试从该文件读取内容，那么什么也读不到。但是 /dev/null 文件非常有用，将命令的输出重定向到它，会起到"禁止输出"的效果。

如果希望屏蔽 stdout 和 stderr，可以这样写：

```shell
command > /dev/null 2>&1
```

# 引入其他sh文件

```shell
. filename   # 注意点号(.)和文件名中间有一空格
或
source filename
```

## 例子

### sh1.s

> *被包含的文件 sh1.sh 不需要可执行权限* 

```shell
url="http://www.baidu.com"
```

### sh2.sh

```shell
#使用 . 号来引用sh1.sh 文件
. ./sh1.sh

# 或者使用以下包含文件代码
# source ./sh1.sh
echo "百度官网地址：$url"
```

### 执行

```shell
chmod +x sh2.sh 
./sh2.sh 
百度官网地址：http://www.baidu.com
```