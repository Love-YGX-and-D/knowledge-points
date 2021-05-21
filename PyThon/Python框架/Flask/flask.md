# 简单地应用

```python
from flask import Flask
app = Flask(__name__)
# app参数
# app = Flask(__name__,template_folder='templates',static_url_path='/xxxxxx')

# 配置端口
# app.config['DEBUG']=True
@app.route('/')
def hello_world():
   return 'Hello World’

if __name__ == '__main__':
   app.run()
```

# flask配置文件

```python
flask中的配置文件是一个flask.config.Config对象（继承字典）,默认配置为：
    {
        'DEBUG':                                get_debug_flag(default=False),  是否开启Debug模式
        'TESTING':                              False,                          是否开启测试模式
        'PROPAGATE_EXCEPTIONS':                 None,                         
        'PRESERVE_CONTEXT_ON_EXCEPTION':        None,
        'SECRET_KEY':                           None,
        'PERMANENT_SESSION_LIFETIME':           timedelta(days=31),
        'USE_X_SENDFILE':                       False,
        'LOGGER_NAME':                          None,
        'LOGGER_HANDLER_POLICY':               'always',
        'SERVER_NAME':                          None,
        'APPLICATION_ROOT':                     None,
        'SESSION_COOKIE_NAME':                  'session',
        'SESSION_COOKIE_DOMAIN':                None,
        'SESSION_COOKIE_PATH':                  None,
        'SESSION_COOKIE_HTTPONLY':              True,
        'SESSION_COOKIE_SECURE':                False,
        'SESSION_REFRESH_EACH_REQUEST':         True,
        'MAX_CONTENT_LENGTH':                   None,
        'SEND_FILE_MAX_AGE_DEFAULT':            timedelta(hours=12),
        'TRAP_BAD_REQUEST_ERRORS':              False,
        'TRAP_HTTP_EXCEPTIONS':                 False,
        'EXPLAIN_TEMPLATE_LOADING':             False,
        'PREFERRED_URL_SCHEME':                 'http',
        'JSON_AS_ASCII':                        True,
        'JSON_SORT_KEYS':                       True,
        'JSONIFY_PRETTYPRINT_REGULAR':          True,
        'JSONIFY_MIMETYPE':                     'application/json',
        'TEMPLATES_AUTO_RELOAD':                None,
    }
  
方式一：
    app.config['DEBUG'] = True
  
    PS： 由于Config对象本质上是字典，所以还可以使用app.config.update(...)
  
方式二：
    app.config.from_pyfile("python文件名称")
        如：
            settings.py
                DEBUG = True
  
            app.config.from_pyfile("settings.py")
  
    app.config.from_envvar("环境变量名称")
        环境变量的值为python文件名称名称，内部调用from_pyfile方法
  
  
    app.config.from_json("json文件名称")
        JSON文件名称，必须是json格式，因为内部会执行json.loads
  
    app.config.from_mapping({'DEBUG':True})
        字典格式
  
    app.config.from_object("python类或类的路径")
  
        app.config.from_object('pro_flask.settings.TestingConfig')
  
        settings.py
  
            class Config(object):
                DEBUG = False
                TESTING = False
                DATABASE_URI = 'sqlite://:memory:'
  
            class ProductionConfig(Config):
                DATABASE_URI = 'mysql://user@localhost/foo'
  
            class DevelopmentConfig(Config):
                DEBUG = True
  
            class TestingConfig(Config):
                TESTING = True
  
        PS: 从sys.path中已经存在路径开始写
      
PS: settings.py文件默认路径要放在程序root_path目录，如果instance_relative_config为True，则就是instance_path目录
 
配置文件
```



# app.run()参数设定

```python
app.run(host, port, debug, options)
所有参数都是可选的
序号	参数和说明
1	host 主机名来听。默认为127.0.0.1（本地主机）。设置为'0.0.0.0'使服务器在外部可用
2	port 默认为5000
3	debug 默认为false。如果设置为true，则提供调试信息
4	options 被转发到底层的Werkzeug服务器。
```

# flask路由

## 方式一

```python
@app.route(‘/hello’)
def hello_world():
   return ‘hello world’
```

## 方式二

```python
def hello_world():
   return ‘hello world’
app.add_url_rule(‘/’, ‘hello’, hello_world)   # ‘hello’是别名
```

## 重点/注意点

```python
考虑以下脚本中定义的规则 -
@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python'

两条规则看起来都很相似，但在第二条规则中，使用了尾部斜线 （/） 。因此，它变成了一个规范的URL。

因此，使用 / python 或 / python / 返回相同的输出。但是，在第一条规则的情况下， / flask / URL会导致 404 Not Found 页面。
```

# 路由传参：

## 方式

```python
@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name
```

### 变量转换

```python
#转换为整型：
@app.route('/blog/<int:postID>')  # <path:path>
def show_blog(postID):
   return 'Blog Number %d' % postID

#转换为浮点数：
@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo
```

# url_for路由传参

> 该函数接受函数的名称作为第一个参数，并接受一个或多个关键字参数，每个参数对应于URL的变量部分。
>
> ```
> url_for('函数名称/装饰器名称',参数【name = user】)
> ```

