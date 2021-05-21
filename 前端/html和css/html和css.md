---
typora-copy-images-to: ./
---

# 布局步骤

```css
第一步： 清除默认样式
第二步： 划分模块
第三步： 设置模块的大小以及位置
第四步： 划分下一级模块
```

# html和css

## 修改内容

```css
contenteditable='true'
```

## 引入网页头像

```css
<link rel="shortcut icon" href="img/...ico">
```

## css样式表的引入方式

```html
css样式表的引入方式
1、外链式
	<link href="" rel="stylesheet">
2、嵌入式
	<style></style>
3、行内样式
	<div style="width:200px;height:200pxs;"></div>
4. @import url('')
```

## 文件命名以及变量命名

```css
命名规范
1、严格区分大小写
2、可以采用字母数字下划线$,数字不开头
3、命名语义化
4、可以采用驼峰命名法
```

## 清除默认样式

```css
清楚边距
    *{
        margin: 0;
        padding: 0;
        list-style: none;
    }
a标签清楚下划线和颜色
    a{
        color: black;
        text-decoration: none;
    }
```

## css中颜色的表示方式

```css
css中颜色的表示方式：
1.预定义的颜色【关键字颜色】   red   pink  blue yellow
2.#6位数的色值   #00-00-00 红绿蓝
3.rgb（红，绿，蓝）    ：rgb([0-255],[0-255],[0-255])
4.rgba（red，green，blue，透明度）    ：rgba([0-255],[0-255],[0-255]，[0-1])
	0-1:  0全透明，1不透明
```

## html中的标签和属性

```html
html：
标签：
按照语法分类：
    1.单标签：只有开始标签
         meta  img a 
    2.双标签：有开始标签和结束标签
        <html></html>
    3.属性的语法
    语法：
      属性名 = "属性值"
      属性名 = "属性值1 属性值2"
注意:
    1、标签名和属性名之间要有空格
    2、多个属性之间要有空格
    3、多个属性值之间要有空格
	4.开始标签  标签名后有空格	

按照标签在页面中的呈现效果分类：
    1、行内元素
        行内元素定义:在一行内显示，只能设置左右间距，不可以设置上下间距。
        举例：span del i em b strong a(title="鼠标移入时显示的文字";target=" "(新窗口打开的位置 			_self:在本窗口打开;_blank:在新窗口打开) ...
    2、块元素
        块元素定义：可以设置宽高，独占一行。
        举例：div 标题标签 列表标签 段落标签 ...
    3、行内块元素
        行内块元素定义：可以设置宽高，在一行显示。
        举例：img 【title="鼠标移入时显示的文字" 】 表单控件
元素的转换
    块元素：    display:block;
    行内块元素：display:inline-block;
    行内元素：  display:inline;
元素的级别
	块元素 > 行内块元素 > 行内元素
元素嵌套规范
    1、同一级别可以相互嵌套
    2、级别高的元素可以嵌套级别低的元素
    3、段落标签只能嵌套行内元素
    4、a标签不可以嵌套a标签；p不能嵌套p
```

## iframe显示相应的模块

```css
<a href="lianjie" target="main">
<iframe src="" frameborder="0" name='main'></iframe>
a链接再iframe中显示
```



## 盒子模型及其问题

```css
四部构成：
    1、margin  外间距 盒子与盒子之间的距离
    2、border  边框
    3、padding 内填充（内间距） 边框与内容之间的距离。
    4、content 内容
 margin-top \ margin-right \margin-bottom \margin-left 
    margin: 50px;  上 右 下 左
    margin: 50px 100px;  上下    左右
        margin:0 auto;  auto自动
    margin: 50px 100px 150px; 上 左右 下
    margin: 50px 100px 150px 200px;  上 右 下 左
    border: 1px solid red;
    border-top \ border-right \border-bottom \ border-left 
	border-top-width：上边框的宽度

padding:设置方法同margin

content: ;
    width :  数值  百分比 auto
    height:  数值  百分比 auto

盒子模型的问题：
    1.大部分元素的margin和padding默认为0，但有一部分的margin和padding不为0，例如body  标题标签（h1-h6）（ul ol  il等列表标签）	段落标签
    2.想领的两个块元素的margin会重合，值会取最大值
    3.margin可以为[负数]   ，padding不可以设置[负数]。
    4.行内元素margin只有左右，没有上下
    5.如果（1）发生嵌套关系的元素，（2）父元素没有上边框，（3）上padding ，（4）父元素与子元素之间没有别的内容，此时子元素margin-top就会作用到父元素身上	
margin-top的解决方式：
    1.用父元素的padding-top代替子元素的margin-top；
    2.给父元素添加overflow：hidden；
   		
```

