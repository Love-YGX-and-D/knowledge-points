# 浏览器的作用

1.呈现内容

​	内核：解析内容和样式              -webkit-  /-ms-/-moz-/-0- 

2.实现交互逻辑              （js引擎）  v8引擎/

3.进行数据传递				    chrome net 引擎（上网）



# linux

> 操作系统的内核

> Ubuntu最受欢迎的linux发行系统，永久免费，开源分享，定期更新和发布，6个月发布一个版本，由年份和月定，

# Ubuntu windows安装过程

1.下载ubuntu的镜像文件

​	官网下载：https://www.ubuntu.com/download/alternative-downloads

​	镜像下载：https://mirrors.tuna.tsinghua.edu.cn/ubuntu-releases/

​	下载类型：ubuntu-14.04.5-desktop

2.虚拟机vmware

 	linux操作命令（多用户，多任务的支持远程操作的系统）
 	terminal  搜索工具
 	ctrl shift +   放大窗口
 	ctrl shift  t   增加窗口
 	alt 1，2，3  切换对应的1 2 3窗口

 只有一个根目录
	3./sbin 重要的系统二进制 (system binaries) 文件
​	4./bin  重要的二进制 (binary) 应用程序，操作命令存放的地方
​	5./dev 设备文件（硬盘，键盘，鼠标等）
​	6./boot 系统启动的配置文件
​	7./etc （配置文件  启动脚本等」系统级别「），安装程序后，在etc设置在这个目录用来存放所有的系统管理所需要的配置文件
​	8./home 本地用户主目录（家目录，普通用户）
​	9./lib 系统库文件（系统的核心文件）（ls在其中）
​		在bin和sbin（超级管理员）
​	10./lost+found  系统运行的临时文件夹「一般不用动」
​	11./media   管理 移动设备（插入的麦克风等）[其他盘/u盘等]
​	12./mnt   管理整个文件系统，让用户临时挂载别的文件系统
​	13./opt  提供一个可选的应用程序安装目录（默认）
​	14./proc 管理程序在进程在成产生的垃圾，这个目录的内容不在硬盘，而在内存里
​	15./root 关于超级管理员的东西，超级权限者的用户主目录
​	16./sys 系统的临时文件，存在内存里
​	17./tmp 整个操作系统的临时文件（所有用户都可以操作）
​	18./usr 包含绝大部分用户自己的配制文件
​	19./var  变量，经常变化的文件，例如：日志 数据
​	20./run  在文件运行时用的（不要放东西）

# 常用的命令

##  一、切换目录

​	 cd  切换目录
​		/ 根目录
​		~家目录   「windows系统下的c/user/你的名字/ 」
​	 cd .  当前目录
​	 cd .. 返回上一级
​	 cd ../../ 返回上两极
​	 cd ../../../      返回上三级
​	 cd  路径
​         cd - 后退（回到最近一次的目录）
  	cd 进入家目录

## 二、清屏

​	clear 清屏

## 三、ls/tree

​	ls（list）  查看目录内容
​	 参数：
​	   -a   全部（包括隐藏的）
​	   -l   文件的详细信息 【文件】
​	   -al  组合用
​	   --help
​		d rwx  rwx   r -x
​		 d：文件类型【d：文件夹/目录，-:文件】
​		 rwx:所有者[读/写/执行]
​		 rwx:所有组
​		 r-x:其他组
​		   的权限
​		 r 可读：读取文件的数据（cat）
​		 w 可写：增减删除文件（vim等）
​		 x 可执行：列出目录下文件的详细信息
​		更改文件的所有者/操作权限：chown 参数 用户：用户组 目录 /文件
​			参数：
​			   -R  递归【文件/文件夹】
​		更改文件的其他者/其他者的操作权限：
​			方法一：chmod u=rwx/g=rwx/o=rw- 文件/目录
​			方法二：chmod 777/776/...  文件/目录			
​			   1：执行x，2：写w，4：读r ，3：xw，5：sr，6：wr，7：rwx
​	tree：以树状图列出目录的内容[sudo apt install tree]

## 四、man

​	man f/q   一页一页翻，/退出（man ls（操作手册））

## 五、查看命令的位置which

​	which ls

## 六、pwd 输出文件路径（当前的）

​	

## 七、文件操作

