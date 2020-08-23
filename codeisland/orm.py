from copy import deepcopy as dc
from sqlite3 import Connection
#from .main import print
def to_connect(connection:Connection):
	"""Help this module to connect a 'sqlite3.Connection' object."""
	global _conn
	_conn = connection
	global _curs
	_curs = _conn.cursor()
class Model(object):
	r"""
	Model base class.
	Example:
	>>> class mymodel(Model):
	... 	nullfield = type(None)
	... 	integerfield = int
	... 	realfield = float
	... 	textfield = str
	... 	blobfield = bytes
	... 	#notnulltext = (str,'notnull') Not realized
	... 	#uniquetext = (str,'unique') Not realized
	... 	#primarykeytext = (str,'primary_key') Not realized
	... 	#foreignkeytext = (str,'foreign_key-another_model_name-key_name') Not realized
	... 	#defaulttext = (str,{'default':'default value'}) Not realized
	"""
	def __init__(self,**args):
		global _curs
		global _conn
		fields = self.__get_fields()
		self.__tablename__ = str(self.__class__).replace("<class '",'').replace("'>",'').split('.')[-1]
		for i in fields:
			if type(eval('self.'+i)) == type:
				assert type(args[i]) == eval('self.'+i),'TypeError'
			else:
				assert type(args[i]) == eval('self.'+i)[0],'TypeError'
		value=''
		for i in fields:
			if type(args[i])==str:
				value=value+args[i].__repr__()+','
			elif type(args[i])==bytes:
				value=value+args[i].decode().__repr__()+','
				continue
			else:
				value=value+args[i].__repr__()+','
		insert = 'INSERT INTO '+self.__tablename__+' VALUES({});'.format(value)
		iill=list(insert)
		iill[-3]=''
		insert=''
		for i in iill:
			insert=insert+i
		try:
			_curs.execute(insert)
			_conn.commit()
		except:
			print("Insert data into model '"+self.__tablename__+"' failed.Rolling back...")
			_conn.rollback()
			raise
	@classmethod
	def __get_fields(self):
		r"""
		Pick fields.
		Example:
		>>> class mym(Model):
		... 	a=int
		... 	b=(int,'primary_key')
		... 	c=[int,'unique']
		... 	def d(self):
		... 		pass
		... 
		>>> mym._get_fields()
		['a','b','c']
		"""
		dir_object_ = dir(object)
		dir_Model_ = dir(Model)
		_fields = dir(self)
		for i in dir_object_:
			if i in _fields:
				_fields.remove(i)
		for i in dir_Model_:
			if i in _fields:
				_fields.remove(i)
		fields = dc(_fields)
		for i in _fields:
			if type(eval('self.'+i)) != type and type(eval('self.'+i)) != tuple and type(eval('self.'+i)) != list:
				fields.remove(i)
		print(fields)
		return fields
	@classmethod
	def select(cls,select=''):
		r"""Function for SELECT.
			example:
			>>> a=mymodel(None,1,0.1,'',b'','notnull','unique','primarykey')
			>>> mymodel.select('*')
			((None,1,0.1,'',b'','notnull','unique','primarykey',),)
			>>> #a=mymodel(None,1,0.1,'lalala',b'','notnull','unique','primarykey')
			>>> #mymodel.select('floatfield,textfield',where='textfield lalala equal') Not realized
		"""
		global _curs
		global _conn
		__tablename__ = str(cls).replace("<class '",'').replace("'>",'').split('.')[-1]
		slc='SELECT '+select+' FROM '+__tablename__+';'
		try:
			_curs.execute(slc)
			_conn.commit()
			return _curs.fetchall()
		except:
			print("Search data in model '"+__tablename__+"' failed.Rolling back...")
			_conn.rollback()
			raise
	@classmethod
	def create(cls):
		r"""Create the table."""
		fs=cls.__get_fields()
		fd={}
		for i in fs:
			fd[i]=eval('cls.'+i)
		for i,j in fd.items():
			if j == int:
				fd[i]='INTEGER'
			elif j == float:
				fd[i]='REAL'
			elif j == str:
				fd[i]='TEXT'
			elif j == bytes:
				fd[i]='BLOB'
		__tablename__ = str(cls).replace("<class '",'').replace("'>",'').split('.')[-1]
		crtast='CREATE TABLE '+__tablename__+'({});'
		for i,j in fd.items():
			crtast=crtast.format(i+' '+j+',{}')
		crtast=crtast.replace(',{}','')
		_curs.execute(crtast)
		_conn.commit()
if __name__ == '__main__':
	from _sqlite3 import connect
	db = connect('sqlite3.db')
	to_connect(db)
	class MyModel(Model):
		blob=bytes
		integer=int
		real=float
		text=str
	#MyModel(text='',integer=1,real=0.1,blob=b'')
	print(MyModel.select('real'))
