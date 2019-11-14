#create a dict ,add datas like ,roll_no ,name , marks,along with gender,now i want to print all the name and marks whose gender is male,how would you do that ?
dict={'roll':[1,2,3,4],'name':["ram","sita","krisha","malle"],'marks':[20,30,40,50],'gender':['male','female','female','female']}
for i in range (len(dict['roll'])):
    if dict['gender'][i]=='male':
     print(dict['marks'][i])
     print(dict['name'][i])


