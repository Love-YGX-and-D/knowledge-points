# for循环的下标

```python

```

# 过滤器

> 过滤器是通过管道负号（|）进行使用的
>
> {{ name | length }}  :返回name的长度

## abs:返回一个数的绝对值

> {{ -1 | abs }}

## default(value,default_value,boolean=false):当前没有变量值，用参数值代替

> {{ name | default('小红') }} :=> 入伙name不存在，则使用  ` 小红`代替
>
> boolean=False  =》 ： 默认在只有这个变量为undefined的时候才会使用default中的默认值；   如果想使用python的形式判断是否为false，则可以传递boolean=true。可以使用or

## escape(value)/e: 转义字符

> 将value中的<>等符号转义为HTML重的符号
>
> {{ content |escape }}     或者  {{ content | e }}

## first（value）：返回一个序列的第一个元素

> {{ name | first  }}

## last（value）：返回一个序列的最后一个元素

> {{ name | last}}

## format(value,*args,**kargs):格式化字符串

> {{ '%s'-'%s' | format('Hello','Foo!')}}  => 输出  ： Hello - Foo！

## length(value) :返回一个序列或者字典的长度

> {{ name|length }}

## join(value,d='拼接符')：返回一个序列用d这个参数的值拼接成的字符串

> {{ array | join(',')}}

## safe(value)：特殊

> 如果开启了全局转义，那么safe过滤器会将变量关掉转义。
>
> {{ content_html | safe }}

## int(value):将值转换为整形

## float(value):将值转换为浮点型

## string（value）： 将value转换为字符串

## lower（value）：将字符变为小写

## upper（value）：将字符变为大写

## replace（value，old，new）：替换

>  将old替换为new

## truncate（value，length=255，killwords=False）截取length长度的字符串

## trim：截取字符串前面和后面的空白字符串

## wordcount（value）：计算长字符串中单词个数