## 宽高的设置和计算

```css
height：auto  /  百分比  /   px； 
width：auto  /  百分比  /   px； 
height：auto； 参照与父元素
width：auto；参照与内容
box-sizing：border-box；  将边框算入盒子内；

一个元素实际的宽高
实际宽度 = border-left + padding-left + width +paddint-right + border-right;
实际高度 = border-top + padding-top + height + padding-bottom + border-bottom;
```

## 浮动

```css
作用：让块元素横排排列
  样式： float：left；从左往右排列
	    float：right；从右往左排列
原理：让元素脱离文档流，让元素从文档层浮动到浮动层。
引发的问题：父元素不设置高度，子元素都浮动，浮动的子元素撑不开父元素。（浮动的元素脱离文档流）
	*解决方式一：给父元素添加  overflow：hidden；（超出部分隐藏）
	*解决方式二：在父元素内容最后添加拥有清除浮动属性的元素。
		 		clear：right/left/both ；  别的浮动对它的影响清除掉
	  		例：
                .box：after{
                    content: "";
                    display:block;
                    width: 0;
                    height: 0;
                    clear:both;
                }
	*解决方式三：父元素能设置高度的尽量设置高度
浮动之后的块元素参照内容：属性值 auto
```

## 定位

```css
定位的元素脱离文档层，到达定位层
定位的元素会多出5个样式：
	top right bottom left z-index：999
	上    右    下    左    层级（层级越高，离用户越近）【只能在有定位属性的元素上才能用】
层级：
z-index：整数；
定位的几种方式：
1.相对定位：
	相对于自身来定位，在文档层中保留原来的位置
	用法：
	     position：relative；
2.绝对定位：
	相对于最近的 定位的 祖先元素 来定位，完全脱离文档流（其他顶替其位置）
	用法：
	     position：absolute；
		+方向值
3.固定定位：
	相对于浏览器的四条边，完全脱离文档流
	用法：
	    position：fixed；
	top与bottom同时定义，那个样式会作用到元素身上的判断关系：
       top的权重比bottom的权重大
       left的权重比right的权重大
  元素作用时：
    1.如果是
        position：relative；
        left：；
        margin：；
        先作用margin，在作用relative；
    2.如果是
        position：absolute；
        left：；
        margin：；
        先作用absolute，在作用margin；
定位元素的居中方式：
方法一：
	1.水平居中：
		position：absolute；
		left：50%；
		margin-left：-自身长度的一半；
	2.垂直居中：
		position：absolute；
		top：50%；
		margin-top：-自身长度的一半；
	3.绝对居中：
		position：absolute；
		left：50%；
		top：50%；
		margin-left：-自身长度的一半；
		margin-top：-自身长度的一半；
方法二：
	1.水平居中：
		position：absolute；
		left：0；
		right：0
```

## 2D和3D

