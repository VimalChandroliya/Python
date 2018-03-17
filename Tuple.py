#String Tuples immutable
str1 = "Vimal"
str2 = "Chandroliya"

#concatination
print(str1+str2)

#Repetition
print(str1*2)

#Slicing
print(str2[3:6])
print(str2.count('a',0,13))
print(str2.find('nd'))
print(str2.isalpha())

#Tuples
tup = ('abc','def','fgh')
print('Length :',tup.__len__())

#concatination
print(tup+('abcd','bcde'))

#Repetition
print(tup*2)

#slicing Indexing
print(tup[1:4])
print(tup[2])
