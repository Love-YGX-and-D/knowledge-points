b-s架构：可以随时访问最新的内容， 免去用户的下载，  延迟在于网络，不能够流畅的操作，体验不好

c-s架构：延迟在与硬件，必须有客户端，更新不及时

ajax：数据更新，体验性更好

# URL(Uniform Resource Locator,统一资源定位符),

# ajax步骤：

```js
1. var ajax=new XMLHttpRequest（）
2. ajax.onload=function（）{
   ajax.response监听返回页面数据   以文本的方式返回【字符串】
   ajax的返回值【获取数据】 
     ajax.responseType=“document”  指定获取的文本类型【默认text】json/txt/document/blog【二进制】
     文本/str: ajax.response
     文档: ajax.responseXML

}

3. ajax.open（“数据获取方式”，“操作页面”）
4. ajax.send（） 发送界面
```



# a ：ajax解决的问题

## 1.按需获取东西/数据

## 2. 页面无刷新获取 /操作数据

## 3. 让基于B-S架构的软件能够像C-S结构的软件操作流畅

# b：async JavaScript and xml

# c：new XMLHttpRequeset

# d：open()    send()   onload()

# e:可以处理多种类型的返回的数据

> text json blob arraybuffer document

# f：传递数据 get /post

# g：封装ajax

```js

function ajax(params,div) {
  //判断输入处理数据是否合法
    if (typeof params!=="object"){
        console.error("参数类型不对")
        return
    }
 //判断url是否存在
    var url=params.url
    if (!url){
        console.error("请输入有效的地址路径")
        return
    }
//数据处理
    var type=params.type ||"get"
    var dataType=params.dataType||"text"
    var data=params.data
    if (typeof  data=="object"){
        var str=""
        for (i in data){
            str+=i+'='+data[i]+'&'
        }
        str=str.slice(0,-1)
    }
//ajax执行
    var ajax=new XMLHttpRequest()
    if (type=="get"){
        ajax.onload=function(){
            document.querySelector(div).innerHTML=ajax.response
            params.success(params.data)
        }
        ajax.open(type,url+"?"+str)
        ajax.send()
    }else{
        ajax.onload=function(){
            document.querySelector(div).innerHTML=ajax.response
            params.success(params.data)
        }
        ajax.open(type,url)
        ajax.setRequestHeader("content-type","application/x-www-form-urlencoded")
        ajax.send(str)
    }
}
//功能实现
var btns=document.querySelector("button")
btns.onclick=function(){
    ajax({
        url:"/ajax",
        type:"post",   //默认get
        dataType:"Text",  //默认text
        data:{name:"zhangsan",age:18},
        success:function (data1) {
            console.log(data1)
        }
    },div="div")
}
```

# ajax和服务器的优缺点

## ajax：

### 优点：

用户体验性比较流畅，减轻服务器压力，有利于协同工作

### 缺点

首页加载速度慢，业务逻辑清晰不清晰，人的工作量比较大

## 服务器：

### 优点

首页加载速度快，业务逻辑清晰，工作量少

### 缺点

用户体验性差，服务器压力大，不利于协同开发

### mvvm：model[模型-数据] view[视图-模板-html+css]

> 数据到视图，视图到数据，   双向数据绑定

angular    react    vue

#ajax跨域
## 1.jsonp 
###优点:快捷,访问速度快,
###缺点:诸多限制,局限小 两个服务器都是自己的,或者对方配合法让服务
###原理:利用script标签对跨域的问题
###应用:jquery

## 2.代理 流程比较复杂,几乎没有限制
### 优点:没有任何优点
### 缺点:效率慢
### 原理:python具有客户端的能力
### 应用:爬虫,动态跨域获取信息



# 实例

```css

var ajax=new XMLHttpRequest()
ajax.onload=()=>{
    this.name=JSON.parse(ajax.response)[0].name
    this.age=JSON.parse(ajax.response)[0].age
    this.sex=JSON.parse(ajax.response)[0].sex
}
ajax.open("get","/ajax/one?id="+this.id)
ajax.send()
```

# fetch

```css
var str="id="+this.id+"&name="+this.name+"&age="+this.age+"&sex="+this.sex
fetch("/ajax/edit?"+str).then((e)=> {
    return e.text()
}).then((e)=> {
    if (e=="ok"){
        this.$router.push("/")
    }
})
```

