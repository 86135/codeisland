codemao（编程猫）用户86135开发的网页框架，基于socket，测试版
举个例子：
------------
|main.py x|
----------------------------------------------------
import codeisland
#不用from codeisland import CodeIsland，除非你愿意
cdil=CodeIsland()
@cdil.route('/')
def index():
    return open('<some file path here>','rb').read()
cdil()
#当然，也可以cdil.run()
----------------------------------------------------
0.0.1更新：
[ + ] 能自定义404、500时显示内容
[ c ] 按Ctrl+c时退出run方法
后续还会开发，敬请期待。
如有bug或建议，请发邮件：340260733@qq.com
