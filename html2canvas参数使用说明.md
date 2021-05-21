html2canvas

## 参数使用说明

| 参数                   | 默认值                    | 说明注释                                                     |
| ---------------------- | ------------------------- | ------------------------------------------------------------ |
| allowTaint             | `false`                   | Whether to allow cross-origin images to taint the canvas<br /> 是否允许跨域图像污染画布 |
| backgroundColor        | `#ffffff`                 | Canvas background color, if none is specified in DOM. Set `null` for transparent<br />画布背景色（如果未在DOM中指定）。设置`null`为透明 |
| canvas                 | `null`                    | Existing `canvas` element to use as a base for drawing on<br />现有`canvas`元素用作绘图的基础 |
| foreignObjectRendering | `false`                   | Whether to use ForeignObject rendering if the browser supports it<br />如果浏览器支持，是否使用ForeignObject渲染 |
| imageTimeout           | `15000`                   | Timeout for loading an image (in milliseconds). Set to `0` to disable timeout.<br />加载图像的超时时间（以毫秒为单位）。设置`0`为禁用超时。 |
| ignoreElements         | `(element) => false`      | Predicate function which removes the matching elements from the render.<br />谓词功能，可从渲染中删除匹配的元素 |
| logging                | `true`                    | Enable logging for debug purposes<br />启用日志记录以进行调试 |
| onclone                | `null`                    | Callback function which is called when the Document has been cloned for rendering, can be used to modify the contents that will be rendered without affecting the original source document.<br />克隆文档以进行渲染时调用的回调函数可用于修改将要渲染的内容，而不会影响原始源文档 |
| proxy                  | `null`                    | Url to the [proxy](http://html2canvas.hertzen.com/proxy/) which is to be used for loading cross-origin images. If left empty, cross-origin images won’t be loaded.<br />[代理](http://html2canvas.hertzen.com/proxy/)将用于加载跨域图像的网址。如果留空，则不会加载跨域图像。 |
| removeContainer        | `true`                    | Whether to cleanup the cloned DOM elements html2canvas creates temporarily<br />是否清除HTML2canvas临时创建的克隆DOM元素 |
| scale                  | `window.devicePixelRatio` | The scale to use for rendering. Defaults to the browsers device pixel ratio.<br />用于渲染的比例尺。默认为浏览器设备像素比率。 |
| useCORS                | `false`                   | Whether to attempt to load images from a server using CORS<br />是否尝试使用CORS从服务器加载图像 |
| width                  | `Element` width           | The width of the `canvas`<br />                              |
| height                 | `Element` height          | The height of the `canvas`<br />                             |
| x                      | `Element` x-offset        | Crop canvas x-coordinate<br />                               |
| y                      | `Element` y-offset        | Crop canvas y-coordinate<br />                               |
| scrollX                | `Element` scrollX         | The x-scroll position to used when rendering element, (for example if the Element uses `position: fixed`)<br />渲染元素时要使用的x滚动位置（例如，如果Element使用`position: fixed`） |
| scrollY                | `Element` scrollY         | The y-scroll position to used when rendering element, (for example if the Element uses `position: fixed`)<br />呈现元素时要使用的y-scroll位置（例如，如果Element使用`position: fixed`） |
| windowWidth            | `Window.innerWidth`       | Window width to use when rendering `Element`, which may affect things like Media queries<br />渲染时要使用的窗口宽度`Element`，这可能会影响媒体查询之类的内容 |
| windowHeight           | `Window.innerHeight`      | Window height to use when rendering `Element`, which may affect things like Media queries<br />渲染时要使用的窗口高度`Element`，这可能会影响媒体查询之类的内容 |

