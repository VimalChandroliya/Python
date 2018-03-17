# #Mutable no duplicate
# mySet = {1,2,2,3,3,4,5,6,7}
# print(mySet)
#
# mySet1 = {1,2,'c'}
# mySet2 = {1,'b','c'}
#
# #Union
# print(mySet1 | mySet2)
#
# #intersection
# print(mySet1 & mySet2)
#
# #difference
# print(mySet1-mySet2)
# print(mySet2-mySet1)


fileset = {2015,2017,2019}
filelist = [2015,2017,2017]
print(filelist)
print(type(filelist))

filelist = set(filelist) #Set
print(filelist)
print(type(filelist))

filelist = list(filelist) #List
print(filelist)
print(type(filelist))


