# 1- write a program which takes 2 inputs from the user : weight(kg) and height(meter) and prints the BMI in the output.
BMI = weight / (square of height)
weight = int(input("Please enter weight in kg: "))
height = int(input("Please enter height in meter: "))
bmi = weight/(height**2)
print(f"BMI = {bmi}")
print("BMI = " + str(bmi))
print("BMI =", bmi)

# 2- write a program which takes the name of the user as input and replace all the occurence of character 'a' in the name to 'b' and print it.
name = input("Please enter name: ")
newname = name.replace("a", "b")
print(newname)

#3- write a program which takes 2 inputs from user as principal amount (int) and rate of annual interest (float)
# and print the expected total amount  after  2 years.
amt = int(input("Please enter principal amount: "))
interest = float(input("Please enter rate of interest: "))
print("Expected total amount after 2 years is: ", amt + (amt*2*interest)/100)

#4- write a program which takes city name from user input. irrespective of in which case user enters the city name,
# print the city name in camel case meaning first letter should be capital and rest in small.
city = input("Please enter city name: ")
print(city.title())

#5- write a program which takes the name of the user as input and print the index of character 'a' in the string.
# if 'a' is not there then return -1.
name = input("Please enter name: ")
print(name.rfind("a"))
print(name.find("a"))

#6-  Display the number of letters in the below string
my_word = "antidisestablishmentarianism"
print(len("antidisestablishmentarianism"))

#7- take 3 inputs from user : first name , last name and age . Display the information in below format
# example
# Display : my name is Mohit Sharma and I am 32 years old.
# note that first letter of first name and last name both should be in capital letters and rest in small.
first_name = input("Please enter first name: ")
last_name = input("Please enter last name: ")
age = input("Please enter age: ")
print(f"My name is {first_name.capitalize()} {last_name.capitalize()} and I am {age} years old.")

# 8-take 3 inputs from user : first name , last name and company name. create the email alias for the user and display it.
# Email alias is first 2 letters of first name , last 3 letters of last name and @company.com
# example
# Display : morma@infosys.com
# note full email id should -be in lower case
first_name = input("Please enter first name: ")
last_name = input("Please enter last name: ")
comp_name = input("Please enter company name: ")
org = ".com"
email_alias = first_name[:2] + last_name[-3:] + "@" + comp_name + org
print(email_alias.lower())

