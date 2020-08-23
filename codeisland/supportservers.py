from socketserver import BaseRequestHandler
'''For SSS(Support SocketServer),SHS(Support HTTP.Server) and SWS(Support WSGI Server).'''
class SSSRequestHandler(BaseRequestHandler):
	'''For SSS(Support SocketServer) server. Override the "handle" method.'''
	rd={}
	l404=[lambda: b'<img src="https://http.cat/404.jpg" /><br />(Image is from http.cat)','text/html']
	l500=[lambda: b'<img src="https://http.cat/500.jpg" /><br />(Image is from http.cat)','text/html']
	def handle(SSS):
		while True:
			con=SSS.request
			headers = con.recv(1024).decode('utf-8').split('\r\n')
			try:
				path = headers[0].replace(' HTTP/1.1','').split()[1]
			except:
				con.send(b'HTTP/2.x 400 Bad Request\r\nServer: SSS\r\n\r\n')
				continue
			method = headers[0].replace(' HTTP/1.1','').split()[0]
			try:
				from json import loads
				if method == 'POST':
					SSS.formdata=loads(headers[-1])
				if '?' in path:
					llll=path.split('?')
					path=llll[0]
					SSS.formdata=cdil.__process_form_data_to_dict(llll[1])
				if not (path in SSS.rd.keys()):
					runfunc=SSS.l404[0]()
					con.send(b'HTTP/2.x 404 Not Found\r\nContent-type: '+SSS.l404[1].encode()+b'\r\nServer: SSS\r\n\r\n')
					print(headers[0],headers[2],'404 Not Found')
					con.send(runfunc)
					continue
				for i in SSS.rd.keys():
					if path==i:
						if SSS.rd[i][1]==method:
							runfunc=SSS.rd[i][0]()
							if runfunc==b'':
								con.send(b'HTTP/2.x 204 No Content\r\nServer: SSS\r\n\r\n')
								con.send(b'')
								print(headers[0],headers[2],'204 No Content')
							else:
								con.send(b'HTTP/2.x 200 OK\r\nContent-type: '+bytes(SSS.rd[i][2],encoding="utf8")+b'\r\nServer: SSS\r\n\r\n')
								con.send(runfunc)
								print(headers[0],headers[2],'200 OK')
			except Exception as e:
				runfunc=SSS.l500[0]()
				con.send(b'HTTP/2.x 500 Internal Server Error\r\nContent-type: '+SSS.l500[1].encode()+b'\r\nServer: SSS\r\n\r\n')
				con.send(runfunc)
				print(headers[0],headers[2],'500 Internal Server Error')
				def r(e):
					raise e
				from threading import Thread as TH
				TH(target=r,kwargs={'e':e}).start()
				continue