​	7.1创建文件/添加内容
​		echo hello > "1.txt"（1.txt）    【>(重定向)】（覆盖）
​		echo 456 >> 1.txt  追加（创建文件和内容）
​		touch 2.txt 创建文件（有的话不再创建）
​		vim 3.txt  创建文件
​	7.2查看文件内容
​		cat 1.txt 预览（1.tab键  自动补全）
​		cat/more/head/tail
​	7.3编辑文件内容
​		gedit 1.txt   打开编辑文件（有gedit软件）
​		vim 1.txt 编辑1.txt
​	  		i  插入
​	  		esc推出
​	  		：w  写
​	  		：q  退出（：wq）
​	7.4复制文件
​		cp 1.txt 2.txt 把1.txt拷贝放到同级的2.txt
​	7.5删除文件
​		rm 1.txt 删除
​		rm *.txt  删除所有的txt文件
​		rm -I a b c 同时删除a b c文件

## 八、目录（操作）

​	8.1创建目录
​		mkdir  a  创建a目录
​		mkdir -p a/b   a目录下创建b目录
​		mkdir -p a/b/c 创建树形结构（层级结构）
​	8.2删除目录
​		rmdir a 删除a目录（只能删除空目录）
​		rmdir -p a/b/c   删除连续的空目录a/b/c   *删除带层级的空目录
​		rm -rf a  删除a文件夹
​		rm -I -rm a b c 同时删除a b c目录
​	8.3移动目录
​		mv a aaa  把a移动到aaa里面
​		mv a aa/aaa  把a移动到aa下的aaa里面
​		mv a ../aa   把a移动到aa的上一级里面
​	8.4拷贝复制目录
​		cp 源文件 -r 目标文件   拷贝目录

## 九、查找find/grep

​	find：查找相关的文件夹、文件夹
​		find 内容（内容支持正则）
​	grep 查找内容
​	| 管道、过滤
​	 grep a *.txt   在所有的.txt文件中查找内容中含有a的
​	 grep sudo find ngi* | grep con
​	

## 十、历史记录history

​	参数
​	 -c  清空所有的历史记录

## 十一、文件的压缩/解压

​	「打包」tar -cvf 目标文件 源文件
​	  参数：
​		-c 压缩
​		-v 视图可见
​		-f 文件
​		-x 解压
​	「解包」 tar -xvf 源文件 -C 目标文件
​	「压缩」tar -zcvf 目标文件 源文件
​	  参数：
​		-z：gzip压缩 
​		-j：bz2压缩
​	「解压」 tar -zxvf 源文件 -C 目标文件

	[zip]
	
	  压缩：
 		zip -r 目标文件 源文件     －r表示递归压缩子目录下所有文件.

	  解压：
		unzip -o 源文件 -d  目标文件 【绝对路径】
			-o:不提示的情况下覆盖文件；
			-d:-d /home/sunny 指明将文件解压缩到/home/sunny目录下；
		unzip  源文件：在当前目录下解压
	    3.其他
		zip -d myfile.zip smart.txt
		  删除压缩文件中smart.txt文件
		zip -m myfile.zip ./rpm_info.txt
		  向压缩文件中myfile.zip中添加rpm_info.txt文件
## 十二、链接ln（不管硬链还是软链，一改全改）

​	   ln 源文件 目标文件（绝对路径{同一级可以忽略不写}）
​	     （无参数）硬链接，占用内存空间
​	      -s  软链接，不占用内存空间

## 十三、文件传输（双方都遵守同一协议）

​	ssh
​		压缩传输速度快，加密安全，口令传输
​		默认端口号：22

	上传到服务器：
		scp -r 文件 用户名@用户ip：存放的绝对路径
	下载到本机：
		scp -r  用户名@用户ip：存放的绝对路径的文件 目标的绝对路径
		参数：-p  端口号
## 十四、安装/删除程序sudo apt-get install synaptic

### 	14.1 APT包【ubuntu中】

​	   安装：sudo apt-get install 包名1 包名2
​	   1.卸载/删除：sudo apt-get remove 包名
​	   2.删除依赖关系：apt-get --purge remove 包名1 包名2
​	   3.删除该软件的依赖包： apt-get autoremove 包名
​	   清理无用的包：sudo apt-get clean &&  sudo apt-get autoclean
​	   更新：sudo apt-get update
​	   帮助：apt-get help 
​	   升级更新系统： sudo apt-get upgrade	
​	   下载该包的源码：sudo apt-get source 包名

### 	14.2 添加源（库中没有的时候）

​	   添加包地址：sudo add-apt-repository ppa：地址【webupd8team/java】
​		没有add-apt-repository ，运行 sudo apt-get install soft
​	   

### 	14.3 deb包