```css
2D和3D属性：
1.平移样式
	transform:translate(x,y);  向上为负， 向下为正
		transform:translateX(100px);
	transform：rotate（180deg）   ；  （1turn）转一圈
	平移  transform:translate（）   例子：translate（x，y） translateX（）
	旋转  transform:rotate（）   例子rotate（180deg）顺时针   -180deg  逆时针
		transform：rotate（）空格translate（）；
	       transform-origin:px px;变换的中心点；
			left center；
	缩放  transform:scale（）	  例子：scale（2）  放大为原来的2倍  scale（0.n）缩小为原                                        来的0.n   scale（m，n）  x轴m，y轴n
	斜切  transform:skew（）	  例子：skew（45peg）  左拉伸45°  skew（45peg，m）
	      
2. 过渡transition
	transition：all 0.5s；
		   全部 时间
3.过渡的属性样式：  transition-property:   ，   ;
    可以为：属性的全部样式
4.过度的总时间： transition-duration：；
5.过渡的时间函数： transition-timing-function：；
		linear（匀速）   ease（开头结尾慢，中间快）
		cubic-bezier（1，0.07，0.54，0.21） 贝塞尔曲线
6.延迟   transition-delay：；

3d效果：和2d的一样transition，transform；
    prespective：给父元素加prespective（灭点的值）
    prespective-origin：x y；灭点的位置   调整观察的角度（大多数情况不设置）
    transform：ratate3d（0-1的值,0-1的值,0-1的值,45deg）
        transform：ratateY（45deg）
    transform：translate3d（0-1，0-1，px）

父元素：transform-style：preserve-3d；
```

## 动画

```css
动画规则：
	@keyframes 动画名（随便给）{
		（动画规则）
		from{}
		to{}
	}
	@keyframes 动画名（随便给）{
		（动画规则）
		0%{}
		50%{}
		100%{}
	}
	@keyframes animation1{
		from{
		   background-color:red;
		}
		to{
		   background-color:blue;
		}
	}

挂载动画:将动画加到元素身上
	.元素{
		animation：animation1 时间  步数 时间函数 延迟时间 次数 ；
	}
挂载多个动画：
	.元素{
		animation：animation1 时间,animation2 时间,animation1 时间；
         其他动画的相同的可以附件通过animation属性；
	}
animation的样式
动画名：animation-name
时间： animation-duration 
步数：animation-steps：8；
时间函数：animation-timing-function
延迟： animation-delay
动画次数： animation-iteration-count：infinite（无限次）/2；
指定下一次动画是否逆向：animation-direction：alternate（逆向）/ normal（常规）；
最后的状态：animation-fill-mode：backwards（默认（保持一开始的状态））/forwards（保持当前的状态）；
状态即指定动画是否运动： animation-play-state: running（运行）/paused（静止）;

```

## 元素分类

```css
按照在页面中的呈现效果：
1.行内元素：在一行内显示 ，不可以设置宽高 ：（存放文字）
	span a b i strong del
2.行内块元素：在一行内显示，可以设置宽高：（有缝隙   不常用）
	img  表单控件
3.块元素 ：可以设置宽高，独占一行
	div 标题标签（h1-h6） 列表标签（ul-li  ol-li     dl>dt+dd  段落标签 （p pre））
元素嵌套规范：
    1.同一级别可以相互嵌套
    2.级别高的可以嵌套级别低的元素
    3.p标签只能嵌套行内元素
    4.a链接不能相互嵌套
元素的转换：
    1.块元素：display：block；
    2.行内块元素：display：inline-block；
    3.行内元素：display：inline；
```

## 背景图片以及浏览器内核

