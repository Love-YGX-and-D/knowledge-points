# 简单开始创建

## 创建项目

```python
django-admin startproject 项目名称
```

## Django应用包中的目录信息

```python
mysite
	__init__.py
    settings.py 配置文件
    urls.py	路由文件
    wsgi.py 服务器文件
    mange.py django指令文件
```

## 创建Django应用

```python
python manage.py startapp 应用名

mysite 项目包
polls 应用包
	migrations 迁移文件包
    --init__.py
    admin.py 自定义后台界面
    apps.py 应用的一些配置，主要设置应用名称
    models.py 数据模型（要创建什么数据表，表结构）
    tests.py 测试文件
    views.py 视图(MVT中的V)
manage.py 工具文件
```

## 配置项目（settings.py）

```python
1.	语言
	LANGUAGE_CODE = 'zh-hans'
2. 	时区
	TIME_ZONE = 'Asia/Shanghai'
3.	应用
    INSTALLED_APPS = [
		...,
        'polls', #应用名
    ]
4.	数据库
	# 默认数据库
	DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'polls',  #使用的数据库
            'HOST':'localhost',
            'PORT':3306,
            'USER':'root',
            'PASSWORD':'1002',
        }
    }
```

## 启动服务
```python
python manage.py runserver
python manage.py runserver 8080
python manage.py runserver 0.0.0.0:8000
```

## 创建视图

1. 在应用视图文件中创建视图函数(/应用/views.py)

   ```python
   from django.shortcuts import render
   from django.http import HttpResponse
   #jsonResponse   接受json数据
   # Create your views here.
   def index(request):  #参数
       return HttpResponse("123")
   
   ```

2. 在应用中创建路由文件(urls.py)

   ```python
   from django.urls import path
   from . import views
   urlpatterns = [
       path('',views.index,name=''),
       ...
   ]
   ```

3. 在项目文件包中导入应用路由，(mysite/urls.py)

   ```python
   from django.contrib import admin
   from django.urls import path,include
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('polls/', include("polls.urls")),
   ]
   ```


## 配置数据库

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "polls",
        'HOST':'127.0.0.1',
        'PORT':'3306',
        'USER':'ROOT',
        'PASSWORD':'1002'
    }
}
在mysite/__init__.py中写入
import pymysql
pymysql.install_as_MySQLdb()
```

## 创建数据库

```python
polls/models.py

from django.db import models

# Create your models here.

class Question(models.Model):
    question_text=models.CharField(max_length=200)   #必填选项max_length
    pub_date=models.DateTimeField()

