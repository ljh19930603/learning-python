li = ["a","b","mpilgrim","z","example"]
print(li)
print(li[1])#第二个元素
print(li[-1])#倒数第一个元素
print(li[-3])#倒数第三个元素
print(li[1:3])#第二个元素到第三个元素.区间是左闭右开
print(li[1:-1])
print(li[0:3])
li.append("new")#在末尾添加new元素
print(li)
li.insert(2,"new")#在第二个元素之后添加new元素
print(li)
li.extend(["two","elements"])#将list拼接在一起
print(li)
print(li.index("example"))#example的位置
li.remove("z")#删除z元素
print(li)
li.remove("new")#删除首次出现的一个值
print(li)
print(li.pop())#删除list的最后一个元素,然后返回删除元素的值
print(li)