```css
背景图
    先设大小，在引background；
    background: url('路径') no-repeat left bottom/contain；
              //图片位置    禁止重复  位置（top bottom left right）
1. 路径：background-image：url（“”），url（“”）；加载多张背景图
2. 背景图大小：  background-size：100px auto，100px auto；  会重复
3. 背景的图重复：
	      background-repeat：no-repeat，repeat；（无重复）
	      background-repeat：repeat-x（x方向重复）
	      background-repeat：repeat-y（y方向重复）
4. 背景图的位置：
	      background-position：x  y；（数值  方位值（top/bottom  left/right center（可以省略））  ）
5. 背景开始渲染的位置： background-origin:    ;
		padding-box；（默认）从padding位置开始渲染
		border-box；从边框的位置开始渲染
		content-box；从内容的位置开始渲染
6. 图片结束渲染的位置：background-clip: ;
		padding-box；（默认）从padding位置结束渲染
		border-box；从边框的位置结束渲染
		content-box；从内容的位置结束渲染
7. 使得背景图加载到浏览器中
 	background-attachment: fixed;
8.可以简写：
	background：空格隔开；
9.  背景图渐变
	background: linear-gradiend(top，颜色1，颜色2，颜色n)
                       //渐变开始的方向（默认top） 类似25deg（25度）
10.浏览器内核//背景色渐变
	1.  /* 标准语法 */
	 	例子：background: linear-gradient(top,#3bbcff,#47eaff);	
	2.  /* 谷歌内核 -webkit- */
		例子：background: -webkit-linear-gradient(top,#3bbcff,#47eaff);
	3. /* 火狐内核 -moz- */
		例子：background: -moz-linear-gradient(top,#3bbcff,#47eaff);
	4. /* 欧鹏内核 -o- */
		例子：background: -o-linear-gradient(top,#3bbcff,#47eaff);
	5. /* IE内核 -ms- */
		例子：background: -ms-linear-gradient(top,#3bbcff,#47eaff);

```

## 文件的读取方法路径

```css
绝对路径：从盘符开始的一条完整路径
相对路径：两个文件的位置关系
```

## 边框的相关属性【圆角，边框形状】

```css
border-radius：边框的半径   设置圆角 n%或者num像素
border-style:dotted solid double dashed; 
      上边框是点状
      右边框是实线
      下边框是双线
      左边框是虚线	
```

## 透明度

```css
透明性的选择：（整个容器都变）
opacity：；0-1之间的值；
```

## 字体

```css
font-family =“ 字体”     //字体样式可以被继承
letter-space:   字间距
```

## 鼠标移入样式

```css
span标签
  cursor：pointer；   鼠标样式：手型
```

## 阴影

```css
box-shadow：x轴偏移量  y轴偏移量  阴影的模糊程度  阴影的大小（0和本身一样大小）  阴影的颜色 inset(内阴影)【默认外阴影】；
```

## 引入字符图标

```css
引入字符图标：
行内元素  随意  
span  class=“iconfont 图标类名”
可调节样式： 同文字
```

## 文档流

```css
文档流：
     标准情况下 ，页面元素从左往右  从上往下  依次排列
```

## flex布局(规范的设计稿)-弹性布局

```css
容器（父元素）的属性：【display:flex;】
	*flex-direction: 决定主轴方向。
        row 主轴在水平方向，从左向右（默认）。
        row-reverse 主轴在水平方向，从右向左
        column 主轴在垂直方向，从上到下
        column-reverse  主轴在垂直方向，从下到上
	*flex-wrap: 决定项目换行
		wrap: 项目换行
		nowrap:  项目不换行（默认值）
		wrap-reverse： 项目换行且反转
	*justify-content: 决定项目在主轴的对齐方式
		flex-start;主轴的起点
		flex-end;主轴的终点
		center;主轴的中心
		space-between;两端对齐
		space-around;项目两侧距离相等
	*align-items：项目在交叉轴上的对齐方式（适用于一根轴线与多跟轴线）
		flex-start:交叉轴的起点
		flex-end：交叉轴的终点
		Center：交叉轴的中心
		baseline： 基线对齐（文本底部）
	*align-content:定义项目在交叉轴上的对齐方式（仅适用于多根轴线）
		flex-start;交叉轴的起点
		flex-end;交叉轴的终点
		center;交叉轴的中心
		space-between;两端对齐
		space-around;两侧距离相等	
子元素（项目）的属性：
	*order：定义项目的排列顺序，数值越小，越靠前，默认值为0（可以取负值）。
	*flex-grow:定义项目的放大比例。默认值为0，即使存在剩余空间，也不放大。
	*flex-shrik：定义项目的缩小比例，默认值为1，空间不足，项目缩小;值为0时,空间不足,项目也不缩小.
	*flex-basis: 定义项目占据的主轴空间.默认auto或者自己添加像素;
	*align-self:定义单个项目在交叉轴的对齐方式.
		flex-start:交叉轴的起点
		flex-end：交叉轴的终点
		Center：交叉轴的中心
```

