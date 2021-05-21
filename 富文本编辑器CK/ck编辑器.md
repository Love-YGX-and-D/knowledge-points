# 安装和配置

## 1.js配置

```css
1.在index.html中引入文件ckeditor.js
<script src='static/ckeditor/ckeditor.js' type="text/javascript"></script>
2.配置webpack文件配置  build/webpack.base.conf.js
module.exports = {
 externals: {
    "CKEDITOR": "window.CKEDITOR"
  },
}
3.<textarea id="editor" rows="10" cols="80"></textarea>

js中需要引入，生命周期中mounted需要引入如下代码
import CKEDITOR from 'CKEDITOR';
mounted() {
  CKEDITOR.replace('editor', {height: '400px', width: '100%', toolbar: 'toolbar_Full'});
  this.editor = CKEDITOR.instances.editor;
}

```

## 2.npm命令安装

```css

```



# 1、获取内容getData()**

```javascript
添加一片文章，就要获取编辑器中的内容，上文中，我们已经保存了编辑器实例，可以用this.editor调用，所以获取内容就变得简单了
this.editor.getData()
```

# **2.初始化编辑器内容setData()**

```javascript
编辑一篇文章时，需要将文章信息放入编辑器，在此，我们使用setData()方法，contentVal指文章内容，自行替换

this.setData(contentVal)
```

# **3、编辑器设为只读 isReadOnly**

```javascript
展示一篇文章，我们绝对不能直接放在容器中将保存的内容通过v-html直接渲染出来
editor.isReadOnly = true; //将编辑器设为只读
```

# **4、设置为中文**

```javascript
引入中文包
 import '@ckeditor/ckeditor5-build-decoupled-document/build/translations/zh-cn'import '@ckeditor/ckeditor5-build-decoupled-document/build/translations/zh-cn'

初始化编辑器时进行配置
CKEditor.create(document.querySelector('#editor'), {
  language: 'zh-cn',
}).then(editor => {      
}).catch(error => {        
});

```

# 高级

## npm init:一路回车

根目录的node_modules   ==>实现共用

根目录没有,在子孩子中找,子孩子中没有,则在当前目录创建node_modules文件,在放进



解决npm安装是cpu占用过高问题

```css
npm install typescript --registry=http://registry.npm.taobao.org

```

