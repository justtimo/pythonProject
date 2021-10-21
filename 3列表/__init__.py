list=['宝马','奔驰','法拉利','路虎']
#访问列表
print(f"\n-------------")
print(list[0].title())
#修改
print(f"\n-------------")
list[0]='夏利'
print(list[0])
#添加
print(f"\n-------------")
list.append('特斯拉')
print(list)
#插入
print(f"\n-------------")
list.insert(0,'别经现代')
print(list)
#删除  del无返回值  pop有返回值
print(f"\n-------------")
del list[0]
print(list)
last=list.pop()
print(last)
print(list)
first=list.pop(0)
print(first)
print(list)

list.remove('奔驰')
print(list)
#排序
print(f"\n-------------")
list.append('本田')
list.append('世界')
list.append('雪佛兰')
print(f"排序前{list}")
list.sort()
print(f"sort永久排序后 {list}")
print(f"\n-------------")
list.reverse()
print(f"排序前{list}")
print(f"sorted临时排序后list的值:{sorted(list)}")
print(f"sorted临时排序后原本list的值{list}")
#长度
print(f"\n-------------")
print(f"长度{len(list)}")