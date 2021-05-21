在Scipy库下

# Numpy

> 多维数组及处理数组的能力

## 两种对象

* ndarray：存储单一数据的多维数组
* ufunc：对数组进行处理的函数

## 数组

### 一维数组

```python
np.array([1,2,3])
指定类型：np.array(([1, 2], [3, 4]), dtype=complex)
```

### 二维数组

```python
np.array([[1,2],[3,4]])
```

### 三维数组

```python
b=np.array([[[1,2],[3,4]],[[8,5],[6,7]]])

取8：b[1,0,0]   #第一个矩阵的m行n列
切片：b[1,m:n,m1:n1]  #第一个矩阵的m行到n行的m1列到n1列的数

索引：
	b[b>7]
花式索引：
	b[[m1,m2,m3],[n1,n2,n3]]    #mi行ni列的数（跳着取）
```

### 全零（0）矩阵

```python
一维：np.zeros(2)  #1行2列
二维：np.zeros((2,3))   #2行3列
三维：np.zeros((3,4,2))  #3个4行2列的全零阵
```

### 全1矩阵

```python
一维：np.ones(2)  #一行两列
二维：np.ones((2,3))  #2行3列
三维：np.ones((2,3,4))  #2个3行4列的数组组成的3维数组
```

### 单位阵

```python
np.eye(3) #3维的单位阵
```

### 常数阵

```python
np.full((2,3),10)  #2行3列的全是10的
```

### 顺序数组

```python
一维：np.arange((10))   #从0-9 （类似range）

二维：np.arange(6,12).reshape(2,3)
	np.arange(1,11,2,dtype=float) # 2代表步长,dtype代表创建的数值类型
	np.arange(1,11,2).reshape(n,m)   #重新调整数组，调整为n行m列（n或者m值为-1,系统根据另一个值计算行或列），

三维：np.arange(24).reshape(2,3,4)
```

###  等差数列

```python
np.linspace(1,3,4,endpoint=False)  #1,3中间平均取4个（默认取到结束值）,endpoint是否取最后一个，
```

### 等比数列

```python
np.logspace(1,3,num=5,endpoint=True,base=10.0,)  #1,3中间取5个（取到结束值），公比base
```

### np.empty():依赖内存随机

```python
函数empty创建一个内容随机并且依赖内存状态的数组。默认创建的数组类型(dtype)都是float64。

二维：np.empty((2,3))
三维：np.empty((2,3,1))
```

### np.indices((3,3))

> indices（）将创建一组数组（堆叠为一个更高维度的数组），每个维度一个，每个都代表该维度的变化。 

```python
np.indices((3,3))

:
    [
        [
            [0, 0, 0], [1, 1, 1], [2, 2, 2]
        ], 
        [
            [0, 1, 2], [0, 1, 2], [0, 1, 2]
        ]
    ]
```

### np.random.random()/np.random.ranint()

> 不包括尾数

```python
二维：np.random.random((2,3))
三维：np.random.random((2,3,2))
np.random.ranint(1,8,size=(m，n))
```

## 数组的属性/方法

### 类型（type）

### 维数（ndim）

### 形状（shape）

```python
a.shape[0]  行数
a.shape[1]  列数
```

#### 改变数组形状

##### 拉平数组（a.ravel（））

##### 直接修改( a.shape=(n,m))

##### reshape

### 大小（size）

> 返回矩阵元素的个数

### 矩阵中元素的类型（dtype）

> 类型有：int32，float64

### 类型名字(dtype.name)

### 数据类型转换（astype（int））

### 每个元素占得字节数（itemsize）

### 矩阵在内存中的位置（data）

## 数组的打印

> 一维数组被打印成行，二维数组成矩阵，三维数组成矩阵列表

> 如果一个数组用来打印太大了，NumPy自动省略中间部分而只打印角落。禁用NumPy的这种行为并强制打印整个数组，你可以设置printoptions参数来更改打印选项。`np.set_printoptions(threshold=np.nan)`

## 数组/矩阵的运算

### +、-、*、/、幂、平方根、三角运算、对数、转置，where、unique

> 同型矩阵的对应元素操作

```python
+:np.add(a,b)
-:np.subtract(a,b)
*:np.divide(a,b)
/:np.multiply(a,b)
幂：np.exp(a）
平方根：np.sqrt（a）
三角运算：np.sin()\np.cos()\np.tan()\..
对数：np.log（a）
转置：np.transpose（a）\a.T
位置：np.where(a>7)
去重：np.unique(去重的数字)
```

### 聚合函数

#### 数组求和

```python
总体求和：
	np.sum(a)
	a.sum()
每行求和：(axis:轴)
	np.sum(a,axis=1)
每列求和：
	np.sum(a,axis=0)
```

