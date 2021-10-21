lists=['宝马','奔驰','法拉利','路虎','特斯拉','别经现代','本田','雪佛兰']
for car in lists:
    print(car)

print(f"\n-------使用range()1")
for value in range(1,5):
    print(value)

print(f"\n-------使用range()2")
numebrs=list(range(1,5))
squs=[]
for number in numebrs:
    suq=number ** 2
    squs.append(suq)
print(squs)

print(f"\n-------简单统计")
numebrs1=list(range(0,10))
print(max(numebrs1))
print(min(numebrs1))
print(sum(numebrs1))

print(f"\n-------切片: 使用部分列表")
#索引0-2
print(f"索引0-2:{numebrs1[0:3]}")
#索引0-4
print(f"索引0-4:{numebrs1[:4]}")
#列表中最后4个
print(f"列表中最后4个:{numebrs1[-4:]}")
#包含整个列表 : 用于复制
numbers2=numebrs1[:]
print(f"numbers1:{numebrs1}")
print(f"numbers2:{numbers2}")
#便利切片
for value in numebrs1[-4:]:
    print(value)

print(f"\n-------元祖:不可变列表 只含有一个元素的元祖必须包含逗号 name=('wby' , ) ")
names=('wby','wby1',"wby2","wby3")
print(f"names:{names}")
#names[0]='wangwei'     #将会报错
#修改元祖 : 重新给元祖赋值
names=('ww','ww1','ww2')
print(f"赋值后的names:{names}")