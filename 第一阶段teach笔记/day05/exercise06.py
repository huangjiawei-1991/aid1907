list01 = [3,45,8,12,36,7,3]
#         0  1 2 3  4  5 6
#把list01中大于10的数字存入另一个列表
# result_list = []
# for item in list01:
#     if item > 10:
#         result_list.append(item)
# print(result_list)

#获取list01中最大的数 不使用max()
#假设最大值为列表的第一个数
max_value = list01[0]
# #循环取出列表剩余的全部数据和最大值比较
# for item in list01[1:]:
# #如果当前项比最大值大 将最大值赋值为当前项
#     if item > max_value:
#         max_value = item
# for i in range(1,len(list01)):
#     if list01[i] > max_value:
#         max_value = list01[i]
# #循环结束后 打印最大值
# print(max_value)

#删除列表list01中所有的奇数
# for item in list01:
#     if item % 2:
#         list01.remove(item)
# print(list01)

#倒序删除 #17：12~17:25

for i in range(len(list01)-1,-1,-1):
    if list01[i] % 2:
        print(list01[i])
        # list01.remove(list01[i])
        del list01[i]
print(list01)









