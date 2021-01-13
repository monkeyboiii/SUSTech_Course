使用方法:

1. 只需要改config.json文件中的username(学号), password, course_forms三个参数

2. course_forms是先正常登录tis网站, 点开"我要选课", 按F12打开开发者模式, 再点击"选课"按钮选要抢的课,
看到addGouwuche请求, 把这个post请求的body参数作为字符串复制进course_forms数组, 详见图片.

3. 之后直接在终端里python main.py运行.