```python
@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))
 
输入：http：// localhost：5000 / user / admin 
输出： hello_admin

输入：http：// localhost：5000 / user / mvl
输出： hello mvl as Guest
```

# 蓝图

## 作用

```html
将不同的功能模块化
构建大型应用
优化项目结构
增强可读性,易于维护（跟Django的view功能相似）
```

## 子文件

```python
from flask import Blueprint,make_response,send_from_directory
download1=Blueprint("download1",__name__)

# 下载角色
@download1.route("/role")
def role():
    pass
```

## 主文件

```python
# 导入
from url.selectAll import selectAll   在主入口文件的url文件夹中存放
from download1 import download1   在主入口文件的同级目录

# 注册
app.register_blueprint(download1,url_prefix="/ajax/download1")
参数说明：download1：文件名
		url_prefix: 路由名（前面几个）
```

# flask请求和相应

```python
from flask import Flask,request,render_template,redirect,make_response 
请求相关信息
    # request.method
    # request.args
    # request.form
    # request.values
    # request.cookies
    # request.headers
    # request.path
    # request.full_path
    # request.script_root
    # request.url
    # request.base_url
    # request.url_root
    # request.host_url
    # request.host
    # request.files
    # obj = request.files['the_file_name']
    # obj.save('/var/www/uploads/' + secure_filename(f.filename))
 
响应相关信息
    # return "字符串"
    # return render_template('html模板路径',**{})
    # return redirect('/index.html')
    # response = make_response(render_template('index.html'))
    # response是flask.wrappers.Response类型
    # response.delete_cookie('key')
    # response.set_cookie('key', 'value')
    # response.headers['X-Something'] = 'A value'
    # return response
```

# Flask HTTP方法【数据提交的方法】

> ```
> 获取数据的提交方法： request.method 
> ```

| 序号 | 方法和说明                                                   |          接收方式          |
| ---- | ------------------------------------------------------------ | :------------------------: |
| 1    | GET 将数据以未加密的形式发送到服务器。最常见的方法。         | request.args.get("变量名") |
| 2    | HEAD 与GET相同，但没有响应主体                               |                            |
| 3    | POST 用于将HTML表单数据发送到服务器。通过POST方法接收的数据不会被服务器缓存。 |  request.form【"变量名"】  |
| 4    | PUT 用上传的内容替换目标资源的所有当前表示。                 |                            |
| 5    | DELETE 删除由URL给出的所有目标资源的所有表示                 |                            |

# flask静态文件

## 方式一：

```python
from flask  import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
   return render_template("index.html")
if __name__ == '__main__':
   app.run(debug = True)
```

```html
<html>

   <head>
      <script type = "text/javascript"
         src = "{{ url_for('static', filename = 'hello.js') }}" ></script>
   </head>
   <body>
      <input type = "button" onclick = "sayHello()" value = "Say Hello" />
   </body>
</html>
```

```js
function sayHello() {
   alert("Hello World")
}
```

## 方式二：

```html
<script src="../static/js/jquery-3.2.1.js"></script>
<link rel="stylesheet" href="../static/css/reg_login.css">
<link rel="stylesheet" href="http://at.alicdn.com/t/font_898522_648ntzxbu5e.css">
```

```html
正常写，安装css规则
```

# flask发送数据到表单

py文件

```python
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)
```

**student.html** 

```html
<html>
   <body>
      <form action = "http://localhost:5000/result" method = "POST">
         <p>Name <input type = "text" name = "Name" /></p>
         <p>Physics <input type = "text" name = "Physics" /></p>
         <p>Chemistry <input type = "text" name = "chemistry" /></p>
         <p>Maths <input type ="text" name = "Mathematics" /></p>
         <p><input type = "submit" value = "submit" /></p>
      </form>
   </body>
</html>
```

**（result.html）** 

```html
<!doctype html>
<html>
   <body>
      <table border = 1>
         {% for key, value in result.items() %}
            <tr>
               <th> {{ key }} </th>
               <td> {{ value }} </td>
            </tr>
         {% endfor %}
      </table>
   </body>
</html>
```

# flask文件上传

需要一个enctype属性设置为'multipart / form- data'的HTML表单，将该文件发布到URL。URL处理程序从 **request.files []** 对象中提取文件并将其保存到所需的位置。

每个上传的文件首先保存在服务器上的临时位置，然后再保存到最终位置。目标文件的名称可以是硬编码的，也可以从 **request.files [file]** 对象的filename属性中获取。但是，建议使用 **secure_filename（）** 函数获取它的安全版本。

可以在Flask对象的配置设置中定义默认上传文件夹的路径和上传文件的最大大小。

| app.config[‘UPLOAD_FOLDER’]      | 定义上传文件夹的路径                  |
| -------------------------------- | ------------------------------------- |
| app.config [ 'MAX_CONTENT_PATH'] | 指定要上传的文件的大小 - 以字节为单位 |

## 例子

### py文件

```python
from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

if __name__ == '__main__':
   app.run(debug = True)
```

### html页面

```html
<html>
   <body>
      <form action = "http://localhost:5000/uploader" method = "POST"
         enctype = "multipart/form-data">
         <input type = "file" name = "file" />
         <input type = "submit"/>
      </form>
   </body>
</html>
```