#### 最大值（最小值）

```python
总体求最值：
	np.min（a）\ a.min()
    np.max（a）\ a.max()
每行求最值：
	np.min(a,axis=1)
    np.max(a,axis=1)
每列求最值：
	np.min(a,axis=0)
    np.max(a,axis=0)
```

#### 平均值

```python
np.mean(a)
```

#### 中位数

```python
np.median(a)
```

#### 累计求和

```python
np.cumsum(a)
每次求和结果于下一个元素作用求和
```

#### 相邻两个元素求差值

```python
np.diff(a)
```

#### 矩阵最小(大)值所在的位值

```python
np.argmin(a)
np.argmax(a)

拉伸成一行在。。。
可以有轴
```

#### 矩阵元素的替换

```python
np.clip(a,5,9)
在矩阵a中，`小于5的替换为5`, `大于9的替换为9`
```

#### 矩阵的逐行排序

```python
np.sort(a,axis=0/1)
```

### 合并/拼接、分割数组

#### 合并/拼接数组

```python
合并/拼接：
	np.concatenate((a,b)[,axis=0/1])  #axis=0：b在下，axis=1：b在右
    行拼接：
    	np.vstack((a,b))
    列拼接：
    	np.hstack((a,b))
```

#### 分割数组

```python
np.hsplit(a,3)    #纵向分割数组为3份
np.vsplit(a,2)    #横向分割数组为2份
```

## 导入txt文件

```python
np.loadtext()
```

## 线性代数计算

### 矩阵和矢量积

```python
np.dot(a,b)  # 数组a,b的点积
np.vdot(a,b)  # 向量a,b的点积
np.inner(a,b)   # 数组a，b的内积
np.outer(a,b)   # 数组a，b的外积
np.matmul（a，b）  # 数组a，b的矩阵的成绩
np.tensordot(a,b [,轴])   #沿指定轴计算张量点积
np.linalg.matrix_power(a,n)   #将方阵提高到（整数）幂n

```

### 分解

#### Cholesky分解 

> np.linalg.cholesky（a） 
>
> 正定矩阵的分解：l=np.linalg.cholesky(b)得到下三角矩阵,np.dot(l,l.T)=b

#### (svd)奇异值分解

```python
np.linalg.svd（a）

非正定矩阵的分解:U,s,V=np.linalg.svd(b),S=np.array([[s[0],0],[0,s[1]]),则np.dot(U,np.dot(S,V)))=b
```

### 特征值

#### 方阵特征值（特征向量）

> np.linalg.eig(a)

#### Hermitian或对称矩阵的特征值（特征向量）

> np.linalg.eigh(a [,UPLO])

#### 一般矩阵的特征值

> 特征值、特征向量：u,v=np.linalg.eigvals(a)  

#### 计算Hermitian或者实对称矩阵的特征值

> np.linalg.eigvalsh(s [,uplo])

### 范数/行列式/条件数/逆/迹/秩

#### 逆

> np.linalg.inv(a)

#### 范数

> np.linalg.norm(a[,ord,axis,keepdims])
>
> 默认求2范数，ord=1求1范数，ord=np.inf求无穷范数
>
> 1-范数:将矩阵沿列方向取绝对值求和，然后选出数值最大的那个值
>
> 2-范数：矩阵的最大特征值开平方

#### 条件数

> np.linalg.cond(x [,p])

#### 行列式

> np.linalg.det(a)

#### 迹

