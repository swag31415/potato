from lark import Lark

with open('grammar.lark', 'r') as f:
  potato = Lark(f.read(), start='file_input')

tree = potato.parse('''def fun(x): x + sin(x)
''')
print(tree)
print(tree.pretty())