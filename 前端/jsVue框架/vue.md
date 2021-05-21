# mvvm

mvc[model view controller]  ---前后端分离  ->   mvvm[model view 双向数据绑定]  ---前端框架



# 指令





# 生命周期函数

mounted(){

​	fetch("抓取数据的路径").then(function (e){

​		return e.json()

​	}),then((e)=>{

​		this.aa=e

​	})

}





# 路由

m:模型-v:视图-c:控制器







# 状态





# 组件

> 函数



完整的结构

完善的逻辑

完整的数据



# 案例

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script src="vue.min.js"></script>
</head>
<body>
<div class="app">
    <input type="text" class="num1" v-model="one">+<input type="text" class="num2" v-model="two">
    <br><span v-text="result()"></span>
    <br><span v-text="result1"></span>
    <br><span v-text="result2"></span>
</div>
</body>
</html>
<script>
    // var num1=document.querySelector(".num1")
    // var num2=document.querySelector(".num2")
    // var submit=document.querySelector(".submit")
    // var span=document.querySelector("span")
    // submit.onclick=function () {
    //     var num11=Number(num1.value)
    //     var num22=Number(num2.value)
    //     if (typeof num11=="number" && typeof num22=="number"){
    //         span.innerHTML=num11+num22
    //     }
    // }
    // new Vue({
    //     el:".app",
    //     data:{
    //         one:0,
    //         two:0
    //     }
    // })
    setTimeout(function () {
        new Vue({
            //vue接管的范围
            el:".app",
            //数据区域
            data:{
                one:0,
                two:0,
                result2:0,
            },
            //逻辑区域,result是一个方法,只要data中的数据变化一次，就会执行一次
            methods:{
                result(){
                    if(this.one*1>10){
                        return this.one*1-this.two*1
                    }else{
                        return this.one*1+this.two*1
                    }
                }
            },
            //逻辑计算区域,result是一个数据，和区间的变量有关，区间变量改变就会执行---动态变化的数据
            computed:{
                result1(){
                    if(this.one*1>10){
                        return this.one*1-this.two*1
                    }else{
                        return this.one*1+this.two*1
                    }
                }
            },
            //指定【定义】一下返回值在data部分，数据渲染直接在‘t-text’后使用
            watch:{
                one(o,t){
                    return this.result2=this.one*1+this.two*1
                },
                two(o,t){
                    return this.result2=this.one*1+this.two*1
                }
            }
        })
    },2000)
</script>
```

# 创建开发环境

## 1.安装手架

```css
npm install -g @vue/cli
```

## 2.创建

```css
vue create 名字
vue init packweb 
```

# 全局跳路由

this.$router.push("/")

# 组件数据参数

```vue
<template>
    <el-container class="max">
        <el-header class="head">
            头部欢迎区
        </el-header>
        <el-container class="con">
            <el-aside class="Aside">
                <el-button type="success" @click="addTableName()">添加表</el-button>
                <div class="block">
                    <el-tree :data="menus" show-checkbox node-key="id" default-expand-all :expand-on-click-node="false">
                        <span class="custom-tree-node" slot-scope="{ node, data }">
                            <span v-if="data.type==1"><i class="el-icon-message"></i>{{ node.label }}</span>
                            <span v-else><i class="el-icon-tickets"></i>{{ node.label }}</span>
                            <el-button type="text" size="mini" @click="() => append(data)" v-show="data.type==1">添加</el-button>
                            <el-button type="text" size="mini" @click="() => remove(node, data)">删除</el-button>
                        </span>
                    </el-tree>
                </div>
            </el-aside>
            <el-container class="conSon">
                <el-main class="main">
                    主区
                    <router-view>

                    </router-view>
                </el-main>
                <el-footer class="foot">页码区

                </el-footer>
            </el-container>
        </el-container>
    </el-container>
