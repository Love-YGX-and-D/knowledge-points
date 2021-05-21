# 关于ubuntu
- 永久免费
- 开源分享
- 定期更新和发布，六个月发布一个版本，Ubuntu 的版本号是根据我们发布一个版本的日期而定。版本号由该次发布的年份和月份组成
- Ubuntu (发音"oo-BOON-too"--“乌邦图”) 天下共享，连接起每个人

## 1. 目录和文件系统
- / 根目录
- <span style=color:red>/bin - 重要的二进制 (binary) 应用程序</span>。bin就是binary，二进制。/bin目录放置可执行文件，root和一般账号都可以使用，如cat, chmod, mv, mkdir等。其实系统有很多放置执行文件的目录，但/bin 目录比较特殊，因为/bin 放置的是在单用户模式下还能够被操作的命令
- /boot - 启动 (boot) 配置文件，这个目录主要存放开机会使用的文件，如Linux内核和系统启动文件
- /dev - 设备 (device) 文件，存放所有设备文件，包括硬盘、分区、键盘、鼠标、USB、tty等。注：在Linux系统上，任何设备与接口设备都是以文件的形式存在于这个目录当中的
- <span style=color:red>/etc - 配置文件、启动脚本等 (etc)</span>，例如/etc/passwd存放用户账户信息，/etc/hostname文件存放主机名
- <span style=color:red>/home - 本地用户主 (home) 目录</span>
- /lib - 系统库 (libraries) 文件，存放开机时会用到的函数库，以及/bin和/sbin目录下的命令调用的函数库
- /lost+found - 在根 (/) 目录下提供一个遗失+查找(lost+found) 系统
- /media - 挂载可移动介质 (media)，诸如 CD、数码相机等，它下面存放可删除的设备，包括软盘，光盘，DVD等设备文件
- /mnt - 挂载 (mounted) 文件系统
- /opt - 提供一个供可选的 (optional) 应用程序安装目录
- <span style="color:red">/proc - 特殊的动态目录，这个目录本身是一个虚拟文件系统。它放置的数据都是在内存当中，例如系统内核，进程等</span>
- /root - root (root) 用户主文件夹，读作“slash-root”
- /sbin - 重要的系统二进制 (system binaries) 文件，这些命令只有root用户才能用设置系统，其他用户最多只能用来“查询”而已
- /sys - 系统 (system) 文件，这个目录跟/proc 非常类似，也是一个虚拟的文件系统，主要也是记录与内核相关的信息。这个目录同样不占硬盘容量
- /tmp - 临时(temporary)文件，就是用来存放临时文件的地方，所有用户都可以访问。该目录不要放重要数据
- /usr - 包含绝大部分所有用户(users)都能访问的应用程序和文件
- /var - 经常变化的(variable)文件，诸如日志或数据库等
- <span color="red">/run - 要特别注意的是：它使用tmpfs文件系统，这是一种存储在内存中的临时文件系统，当机器关闭的时候，文件系统自然就被清空了</span>

## 2. 常用命令
- 查看帮助文档
   ```
    command --help
    man command    [manual]
   ```
- ls（选项）（参数） 查看指定目录下的内容

    **选项**

    ```
    $  -a：显示所有档案及目录（ls内定将档案名或目录名称为“.”的视为影藏，不会列出）；
    $  -l：以长格式显示目录下的内容列表。输出的信息从左到右依次包括文件名，文件类型、权限模式、硬连接数、所有者、组、文件大小和文件的最后修改时间等
    $  -t：用文件和目录的更改时间排序；
    ```
    **参数**
    ```
    $ 指定要显示列表的目录，也可以是具体的文件
    $ 文件或目录支持正则的写法  *?[]
    ```

- which ( 命令 )

    ```
    $ 可执行程序的绝对路径
    ```

- cd (目录)
    ```
    $ 用于切换当前工作目录至指定目录
    $ 可为绝对路径或相对路径
    $ 目录名称省略，则变换至使用者的 home 目录 ，"~"也标识home目录
    $ "-" 快速回到上一次所在目录
    $ "/" 表示根目录
    $ "." 则是表示目前所在的目录
    $ ".." 则表示目前目录位置的上一层目录
    ```

- pwd

    ```
    $ 执行pwd指令可立刻得知您目前所在的工作目录的绝对路径名称
    ```
— clear
    ```
    $ 清空屏幕
    ```

