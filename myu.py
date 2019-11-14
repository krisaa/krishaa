#this is test message for git purpose


dict={'rollno':[1,2,3,4], 'name':['subash','aakash','susma']}
roll=dict['rollno']
nam=dict['name']
data=input('enter your rollno')
for i in range (len(roll)):
    if roll[i]==data:
        temp=i

        print(nam[temp])