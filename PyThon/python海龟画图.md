# 1.导入turtle包

import turtle

##   1.画布canvas设置

###      1.设置画布大小

```python

	turtle.screensize(canvwidth=None, canvheight=None, bg=None)
    	例子：turtle.screensize(800, 600, "green")
			 turtle.screensize() #返回默认大小(400, 300)
	turtle.setup(width=0.5, height=0.75, startx=None, starty=None)
    	width, height: 输入宽和高为整数时, 表示像素; 为小数时, 表示占据电脑屏幕的比例
        (startx, starty): 这一坐标表示 矩形窗口左上角顶点的位置, 如果为空,则窗口位于屏幕中心
```

##      2.画笔

###          1.画笔描述

```css
在画布上,默认有一个坐标原点为画布中心的坐标轴, 坐标原点上有一只面朝x轴正方向小乌龟. 这里我们描述小乌龟时使用了两个词语:坐标原点(位置),面朝x轴正方向(方向), turtle绘图中, 就是使用位置方向描述小乌龟(画笔)的状态
```

###          2.画笔的属性（颜色、画线的宽度、速度）

```python
画笔(画笔的属性，颜色、画线的宽度)
	1) turtle.pensize()：设置画笔的宽度；turtle.width() 
	2) turtle.pencolor(); 没有参数传入,返回当前画笔颜色,传入参数设置画笔颜色,可以是字符串如"green", "red",也可以是RGB 3元组,
	3) turtle.speed(speed): 设置画笔移动速度,画笔绘制的速度范围[0,10]整数, 数字越大越快    
```

### 	  3.画图的命令

> 3种:一种为运动命令，一种为画笔控制命令,还有一种是全局控制命令

turtle.showturtle()   : 显示箭头

turtle.write("")   :    写字符串

#### 		1.画笔运动命令:

```python

		命令							说明
turtle.forward(distance)	向当前画笔方向移动distance像素长
turtle.backward(distance)	向当前画笔相反方向移动distance像素长度
turtle.right(degree)	    顺时针移动degree°
turtle.left(degree)	        逆时针移动degree°
turtle.pendown()	        移动时绘制图形,缺省时也为绘制
turtle.goto(x,y)	        将画笔移动到坐标为x,y的位置；去哪里
turtle.penup()	            移动时不绘制图形,提起笔，用于另起一个地方绘制时用
turtle.speed(speed)	        画笔绘制的速度范围[0,10]整数
turtle.circle()	            画圆,半径为正(负),表示圆心在画笔的左边(右边)画圆

```

#### 		2.画笔控制命令:

```python
命令	说明
turtle.pensize(width)	绘制图形时的宽度
turtle.pencolor()	画笔颜色
turtle.fillcolor(colorstring)	绘制图形的填充颜色
turtle.color(color1, color2)	同时设置pencolor=color1, fillcolor=color2
								只有一个参数是设置画笔的颜色
turtle.filling()	返回当前是否在填充状态
turtle.begin_fill()	准备开始填充图形
turtle.end_fill()	填充完成；
turtle.hideturtle()	隐藏箭头显示；
turtle.showturtle()	与hideturtle()函数对应
```

#### 		3.全局控制命令

```python
命令	说明
turtle.clear()	清空turtle窗口，但是turtle的位置和状态不会改变
turtle.reset()	清空窗口，重置turtle状态为起始状态
turtle.undo()	撤销上一个turtle动作
turtle.isvisible()	返回当前turtle是否可见
stamp()	复制当前图形
turtle.write(s[,font=("font-name",font_size,"font_type")])	写文本，s为文本内容，font是字体的参数，里面分别为字体名称，大小和类型；font为可选项, font的参数也是可选项
```

### 	4.命令详解

```python
3. 命令详解
3.1 turtle.circle(radius, extent=None, steps=None)
描述: 以给定半径画圆
参数:
radius(半径); 半径为正(负),表示圆心在画笔的左边(右边)画圆
extent(弧度) (optional);
steps (optional) (做半径为radius的圆的内切正多边形,多边形边数为steps)

举例:
circle(50) # 整圆;
circle(50,steps=3) # 三角形;
circle(120, 180) # 半圆
```

## 3.例子

```python
太阳花
import turtle as t
import time
t.color("red", "yellow")
t.speed(10)
t.begin_fill()
for _ in range(50):
    t.forward(200)
    t.left(170)
end_fill()
time.sleep(1)
```

```python
import turtle
import time


turtle.pensize(5)
turtle.pencolor("yellow")
turtle.fillcolor("red")
 
turtle.begin_fill()

for i in range(5):
    turtle.forward(200)
    turtle.right(144)
turtle.end_fill()
time.sleep(2)

turtle.penup()
turtle.goto(-150,-120)
turtle.color("violet")
turtle.write("Done", font=('Arial', 40, 'normal'))
time.sleep(1)
```

```python
螺旋线

import turtle
t=turtle.Pen()
for i in range(360):
    t.forward(i)
    t.left(59)
```

# 画同心圆

```python
import turtle

t=turtle.Pen()

t.width(4)
t.speed(10)

my_color=("red",'green','yellow','pink')
for i in range(10):
    t.penup()
    t.goto(0,-i*10)
    t.pendown()
    t.color(my_color[i%len(my_color)])
    t.circle(20+i*10)

turtle.done()    #画完保留界面
```

# 计算距离

```python
import turtle

# 定义多个点的坐标
x1,y1=100,100
x2,y2=100,-100
x3,y3=-100,-100
x4,y4=-100,100

# 绘制图
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)

distance=((x4-x1)**2+(y4-y1)**2)**0.5
print(distance)

```



 