## 3.文件管理常用命令
- ls
- touch (文件名)
    ```
    $ 修改文件或者目录的时间属性，包括存取时间和更改时间。若文件不    存在，系统会建立一个新的文件
    ```
- echo (输出内容)
    ```
    $ 在命令行输出内容
    $ 用 ">" 符号可以重定向
    $ 用 ">>"符合可以追加内容
    ```
- cat (选项) (参数)
    **选项**
    ```
    $ -n 或 --number：由 1 开始对所有输出的行数编号。

    $ -b 或 --number-nonblank：和 -n 相似，只不过对于空白行不编号。
    ```
    **参数**
    ```
    $ 要输出的文件
    ```

- more (选项) (参数)
    **选项**
    ```
    $ -num 一次显示的行数
    $ +num 从第 num 行开始显示
    $ +/pattern 在每个文档显示前搜寻该字串（pattern），然后从该字串之后开始显示
    ```
    **参数**
    ```
    $ 要显示的文件
    ```
    **常用的操作命令**
    ```
    $ Enter 向下n行，需要定义。默认为1行
    $ Ctrl+F 向下滚动一屏
    $ 空格键 向下滚动一屏
    $ Ctrl+B 返回上一屏
    $ = 输出当前行的行号
    $ ：f 输出文件名和当前行的行号
    $ V 调用vi编辑器
    $ q 退出more
    ```
- gedit 文件名   编辑指定的文件
- vi  文件名     编辑指定的文件
- mkdir (选项) (参数)
    **选项**
    ```
    $ -p 可以创建递归目录
    ```
    **参数**
    ```
    $ 指定要创建的目录
    ```
- rmdir (选项)  (参数)
    **选项**
    ```
    $ 删除空的目录
    $ -p 是当子目录被删除后使它也成为空目录的话，则顺便一并删除
     如：rmdir -p aaa/bbb
    $ 在工作目录下的 aaa 目录中，删除名为 bbb 的子目录。若 bbb 删除后，aaa 目录成为空目录，则 BBB 亦予删除,否则只删除bbb，aaa则不予删除
    ```
    **参数**
    ```
    $ 要删除的目录
    ```

- rm (选项) (参数)
    **选项**
    ```
    $ -i 删除前逐一询问确认。
    $ -f 即使原档案属性设为唯读，亦直接删除，无需逐一确认。
    $ -r 将目录及以下之档案亦逐一删除。
    ```
    **参数**
    ```
    $ 要删除的文件或是目录
    ```

- cp (选项) source dest
    **选项**
    ```
    $ -p：除复制文件的内容外，还把修改时间和访问权限也复制到新文件中。
    $ -r：若给出的源文件是一个目录文件，此时将复制该目录下所有的子目录和文件
    ```
    **source**
    ```
    $ 要复制的文件名
    ```
    **dest**
    ```
    $ 目标地址
    ```
- mv (选项) source dest
    **选项**
    ```
    $ -i: 若指定目录已有同名文件，则先询问是否覆盖旧文件;
    $ -f: 在mv操作要覆盖某已有的目标文件时不给任何指示;
    ```
    **source**
    ```
    $ 要移动或修改的文件名
    ```
    **dest**
    ```
     要移动或修改的目标地址
    ```

- ln (选项) source dest
    `ln命令是一个非常重要命令，它的功能是为某一个文件在另外一个位置建立一个同步的链接`
    **硬链接**
    ```
    1.硬链接，以文件副本的形式存在。但不占用实际空间。
    2.不允许给目录创建硬链接
    3. ln  source dest
    4. 用 rm 命令 删除硬链接
    ```
    **软连接**
    ```
    1.软链接，以路径的形式存在。类似于Windows操作系统中的快捷方式
    2.软链接可以 跨文件系统 ，硬链接不可以
    3. ln -s source dest
    4. 用 rm 命令 删除硬链接
    ```
- grep (选项) (参数) 从文件里面找内容
    **选项**
    ```
    $ 要查找的范式
    ```
    **参数**
    ```
    $ 要查询的文件
    ```
- find path -option  找文件
    ```
    $ find . -name "*.c" 前目录及其子目录下所有延伸档名是 c 的文件列出来
    $ find . -type f     将目前目录其其下子目录中所有一般文件列出
    $ find . -ctime -20  将目前目录及其子目录下所有最近 20 天内更新过的文件列出
    ```