# 模板渲染（render_template()）

## 返回页面

```python
@app.route('/')
def index():
   return render_template(‘hello.html’)
```

## 返回页面且带数据

```python
html前端接收/渲染页面
    <!doctype html>
    <html>
       <body>
          <h1>Hello {{ name }}!</h1>
       </body>
    </html>
后台形式：
    @app.route('/hello/<user>')
    def hello_name(user):
       return render_template('hello.html', name = user)   【字符串/json格式的字符串】
```

## 返回数据

```python
@app.route('/hello/<user>')
    def hello_name(user):
       return 数据  【字符串/json格式的字符串】
```

## jinjia渲染

### 循环/条件：{％...％}

> 标签

#### 条件

```python
{% if marks>50 %}
<h1> Your result is pass!</h1>
{% else %}
<h1>Your result is fail</h1>
{% endif %}
```

#### 循环

```python
{% for key, value in result.iteritems() %}
<tr>
    <th> {{ key }} </th>
    <td> {{ value }} </td>
</tr>
{% endfor %}
```

### {{...}}将表达式打印到模板输出

### {＃...＃}不包含在模板输出中的评论

### ＃... ##线路语句

# flask Cookies

```python
存储在客户端浏览器上
一个 Request对象 包含了cookie的属性。它是所有cookie变量及其对应值的字典对象，客户端已发送。除此之外，cookie还会存储其到期时间，路径和站点的域名
在Flask中，cookies设置在响应对象上。使用 make_response（） 函数从视图函数的返回值中获取响应对象。之后，使用响应对象的 set_cookie（） 函数来存储cookie
回读一个cookie很容易。 request.cookies 属性的 get（） 方法用于读取cookie。
```

## 设置

```python
resp = make_response(render_template('readcookie.html'))
resp.set_cookie('userID', user)
```

## 读取/获取

```python
name = request.cookies.get('userID')
```

# flask sessions【会话】

> 与cookie不同，seesion是存储在服务器上的
>
> session是客户端登录到服务器并注销的时间间隔，需要在词会话中进行的数据存贮在服务器上的临时目录中
>
> 与每个可短的session分配一个会话id，session数据存储在cookie顶部，服务器以加密方式签名，对于这种加密，flask应用程序需要一个定义的secret_key；使用：app.session_key=‘自定义密码’
>
> session对象也是一个包含session变量和关联值的键值对的字典对象

## 设置session

```python
session['key']=value
```

## 释放session

```python
session.pop（‘key’，None）
```

# flask重定向和错误

> 调用时，返回一个相应对象，并将用户重定向到具有指定状态码的另一个目标的位置

## 原型（redirect）

```python
redirext(location[路径],statuscode[默认302],response[实例化响应])
```

## abort（错误码）：返回错误

```python
400:错误的请求
401：用于未经身份验证
403：没有权限
404：未找到
406：不可接受
415：用于不支持的媒体类型
429：请求过多
```

# flask：消息闪烁

> 一个好的基于GUI的应用程序向用户提供关于交互的反馈；如：消息框
>
> flask框架的闪烁系统使得可以在有一个视图中创建一个消息并将其呈现在 名为  **next** 的视图函数中

## flash（）：将消息传递给下一个请求，该请求通常是一个模板

```mysql
flash（刷新的实际消息，“错误/信息/警告”【可选参数】）：
```

## get_flashed_messages()：从session中删除消息

```python
get_flashed_messages(with_categories【可选参数】,category_filter【可选参数】)
如果收到的消息有具体类别，则第一参数是元组形式；第二个参数对于仅显示特定消息很有用
```

## 应用

### 模板

```python
{% with messages = get_flashed_messages() %}
	{% if messages%}
		{% for message in messages %}
        	{{message}}
         {% endfor%}
     {% endif%}
{% endwith%}
```

### py文件

```python
...
@app.route("/")
def index():
    return rend_template('index.html')

@app.route("/login",methods=['POST','GET'])
def login():
    error=None
    if request.method=='POST':
        if request.form['username'] != 'admin' or request.form['password']!='admin':
            error='账号或密码不正确，请再试一次'
        else:
            flash("您已经成功登录了")
            return redirect(url_for("index"))
    return rend_template('login.html',error=error)   # 如果验证不成功，登录模板将重新显示并显示错误消息
```

### 模板

#### login.html

```html
。。。
<body>

	{% if error %}
    	error:{{error}}
     {% endif %}
    
    <form action="login" method=post>
    	<input type='text' name='username' value='{{request.form.username}}'>
        <input type='password' name='password'>
    	<input type='submit' value='登录'>	
    </form>

</body>
```

#### index.html:登录成功，在此模板闪烁成功的消息

```html
。。。
<body>
    {% with messages=get_flashed_messages() %}
    	{% if messages %}
    		{% for message in messages%}
    			{{message}}
    		{% endfor %}
    	{% endif %}
    {% endwith%}
    
    <a href='{{url_for('login')}}'>登录？</a>	
</body>

```

# 文件上传

## 模板

```html
。。。
<fom action='地址/uploader' method='POST' enctype='multipart/form-data'>
    <input type='file' name='file'>
    <input type='submit' value='上传'>
</fom>
```

## py文件

