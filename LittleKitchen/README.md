## 小小厨app说明文档：

#### 一、需安装的环境以及软件

1、Python3.7 解析器（https://www.python.org/getit/）------3.7.0

2、WampServer64或者MySQL数据库（环境安装文件夹中附带WampServer64安装包）

#### 二、下载安装python运行环境

<https://www.python.org/downloads/release/python-372/>

下载：

![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml\wps7189.tmp.jpg) 

安装：（请勾选“Add Python 3.7 to PATH”选项，之后一路确定即可）

![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml\wps7199.tmp.jpg) 

#### 三、win+R进入cmd命令窗口，输入python，出现“>>>”表示python环境变量安装成功。

1、Win+R    输入cmd   确定：

![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml\wps719A.tmp.jpg) 

2、输入python 出现以下界面，即为成功。然后输入 exit() 

![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml\wps719B.tmp.jpg) 

 

#### 四、导入数据库以及项目中使用的包

1、先打开环境安装文件夹，安装其中的wamp64（按照安装说明顺序安装，之后一路确定即可）

![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml\wps71AC.tmp.jpg) 

2、打开wamp64，点击右下角图标，打开phpMyAdmin，新建名为LittleKitchen的数据库 ，如图所示：

![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml\wps71AD.tmp.jpg)![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml\wps71AE.tmp.jpg) 

3、左侧列表中找到刚刚创建的数据库，点击打开，右侧上方点击导入，如图：

![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml\wps71AF.tmp.jpg)![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml\wps71C0.tmp.jpg) 

在导入界面选择sql文件（环境安装文件夹中附带），点击执行

4、导入包

打开项目文件夹，

![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml\wps71C1.tmp.jpg) 

![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml\wps71C2.tmp.jpg) 

输入cmd回车之后进入命令行，如下：

![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml\wps71D2.tmp.jpg) 

在命令行界面输入 python -m pip install -r packages.txt 命令，导入所需模块。

（packages.txt文件在项目文件夹中）

![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml\wps71D3.tmp.jpg) 

​    

#### 五、运行程序

1、打开wamp64，保证数据库可连接

![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml\wps71D4.tmp.jpg) 

 

2、输入python manage.py runserver 命令，

![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml\wps71E5.tmp.jpg) 

3、在浏览器地址栏中输入 127.0.0.1:8000 即可访问。

![img](file:///C:\Users\ADMINI~1\AppData\Local\Temp\ksohtml\wps71E6.tmp.jpg) 