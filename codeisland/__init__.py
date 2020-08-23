'''
range()函数返回的是range类型，而不是list。
'''
from .main import CodeIsland,print
from .supportservers import SSSRequestHandler
from .supportservers import SHSRequestHandler
from .supportservers import SWSRequestHandler
from .orm import Model
import builtins
builtins.CodeIsland=CodeIsland