```python
import os

@app.route("/uploader",methods=['GET','POST'])
def upload_file():
    f=request.files['file']
    filename=str(math.ceil(time.time() * 1000000))+"+"+str(utell)+"+"+secure_filename(file.filename)
    path=os.path.join("./","update",filename)
    file.save(path)
    return "ok"
```

# flask扩展

> 为flask应用程序添加了特定类型的支持。flask扩展注册表是一个可用扩展的目录，所需的扩展名可以通过pip下载

- flask扩展名通常命名为flask-foo，要导入   ：  from flask_foo import [class,function]
- 低于0.7的flask版本， 使用 from flask。ext import foo
- 需要激活兼容性模块，可以用flaskext_compat.py来安装：

```python
import flaskext_compat
flaskext_compat.activate()
from flask.ext import foo
```

## Flask Mail:为flask应用程序提供SMTP接口

> 使得用任何电子邮件服务器设置一个简单的界面变得非常简单

### 安装

```python
pip install Flask-Mail
```

### 配置Flask-Mail

| 序号 | 参数和说明                                                   |
| ---- | :----------------------------------------------------------- |
| 1    | MAIL_SERVER 邮件服务器的名称/IP地址                          |
| 2    | MAIL_PORT 服务器的端口号                                     |
| 3    | MAIL_USE_TLS 启用/禁用传输层安全层加密                       |
| 4    | MAIL_USE_SSL 启用/禁用安全套接字层加密                       |
| 5    | MAIL_DEBUG 调试支持。默认使                                  |
| 6    | MAIL_USERNAME 发件人的用户名                                 |
| 7    | MAIL_PASSWORD 发件人的密码                                   |
| 8    | MAIL_DEFAULT_SENDER 设置默认发件人                           |
| 9    | MAIL_MAX_EMAILS 设置要发送的最大邮件大小                     |
| 10   | MAIL_SUPPRESS_SEND 如果app.testing设置为True，则发送被抑制   |
| 11   | MAIL_ASCII_ATTACHMENTS 如果设置为True，则将附加的文件名转换为ASCII |

```python
Flask邮件模块包含以下重要类的定义。

邮件类：它管理电子邮件消息的要求。类构造函数采用以下形式 -
`flask-mail.Mail(app = None)`
构造器将Flask应用程序对象作为参数。

Mail类的方法
	序号	方法和说明
	1	send() 发送Message类对象的内容
	2	connect() 与邮件主机打开连接
	3	send_message() 发送消息对象

消息类
： 它封装了一封电子邮件。消息类的构造函数有几个参数 -
flask-mail.Message(subject, recipients, body, html, sender, cc, bcc,
   reply-to, date, charset, extra_headers, mail_options, rcpt_options)
消息类方法
	attach（） - 向消息添加附件。 该方法采用以下参数 -
		文件名 - 要附加的文件的名称
		content_type - 文件的MIME类型
		数据 - 原始文件数据
		处置 - 内容处置，如果有的话。
	add_recipient（） - 向消息添加另一个收件人

在以下示例中，Google的Gmail服务的SMTP服务器用作Flask-Mail配置的MAIL_SERVER。

第1步 - 在代码中从flask-mail模块导入Mail和Message类。
	from flask_mail import Mail, Message

第2步 - 然后根据以下设置配置Flask-Mail。
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
    app.config['MAIL_PASSWORD'] = '*****'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    
第3步 - 创建一个Mail类的实例。
	mail = Mail(app)
    
第4步 - 在由URL规则映射的Python函数 （'/'）中 设置Message对象。
    @app.route("/")
    def index():
       msg = Message('Hello', sender = 'yourId@gmail.com', recipients = ['id1@gmail.com'])
       msg.body = "This is the email body"
       mail.send(msg)
       return "Sent"
    
第5步 - 整个代码如下。 在Python Shell中运行以下脚本并访问 http：// localhost：5000 /。

    from flask import Flask
    from flask_mail import Mail, Message

    app =Flask(__name__)
    mail=Mail(app)
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
    app.config['MAIL_PASSWORD'] = '*****'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail = Mail(app)

    @app.route("/")
    def index():
       msg = Message('Hello', sender = 'yourId@gmail.com', recipients = ['id1@gmail.com'])
       msg.body = "Hello Flask message sent from Flask-Mail"
       mail.send(msg)
       return "Sent"

    if __name__ == '__main__':
       app.run(debug = True)
请注意，Gmail服务中的内置不安全功能可能会阻止此登录尝试。您可能不得不降低安全级别。请登录到您的Gmail帐户并访问此链接以降低安全性。
```

## Flask WTF : 一个灵活的表单，渲染和验证库

> 增加了WTForms的渲染和验证
>
> 注意： 已安装的软件包包含一个 **Form** 类，该类必须用作用户定义表单的父级

### 安装

> pip install flask-WTF

### **WTforms** 包包含各种表单域的定义。

