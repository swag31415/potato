from lark import Lark

with open('grammar.lark', 'r') as f:
  potato = Lark(f.read(), start='code')

tree = potato.parse('with open("grammar.lark", "r") as f')
print(tree)
print(tree.pretty())