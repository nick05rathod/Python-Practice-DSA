# lst=[1,2,3]
# lst.append([4,5])
# flat_list=[]
# for i in lst:
#     print(i)
#     for item in i:
#         flat_list.append(item)

# print(flat_list)


# new_list=[10,20,30,40,50]
# reversed_list=new_list[::-1]
# print(reversed_list)


number=[1, 2, 3, 1, 2, 4, 5, 6, 5]
duplicate_item=list(set([i for i in number if number.count(i)>1]))
print(duplicate_item)
        