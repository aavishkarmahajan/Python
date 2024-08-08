# 1- given a list of numbers, write a program to find the mean of the numbers in list
nums = [1, 2, 3, 4, 5]
sum_nums = sum(nums)  # directly get sum here no need to loop through elements
# for i in nums:
#     sum_nums = sum_nums + i
count_nums = len(nums)
mean = int(sum_nums / count_nums)
print(f"Mean is: {mean}")

# 2- given a list of numbers unsorted, write a program to find the median of the numbers in list
nums = [22, 56, 3, 65, 23]
# nums = [22, 56, 3, 65, 23, 8]
nums.sort()  # 3, 22, 23, 56, 65
# nums.sort()  # 3, 8, 22, 23, 56, 65
n = len(nums)
if n % 2 == 0:
    median = int((nums[n // 2 - 1] + nums[n // 2]) / 2)
else:
    median = nums[n // 2]
print("Median is: ", median)

# 3- from a list of numbers create 2 list , one containing only the even numbers and other only the odd numbers
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_nums = []
even_nums = []
for i in nums:
    if i % 2 == 0:
        even_nums.append(i)
    else:
        odd_nums.append(i)
print("Odd list: ", odd_nums)
print("Even list: ", even_nums)

# 4- create a dictionary to store following attributes of CSK
# key "CSK" ; attributes : team full name , captain , playing 11 for each match(name of players),
# opponent name (assume there are 3 matches only against MI, RCB , GT ) and result won/loss
ipl_team = {
    "CSK": {"name": "Chennai Super Kings",
            "captain": "MSD",
            "match1": {
                "opponent": "MI",
                "playing11": ["MSD", "Ruturaj Gaikwad", "Devon Convay", "Rachin Ravindra", "Shivam Dube",
                              "Ajinkya Rahane", "Pathirana", "Ravindra Jadeja", "Daryl Mitchel", "Tushar Deshpande",
                              "Deepak Chahar"],
                "result": "won"
            },
            "match2": {
                "opponent": "RCB",
                "playing11": ["MSD", "Ruturaj Gaikwad", "Devon Convay", "Rachin Ravindra", "Shivam Dube",
                              "Ajinkya Rahane", "Pathirana", "Ravindra Jadeja", "Daryl Mitchel", "Tushar Deshpande",
                              "Shardul Thakur"],
                "result": "won"
            },
            "match3": {
                "opponent": "GT",
                "playing11": ["MSD", "Ruturaj Gaikwad", "Devon Convay", "Rachin Ravindra", "Shivam Dube",
                              "Ajinkya Rahane", "Teekshna", "Ravindra Jadeja", "Daryl Mitchel", "Mitchel Santner",
                              "Shardul Thakur"],
                "result": "lost"
            }
            }
}

# 5- in the previous dictionary add one more item for RCB. you can choose any 3 opponents.
ipl_team["RCB"] = {"name": "Royal Challengers Bangalore",
                   "captain": "Faf du Plessis",
                   "match1": {
                       "opponent": "MI",
                       "playing11": ["Faf du Plessis", "Virat Kohli", "Glen Maxwell", "Dinesh Kartik", "Cameron Green",
                                     "Rajat Patidar", "Mohammed Siraj", "Swapnil Singh", "Yash Dayal",
                                     "Lockie Ferguson", "Reece Topley"],
                       "result": "won"
                   },
                   "match2": {
                       "opponent": "CSK",
                       "playing11": ["Faf du Plessis", "Virat Kohli", "Glen Maxwell", "Dinesh Kartik", "Cameron Green",
                                     "Alzarri Joseph", "Mohammed Siraj", "Karn Sharma", "Yash Dayal",
                                     "Lockie Ferguson", "Reece Topley"],
                       "result": "lost"
                   },
                   "match3": {
                       "opponent": "GT",
                       "playing11": ["Faf du Plessis", "Virat Kohli", "Glen Maxwell", "Dinesh Kartik", "Cameron Green",
                                     "Rajat Patidar", "Mohammed Siraj", "Swapnil Singh", "Yash Dayal",
                                     "Lockie Ferguson", "Reece Topley"],
                       "result": "lost"
                   }
                   }

# 6- write a program to take a positive number as input from user.
# if the user enters negative number then keep prompting him to enter positive number until he enters the positive number and then print the same
num = int(input("Please enter a positive number"))
# if num < 0:
#     print("Entered number is not a positive number. Please enter a positive number only")
# else:
#     print("Thank you. The number you entered is: ", num)
while num <= 0:
    print("The number you've entered is not a positive number")
    num = int(input("Please enter a positive number"))
print("Thank you. The number you entered is: ", num)

# 7- consider the below list of list contains following information :
# 1. The name of a university
# 2. The total number of enrolled students
# 3. The annual tuition fees
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
# write a program to print following information :
# 1- a list of all the universities  : ['California Institute of Technology','Harvard',..so on]
# 2- total number of student enrolled in all the universities together
# 3- mean of tuition fees

# 1- a list of all the universities  : ['California Institute of Technology','Harvard',..so on]
univ_names = []
for i in range(len(universities)):
    univ_names.append(universities[i][0])
print("University names are: ", univ_names)

# 2- total number of student enrolled in all the universities together
total_students = 0
for i in range(len(universities)):
    total_students = total_students + universities[i][1]
print("Total number of students enrolled in all the universities is: ", total_students)

# 3- mean of tuition fees
sum_fees = 0
no_of_univ = len(universities)
for i in range(no_of_univ):
    sum_fees = sum_fees + universities[i][2]
print("Mean of tuition fees is: ", int(sum_fees/no_of_univ))

# 8- write a program to convert above universities list to a dictionary. the keys should be the name of the university
# { "California Institute of Technology": {"students": 2175, "fees": 37704},
#     "Harvard": {"students": 19627, "fees": 39849},
#     "Massachusetts Institute of Technology": {"students": 10566, "fees": 40732},
#     "Princeton": {"students": 7802, "fees": 37000},
#     "Rice": {"students": 5879, "fees": 35551},
#     "Stanford": {"students": 19535, "fees": 40569},
#     "Yale": {"students": 11701, "fees": 40500}
# }

univ_dict = {}
for university in universities:
    univ_dict[university[0]] = {"student_count": university[1], "fees": university[2]}
print(univ_dict)

# 9-  write a program that reverses a given string. For example, if the input is "Hello" from user, the output should be "olleH"
# solution 1
ip_str = input("Please enter a string: ")
rev_ip_str = ""
for ch in ip_str:
    rev_ip_str = ch + rev_ip_str
print("Reverse string is: ", rev_ip_str)

# solution 2
ip_str = input("Please enter a string: ")
print("Reverse string is: ", ip_str[::-1])

# 10- write a program that finds the largest number in a list(unsorted) of integers without using sort/sorted method.
# num_list = [2, 5, 1, 3, 65, 22]
nums = input("Please enter comma separated numbers")
num_list = nums.split(",")
largest_num = int(num_list[0])
for i in num_list:
    if int(i) > largest_num:
        largest_num = int(i)
print("Largest number is: ", largest_num)
