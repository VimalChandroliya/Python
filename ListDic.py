# #mutable List Dictonary Sets
#
# list = [1,'a',2.5]
# print(list)
#
# list.append('vimal')
# print(list)
#
# list.extend([5,'c'])
# print(list)
#
# list.insert(2,'b')
# print(list)
#
# list.pop()
# print(list)
#
# #Dictonary key value pair
# myDict={} #empty
# myDict={1:'apple' , 2:'ball'}
# print(myDict)
# myDict.update({4:'abc'})
# print(myDict)
#
# myDict1={'name':'vimal',2:'ball'}
# print(myDict1)
#
# myDict2={1:'apple',2:[1,2,'vimal']}
# print(myDict2)
#
myDict3 = dict([(1,'apple'),(2,'ball')])
print(myDict3)
print(myDict3[1])
print(len(myDict3))
print(myDict3.keys())
print(myDict3.values())

myDict3.clear()
print('Clear' ,myDict3)


filelist = list(range(2000,2020,2))
print(filelist)