## 4.文件解压缩
- tar (选项) dest (mode) source
    **选项**
    ```
    $ -c 创建打包文件。
    $ -v 显示打包过程
    $ -f 指定打包后的文件名
    $ -x 解包
    $ -z 压缩格式 gzip
    $ -j 压缩格式  bz2
    ```
    **mode**
    ```
    $ -C 解压到指定目录
    ```
    **dest**
    ```
    $ 打包后的文件名  xxx.tar
    $ 打包并压缩成gzip格式     xxx.tar.gz
    $ 打包并压缩成bz2格式     xxx.tar.bz2
    ```
    **source**
    ```
    $ 要打包的文件
    ```

- zip 压缩
    ```
    $ zip dest source
    ```
- unzip (-d) (path) 解压
    ```
    $ unzip dest
    ```
## 5.磁盘管理
- cd  切换目录
- df (选项) (参数)   查看磁盘使用情况
    **选项**
    ```
    $ -h 可读的格式显示
    $ -a, --all 包含所有的具有 0 Blocks 的文件系统
    ```
    **参数**
    ```
    $ df -h /run
    ```
- du (选项) (参数) 查看当前目录的存储状态
    **选项**
    ```
    $ -h 可读的格式显示
    ```
    **参数**
    ```
    $ du -h /run
    ```
## 6.文件传输
- scp (可选参数) file_source file_target
    **可选参数**
    ```
    $ -r 递归拷贝目录
    $ -v：详细方式显示输出。scp和ssh(1)会显示出整个过程的调试信息。这些信息用于调试连接，验证和配置问题
    $ -P port：注意是大写的P, port是指定数据传输用到的端口号
    ```
    **file_source**
    ```
    $ 要拷贝的源文件
    ```
    **file_target**
    ```
    $ 目标地址
    ```
    **案例**
    ```
    $ 本地文件上传服务器 scp -r local_folder remote_username@remote_ip:remote_folder
    $ 从服务器下载本地文件 scp -r remote_username@remote_ip:remote_folder local_folder
    ```
- windows和linux传输文件
    1. 下载`PSCP.exe`,配置Windows的环境变量Path，或者直接通过命令行访问到pscp.exe
    2. 把本地文件file传输到Linxu服务器的目录中
    ```
    $ pscp  -r 本地目录 用户名@LinuxIP:目录
    ```
    3. 从Linux向Windows复制文件或目录
    ```
    $ pscp  -r 用户名@LinuxIP:目录 本地目录
    ```
## 7.网络通讯
- ifconfig 查看或设置网卡
    ```
    启动关闭指定网卡
    $ ifconfig eth0 down
    $ ifconfig eth0 up
    ```
    ```
    配置IP地址
    $ ifconfig eth0 192.168.1.56 netmask 255.255.255.0 broadcast 192.168.1.255
    ```
- netstat   利用netstat指令可让你得知整个Linux系统的网络情况
    ```
    显示UDP端口号的使用情况
    $ netstat -apu

    ```
- ping  用于检测主机

## 8.权限管理
- sudo -s
- whoami 查看当前用户
- who 查看所有登陆用户
- useradd (选项) (参数)
    **选项**
    ```
    $ -d 指定用户登入时的启始目录
    $ -m 自动建立用户的登入目录
    $ -g 指定用户所属的群组
    $ -G 追加用户所属的群组
    ```
    **参数**
    ```
    $ 用户名
    $ user add -d aaa -m aaa -g aaa username
    ```
- usermod  修改用户
- passwd 修改密码
- su    切换账户
- userdel (参数) (选项)
    **参数**
    ```
    $ -f 强制删除

    ```
    **选项**
    ```
    $ 要删除的用户名
    $ userdel -f username
    ```
- groupadd (组名) 添加一个用户组
- groupamod (选项) (参数) 修改用户组的信息
    **选项**
    ```
    $ -g<群组识别码>：设置欲使用的群组识别码；
    $ -n<新群组名称>：设置欲使用的群组名称。
    ```
    **参数**
    ```
    组名：指定要修改的工作的组名。
    ```

    ```
    让改用户组拥有sudo的功能
    $ groupmod -a -G sudo groupname
    $ groupmod -a -G adm  groupname
    ```
- gpasswd (参数) (用户) (组) 将用户从用户组中添加或删除
  **参数**
  ```
  $ -a : 添加用户到组
  $ -d : 从组删除用户
  $ gpasswd -a userA groupA
  ```