class Choice(models.Model):
    question=models.ForsegnKey(to=Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
```

## 创建迁移文件

```python
python manage.py makemigrations polls
```
## 执行迁移文件
```python
python manage.py migrate
```
## 不能被实例

```mysql
class Metal:
	abstract =True
```

# 模型视图操作

## 数据获取

### 原生sql语句

```sql
lei.objects.raw('sql语言')
```



### 多选框

```python
request.POST.getlist('字段)
```

## 数据保存

### 数据添加

```python
# models.UserInfo.objects.create(user='yangmv', pwd='123456')
# 或者
# obj = models.UserInfo(user='yangmv', pwd='123456')
# obj.save()
# 或者
# dic = {'user': 'yangmv', 'pwd': '123456'}
# models.UserInfo.objects.create(**dic)
```



### 一对多（外键）：

```python
c=Class.objects.filter(id=c).first()
Student.objects.create(name=name,tell=tell,c=c)

```

### 一对一：

```python

```

### 多对多：

```python
projext.objects.add(1,2,3)
project.object.remove(1)
project.object.set()   #重置
project.object.clear()
```

## 数据修改

### 删除

```python
Course.objects.filter(id=id).delete()
```

### 修改/更新

```python
Course.objects.filter(id=id).update(字段=字段值)
```

# 加入静态js

```python
{% load static %}
<script src="{% static 'demo/js/jj.js'%}"></script>
路径设置：
	
```

# 数据单位创建

```python
字符：models.CharField(max_length=数,error_message={
    'required':'提示信息'    
}，validators=[ 自己或者系统带的验证函数  ])
邮箱：models.EmailField()
选择：models.IntegerField(
	choices=(
    	(0，男)，
        （1，女），
    )
)
布尔：models.BooleanField(default=True/False)
文本;models.TextField(max_length=数)
自增：models.AutoField(primary_key=True)
```

# 验证器

```python
# models层
name=models.CharField(max_length=20,validators=[my_validators1])

def my_validators1(value):
    id value[0:] != 'abc':
        raise ValidationError('必须以abc开头')
        

```

# 跨域

```python
在form中添加：
	{% csrf_token %}   #标签（跨域验证口令），解决跨域问题
    必须有返回值
```

# 过滤

```python
{{ h2 | safe }}
```

# form验证

```python
password=forms.CharField(max_length=16,help_text='密码长度不多于20位',label='密码',widget=forms.PasswordInput(attrs={
        'class':'类名'
    }))


前台取：
label： form。password.label
label的dom元素：form.password.label_tag


form.cleaned_date 
form.is_bound
```

# django使用富文本编辑器ck

```python
https://www.cnblogs.com/ianduin/p/7732983.html
```

# 静态文件加载

```python
css/js  加载
{% load static %}
<link rel="stylesheet" href="{% static '/pingtai/css/public.css' %}">

img加载
{% load staticfiles %}
<img src=" {% static '/pingtai/img/header_ad/logo.gif' %}" alt="">

加载模板
{% include '模板路径'%}
    
a链接

```

# session设置

## 保存数据库

### settings.py

```python
SESSION_ENGINE = 'django.contrib.sessions.backends.db'   # 引擎（默认）

SESSION_COOKIE_NAME = "sessionid"    # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
SESSION_COOKIE_PATH = "/"               # Session的cookie保存的路径（默认）
SESSION_COOKIE_DOMAIN = None            # Session的cookie保存的域名（默认）
SESSION_COOKIE_SECURE = False           # 是否Https传输cookie（默认）
SESSION_COOKIE_HTTPONLY = True          # 是否Session的cookie只支持http传输（默认）
SESSION_COOKIE_AGE = 1209600            # Session的cookie失效日期（2周）（默认）
SESSION_EXPIRE_AT_BROWSER_CLOSE = False        # 是否关闭浏览器使得Session过期（默认）
SESSION_SAVE_EVERY_REQUEST = False      # 是否每次请求都保存Session，默认修改之后才保存（默认）
	
```

### 使用

```python
# 获取、设置、删除Session中数据
request.session['k1']   #设置
request.session.get('k1',None)   #获取
request.session['k1'] = 123   #设置
request.session.setdefault('k1',123)   # 存在则不设置默认
del request.session['k1']   #删除


# 所有 键、值、键值对
request.session.keys()
request.session.values()
request.session.items()
request.session.iterkeys()
request.session.itervalues()
request.session.iteritems()

# 用户session的随机字符串
request.session.session_key

# 将所有Session失效日期小于当前日期的数据删除
request.session.clear_expired()

# 检查 用户session的随机字符串 在数据库中是否
request.session.exists("session_key")

# 删除当前用户的所有Session数据
request.session.delete("session_key")
request.session.clear()

request.session.set_expiry(value)
* 如果value是个整数，session会在些秒数后失效。
* 如果value是个datatime或timedelta，session就会在这个时间后失效。
* 如果value是0,用户关闭浏览器session就会失效。
* 如果value是None,session会依赖全局session失效策略。
```

## 文件

### setting.py

```python
SESSION_ENGINE = 'django.contrib.sessions.backends.file'    # 引擎
SESSION_FILE_PATH = None  or  '相对路径'                                   # 缓存文件路径，如果为None，则使用tempfile模块获取一个临时地址tempfile.gettempdir()                                                            # 如：/var/folders/d3/j9tj0gz93dg06bmwxmhh6_xm0000gn/T


SESSION_COOKIE_NAME ＝ "sessionid"        # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串
SESSION_COOKIE_PATH ＝ "/"                    # Session的cookie保存的路径
SESSION_COOKIE_DOMAIN = None                  # Session的cookie保存的域名
SESSION_COOKIE_SECURE = False                 # 是否Https传输cookie
SESSION_COOKIE_HTTPONLY = True                # 是否Session的cookie只支持http传输
SESSION_COOKIE_AGE = 1209600                  # Session的cookie失效日期（2周）
SESSION_EXPIRE_AT_BROWSER_CLOSE = False       # 是否关闭浏览器使得Session过期
SESSION_SAVE_EVERY_REQUEST = False            # 是否每次请求都保存Session，默认修改之后才保存
```

### 使用同数据库

## 缓存

### setings.py

```python
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # 引擎
SESSION_CACHE_ALIAS = 'default'                # 使用的缓存别名（默认内存缓存，也可以是memcache），此处别名依赖缓存的设置

SESSION_COOKIE_NAME ＝ "sessionid"    # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串
SESSION_COOKIE_PATH ＝ "/"                            # Session的cookie保存的路径
SESSION_COOKIE_DOMAIN = None                         # Session的cookie保存的域名
SESSION_COOKIE_SECURE = False                       # 是否Https传输cookie
SESSION_COOKIE_HTTPONLY = True                     # 是否Session的cookie只支持http传输
SESSION_COOKIE_AGE = 1209600                         # Session的cookie失效日期（2周）
SESSION_EXPIRE_AT_BROWSER_CLOSE = False               # 是否关闭浏览器使得Session过期
SESSION_SAVE_EVERY_REQUEST = False                   # 是否每次请求都保存Session，默认修改之后才保存
```

### 使用同数据库使用

## 缓存+数据库Session

### settings.py

```python
数据库用于做持久化，缓存用于提高效率
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'        # 引擎
```

### 使用同数据库

## 加密session

### setting.py

```python
 SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'   # 引擎
```

### 使用一样

## Session的用户验证

```python
def login(func):
    def wrap(request, *args, **kwargs):
        # 如果未登陆，跳转到指定页面
        if request.path == '/test/':
            return redirect('http://www.baidu.com')
        return func(request, *args, **kwargs)
    return wrap
```

# cookie

```python
cookies
获取cookies   request.COOKIES['username']
设置cookie      response.set_cookie('key','value',max_length=秒钟,expires=日期)
path="/" 那个页面下可以使用cookie
domain  =""  生效的域名
secure = False https传输
httponly = js中获取不到
```

# 验证码

> django-simple-captcha

## 安装django-simple-captcha

> pip install django-simple-captcha

## 配置

- 在settings.py中添加 应用  ‘captcha’，
- 在主路由中添加： path('captcha/', include('captcha.urls')),
- 执行迁移： python manage.py migrate
- 引入所需文件在自定义模板或者其他位置：  from captcha.fields import CaptchaField
- 在需要的地方实例 ： captcha=CaptchaField()
- 点击刷新参考下面的代码

## 验证码跨域问题的解决

```js
$('.captcha').click(function () {
    // $.ajaxSetup({data: {csrfmiddlewaretoken: '{{ csrf_token }}' },})  方式一
    $.ajax({
        url:'/captcha/refresh/',
        type:'post',
        // 方式二
        data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
        success:function (e) {
            $('.captcha').attr('src',e['image_url'])
            $('#id_yzm_0').val(e['key'])
        }
    })
})
```

# 模板和组件

## 模板

```python
# 模板写法
    {% extends '模板位置'%}
        {% block 模板名称 %}
    {% endblock  %}    
# 引入写法
	{% block 模板名称 %}
    {% endblock %}
```

## 组件

```python
{% include '组件位置' %}
```

# 带图片的

```python
mban(request.POST,request.FILES)
```

# 新添加提交

```python
form=moxing(request.form)
form.is_valid()
obj=from.save(commit=false)
obj.a=模型.objects.filter(条件).first()
obj.save()

```

# 中间件

```python
settings.py
	写入中间件 （middleware）



my（文件）
	__init__.py
    my.py

    
my.py
from django.utils.deprecation import MiddlewareMixin

class mys(MiddlewareMixin):
    def process_request(self,request):
        print('请求')   # 不能有return
    def process_respose(self,request,response):
        # 必须有return
        print('响应')
        return response
    def process_view(self,request,callback,callback_arg,callback_kwarg):
        print('ciew' )    # 不需要return
    def process_exception(self,request,exception):
        # 可跟可不跟
        # 不加return （先2后1）  在相应
        # 加return   执行2 ，后面不执行

class mys2(MiddlewareMixin):
    def process_request(self,request):
        print('请求2')   # 不能有return
    def process_respose(self,request,response):
        # 必须有return
        print('响应2')
        return response
    
    
    请求-请求2-试图-想应2-相应
```

# 字段唯一值等设置

```python
建立一个简易Model 

class Person(models.Model):   GENDER_CHOICES=(    (1,'Male'),    (2,'Female'),    )   name=models.CharField(max_length=30,unique=True,verbose_name='姓 名')    birthday=models.DateField(blank=True,null=True)   gender=models.IntegerField(choices=GENDER_CHOICES)   account=models.IntegerField(default=0)　　 
blank 

设置为True时，字段可以为空。设置为False时，字段是必须填写的。字符型字段CharField和TextField是用空字符串来存储空值的。 

null 

设置为True时，django用Null来存储空值。日期型、时间型和数字型字段不接受空字符串。所以设置IntegerField，DateTimeField型字段可以为空时，需要将blank，null均设为True。 

如果想设置BooleanField为空时可以选用NullBooleanField型字段。 

max_length 

为CharField型字段设置最大长度。 

choices 

由元素为2-tuples的序列(list或者tuple)作为字段的choices。2-tuple的第一个元素存储在数据库中，第二个元素可由 get_FOO_display方法得到。 

>>>p=Person(name='Sam',gender=1)  >>>p.save()  >>>p.gender  1  >>>p.get_gender_display()  u'Male' 
如果choices的选项过多的话，最好考虑使用ForiegnKey。 

default 

为字段设定默认值。 

默认值不能是一个可变对象（模型实例，列表，集合等），作为到同一个实例的参考，该对象将用作所有新的模型实例中的默认值。相反，在一个可调用的对象中封装所需的默认值。例如，如果你有一个自定义JSONField，并希望指定一个作为默认的字典，使用一个lambda表达式如下： 

contact_info = JSONField("ContactInfo", default=lambda:{"email": "to1@example.com"}) 
verbose_name 

设置此字段在admin界面上的显示名称。 

unique 

设置为True，此字段在数据库中必须是唯一的。 

>>>p=Person(name='Sam',gender=1)  >>>p.save()  >>>p=Person(name='Sam',gender=2)  >>>p.save()  IntergrityError: column name is not unique 
primary_key 

如果设置为True，则此字段成为Model的主键。一般情况下，django会为Model自动添加一个叫id的IntegerField字段作为主键。
```