> np.	trace(A)(主对角线上各元素之和）

#### 秩

> np.linalg.matrix_rank(A)



### 求解方程个反转矩阵

#### 求解线性方程组或者线性标量方程组

> np.linalg.solve(a,b)

#### 求解x的张量方程：ax=b

> np.linalg.tensorsolve(a,b)

#### 将最小二乘解返回到线性矩阵方程

> np.linalg.lstsq(a,b [,rcond])



# Panadas

>  import panadas as pd

> 数据结构和数据分析

## 两种数据结构：

### Series

> 索引值可以重复（自定义）

### DataFrame

> 一组有序的列，每列可以是不同的值类型（数值、字符、布尔等）

## 读excle文件

```python
# data1 = pd.read_excel('C:\\Users\\Administrator\\Desktop\\remmand.xlsx')
# data = data1.values
# data = data.T
```

## Series

> 构建出来为一列数

### 创建序列

```python
s=pd.Series(data,index,dtype,copy)
data的数据类型：
	列表： data=[1,2,3,4]
    	a=pd.Series([1,2,3],index=['a','b','c'],dtype='int',name='something')
    一维数组： data=np.array([1,2,3,4])
    	d=pd.Series(np.array([1,2,3]),dtype='int',name='something')
    标量： data=5
    	b=pd.Series(5,index=['a','b','c'],dtype='int',name='something')
    字典型（字典的键用于构建索引）： data={'a':1,'b':2}
    	c=pd.Series({'a':1,'b':2,'c':2},dtype='int',name='something')
```

### 基本属性(赋值、获取)

* s.index
* s.value
* s.name
* s.dtype
* s.shape
* len(s) [说明：包含缺失值]，s.count()  [说明：不包含缺失值]
* s.unique()  [不重复的值]
* s.value_counts()  : 选出各个value的频数

### 缺失值的操作

#### 给缺失值一个预设

> s.fillna(值)

#### 删除缺失值

> s.dropna()

### 数据操作

#### 取值

* 单行  ： s[0]/s['索引']
* 指定行 ： s[[0,3]]  =>  0行和3行         ;    s[['a','c']]        ==>  a行和c行（a和c为索引）
* 前后几行 ： s.head(值)/s.tail(值)  =>  默认值为5
* 修改/增加值 ： s['a']=3

#### 切片

* s[:2]    ==>  0-1行
* s[-2:]   ==>   访问最后两个元素

#### 索引

* 按索引标签索引

  ```python
  单个：
  	s['a']   #a为索引值
  多个：
  	s[['a','c']]    #a、c为索引值
  ```

* 布尔索引

  ```python
  s[s>条件（s.mean()等）]
  ```

### 运算

> 两个运算的单元必须索引和长度一样，不一样，在缺省位置自动补充Nan

```python
s1=pd.Series([1,2,3],index=['a','b','c'])
s2=pd.Series([3,2,1],index=['a','b','c','d'])

计算
s1.add(s2,fill_value=值)
s1.sub(s2,fill_value=值)
s1.mul(s2,fill_value=值)
s1.div(s2,fill_value=值)
```

## DataFrame

### 创建

```python
df=pd.DataFrame(data,index,columns,dtype,copy)

data:
    列表：
        data=[1,2,3,4]
        data=[[1,2],[3,4]]
        字典形式（键默认为列名）： data=[{'a':1,'b':2},{'a':3,'b':4,'c':5}]
    序列：
    	data={'one':pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2],index=['a','b'])}
    字典：
    	data={'one':[1,2,3,4],'two':[5,6,7,8]}
    多维数组：
    data是另一个DataFrame
    df里是层次索引
```

### 数据操作

#### 追加一列

* df['four']=df['one']+df['three']

#### 取值

##### 列

* 列选择：df['one']
* 列添加：df['three']=pd.Series([10,20,30],index=['a','b','c'])
* 列删除： 
  * del df['one']  ：在原数据上进行操作
  * df.drop(['a'],axis=1)   :   返回一个新数据
* 列名称的修改：df.columns=['','']  给个新的名字

##### 行

* 行切片： df[1:]  
* 列中前两行： `df['one'][:2]`
* 选择前后几行：df.head(n)    df.tail(n)   => n不传值默认是5
* 按标签选择：
  * 选择特定的行  df.loc['a']     /    df.loc[['s']]
  * 按行与列的名称选择某值    df.loc['a','one']    //      df.at['a','one']
  * 通过标签选择多轴：df.loc[:,['one','two']]
* 按位置选择
  * 选择特定的行： df.iloc[0]    /   df.iloc[[0]]
  * 按行与列的名称选择某值：    df.iloc[0,0]  /    df.iat[0,0]
  * 通过标签选择多轴： df.iloc[[0,1],[0,1]]      /    df.iloc[0:3,:]
* 附加行
  * dfa=pd.DataFrame([[5,6],[7,8]],index=['e','f'],columns=['one','two'])
  * df.append(dfa)

#### 布尔索引

> df[df.one>0]    df[df<0]
>
> 过滤： df[df['two'].isin([2,3])]

### 编码区分：

>  pd.get_dummies(df[['dist','floor']])

### 解决共线性

> 随意删除两列（不同分类的列）

### 文件读取

> pd.read_csv('文档路径',sep=‘ ：’，header=None)

### 基本属性

* df.index
* df.columns
* df.values
* df.shape
*  df.info( )   :    获取数据的基本信息
* df.count()   :     非Nan 值得数量
* df.dtypes

### 排序

* df.sort_index(ascending=False)  ：  行索引排序，排索引  ，ascending： 是否升序
* df.sort_values(by='列索引',ascending=False)   :    by以哪列为准

### 藐描述性统计

* df.describe()   ：  是用来计算有关DataFrame列的统计信息的摘要
* df.mean()     、  df.median()
* df.std()     标准差
* df.cumsum    累计总和
* df.min()/df.max()    
* df.idxmin()  /df.idmax ()   取得最值对应的索引 

### 应用函数

> apply（）方法沿DataFrame的轴应用任意函数。默认情况下，操作`按列执行`

* df.apply(np.mean)
* df.apply(np.mean,axis=1)
* df.apply(lambda x:x.max()-x.min())     //  x.replace()

### 缺失数据处理

#### 检查是否存在Nan/缺失数据：

> df.isnull（）.sum（）

#### 去除缺失值：

* df.dropna()
* df.dropna(how='all')   =>   ` all`：全是缺失值时删除；  `any` : 有缺失值时删除
* df.dropna(axis=1)   =》 列方向操作

#### 用预备值填充

> df.fillna(de.mean())

### 拼接: concat

* pd.concat([s,s2],axis=1,key=['one','two'])
* pd.concat([df1,df2],axis=1,join='outer')
* df1.concat(df2,how='outer')   => 等价于上一个

### 合并：merge

> df1   df2有共同的标签

* pd.merge(df1,df2,how='left',on='X1')
* pd.merge(df1,df2,how='right',on='X1')
* pd.merge(df1,df2,how='inner',on='X1')
* pd.merge(df1,df2,how='outer',on='X1')

### 导入导出

> http://pandas.pydata.org/pandas-docs/stable/api.html#input-output

### 绘图

> http://pandas.pydata.org/pandas-docs/version/0.13.1/visualization.html





# Matplotlib

> 绘图

## 导入绘图模块

> import matplotlib.pyplot as plt

## plt.plot中的字段

* 绘制简单的图
  * plt.plot（[1,2,3]）   坐标为：（0,1），（1,2），（2,3）
  * plt.plot（[1,2,3],[4,5,6]）    坐标为：（1,4），（2,5），（3,6）
* 创建画布 ： plt.figure(figsize=(8,4))
* 线框： linewidth/w
* 颜色：color
* 线性：linestyle
* 标记点的形状： marker
* 点的填充色：markfacecolor
* 设置透明度：alpha=0.n（n:0-9）

## 基础

### 显示图例信息（搭配label）

```python
plt.legend(loc='best')
plt.legend(loc='lower/uper right/left')
在plt.plot()中添加字段信息 label=‘图例名称’
```

### 显示中文和负号（正常显示）

```python
中文：
	plt.rcParams['font.sans-serif']=['Microsoft YaHei']
负数：
	plt.rcParams['axes.unicode_minus']=False	
```

### 添加水平轴和竖直轴的文字

```python
plt.xlabel('x轴名字')
plt.ylabel('y轴名字')
```

### 设置x、y轴的刻度范围

```python
plt.xlim(0,10)
plt.ylim(0,10)
```

### 控制图标的刻度

```python
plt.xticks(np.linespace(1,10,10),[str[i]+''for i in range(1,11)])
```

### 添加标题

```python
plt.title('标题')
```

### 添加标注文字

```python
plt.annotate('文字',xy=(2.5,4))    文字和文字开始的位置
```

### 添加箭头

```python
plt.annotate('文字',xy=(2.5,4),xytext=(4,8),arrowprops=dict(facecolor='black'))   : =>   xytext文本位置，箭头重点xy
```

### 显示网格

```python
plt.grid(True)
```

### 设置边框

```python
1. 获取坐标轴信息
	ax=plt.gca()
2. 设置边框
	ax.spines['right/left/top/bottom'].set_color['none']
```

## 子图绘制

### 绘制

#### 方法一

```python
ax1=plt.subplot(221)   ：=》 创建2行2列的第一个
x=...
y=...
plt.plot（x,y）
```

#### 方法二

```python
fig=plt.figure()
ax1=fig.add_subplot(221)
x=...
y=...
plt.plot(x,y)
```

### 添加标题

```python
ax1.set_title('标题')
```

### 添加坐标轴文字

```python
ax1.set_xlabel('x轴坐标信息')
ax1.set_ylabel('y轴坐标信息')
```

## 可视化

### 散点图 :plt.scatter()

### 折线图：plt.plot()

```python
横坐标文字旋转：
	fig.autofmt_xdate(rotation=45)
```

### 条形图

```python
plt.bar(x)
df['文字'].plot(kind='bar')
```

### 直方图

```python
1. plt.hist()
2. df['文字'].plot(kind='hist')
3.累计分布直方图
	df['文字'].plot(kind='hist'，cumulative=True,legend=True,edgecolor='k',alpha=0.4,title='文字')
```

### 饼图：plt.pie（）

### 箱线图：plt.boxplot（）