from http.server import BaseHTTPRequestHandler
class SHSRequestHandler(BaseHTTPRequestHandler):
	'''For SHS(Support Http.Server) server. Override the "handle_one_method" method.'''
	rd={}
	l404=[lambda: b'<img src="https://http.cat/404.jpg" /><br />(Image is from http.cat)','text/html']
	l500=[lambda: b'<img src="https://http.cat/500.jpg" /><br />(Image is from http.cat)','text/html']
	def handle_one_request(SHS):
		con=SHS.request
		headers = con.recv(1024).decode('utf-8').split('\r\n')
		try:
			path = headers[0].replace(' HTTP/1.1','').split()[1]
		except:
			con.send(b'HTTP/2.x 400 Bad Request\r\nServer: SHS\r\n\r\n')
			return
		method = headers[0].replace(' HTTP/1.1','').split()[0]
		try:
			from json import loads
			if method == 'POST':
				SHS.formdata=loads(headers[-1])
			if '?' in path:
				llll=path.split('?')
				path=llll[0]
				SHS.formdata=cdil.__process_form_data_to_dict(llll[1])
			if not (path in SHS.rd.keys()):
				runfunc=SHS.l404[0]()
				con.send(b'HTTP/2.x 404 Not Found\r\nContent-type: '+SHS.l404[1].encode()+b'\r\nServer: SHS\r\n\r\n')
				print(headers[0],headers[2],'404 Not Found')
				con.send(runfunc)
				return
			for i in SHS.rd.keys():
				if path==i:
					if SHS.rd[i][1]==method:
						runfunc=SHS.rd[i][0]()
						if runfunc==b'':
							con.send(b'HTTP/2.x 204 No Content\r\nServer: SHS\r\n\r\n')
							con.send(b'')
							print(headers[0],headers[2],'204 No Content')
						else:
							con.send(b'HTTP/2.x 200 OK\r\nContent-type: '+bytes(SHS.rd[i][2],encoding="utf8")+b'\r\nServer: SHS\r\n\r\n')
							con.send(runfunc)
							print(headers[0],headers[2],'200 OK')
		except Exception as e:
			runfunc=SHS.l500[0]()
			con.send(b'HTTP/2.x 500 Internal Server Error\r\nContent-type: '+SHS.l500[1].encode()+b'\r\nServer: SHS\r\n\r\n')
			con.send(runfunc)
			print(headers[0],headers[2],'500 Internal Server Error')
			def r(e):
				raise e
			from threading import Thread as TH
			TH(target=r,kwargs={'e':e}).start()
			return
from wsgiref.simple_server import WSGIRequestHandler
class SWSRequestHandler(WSGIRequestHandler):
	'''For SWS(Support WSGIServer) server. Override the "handle" method.'''
	rd={}
	l404=[lambda: b'<img src="https://http.cat/404.jpg" /><br />(Image is from http.cat)','text/html']
	l500=[lambda: b'<img src="https://http.cat/500.jpg" /><br />(Image is from http.cat)','text/html']
	def handle(SWS):
		while True:
			con=SWS.request
			headers = con.recv(1024).decode('utf-8').split('\r\n')
			cmdset=SWS.get_environ()
			if headers == ['','']:
				con.send(b'HTTP/2.x 400 Bad Request\r\nServer: SWS\r\n\r\n')
				continue
			path = cmdset['PATH_INFO'] or headers[0].replace(' HTTP/1.1','').split()[1]
			method = cmdset['REQUEST_METHOD'] or headers[0].replace(' HTTP/1.1','').split()[0]
			try:
				from json import loads
				if method == 'POST':
					SWS.formdata=loads(headers[-1])
				if '?' in path:
					llll=path.split('?')
					path=llll[0]
					SWS.formdata=cdil.__process_form_data_to_dict(llll[1])
				if not (path in SWS.rd.keys()):
					runfunc=SWS.l404[0]()
					con.send(b'HTTP/2.x 404 Not Found\r\nContent-type: '+SWS.l404[1].encode()+b'\r\nServer: SWS\r\n\r\n')
					print(headers[0],headers[2],'404 Not Found')
					con.send(runfunc)
					continue
				for i in SWS.rd.keys():
					if path==i:
						if SWS.rd[i][1]==method:
							runfunc=SWS.rd[i][0]()
							if runfunc==b'':
								con.send(b'HTTP/2.x 204 No Content\r\nServer: SWS\r\n\r\n')
								con.send(b'')
								print(headers[0],headers[2],'204 No Content')
							else:
								con.send(b'HTTP/2.x 200 OK\r\nContent-type: '+bytes(SWS.rd[i][2],encoding="utf8")+b'\r\nServer: SWS\r\n\r\n')
								con.send(runfunc)
								print(headers[0],headers[2],'200 OK')
			except Exception as e:
				runfunc=SWS.l500[0]()
				con.send(b'HTTP/2.x 500 Internal Server Error\r\nContent-type: '+SWS.l500[1].encode()+b'\r\nServer: SWS\r\n\r\n')
				con.send(runfunc)
				print(headers[0],headers[2],'500 Internal Server Error')
				def r(e):
					raise e
				from threading import Thread as TH
				TH(target=r,kwargs={'e':e}).start()
				continue
