jQuery：

# 本质：

>  js的框架
>
>  将原生的单个化操作--》批量操作
>
>

主动请求：link / script / img/背景图 

被动请求：a链接，form表单

# 宗旨

## write less   do more

# 作用

```css
优化js的操作
document操作
页面交互
事件
ajax
动效
```

# 特性

> 隐式循环【遍历所有的符合条件的元素】，链式调用【每次返回this】

# jQuery核心函数【可用$代替jQuery】（传入的内容）

## 选择器：返回选择器选中的jQuery对象

```css
jQuery(".box")  返回的是一个  ·数组·
```

## 函数：   给document对象添加 ready 事件

```css
jQuery（function（）{
    
}）
等同于
jQuery（“document”）.ready（function（）{
    
}）
等同于
jQuery（）.ready（function（）{
    
}）
```

```css
jQuery（function（）{

    jQuery(".box")

}）
```

## 传入dom对象：返回jQuery对象

```css
jQuery（function（）{
    let box=document.qjueryselector(".box")
    jQuery(box)   返回jQuery对象

}）

```

## 字符串：认为创建新的节点(包含标签对)

```css
jQuery（function（）{
    jQuery(“<div></div>”).appendTo(jQuery(".box"))  div添加到box下

}）
```

# jQuery的方法



.get()   将jquery对象转换为原生数组





## .css （"样式属性","样式值“） 

```css
$(".box“）.css（）
```

### .css（{json格式的数据}）

```css
$(".box").css({
    backgroundColor:'blue",
    borderRadius:"50%",
})
```



### ：first  所有的第一个，区别于first-child

```css
$(".box:first").css({
    backgroundColor:blue,
    borderRadius:"50%",
})

```

### ：not（.son1） 排除

```css
$(".box:not（.son1）").css({
    backgroundColor:blue,
    borderRadius:"50%",
})
```

### 奇偶 ：even    ：odd

### 筛选：：eq（11）  从0开始计数  返回对应的jQuery对象

### 大于：gt（11）   大于11的都选中

### 小于：lt（）

### ：header   选择所有的标题标签h1-h6

### ：animated  当前动画的元素

```css
$(".son").colick(function(){
    $(this).animate({"margin-left":1000},1000);
    $(".son:animated").css("background","red");
})
```

### :focus

```css

```

## .animate（{ }，1000）动画

## 筛选【过滤】

> jQuery对象身上的方法

### .eq（11）  从0开始计数  返回对应的jQuery对象

### . get（index） 返回对应下标的DOM对象

### .first()

### .last()

### .hasClass("类名")   判断jQuery数组中是否有一个类名为***的对象

> 返回布尔值

### .filter（【选择器】/【元素】/【函数】）

> 筛选出符合条件的对象；返回具体的函数

### .is（“选择器”）:判断是否为某个对象/标签

### .map（高阶函数）：遍历对象，生成一个新的数组或者集合

### .has（选择器）返回选中的jQuery对象，选择对象中含有选择器的后代的对象

### .not（“选择器”） 从jQuery数组中删除选中的元素

### .slice（开始，【结束】）截取指定位置的jQuery对象

### .each（index，item） 遍历jQuery数组    index在前，item在后？

### .index（） 返回jQuery对象在数组中的下标



# 操作属性的方法

```css
传入一个参数，获取对象

传入两个参数，添加属性

.attr（”“）传入一个参数，获取对象   页面中写了才能获取【表象级】

.removeAttr("类名")

.prop("类名")  不用写也可以获取【底层的】

.removeProp("类名")

```

# 操作类名的方法

.addClass()

.removeClass()

.toggleClass()  有删除，没有添加

# 操作内容

## .text（） 获取内容   

## .text（“新加的内容”）

## .html（）

## 表单的内容     .val（）

# jquery对象元素的位置信息

## .offset（） 返回一个位置信息的对象{left:*****,top:******}  相对于浏览器的位置

## .position（） 返回一个位置信息的对象{x****:**,y:******}  相对于定位的祖先元素的位置

## .scrollTop（） 内容被裹起来的高度

## .scrollLeft（）   内容被裹起来的宽度

# 常用方法

## .toArray（）：将jquery数组转换为原生数组

# 事件对象

## e.pageX

## e.pageY  距离浏览器的

## e.target 目标时间源

## e.currentTarget   ==this

## e.stopPropagation （）阻止事件流

## e.preventDefault（） 阻止浏览器默认行为

# 事件

## one()执行一次

## on()

## trigger() 自动触发事件

## triggerHandler()  自动触发，并且清除浏览器默认行为

## hover()移入移出

# 动效（封装了display：block和display：none）

## .slideDown()

## .slideUp() 

# ajax

```css
$.ajax({
	url:"",
    dataType:"jsonp",  // 数据保存在data中 
    success:function(){     //成功后执行的函数
            
    },
    error:function(){       //失败后执行的函数
        
    }
    data中有data属性
    data.data【“山西”】
})

```

# $()参数

```javascript
1.字符串
	a.选择器   将要选择器指向的内容放到jquery中
    b.标签   创建一个新对象
2.undefined
	
3.函数

4.dom元素
```