| 序号 | 标准表格字段和说明                                      |
| ---- | ------------------------------------------------------- |
| 1    | TextField 代表<input type ='text'> HTML表单元素         |
| 2    | BooleanField 代表<input type ='checkbox'> HTML表单元素  |
| 3    | DecimalField 用小数显示数字的文本字段                   |
| 4    | IntegerField 用于显示整数的TextField                    |
| 5    | RadioField 代表<input type ='radio'> HTML表单元素       |
| 6    | SelectField 表示选择表单元素                            |
| 7    | TextAreaField 代表<testarea> html表单元素               |
| 8    | PasswordField 代表<input type ='password'> HTML表单元素 |
| 9    | SubmitField 表示<input type ='submit'>表单元素          |

### WTForms包也包含验证器类。

在验证表单域时非常有用。以下列表显示了常用的验证器。

| Sr.No | 验证器类和描述                                    |
| ----- | ------------------------------------------------- |
| 1     | DataRequired 检查输入栏是否为空                   |
| 2     | Email 检查字段中的文本是否遵循电子邮件ID约定      |
| 3     | IPAddress 验证输入字段中的IP地址                  |
| 4     | Length 验证输入字段中字符串的长度是否在给定范围内 |
| 5     | NumberRange 在给定范围内的输入字段中验证一个数字  |
| 6     | URL 验证输入字段中输入的URL                       |

```python
全部的检验字段：
'DataRequired', 'data_required', 'Email', 'email', 'EqualTo', 'equal_to',
'IPAddress', 'ip_address', 'InputRequired', 'input_required', 'Length',
'length', 'NumberRange', 'number_range', 'Optional', 'optional',
'Required', 'required', 'Regexp', 'regexp', 'URL', 'url', 'AnyOf',
'any_of', 'NoneOf', 'none_of', 'MacAddress', 'mac_address', 'UUID',
'ValidationError', 'StopValidation'
```



### 例子

#### 第一步：创建表单

```python
from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,
   SelectField
from wtforms import validators, ValidationError
# 表单
class ContactForm(Form):
   name = TextField("Name Of Student",[validators.Required("Please enter
      your name.")])
   # 表单对象的 validate（） 函数验证表单数据，并在验证失败时抛出验证错误。该错误消息被发送到模板。在HTML模板中，错误消息是动态呈现的。
  #{% for message in form.name.errors %}
  #  {{ message }}
  #{% endfor %}                                                        
   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
   Address = TextAreaField("Address")
   email = TextField("Email",[validators.Required("Please enter your email address."),
      validators.Email("Please enter your email address.")])
   Age = IntegerField("age")
   language = SelectField('Languages', choices = [('cpp', 'C++'),
      ('py', 'Python')])
   submit = SubmitField("Send")
除了 'name' 字段之外，还会自动创建一个CSRF令牌的隐藏字段。这是为了防止 跨站请求伪造攻击
验证器应用于 名称 和 电子邮件 字段。                                                           
```

说明

```python
渲染时，这将产生一个类似等效的HTML脚本，如下所示。
<input id = "csrf_token" name = "csrf_token" type = "hidden" />
<label for = "name">Name Of Student</label><br>
<input id = "name" name = "name" type = "text" value = "" />
```

#### 第二步： 放入到应显示表单的页面

```python
from flask import Flask, render_template, request, flash
from forms import ContactForm
app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
   form = ContactForm()
   if request.method == 'POST':
      if form.validate() == False:
         flash('All fields are required.')
         return render_template('contact.html', form = form)
      else:
         return render_template('success.html')
   elif request.method == 'GET':
      return render_template('contact.html', form = form)

if __name__ == '__main__':
   app.run(debug = True)
```

#### html内容

```html
<!doctype html>
<html>
   <body>
      <h2 style = "text-align: center;">Contact Form</h2>
      {% for message in form.name.errors %}
         <div>{{ message }}</div>
      {% endfor %}
      {% for message in form.email.errors %}
         <div>{{ message }}</div>
      {% endfor %}
      <form action = "http://localhost:5000/contact" method = post>
         <fieldset>
            <legend>Contact Form</legend>
            {{ form.hidden_tag() }}
            <div style = font-size:20px; font-weight:bold; margin-left:150px;>
               {{ form.name.label }}<br>
               {{ form.name }}
               <br>
               {{ form.Gender.label }} {{ form.Gender }}
               {{ form.Address.label }}<br>
               {{ form.Address }}
               <br>
               {{ form.email.label }}<br>
               {{ form.email }}
               <br>
               {{ form.Age.label }}<br>
               {{ form.Age }}
               <br>
               {{ form.language.label }}<br>
               {{ form.language }}
               <br>
               {{ form.submit }}
            </div>
         </fieldset>
      </form>
   </body>
</html>
```

## Flask SQLAlchemy ：一个功能强大的 **OR映射器** 

### 安装

> ```python
> pip install flask-sqlalchemy
> ```

### 从该模块导入SQLAlchemy类。

```python
from flask_sqlalchemy import SQLAlchemy
```

### 现在创建一个Flask应用程序对象并为要使用的数据库设置URI。

```python
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3
```

### 然后用应用程序对象作为参数创建一个SQLAlchemy类的对象。 

该对象包含ORM操作的辅助函数。它还提供了一个使用其声明用户定义模型的父级模型类。

#### 在下面的代码片段中，创建了一个 **学生** 模型。

```python
db = SQLAlchemy(app)
class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))  
   addr = db.Column(db.String(200))
   pin = db.Column(db.String(10))
   def __init__(self, name, city, addr,pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin
```

