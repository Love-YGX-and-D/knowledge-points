# 列举Http请求中常见的请求方式?

http请求中的8种请求方法

1、opions 返回服务器针对特定资源所支持的HTML请求方法 或web服务器发送*测试服务器功能（允许客户端查看服务器性能）

2、Get 向特定资源发出请求（请求指定页面信息，并返回实体主体）

3、Post 向指定资源提交数据进行处理请求（提交表单、上传文件），又可能导致新的资源的建立或原有资源的修改

4、Put 向指定资源位置上上传其最新内容（从客户端向服务器传送的数据取代指定文档的内容）

5、Head 与服务器索与get请求一致的相应，响应体不会返回，获取包含在小消息头中的原信息（与get请求类似，返回的响应中没有具体内容，用于获取报头）

6、Delete 请求服务器删除request-URL所标示的资源*（请求服务器删除页面）

7、Trace 回显服务器收到的请求，用于测试和诊断

8、Connect HTTP/1.1协议中能够将连接改为管道方式的代理服务器

http服务器至少能实现get、head、post方法，其他都是可选的

# 列举Http请求中的状态码?

## 1xx: 信息

![信息](https://img-blog.csdn.net/20180729162230376?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxODkxODAz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

## 2XX：成功

![成功](https://img-blog.csdn.net/20180729162334281?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxODkxODAz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

## 3XX：重定向

![重点向](https://img-blog.csdn.net/20180729162408735?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxODkxODAz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

## 4XX：客户端错误

![客户端错误](https://img-blog.csdn.net/20180729162433410?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxODkxODAz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)![这里写图片描述](https://img-blog.csdn.net/20180729162443895?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxODkxODAz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

## 5XX：服务器错误

![服务器错误](https://img-blog.csdn.net/20180729162525800?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxODkxODAz/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

# 列举Http请求中常见的请求头?

•Accept:浏览器可接受的MIME类型 
•Accept-Charset: 浏览器通过这个头告诉服务器，它支持哪种字符集 
•Accept-Encoding:浏览器能够进行解码的数据编码方式，比如gzip 
•Accept-Language:浏览器所希望的语言种类，当服务器能够提供一种以上的语言版本时要用到。可以在浏览器中进行设置。 
•Host:初始URL中的主机和端口 
•Referer:包含一个URL，用户从该URL代表的页面出发访问当前请求的页面 
•Content-Type:内容类型 
•If-Modified-Since: Wed, 02 Feb 201112:04:56 GMT利用这个头与服务器的文件进行比对，如果一致，则从缓存中直接读取文件。 
•User-Agent:浏览器类型. 
•Content-Length:表示请求消息正文的长度 
•Connection:表示是否需要持久连接。如果服务器看到这里的值为“Keep -Alive”，或者看到请求使用的是HTTP 1.1（HTTP 1.1默认进行持久连接 
•Cookie:这是最重要的请求头信息之一 
•Date：Date: Mon, 22 Aug 2011 01:55:39 GMT请求时间GMT

