---
typora-root-url: readme_img
---

## 小小厨app说明文档：

#### 一、需安装的环境以及软件

1、Python3.7 解析器（https://www.python.org/getit/）------3.7.0

2、WampServer64或者MySQL数据库（环境安装文件夹中附带WampServer64安装包）

#### 二、下载安装python运行环境

<https://www.python.org/downloads/release/python-372/>

下载：

![image](https://github.com/X-weijia/LittleKitchen/blob/master/LittleKitchen/readme_img/图片1.png)

安装：（请勾选“Add Python 3.7 to PATH”选项，之后一路确定即可）

![image](https://github.com/X-weijia/LittleKitchen/blob/master/LittleKitchen/readme_img/图片2.png) 

#### 三、win+R进入cmd命令窗口，输入python，出现“>>>”表示python环境变量安装成功。

1、Win+R    输入cmd   确定：

![image](https://github.com/X-weijia/LittleKitchen/blob/master/LittleKitchen/readme_img/图片3.png) 

2、输入python 出现以下界面，即为成功。然后输入 exit() 

![image](https://github.com/X-weijia/LittleKitchen/blob/master/LittleKitchen/readme_img/图片4.png) 

 

#### 四、导入数据库以及项目中使用的包

1、先打开环境安装文件夹，安装其中的wamp64（按照安装说明顺序安装，之后一路确定即可）

![image](https://github.com/X-weijia/LittleKitchen/blob/master/LittleKitchen/readme_img/图片5.png) 

2、打开wamp64，点击右下角图标，打开phpMyAdmin，新建名为LittleKitchen的数据库 ，如图所示：

![image](https://github.com/X-weijia/LittleKitchen/blob/master/LittleKitchen/readme_img/图片6.png) 
![image](https://github.com/X-weijia/LittleKitchen/blob/master/LittleKitchen/readme_img/图片7.png) 

3、左侧列表中找到刚刚创建的数据库，点击打开，右侧上方点击导入，如图：

![image](https://github.com/X-weijia/LittleKitchen/blob/master/LittleKitchen/readme_img/图片8.png) 
![image](https://github.com/X-weijia/LittleKitchen/blob/master/LittleKitchen/readme_img/图片9.png) 

在导入界面选择sql文件（环境安装文件夹中附带），点击执行

4、导入包

打开项目文件夹，

![image](https://github.com/X-weijia/LittleKitchen/blob/master/LittleKitchen/readme_img/图片10.png) 

![image](https://github.com/X-weijia/LittleKitchen/blob/master/LittleKitchen/readme_img/图片11.png) 

输入cmd回车之后进入命令行，如下：

![image](https://github.com/X-weijia/LittleKitchen/blob/master/LittleKitchen/readme_img/图片12.png) 
在命令行界面输入 python -m pip install -r packages.txt 命令，导入所需模块。

（packages.txt文件在项目文件夹中）

![image](https://github.com/X-weijia/LittleKitchen/blob/master/LittleKitchen/readme_img/图片13.png) 

​ 

#### 五、运行程序

1、打开wamp64，保证数据库可连接

![image](https://github.com/X-weijia/LittleKitchen/blob/master/LittleKitchen/readme_img/图片14.png) 

2、输入python manage.py runserver 命令，

![image](https://github.com/X-weijia/LittleKitchen/blob/master/LittleKitchen/readme_img/图片15.png) 

3、在浏览器地址栏中输入 127.0.0.1:8000 即可访问。

![image](https://github.com/X-weijia/LittleKitchen/blob/master/LittleKitchen/readme_img/图片16.png) 