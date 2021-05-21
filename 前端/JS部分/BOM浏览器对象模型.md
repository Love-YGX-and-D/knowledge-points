BOM： 浏览器对象模型

> 完成窗口与窗口之间的通信，window对象是其核心对象，

- ##### history【前进，后退，刷新】  是一个对象   使用【window.history】

- ##### location【地址】

- ##### DOM【】

- ##### screen【屏幕】

- ##### frames[真窗口]

- ##### navigation

# window对象：

## 属性

### 1-1：获取浏览器宽高

```css
a.ie8及以上
    window.innerWidth   [获取浏览器宽度] 
    window.innerHeight	[获取浏览器高度]
b.ie8以下
    document.documentElement.ClientWidth [宽度]
    document.documentElement.ClientHeight	【高度】
```

### 1-2： 重新获取浏览器宽高

```
window.onreset=function () {
    NewW=window.innerWidth;
    NewH=window.innerHeight;
}
```

### 1-3：重新设置浏览器大小

​	window.onresize=function（）{

​	}

### 1-4：浏览器滚动事件

​	window.onscroll=function （）{

​	}

### 2.浏览器左上角距离屏幕左上角的偏移量

```css
window.screenTop   [垂直偏移量]
window.screenLeft   [水平偏移量]
```

### 注意：

>  因为window是核心，可以省略window不写

## 方法

### alert()  弹出框

### prompt()  输入框

### confirm()   提示框，返回true或flase

### close()  关闭页面

### open(“url”)  打开页面（“打开的页面的路径【根据本html位置的相对路径】”）

```css
open("url","","width=300,height=200");
```

### setInterval（fn，毫秒数）：隔毫秒数重复不断的执行一个函数fn

```css
方法1
    let t =setInterval(fn,3000)
    function fn(){

    }
方法2
    setInterval(function(){

    },1000)
```

### clearInterval（t）：清除setInterval的时间函数

```css
let t =setInterval(fn,3000)
function fn(){
    
}
clearInterval（t）
```

### setTimeout（fn，1000）   隔一定的时间只执行一次函数

### cleanTimeout（t）    清除时间函数   【用法同上】

# 获取表单的值

```css
对象.value=

清空=“”
```

# history对象

## 属性：

### history.length   用来显示历史记录的长度

## 方法

### history.forward() 前进

### history.back()后退

### history.go(0) 刷新   【1  前进，-1后退；不常用】

# location对象

## 属性：设计获取当前页面的地址

location.href=“ ”  设置或获取页面地址  设置新值

location.host：主机名+端口号

location.hostname：主机名

location.port：端口号

location.protocol：协议

location.pathname： 路径

location.search： ？后面的查询【搜索】字段

## 方法

location.reload( )   重新加载

location.replace（"网页.html"）  页面替换，不会增加历史记录

location.assign（“网页.html”） 页面替换， 能够增加历史记录