</template>
<script>
    let id = 1000;
    export default{
        name:"App",
        data() {
            return{

            }
        },
        methods: {
            addTableName(){
               return this.$router.push("/addTableName")
            },
            append(data) {
                const newChild = { id: id++, label: 'testtest', children: [] };
                if (!data.children) {
                  this.$set(data, 'children', []);
                }
                data.children.push(newChild);
            },
            remove(node, data) {
                const parent = node.parent;
                const children = parent.data.children || parent.data;
                const index = children.findIndex(d => d.id === data.id);
                children.splice(index, 1);
            },
        },
        computed:{
            menus(){
                return this.$store.state.menus
            }
        }
    }
</script>

<style>
    *{
        margin: 0;
        padding: 0;
    }
    html,body{
        height: 100%;width: 100%;
    }
    .max{
        height: 100% !important;width: 100% !important;
    }
    .head{
        height: 8% !important;width: 100% !important;
        background: #cccccc;
    }
    .con{
        height: 92% !important;width: 100% !important;
    }
    .Aside{
        width: 20% !important;height: 100% !important;
        box-sizing: border-box;
        border-right: 3px solid #b0b0b0;
    }
    .conSon{
        width: 80% !important;height: 100% !important;
    }
    .main{
        width: 100% !important;height: 85% !important;
    }
    .foot{
        width: 100% !important;height: 10% !important;
    }
    .custom-tree-node {
        flex: 1;
        display: flex;
        align-items: center;
        justify-content: space-between;
        font-size: 14px;
        padding-right: 8px;
    }

</style>


<template>
    <div>
        <input type="text" v-model="cname"><br>
        <el-radio v-model="type" label="1">文件夹</el-radio>
        <el-radio v-model="type" label="2">文件</el-radio>
        <br>
        <el-button type="success" @click="submit()">确认并提交</el-button>
    </div>
</template>

<script>
    export default {
        name: "addTableNmae",
        data(){
            return{
                type: '1',
                cname:"",
            }
        },
        computed:{
            menus(){
                return this.$store.state.menus
            }
        },
        methods:{
            submit(){
                return this.$store.state.menus.push({label:this.cname,type:this.type})
            }
        }
    }
</script>

<style scoped>

</style>


export default new Vuex.Store({
  state: {
     menus:[]
  },
  mutations: {

  },
    actions:{

    }
})
```







## 路由传参

```vue
传递:
{
    // path:'/edit',
    path:"/edit/:id",
    name:'edit',
    component:edit
 },
获取:
 // this.id=this.$route.query.id;
    this.id=this.$route.params.id

```

# 模板实例化组件

```vue
<template>
    <form1 url="/ajax/edit"></form1>
</template>

<script>
    import form1 from '@/components/form.vue'
    export default {
        name: "edit1",
        components:{form1:form1}
    }
</script>

<style scoped>

</style>
```

```css
<template>
    <div>
        <label for="name">
            <span>姓名</span>
            <input type="text" id="name" v-model="name">
        </label><br>
        <label for="age">
            <span>年龄</span>
            <input type="text" id="age" v-model="age">
        </label><br>
        <label for="sex">
            <span>性别</span>
            <input type="text" id="sex" v-model="sex">
        </label><br>
        <input type="button" value="提交" @click="submit()">
    </div>

</template>

<script>
    export default {
        props:["url"],
        name: "add",
        data(){
            return{
                id:"",
                name:"",
                age:"",
                sex:""
            }
        },

        methods:{
            submit(){
                var str="name="+this.name+"&age="+this.age+"&sex="+this.sex
                fetch(this.url+"?"+str).then((e)=> {
                    return e.text()
                }).then((e)=> {
                    if (e=="ok"){
                        this.$router.push("/")
                    }
                })
            }
        }
    }
</script>

<style scoped>

</style>
```

# vue安装卸载

```css
sudo npm install -g vue-cli 安装
sudo npm install -g @vue/cli 安装最近vue3
sudo npm unintall -g vue-cli 卸载
```

# vue创建环境

## vue2创建

```css
vue init webpack 工程名称
cd aaa
npm run serve 启动环境
```

## vue3创建

```css
vue create 工程文件
```