- groupadel 删除用户组
- groups 查看当前用户所属的用户组
- chgrp (选项) (参数) 用来改变文件或目录所属的用户组
  **选项**
  ```
  $ -R或——recursive：递归处理，将指令目录下的所有文件及子目录一并处理；
  $ chgrp -R groupname /usr/meng
  ```
  **参数**
  ```
  组：指定新工作名称；
  文件：指定要改变所属组的文件列表。多个文件或者目录之间使用空格隔开。
  ```
- chmod (选项) (参数)
    **选项**
    ```
    $ u 表示该文件的拥有者，g 表示与该文件的拥有者属于同一个群体(group)者，o 表示其他以外的人，a 表示这三者皆是
    $ r 表示可读取 4，w 表示可写入 2，x 表示可执行 1
    $ -R : 对目前目录下的所有文件与子目录进行相同的权限变更(即以递回的方式逐个变更)
    ```
    **参数**
    ```
    rwx r读4 w写2 x执行1
    chmod u=rwx g=rwx o=rwx
    $ chmod u=rwx,g=rw,o=r file
    ```

## 9.软件安装和管理
- APT (Advanced Package Tool,高级软件包工具) 是一个强大的包管理系统，而那些图形化程序如 添加/删除 应用程序 和 Synaptic 都是建立在它的基础之上的。APT 自动处理依赖关系并在系统软件包执行其他操作以便安装所要的软件包
- 添加包地址:
  - sudo add-apt-repository ppa:webupd8team/java
  - 如果没有 add-apt-repository 这个命令，运行 sudo apt-get install software-properties-common python-software-properties
  - ppa 全称为Personal Package Archives(个人软件包档案),是UbuntuLaunchpad网站提供的一项服务
- 安装软件包：
  - sudo apt-get install packagename
- 删除软件包：
  - sudo apt-get remove packagename
- 删除软件包包括配置文件
  - apt-get --purge remove mysql-server mysql-client
- 删除该软件的依赖包
  - apt-get autoremove mysql-server mysql-client
- 清理无用的包
  - sudo apt-get clean && sudo apt-get autoclean
- 获取新的软件包列表：
  - sudo apt-get update
- 升级有可用更新的系统：
  - sudo apt-get upgrade
- 下载该包的源代码
  - apt-get source package

- 列出更多命令和选项：
  - apt-get help

## 10. 其他常用系统命令
- 关机
  ```
  $ halt 立刻关机
  $ poweroff 立刻关机
  $ shutdown -h now 立刻关机(root用户使用)
  $ shutdown -h 10 10分钟后自动关机
  ```
- 重启
  ```
  $ reboot
  $ shutdown -r now
  $ shutdown -r now 10
  $ shutdown -r 20:35
  $ shutdown -c 取消重启
  ```
- 进程
  ```
  ps -aux  显示所有包含使用者的进程
  top 动态显示所有进程
  kill pid  杀死进程
  kill -9 pid  强制杀死进程
  ```



## 11.vi\vim编辑器

## 12.安装 pycharm
    ```
    1. 安装java运行环境
    sudo add-apt-repository ppa:webupd8team/java
    sudo apt-get update
    sudo apt-get install oracle-java8-installer
    2. 运行命令
    java -version
    javac -version
    如果以上两个命令找不到的话，执行第二步，否则跳过第三步
    3. 添加全局变量
    echo JAVA_HOME="/usr/lib/jvm/java-8-oracle" >> /etc/environment
    source /etc/environment
    4. 安装pycharm
    到pycharm官网下载在linux的安装包
    解压

    并且运行 bin/pycharm.sh
    $ sudo sh pycharm/bin/pychar.sh

    5. 破解
    到http://idea.lanyus.com/网站获取注册码
    6. 创建快捷方式
    - Ubuntu的快捷方式都放在/usr/share/applications，首先在该目录下创建一个Pycharm.desktop
    - 在 该文件写入以下配置：
    [Desktop Entry]
    Type=Application
    Name=Pycharm
    GenericName=Pycharm3
    Comment=Pycharm3:The Python IDE
    Exec="/XXX/pycharm/bin/pycharm.sh" %f
    Icon=/XXX/pycharm/bin/pycharm.png
    Terminal=pycharm
    Categories=Pycharm;
    - 锁定到启动器
    ```
## 13.ubuntu修改时区和时间的方法
    ```
    参考： https://blog.csdn.net/YEYUANGEN/article/details/52103445
    ```
