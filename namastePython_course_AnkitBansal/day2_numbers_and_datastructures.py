# 1- write a program which takes single input from user contaning first name,last name and age as comma separated value
# and display then in 3 lines in given format below.
# example user input : Ankit,Bansal,35
# output:
# First name is Ankit
# last name is Bansal
# Ankit is 35 years old

user_input = input("Please enter first name, last name and age as comma separated values: ")
user_input_list = user_input.split(",")
print("First name is " + user_input_list[0])
print("last name is " + user_input_list[1])
print(user_input_list[0] + " " + "is" + user_input_list[2] + " " + "years old")

# 2- given 2 list as list1= [1,3,4] and list2 = [2,4,6]
# combine the 2 list and display the same without using extend method

list1 = [1, 3, 4]
list2 = [2, 4, 6]
# list3 = [list1[0], list2[0], list1[1], list2[1], list1[2], list2[2]]
# print(list3)
print(list1 + list2)

# 3- given a list list1=[1,2,3,4,5,6,7,8]
# display a new list which contains only odd position index values from above list.

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
# newList = [list1[1], list1[3], list1[5], list1[7]]
newList = list1[1::2]
print(newList)

# 4- take a ipl team name as input from user and display a list of all elements from that name.

ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']
team = input("Please enter a team name: ")
print(ipl[ipl.index(team):])

# 5- ipl= ['CSK','MI','KKR','LSG','PBKS']
# take a ipl team name as input from user and display a list of all elements except input one
ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']
input_team = input("Please enter team name: ")
ipl.pop(ipl.index(input_team))
print(ipl)

# 6- ipl= ['CSK','MI','KKR','LSG','PBKS']
# take a user input contains 2 comma separated values index,new_team . replace the index element of list with new value and display the same
ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']
newTeamInput = input("Please enter index and new team name as comma separated values: ")
newTeamValues = newTeamInput.split(",")
newTeamIdx = int(newTeamValues[0])
newTeamName = newTeamValues[1]
ipl[newTeamIdx] = newTeamName
print(ipl)

# 7- ipl= ['CSK','MI','KKR','LSG','PBKS']
# take ipl team name as user input. display True if the team exists else display False.
ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']
teamName = input("Please enter team name to check if exists: ")
check = teamName in ipl
print(check)

# 8-ipl= ['CSK','MI','KKR','LSG','PBKS']
# take a user input contains 2 comma separated values index,new_team . Add the new value at that index in the list.
# Display the old list , new list,length of original and new list
# example : input : 2,SRH
# output :
# old list : ['CSK','MI','KKR','LSG','PBKS'] and length 5
# new list : ['CSK','MI','SRH','KKR',LSG','PBKS'] and length 6
ipl = ['CSK', 'MI', 'KKR', 'LSG', 'PBKS']
user_input = input("Please enter index and new team name as comma separated values: ")
user_input_list = user_input.split(",")
newIdx = int(user_input_list[0])
newVal = user_input_list[1]
print("old list: ", ipl)
print("and length: ", len(ipl))
ipl.insert(newIdx, newVal)
print("new list: ", ipl)
print("and length: ", len(ipl))
