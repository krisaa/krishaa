#concatenate l1 and l2
#add l1 in l2
#l3 add programing language
#remove unwanted data from L1

L1 =[1,"red", 2,3]
L2 =["apple","orange",]
L3 =["php","python","java"]
L4=L1+L2
print(L4)
L2.extend(L1)
print(L2)
L1.remove("red")
print(L1)
L3.append("C++")
print(L3)
print(L1.pop())
print(L1)
for fruit in L2:
    print(fruit)


