

#concatinate multiple dictionaries
dict1={'no1':10, 'no2':20}
dict2={'no3':10, 'no4':20}
dict4 ={}
for d in (dict1,dict2):dict4.update(d)
print(dict4)