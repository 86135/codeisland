'''
range()函数返回的是range类型，而不是list。
'''
from socket import socket
from sys import stdout
def print(*objects,sep=' ',end='\n'):
	for i in objects:
		stdout.write(i.__str__())
		if objects.__len__()>1:
			stdout.write(sep)
	stdout.write(end)
runbool=True
def ex(signum,frame):
	global runbool
	runbool=False
from .supportservers import SSSRequestHandler
from .supportservers import SHSRequestHandler
from .supportservers import SWSRequestHandler
from socketserver import TCPServer
from http.server import HTTPServer
from wsgiref.simple_server import WSGIServer
class CodeIsland(object):
	def __init__(cdil,host:str='127.0.0.1',port:int=1300,server='CodeIsland'):
		assert server in ['CodeIsland','SSS','SHS','SWS'],'Not support your server'
		cdil.__server=server
		cdil.__hopo = (host,port)
		cdil.__rd = {}
		cdil.__socket = socket()
		cdil.__path = '/'
		cdil.__method = 'GET'
		cdil.__mimetype='text/plain'
		cdil.__mimetype404='text/plain'
		cdil.__mimetype500='text/plain'
		cdil.__404=[lambda: b'<img src="https://http.cat/404.jpg" /><br />(Image is from http.cat)','text/html']
		cdil.__500=[lambda: b'<img src="https://http.cat/500.jpg" /><br />(Image is from http.cat)','text/html']
	def route(cdil,path:str='/',method:str='GET',mimetype='text/html'):
		assert path[0] == '/',"/"
		cdil.__path = path
		cdil.__method = method
		cdil.__mimetype=mimetype
		return cdil.__routeD
	def __process_form_data_to_dict(cdil,formdata):
		l=formdata.split('&')
		from copy import deepcopy as dc
		ll=dc(l)
		l=[i.split('=') for i in ll]
		d={}
		for i in l:
			d[i[0]]=i[1]
		return d
	def __routeD(cdil,func):
		cdil.__rd[cdil.__path]=func,cdil.__method,cdil.__mimetype
		cdil.__path='/'
	def if404(cdil,mimetype='text/html'):
		cdil.__mimetype404=mimetype
		return cdil.__if404D
	def __if404D(cdil,func):
		cdil.__404=[]
		cdil.__404.append(func)
		cdil.__404.append(cdil.__mimetype404)
		cdil.__mimetype404='text/plain'
	def if500(cdil,mimetype='text/html'):
		cdil.__mimetype500=mimetype
		return cdil.__if500D
	def __if500D(cdil,func):
		cdil.__500=[]
		cdil.__500.append(func)
		cdil.__500.append(cdil.__mimetype500)
		cdil.__mimetype500='text/plain'
	def run_CodeIsland(cdil):
		'''Run web project use a server called CodeIsland and based on socket'''
		cdil.__socket.bind(cdil.__hopo)
		cdil.__socket.listen(10)
		print('Server on port '+str(cdil.__hopo[1]))
		global runbool
		while runbool:
			from signal import signal,SIGINT
			signal(SIGINT,ex)
			con=cdil.__socket.accept()[0]
			headers = con.recv(1024).decode('utf-8').split('\r\n')
			try:
				path = headers[0].replace(' HTTP/1.1','').split()[1]
			except:
				con.send(b'HTTP/2.x 400 Bad Request\r\nServer: CodeIsland\r\n\r\n')
				continue
			method = headers[0].replace(' HTTP/1.1','').split()[0]
			try:
				from json import loads
				if method == 'POST':
					cdil.formdata=loads(headers[-1])
				if '?' in path:
					llll=path.split('?')
					path=llll[0]
					cdil.formdata=cdil.__process_form_data_to_dict(llll[1])
				if not (path in cdil.__rd.keys()):
					runfunc=cdil.__404[0]()
					con.send(b'HTTP/2.x 404 Not Found\r\nContent-type: '+cdil.__404[1].encode()+b'\r\nServer: CodeIsland\r\n\r\n')
					print(headers[0],headers[2],'404 Not Found')
					con.send(runfunc)
					continue
				for i in cdil.__rd.keys():
					if path==i:
						if cdil.__rd[i][1]==method:
							runfunc=cdil.__rd[i][0]()
							if runfunc==b'':
								con.send(b'HTTP/2.x 204 No Content\r\nServer: CodeIsland\r\n\r\n')
								con.send(b'')
								print(headers[0],headers[2],'204 No Content')
							else:
								con.send(b'HTTP/2.x 200 OK\r\nContent-type: '+bytes(cdil.__rd[i][2],encoding="utf8")+b'\r\nServer: CodeIsland\r\n\r\n')
								con.send(runfunc)
								print(headers[0],headers[2],'200 OK')
			except Exception as e:
				runfunc=cdil.__500[0]()
				con.send(b'HTTP/2.x 500 Internal Server Error\r\nContent-type: '+cdil.__500[1].encode()+b'\r\nServer: CodeIsland\r\n\r\n')
				con.send(runfunc)
				print(headers[0],headers[2],'500 Internal Server Error')
				def r(e):
					raise e
				from threading import Thread as TH
				TH(target=r,kwargs={'e':e}).start()
				continue
	def run_SSS(cdil):
		'''Run web project use a server called SSS(Support SocketServer) and based on socketserver'''
		sss=SSSRequestHandler
		sss.rd=cdil.__rd
		sss.l404=cdil.__404
		sss.l500=cdil.__500
		try:
			TCPServer(cdil.__hopo,sss).serve_forever()
		except KeyboardInterrupt:
			pass
	def run_SHS(cdil):
		'''Run web project use a server called SHS(Support Http.Server) and based on http.server'''
		shs=SHSRequestHandler
		shs.rd=cdil.__rd
		shs.l404=cdil.__404
		shs.l500=cdil.__500
		try:
			HTTPServer(cdil.__hopo,shs).serve_forever()
		except KeyboardInterrupt:
			pass
	def run_SWS(cdil):
		'''Run web project use a server called SWS(Support WSGIServer) and based on wgsiref.simple_server'''
		sws=SWSRequestHandler
		sws.rd=cdil.__rd
		sws.l404=cdil.__404
		sws.l500=cdil.__500
		try:
			WSGIServer(cdil.__hopo,sws).serve_forever()
		except KeyboardInterrupt:
			pass
	def run(cdil):
		if cdil.__server=='CodeIsland':
			cdil.run_CodeIsland()
		elif cdil.__server=='SSS':
			cdil.run_SSS()
		elif cdil.__server=='SHS':
			cdil.run_SHS()
		elif cdil.__server=='SWS':
			cdil.run_SHS()
		else:
			raise BaseException('Not support your server')
	def __call__(cdil):
		cdil.run()

