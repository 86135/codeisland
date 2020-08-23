import sys
help_text=r'''
命令行语法：
codeisland [命令]

欢迎使用CodeIsland命令行！目前正在开发，只完成了帮助功能。

命令：
help - 显示帮助
'''
unknown_text=r'''
命令行语法：
codeisland [命令]

无法识别命令。
'''
#好像机器说话。。。
def cli_0_0_4_in_develop(l=sys.argv):
	global help_text,unknown_text
	if l == ['codeisland'] or l == ['CodeIsland'] or l == ['codeisland','help'] or l == ['CodeIsland','help'] or l == ['py','-m','codeisland'] or l == ['py','-m ','CodeIsland'] or l == ['python','-m','codeisland','help'] or l == ['python','-m ','CodeIsland'] or l == ['py','-m','codeisland','help'] or l == ['py','-m ','CodeIsland','help'] or l == ['python','-m','codeisland','help'] or l == ['python','-m ','CodeIsland','help']:
		return help_text
	else:
		return unknown_text
if __name__ == '__main__':
	sys.exit(cli_0_0_4_in_develop())