### 要创建/使用URI中提到的数据库，请运行 **create_all（）** 方法。

```python
db.create_all()
```

**SQLAlchemy** 的 **Session** 对象管理 **ORM** 对象的所有持久性操作。

### 执行CRUD操作 -

- **db.session.add** （模型对象） - 将一条记录插入到映射表中
- **db.session.delete** （模型对象） - 从表中删除记录
- **model.query.all（）** - 从表中检索所有记录（对应于SELECT查询）。

可以使用filter属性将筛选器应用于检索到的记录集。例如，为了在学生表中检索 **city ='Hyderabad'的** 记录，请使用以下语句 -

```
Students.query.filter_by(city = ’Hyderabad’).all()
```

### 例子

#### app.py

```python
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))
   addr = db.Column(db.String(200))
   pin = db.Column(db.String(10))

def __init__(self, name, city, addr,pin):
   self.name = name
   self.city = city
   self.addr = addr
   self.pin = pin

@app.route('/')
def show_all():
   return render_template('show_all.html', students = students.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['city'] or not request.form['addr']:
         flash('Please enter all the fields', 'error')
      else:
         student = students(request.form['name'], request.form['city'],
            request.form['addr'], request.form['pin'])

         db.session.add(student)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)
```

#### showall.html

```html
<!DOCTYPE html>
<html lang = "en">
   <head></head>
   <body>
      <h3>
         <a href = "{{ url_for('show_all') }}">Comments - Flask
            SQLAlchemy example</a>
      </h3>
      <hr/>
      {%- for message in get_flashed_messages() %}
         {{ message }}
      {%- endfor %}
      <h3>Students (<a href = "{{ url_for('new') }}">Add Student</a>)</h3>
      <table>
         <thead>
            <tr>
               <th>Name</th>
               <th>City</th>
               <th>Address</th>
               <th>Pin</th>
            </tr>
         </thead>
         <tbody>
            {% for student in students %}
               <tr>
                  <td>{{ student.name }}</td>
                  <td>{{ student.city }}</td>
                  <td>{{ student.addr }}</td>
                  <td>{{ student.pin }}</td>
               </tr>
            {% endfor %}
         </tbody>
      </table>
   </body>
</html>
```

#### new.html

```html
<!DOCTYPE html>
<html>
   <body>

      <h3>Students - Flask SQLAlchemy example</h3>
      <hr/>

      {%- for category, message in get_flashed_messages(with_categories = true) %}
         <div class = "alert alert-danger">
            {{ message }}
         </div>
      {%- endfor %}

      <form action = "{{ request.path }}" method = "post">
         <label for = "name">Name</label><br>
         <input type = "text" name = "name" placeholder = "Name" /><br>
         <label for = "email">City</label><br>
         <input type = "text" name = "city" placeholder = "city" /><br>
         <label for = "addr">addr</label><br>
         <textarea name = "addr" placeholder = "addr"></textarea><br>
         <label for = "PIN">City</label><br>
         <input type = "text" name = "pin" placeholder = "pin" /><br>
         <input type = "submit" value = "Submit" />
      </form>

   </body>
</html>

```

## Flask Sijax-Sijax接口：轻松地将 **Ajax** 带入您的应用程序。

>  它使用 **jQuery.ajax**来发出AJAX请求。使AJAX易于在web应用程序中使用Python/jQuery库

### 安装：

> pip install flask-sijax

### 原理

```python
SIJAX_STATIC_PATH - 希望镜像Sijax javascript文件的静态路径。 默认位置是 static / js / sijax 。在这个文件夹中， 保存了sijax.js 和 json2.js 文件。

SIJAX_JSON_URI - 从中加载json2.js静态文件的URI

Sijax使用 JSON 在浏览器和服务器之间传递数据。这意味着浏览器需要本地支持 JSON 或从 json2.js 文件获得 JSON 支持。 **

以这种方式注册的函数不能提供 Sijax 功能，因为默认情况下它们不能使用 POST 方法访问（并且Sijax使用POST请求）。

要使 View 函数能够处理 Sijax 请求，可以使用 @ app.route（'/ url'，methods = ['GET'，'POST']） 通过POST对其进行访问 ， 或使用像这样的 @ flask_sijax.route 辅助装饰器-

@flask_sijax.route(app, '/hello')
每个Sijax处理函数（像这样）都会自动接收至少一个参数，就像Python将“自我”传递给对象方法一样。该 “obj_response” 参数是说话返回给浏览器的功能的方式。

def say_hi(obj_response):
   obj_response.alert('Hi there!')
当检测到Sijax请求时，Sijax像这样处理它 -

g.sijax.register_callback('say_hi', say_hi)
   return g.sijax.process_request()
```

### 例子

```python
import os
from flask import Flask, g
from flask_sijax import sijax

path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
app = Flask(__name__)

app.config['SIJAX_STATIC_PATH'] = path
app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'
flask_sijax.Sijax(app)

@app.route('/')
def index():
   return 'Index'

@flask_sijax.route(app, '/hello')
def hello():
   def say_hi(obj_response):
      obj_response.alert('Hi there!')
   if g.sijax.is_sijax_request:
      # Sijax request detected - let Sijax handle it
      g.sijax.register_callback('say_hi', say_hi)
      return g.sijax.process_request()
      return _render_template('sijaxexample.html')

if __name__ == '__main__':
   app.run(debug = True)
```