## 滚动条

```css
overflow-x：auto；超出部分在x轴的表现形式。
            auto：自动；（如果超出，就自动以滚动条的形式显示）
去滚动条：  加在具有overflow属性的元素身上
    ::-webkit-scrollbar{
        height：0；
	}
overflow-x: visible|hidden|scroll|auto|no-display|no-content;
  值	                      描述	                     测试
visible         不裁剪内容，可能会显示在内容框之外。	        测试
hidden	        裁剪内容 - 不提供滚动机制。              	测试
scroll	        裁剪内容 - 提供滚动机制。	                 测试
auto	        如果溢出框，则应该提供滚动机制。	          测试
no-display	    如果内容不适合内容框，则删除整个框。           测试
no-content	    如果内容不适合内容框，则隐藏整个内容。	        测试

```

## 轮播图

```css
swiper(.js).com
```

## 表格

```html
<table border="" width="" bgcolor="背景色" cellspacing="设置单元格间的距离" cellpadding="内填充：内容到边框的距离" >
    <tr bgcolor="">[行]
        <td></td>[列]
        
    </tr>
</table>

```

### 变成可编辑的【td属性】

```css
contenteditable='true'

```



### table身上的属性

```css
table身上的属性：
    border：表格边框 cellspacing：单元格间的间距
    cellpadding：单元格的内容与其边框的内边距 
    bgcolor：表格的背景颜色 background：表格的背景图片
    width：表格宽度 height：表格高度
    border-collaspe：collaspe：边框合并，不叠加 cellspacing：0：边框合并，但合并之后的边框宽度等于		前两个边框宽度之和
    caption：表格标题
	background:表格背景图
	cellspacing:单元格之间的间隙宽度
	align:表格的水平对齐方式，通常是left，center，right
```

### 表格的标题

```css
<caption align="水平对齐方式" valign="标题与表格的相对位置"></caption>
```

### 单元格【tr】【td】

```css
width：单元格宽度height：单元格高度
align：单元格内文本的对齐方式,通常是左，中，右 left，center，right
valign：单元格内文本的对齐方式,通常是上，中，下 top，middle，bottom
nowrap：在为设置单元格宽度时，当文本长度宽于单元格宽度，将要换行时，该标签会使其不换行

    <tr align="center" valign="bottom">
        <td align="center" nowrap>手机空中免费充值</td>
        <td width="100px">IP卡</td>
        <td width="100px" bgcolor="#006400" valign="top">网游</td>
    </tr>
```

### **表格的跨行与跨列**【td】 

```css
rowspan：跨行标签，表示跨了多少行
colspan：跨列标签，表示跨了多少列
<table border="3" bordercolor="plum" width="300" height="100" align="center" cellspacing="0">
    <tr>
        <td rowspan="6" background="../img/4.jpg"></td>
        <td rowspan="3"></td>
        <td rowspan="2"></td>
        <td></td>
    </tr>
    <tr>
        <td ></td>
    </tr>
    <tr>
        <td rowspan="2"></td>
        <td></td>
    </tr>
    <tr>
        <td rowspan="3"></td>
        <td></td>
    </tr>
    <tr>
        <td rowspan="2"></td>
        <td></td>
    </tr>
    <tr>
    	<td></td>
    </tr>
</table>
```

### **表格标签拓展及其属性**

```css
    thead：定义表格的表头。	
    tbody：定义表格主体（正文）。
    tfoot：定义表格的页脚（脚注或表注）。 
    colgroup：标签用于对表格中的列进行组合，以便对其进行格式化。
    注意：不管thead、tbody、tfoot的代码先后顺序如何，html显示时，始终是先显示thead，再显示tbody，最后显示tfoot。
1、<thead> 内部必须拥有 <tr> 标签！
2、<tfoot> 元素内部必须包含一个或者多个 <tr> 标签。
3、<tbody> 元素内部必须包含一个或者多个 <tr> 标签。
4、必须在 table 元素内部使用这些标签。
5、当不同行间的单元格合并时各单元格所在的行不要加tbody标签。
```