​	   安装：
​		1.双击它，然后选择 安装软件包 即可。
​	    	2.终端并输入：sudo dpkg -i package_file.deb
​	       卸载 ：sudo dpkg -r package_name 

### 	14.4 源安装

​	   1.下载源码：wget url【路径】
​	   2.解压 tar -zxvf 源文件
​	   3.进入解压目录 cd 目录
​	   4.找到configure并执行：./configure --prefix=/usr/local【指定安装路径（自己定）】 [--enable -optimizations]{优化}
​	   5.编译：make all
​	   6.安装：make install

#### 	14.4-1 多版本共存

​	    sudo update-alternatives --install /usr/bin/python3【命令路径】  python3 /user/bin/python3.6【目标路径】
​	    update-alternatives --install link name path priority[优先级（数字）]

#### 	14.4-2 指定默认的程序

​	    1.先备份 sudo cp /usr/bin/python /usr/bin/python_bak
​	    2.删除：sudo rm /usr/bin/python
​	    3.重建软连接  sudo ln -s /usr/bin/python3.5 /usr/bin/python  

## 十五、安装发生依赖关系错误的解决办法

​	sudo apt-get -f install

## 十六、磁盘管理

​	df 参数 ： 查看磁盘的使用情况
​		-h：可读的显示格式
​		
​	du 参数 ： 查看目录当前的存储状态
​		du -sh /media/floppy 

   		 -s 意思 summary  -h 意思 human-readable 

## 十七、网络通讯

​	ifconfig 查看或设置网卡
​		启动/关闭指定网卡：
​	 	 ifconfig 网卡名 down
​	 	 ifconfig 网卡名 up
​		配置IP
​		 ifconfig 网卡 修改后的ip netmask（网络掩码） 掩码号  broadcast（广播地址/网关） 192.168.1.255
​	netstat -aup（a：所有的，u：UDP，p：端口，t：TCP协议） ：查看linux系统的网络使用情况

	udp：
	tcp：
## 十八、关机

​	立刻关机：halt【不安全】
​	立刻关机：poweroff【不安全】
​	立刻关机（root用户使用）：shutdown -h now
​	10分钟后自动关机：shutdown -h 10

## 十九、重启

​	reboot 
​	shutdown -r now
​	shutdown -r 10
​	shutdown -r 20：35
​	shutdown -c  取消重启

## 二十、进程

​	ps -aux 显示所有包含使用者的进程
​	   ps -aux  「ps代表进程」
​	top 动态显示所有进程【实时显示】
​	kill pid 杀死进程
​	kill -9 pid【】 强制杀死进程[杀不死的就是守护程序，在/etc/init.d中存放，关程序：/etc/init.d/mysql stop/start/restart]

## 二十一、权限[多用户，多任务]

​	sudo -s
​	查看默认权限：umask
​	whoami 谁在登录
​	who 所有的用户
​	添加用户：
​	  添加用户：useradd -m 用户名
​	    参数：
​		-m ：自动创建家目录
​		-d ：制定用户登录时的起始目录
​		-g ：指定一个组【useradd -m yyy -g ccc ：yyy指定到ccc组下】
​		-G ：追加一个组 
​		   一个用户可以所属多个组
​	    sudo useradd -g root 用户名  ：让用户名***划归到root下
​	  创建密码：passwd 用户名
​	  修改：usermod 用户名 参数 内容 
​	查看用户： cat /etc/passwd
​	删除用户：
​	  在root用户下：userdel -r 用户名
​	  在普通用户下：sudo userdel -r 用户
​	切换账户: su  用户名 
​	组
​       	  创建组：sudo groupadd 组名
​	  查看组：【写在最前面的是主组：修改主组  先指定在追加】
​		  cat /etc/group
​		  groups 用户
​	  修改组：
​		usermod 用户 -g/-G 组名
​	  删除组员：【必须有主组】【现有组再有用户】
​		gpasswd -d 用户 组名
​	  增加组员：
​		gpasswd -a 用户 组名
​	  删除组：
​		groupdel 组名
​	  修改组名：
​		groupmod 源组名 -n 目标组名
​	让用户所属用户组拥有sudo权利：
​	    usermod -a -G sudo 用户
​	    usermod -s -G adm 用户

# 添加全局变量	

## echo $PATH 输出全局变量的值

> export PATH=$PATH:新追加的路径 =》 重启没有了

> vim ~/.profile  放进去

> 软链： 

#！/usr/bin/env python :表明用Python环境执行	

# 防火墙

sudo ufw disable

sudo ufw status	

​	

​	


​	
​	
​	
​	  