```python
当一个Sijax向服务器请求（一个特殊的 jQuery.ajax（） 请求）时，这个请求在服务器上g.sijax.is_sijax_request（） 检测到，在这种情况下，你让 Sijax 处理请求。
所有使用 g.sijax.register_callback（） 注册的函数都公开给浏览器进行调用。
调用 g.sijax.process_request（） 告诉Sijax执行适当的（之前注册的）函数并将响应返回给浏览器。
```

## flask Bootstrap:可以在程序中集成 `Bootstrap`

### 安装

> pip install flask-bootstrap

### 使用

```python
from flask_bootstrap import Bootstrap
#...
bootstrap = Bootstrap(app)
```

初始化 Flask-Bootstrap 之后，就可以在程序中使用一个包含所有Bootstrap 文件的基模版。这个模版利用 Jinja2 的模版继承机制，让程序扩展一个具有基本页面结构的基模版，其中就有用来引入 Bootstrap 的元素。

```html
{% extends "bootstrap/base.html" %}
{% block title %}Flasky{% endblock %}
{% block navbar %}
<div class="navbar navbar-inverse" role="navigation">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle"
            data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="/">Flasky</a>
        </div>
        <div class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li><a href="/">Home</a></li>
            </ul>
        </div>
    </div>
</div>
{% endblock %}

{% block content %}
<div class="container">
    <div class="page-header">
        <h1>Hello, {{ name }}!</h1>
    </div>
</div>
{% endblock %}
```

`Jinja2` 中的 `extends` 指令从 `Flask-Bootstrap` 中导入 `bootstrap/base.html`，从而实现模版继承。`Flask-Bootstrap` 中的基模版提供了一个网页框架，引入了 `Bootstrap` 中的所有 CSS 和 JavaScript 文件。

基模版中定义了可在衍生模版中重定义的块。`block` 和 `endblock` 指令定义的块中的内容可添加到基模版中。

上面这个示例定义了3个块，分别名为 `title`、`navbar`和`content`。这些块都是基模版提供的，可在衍生模版中重新定义。

### `Flask-Bootstrap` 的 `base.html` 模块定义的可用块。

| 块名         | 说明                       |
| ------------ | -------------------------- |
| doc          | 整个HTML文档               |
| html_attribs | <html> 标签的属性          |
| html         | <html> 标签的内容          |
| head         | <head> 标签的内容          |
| title        | <title> 标签的内容         |
| metas        | 一组 <meta> 标签           |
| styles       | 层叠样式表定义             |
| body_attribs | <body> 标签的属性          |
| body         | <body> 标签的内容          |
| navbar       | 用户自定义的导航条         |
| content      | 用户定义的页面内容         |
| scripts      | 文档底部的 JavaScript 声明 |

### 注意：

上表中很多块都是 `Flask-Bootstap` 自用的， 如果直接重定义可能会导致一些问题。如果程序需要向已经有内容的块中添加新内容， 必须使用 `Jinja2` 提供的 `super()` 函数。例如，如果要在衍生模版中添加新的 `JavaScript` 文件，需要这么定义：

```javascript
{% block scripts %}
{{ super() }}
<script type="text/javascript" src="my-script.js"></script>
{% endblock %}
```

# flask面试题

## 1、解释什么是Flask及其好处?

```python
Flask是一个Python编写的Web微框架，让我们可以使用Python语言快速实现一个网站或Web服务。
```

## 2、django和flask的区别

```python
Flask
    Flask确实很“轻”，不愧是Micro Framework，从Django转向Flask的开发者一定会如此感慨，除非二者均为深入使用过
    Flask自由、灵活，可扩展性强，第三方库的选择面广，开发时可以结合自己最喜欢用的轮子，也能结合最流行最强大的Python库
    入门简单，即便没有多少web开发经验，也能很快做出网站
    非常适用于小型网站
    非常适用于开发web服务的API
    开发大型网站无压力，但代码架构需要自己设计，开发成本取决于开发者的能力
    各方面性能均等于或优于Django
    Django自带的或第三方的好评如潮的功能，Flask上总会找到与之类似第三方
    Flask灵活开发，Python高手基本都会喜欢Flask，但对Django却可能褒贬不
    Flask与关系型数据库的配合使用不弱于Django，而其与NoSQL数据库的配合远远优于Django
    Flask比Django更加Pythonic，与Python的philosophy更加吻合
Django
    Django太重了，除了web框架，自带ORM和模板引擎，灵活和自由度不够高
    Django能开发小应用，但总会有“杀鸡焉用牛刀”的感觉
    Django的自带ORM非常优秀，综合评价略高于SQLAlchemy
    Django自带的模板引擎简单好用，但其强大程度和综合评价略低于Jinja2
    Django自带ORM也使Django与关系型数据库耦合度过高，如果想使用MongoDB等NoSQL数据，需要选取合适的第三方库，且总感觉Django+SQL才是天生一对的搭配，Django+NoSQL砍掉了Django的半壁江山
    Django目前支持Jinja等非官方模板引擎
    Django自带的数据库管理app好评如潮
    Django非常适合企业级网站的开发：快速、靠谱、稳定
    Django成熟、稳定、完善，但相比于Flask，Django的整体生态相对封闭
    Django是Python web框架的先驱，用户多，第三方库最丰富，最好的Python库，如果不能直接用到Django中，也一定能找到与之对应的移植
    Django上手也比较容易，开发文档详细、完善，相关资料丰富
```