### 标题栏

```css
《tr》<th></th>《/tr》  用法和td相似  知识自动将单元格内容以粗体显示
```



## 表单控件表单标签

```css
<form action=" " method=" " entype=“>
		action:表单信息提交的位置；
		method：提交的方式
			get：地址栏，信息量少，安全性低
			post：信息量多，比较安全
			entype：数据编码方式
	1.输入文本【输入框】：
        用户名：<input type="text" placeholder="请输入用户名" maxlength="10" value=" " 				name="username" class="">
            placeholder：默认提示文本;
            maxlength:规定输入的最大字符数
            name:本文本框的名字，与后台进行数据交互用
            class:定义本文本框的样式，相当于盒子
		   placeholder下的缩进  
		   text-indent：2em；缩进
	2.输入密码【密码框】：
		密码：<input type="password" placeholder="请输入密码" maxlength="10" value=" " 					name="psw" class="">		
			<input type='hidden'>  //隐藏
	3.单选按钮[name的值必须相同]：
		请选择你的性别：
		<label for="man">   [label实现点什么就选中  ，for中的值和id中的值相同]
		男：<input type="radio" name="sex" id="man" checked>  //checked默认选项
		</label>
		<label for="woman">
		女：<input type="radio" name="sex" id="woman">
		</label>
	4.多选按钮[name的值必须相同]：
		请选择你喜欢的音乐：
		摇滚：<input type="checkbox" checked>
         摇滚：<input type="checkbox" checked>
         摇滚：<input type="checkbox" checked>
	5.下拉列表【下拉框】：
		选择你的学历：
		<select name="" id="" size=3>   #size展开选项，默认不展开
			<option value="">学士</option>
            <option value="">博士</option>
             <option value="">硕士</option>
		</select>
	6.上传文件：
		选择你的照片：
		<input type="file">
	7.留言文本空间：
		<textarea name="" id="" rows="" col="">
		</textarea>
	8.用户是否允许重新设置textarea大小css属性：
		resize: none/both/vertical/horizontal;不允许/上下允许拖动/只能在垂直方向拖动/只能在水平方向		拖动
	9.重置按钮：
		<input type="reset">
	10.提交按钮：
		<input type="submit">
	11.自定义按钮：
		<input type="button" value="按钮">
		<button>搜索</button>
	12.颜色：
		<input type="color">
	13.时间日期：
		年月：<input type="month">
		年周：<input type="week">
		时分：<input type="time">
		年月日：<input type="date">
		年月时分：<input type="datetime-local">
	14.验证
		<input type="email">   邮箱验证
		<input type="tel" autofocus>   电话
	15. autofocus 自动获取焦点	
</form>
```

## 文本模型

- 文本换行

  ```css
  使非中日韩文本换行
  word-break: break-all ;
  ```

- 文本禁止换行

  ```css
  white-space:nowrap;
  ```

- 单行文本溢出部分以省略号显示

  ```css
  overflow: hidden;(放文本的容器)
  text-overflow: ellipsis;
  ```

- 多行文本溢出

  ```css
  1. 指定为弹性盒子
  	display: -webkit-box;
  2. 在弹性盒模型中指定元素的排列顺序
  	-webkit-box-orient: vertical;
  3. 指定文本显示（溢出）的行数;
  	-webkit-line-clamp: 3;
  4. height要是line-height的倍数
  	line-height: 70px;
  5. overflow：hidden；
  ```


## 音频视频标签

- 音频标签

  ```css
  <audio src="" controls loop autoplay></audio>
  			controls 空间向用户显示：
  			loop 循环播放
  			 autoplay当前页面加载完自动播放
  ```

- 视频标签

  ```css
  <video src="" controls loop autoplay></video>
  ```

## H5语义化标签

```css
<header>头部</header>
<nav>导航</nav>
<aside>侧导航<aside>
<section>页面中的某一部分</section>
<main>主体</main>
<footer>底部</footer>
```

## meta标记【签】

