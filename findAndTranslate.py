import re
f = open('testing', 'r')
data = f.read()

x = re.findall(r'interface(.*?)\,',data,re.DOTALL)
print(x)