## 3、Flask-WTF是什么，有什么特点?

Flask的简单WTForms集成，包含CSRF、文件上传和Recaptcha集成。

flask-wtf可以保护表单免受跨站请求伪造（CSRF）的攻击,恶意网站将请求发送到被攻击者已登录的其他网站时就会引发CSRF

## 4、Flask脚本的常用方式是什么?

在shell中运行脚本文件
在python编译器中run

## 5、如何在Flask中访问会话?

一个会话基本上允许记住从一个请求到另一个请求的信息。在Flask中，它使用签名的cookie，以便用户可以查看会话内容并进行修改。用户可以修改会话，只要它有密钥Flask.secret_key。

会话（seesion）会话数据存储在服务器上。 会话是客户端登录到服务器并注销的时间间隔。 需要在此会话中进行的数据存储在服务器上的临时目录中。

```python
from flask import session导入会话对象
session[‘name’] = ‘admin’给会话添加变量
session.pop(‘username’, None)删除会话的变量
```

## 6、解释Python Flask中的数据库连接?

python中的数据库连接有两种方式
在脚本中以用第三方库正常连接，用sql语句正常操作数据库，如mysql关系型数据库的pymsql库
用ORM来进行数据库连接，flask中典型的flask_sqlalchemy，已面向对象的方式进行数据库的连接与操作

##  7、Flask框架依赖组件?

- Route(路由)
- templates(模板)
- Models(orm模型)
- blueprint(蓝图)
- Jinja2模板引擎

## 8、列举使用过的Flask第三方组件?

flask_bootstrap
flask-WTF
flask_sqlalchemy

## 9、简述Flask上下文管理流程?

每次有请求过来的时候，flask 会先创建当前线程或者进程需要处理的两个重要上下文对象，把它们保存到隔离的栈里面，这样视图函数进行处理的时候就能直接从栈上获取这些信息。

## 10、Flask中多app应用是怎么完成?

请求进来时，可以根据URL的不同，交给不同的APP处理

## 11、wtforms组件的作用?

WTForms是一个支持多个web框架的form组件，主要用于对用户请求数据进行验证。

## 12、Flask框架默认session处理机制?

Flask的默认session利用了Werkzeug的SecureCookie，把信息做序列化(pickle)后编码(base64)，放到cookie里了。

过期时间是通过cookie的过期时间实现的。

为了防止cookie内容被篡改，session会自动打上一个叫session的hash串，这个串是经过session内容、SECRET_KEY计算出来的，看得出，这种设计虽然不能保证session里的内容不泄露，但至少防止了不被篡改

## 13、ORM的实现原理?

概念： 对象关系映射（Object Relational Mapping，简称ORM，或O/RM，或O/R mapping），是一种程序技术，用于实现面向对象编程语言里不同类型系统的数据之间的转换。

详细介绍：让我们从O/R开始。字母O起源于”对象”(Object),而R则来自于”关系”(Relational)。几乎所有的程序里面，都存在对象和关系数据库。在业务逻辑层和用户界面层中，我们是面向对象的。当对象信息发生变化的时候，我们需要把对象的信息保存在关系数据库中。 
当你开发一个应用程序的时候(不使用O/R Mapping),你可能会写不少数据访问层的代码，用来从数据库保存，删除，读取对象信息，等等。你在DAL中写了很多的方法来读取对象数据，改变状态对象等等任务。而这些代码写起来总是重复的。 
ORM解决的主要问题是对象关系的映射。域模型和关系模型分别是建立在概念模型的基础上的。域模型是面向对象的，而关系模型是面向关系的。一般情况下，一个持久化类和一个表对应，类的每个实例对应表中的一条记录，类的每个属性对应表的每个字段。

## 14、ORM技术特点：

1.提高了开发效率。由于ORM可以自动对Entity对象与数据库中的Table进行字段与属性的映射，所以我们实际可能已经不需要一个专用的、庞大的数据访问层。 
2.ORM提供了对数据库的映射，不用sql直接编码，能够像操作对象一样从数据库获取数据。

## 15、Flask的依赖

Werkzeug 一个WSGI工具包（web服务网关接口（Python Web Server Gateway Interface，缩写为WSGI）是为python语言定义的web服务器和web应用程序或框架之间的一种简单而通用的借口，其他语言也有类似的接口）
jinja2模板引擎

## 16、Flask是一个MVC模型吗?如果是，可以示例一下吗?

- flask是一个典型的MVC框架
- MVC框架，图形理解 
  ![这里写图片描述](https://img-blog.csdn.net/20180720202921719?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dsX3B5dGhvbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
- flask项目中的MVC理解 
  ![这里写图片描述](https://img-blog.csdn.net/20180720202930363?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dsX3B5dGhvbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)