```css
name="关键字"  cantent="内容"
<mate http-equiv="Refresh" content="10";url="跳转路径">   //每10s刷新一次并且跳转到跳转路径知识的文件
```

## bgsound标签

```css
<bgsound src="路径" loop="播放次数">
```

## body属性

```css
1. bgcolor:背景颜色
2. background：背景图片
3. text：文档中文字的颜色
4. link：超链接的颜色
5. alink：正在访问的超链接的颜色
6. vlink：已访问过的超链接的颜色
7. leftmargin/rightmargin/topmargin/bottommargin： 左/右/上/下边距的像素值
```

## 对文字操作的标签

``` css
1. <p></p>开始一个新段落，可单可双
2. <br>  换行标签，单独标记
3. <pre></pre>预格式化【敲什么样式，显示什么样式】
4. <font></font> 用来设置文字的字体 大小 颜色 粗细等
5. 文字样式标记[均成对出现]
	b  粗体    i 斜体  u 下划线   tt   等宽 
	sup 上标体 sub 下表体   strike 删除线  big 大号字样
	small 小号字样  blink 闪烁字样 em强调字样  strong着重字样  cite引用字样
```

## 列表标签

```css
1. 符号列表
    <ul type="circlr(空心圆点)/disc（实心圆点）【默认】/square（实心方块）">
        <li>
        <li>
    </ul>
2. 排序列表
    <ol type="1(数字) /a（a，b，c..）/ A(A,B,C...)/ i(i,ii,iii,...)/ I(I,II,III,...)">
        <li>
        <li>
    </ol>
```

## a标签

```css
<a   href="路径 " title="鼠标移入时显示的文字"  target=" "(新窗口打开的位置	_self:在本窗口打开;_blank:在新窗口打开；_parent:在当前窗口的父窗口打开链接；_top:在整个浏览器窗口打开) ...

# 包含了一个位置信息，默认的锚是 #top 也就是网页的上端。即是说，当 href=# 的空链接被点击时，页面会跳到最顶端。
而 javascript:void(0) 仅仅表示一个死链接，当 href=javascript:void(0) 的空链接被点击时，页面不会有任何反应。
在页面很长的时候会使用 # 来定位页面的具体位置，格式为：# + id。
如果你要定义一个死链接请使用 javascript:void(0) 。
```

## [字符实体]常用的转义字符

| **显示结果** | **描述**        | **实体名称**       |
| -------- | ------------- | -------------- |
|          | 空格            | &nbsp; &nbsp;  |
| <        | 小于号           | &lt;           |
| >        | 大于号           | &gt;           |
| &        | 和号            | &amp;          |
| "        | 引号            | &quot;         |
| '        | 撇号            | &apos; (IE不支持) |
| ￠        | 分（cent）       | &cent;         |
| £        | 镑（pound）      | &pound;        |
| ¥        | 元（yen）        | &yen;          |
| €        | 欧元（euro）      | &euro;         |
| §        | 小节            | &sect;         |
| ©        | 版权（copyright） | &copy;         |
| ®        | 注册商标          | &reg;          |
| ™        | 商标            | &trade;        |
| ×        | 乘号            | &times;        |
| ÷        | 除号            | &divide;       |

## html实体

| **显示结果** | **描述**          | **实体名称**      |
| ------------ | ----------------- | ----------------- |
|              | 空格              | &nbsp; &nbsp;     |
| <            | 小于号            | &lt;              |
| >            | 大于号            | &gt;              |
| &            | 和号              | &amp;             |
| "            | 引号              | &quot;            |
| '            | 撇号              | &apos; (IE不支持) |
| ￠           | 分（cent）        | &cent;            |
| £            | 镑（pound）       | &pound;           |
| ¥            | 元（yen）         | &yen;             |
| €            | 欧元（euro）      | &euro;            |
| §            | 小节              | &sect;            |
| ©            | 版权（copyright） | &copy;            |
| ®            | 注册商标          | &reg;             |
| ™            | 商标              | &trade;           |
| ×            | 乘号              | &times;           |
| ÷            | 除号              | &divide;          |

# 选择器

