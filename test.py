from lark import Lark
from lark.indenter import Indenter

class PotatoIndenter(Indenter):
  NL_type = '_LINE'
  OPEN_PAREN_types = []
  CLOSE_PAREN_types = []
  INDENT_type = '_INDENT'
  DEDENT_type = '_DEDENT'
  tab_len = 8

with open('grammar.lark', 'r') as f:
  potato = Lark(f.read(), start='code', postlex=PotatoIndenter())

tree = potato.parse("""

f = (x):
  2*x^2 - 5*x - 1
for v in [12,3,4,4,5,1]:
  if v > 12: print(10)
  elif v < 5: print(19)
  elif False: print(None)
  else: print(True)

""")
print(tree)
print(tree.pretty())