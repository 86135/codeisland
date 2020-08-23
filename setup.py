from setuptools import setup,find_packages
ld=r"""
codemao（编程猫）用户86135开发的网页框架，基于socket，测试版
举个例子：
-------------
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
0.0.2更新:
[ + ] 对socketserver的支持
0.0.3更新：
[ c ] 修bug
后续还会开发，敬请期待。
如有bug或建议，请发邮件：340260733@qq.com
"""
classifiers=['Development Status :: 1 - Planning','License :: OSI Approved :: MIT License','Operating System :: Microsoft','Programming Language :: Python :: 3 :: Only']
setup(name='CodeIsland',version='0.0.7',author='86135',author_email='340260733@qq.com',description='codemao用户86135开发的网页框架，基于socket，测试版',long_description=ld,long_description_content_type="text/plain",packages=find_packages(),classifiers=classifiers,python_requires='>=3.6')
