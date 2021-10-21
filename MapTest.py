favorit_map = {
    'wy':'123',
    'er':'we',
    'asd':'wy',
    'asd1':'wy',
    'name':'wby6225104'
    }
getValue=favorit_map.get("wy1")
if getValue != None :
    print('getValue :  ' + getValue)
else:
    print('getValue :  '+'123')

#del favorit_map['er']
print(f"Wwwwww {favorit_map}")

for key,value in favorit_map.items():
    print(f"\nkey :{key}")
    print(f"\nvalue : {value}")

print("----------------")

for value in favorit_map.values():
    #print(f"\nkey :{key}")
    print(f"\nvalue : {value}")

print("----------------")

for key in favorit_map:
    print(f"\nkey :{key}")

print("----------------")

freend=['wy','wby','er','asd','asd1','name1']
for name in sorted(favorit_map):
    print(f" hello , {name}")
    if name in freend:
        print(f" you are my frend {name.title()},you like{favorit_map.get(name)}")

print("----------------")
#去除重复
for value in sorted(set(favorit_map.values())):
    print(f" values is {value}")

print("----------------")
while True:
    message = input("输入数字")
    print(message)
    if message == '22':
        quit() 