## 分类

```css
css选择器
1.通用选择器：
	*｛｝//选择所有的标签
2.群组选择器：
	E1,E2,E3..｛｝//选择E1 E2 E3
3.标签选择器
	标签名｛｝
4.类名选择器：
	.类名｛｝
5.后代选择器
	.E1 .E2｛｝  //选择E1 的后代E2
6.交叉选择器
	标签名.类名｛｝
7.id选择器
 例如  创建id  
	<div id=“box”></div>
	#id名｛｝  //选择页面中id为**的标签
8.伪类选择器：
	鼠标移入状态
        E：hover{ }   E元素选择鼠标移入状态
        E：hover .子类{ }   选择e元素下鼠标移入时子类的变化   
    获取焦点，用于表单的输入
        E: focus{
            outline: none;
         }
9.伪结构选择器：
	E：first-child｛｝   作为子元素的第一个孩子的E标签
	E：last-child｛｝   作为子元素的最后第一个孩子的E标签
	E: nth-child(n){}  //作为子元素的第n个孩子的E标签
	E: nth-last-child(n)   作为子元素的倒数第n个孩子的E标签
	E：first-of-type｛｝ 作为子元素的同类型的第一元素
	E：last-of-type｛｝ 作为子元素的同类型中的最后一个元素
	E: nth-of-type（n）   作为子元素的同类型中的第n个元素
	E: nth-last-of-type(n)  作为子元素的同类型中的倒数第n个元素
		（n）n可以以为num/even（偶数）/odd(奇数)/3n（3的倍数）
		例子：5.15/伪结构选择器
10.伪元素选择器：
	::after{}   在元素之后加入一个
	::before{
		content：“内容之前”；
		color：；
	}      在元素之前
	属于行内元素
::after{}   ::before{}伪元素   content：""；  样式必须写

11.子类选择器
     相邻兄弟选择器
		E1+E2｛｝  选择E1的下一个兄弟元素E2（不能选中上一个兄弟元素）
			div.box>a+img   a和img统计
     子类选择器
		E1>E2{}  选择E1的子类元素E2
			例子：div.box>div.item{$}*20
				div.box>a>img
12.属性选择器
	[属性名]{}   选择所有拥有属性为 属性名 的元素
	[属性名=“value”]｛｝  选择拥有属性名的属性  且属性值为value
	E[属性名=“value”]{}   选择拥有属性名的属性  且属性值为value的E元素
	E[属性名~=“value”]{}    选择拥有属性名的属性  并且属性值一个或者多个，其中一个属性值为value的E元素
	E[value^=“1”]{}    选择拥有 value的属性  并且属性值一个或者多个，其中一个属性值以 1 开头的E元素
	E[value$=“1”]{}    选择拥有 value的属性  并且属性值一个或者多个，其中一个属性值以 1 结尾的E元素
	E[value*=“1”]{}    选择拥有 value的属性  并且属性值一个或者多个，其中一个属性值包含 1 的E元素
             	 例子：属性选择器
```

## 选择器的优先级

```css
宗旨：越具体的优先级越高
 id (100  ) >   class( 10 )>  标签名( 1)
 	.box .son{ }   10+10=20
 abcde优先级（e为个位）：
	a:行内样式
	b:id选择器
	c:类名选择器 伪类选择器（：hover） 属性选择器  
	d:标签选择器 伪元素选择器 （：：after）  
	e:通用选择器有一个
  选择有中有一个abcde在其位置+1
```

# 移动端布局步骤

```css
1. 修改视口
       <meta name="viewport" content="width=device-width">

视口：视觉视口，布局视口，理想视口
em:当前字体的倍率   100px=10em
rem：html字体的倍率 	  
	移动端窗口  375*667
	html{
    	font-size：0.5rem；
	}
	.box{
   	 	width： 750rem；   //375px=750rem*0.5px  ； 100px=1rem
   		 height： 1334rem；
	}
2. 引入rem.js
       <script src="路径"></script>
3. 修改rem.js中设计稿的宽度
4. 100px=1rem
```




