DOM（文档对象模型）document object model

# 获取元素

> 获取body：document.body
>
> 获取html：document.documentElement

## 1. 获取id名的元素：

```css
let 变量=document.getElementById("id名")
	例子： let box=document.getElementById("id名")
```

## 2.获取class名的元素[得到的是集合，可以通过键名访问]

```css
let 对象=document.getElementsByClassName（“class名”）
    通过遍历改变样式
集合通过单个下表改变，不能全部用class名同时改变
```

## 3.  获取标签名的元素[得到的是集合，可以通过键名访问]

```css
let 对象=document.getElementsByTagName（“标签名”）
```

## 4.给对象加类

```css
标签加1个类名
	对象.className=“类名”
div加多个类名 
	对象.className=“类名1 类名2 ”
```

## 5.指定范围的多层级获取【集合】

```css
<div class="box">
    <div class="box1">
        <div class="box2"></div>
    </div>
</div>

多楼层获取
let box=document.getElementClassName("box");
let box1=box.getElementClassName("box1");
let box2=box1.getElementClassName("box2")
```

## 6.获取选择器选中的元素

```css
let liss=document.querySelector("【选择器】");   获取选择器选中的第一个元素
let lis=document.querySelectorAll("【选择器】"); 获取选择器选中的全部元素【集合】【下标或者foreach遍历】
```

## 7.属性选择器

```css
 <textarea name="con" id="text" cols="30" rows="10"></textarea>
let con = document.querySelector("[name=con]")
```

# 操作样式

## 获取样式

### 	获取行内样式

```css
对象.style.样式名
```

### 	获取通用的样式【css和行内】

```css
getComputedStyle(对象,null).样式名
```

## 设置行内样式

```css
对象.style.样式名=“样式值”
对象.style=“background：red；border-radius：50%”
```

## 批量操作类名

```css
对象.className="class类名"
对象.className=“ ”；
对象.classList.add（“”）  添加类
对象.classList.remove（“”）  删除类
对象.classList.toggle（“”）  切换类

对象.id="id名"

外部定义一个样式，加到对象身上，参考第四点
```

# 操作属性

## 操作标准属性

> 已知的，系统自带

```css
对象.属性
例子 ： img.src
```

## 自定义属性

### 获取

```css
对象.getAttrbutte("name")
```

### 设置

```css
对象.setAttrbutte("name","value")
```

# 操作内容

## innerText：不能识别html的标签对

## innerHTML: 可以识别html的标签对

```css
对象.innerText=“内容”
对象.innerHTML=“内容”
```

# 添加事件

对象.对象事件=function（）{

}

# 元素的尺寸和位置

## 对象.offsetWidth:获取元素的真实宽度

## 对象.offsetHeight:获取元素的真实高度

## 对象.offsetTop：对象的上边框距离具有定位的父元素的内边框的垂直距离

## 对象.offsetLeft：对象的左边框距离具有定位的父元素的内边框的水平距离

## 对象.scrollTop：有滚动条的元素，浏览器滚动时在垂直方向的拉动距离

```css
body的兼容
document.body.scrollTop || document.documentElement.scrollTop
```



## 对象.scrollLeft：有滚动条的元素，浏览器在滚动时在水平方向的拉动距离

# 动态创建标签   

### let div=document.createElement（“标签名”）

# 创建的元素放到也面中：

### document.body.appendChild（div）

### 父元素.appendChild（子元素）

