# 1- create a txt file and put 4-5 lines. Now create another file from the previous file and at the end of each line put the count of words.
lines = ["My first file handling code", "Its a lovely day today", "Good morning", "This is my fourth line", "Bye Bye"]
with open("file1.txt", "w") as f1:
    for line in lines:
        f1.write(line + "\n")

with open("file1.txt", "r") as f1, open("file2.txt", "w") as f2:
    for line in f1:
        line = line.strip()
        word_cnt = str(len(line.split()))
        f2.write(line + " " + word_cnt + "\n")

# 2- given below dictionaries of states and their capital:

# pick a state from below dictionary and ask user to enter the capital of the state.If the user answers incorrectly, then repeatedly ask them
# for the capital until they either enter the correct answer or type "exit".
# If the user answers correctly, then display "Correct" and end the program. However, if the user exits without guessing correctly, display
# the correct answer and the word "Goodbye".
capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}
while True:
    state = input("Please enter name of a state in USA: ")
    state = state.title()
    if state in capitals_dict:
        cap = input(f"Please enter the capital of {state}: ")
        cap = cap.title()
        if cap == capitals_dict[state]:
            print("Congratulations!!! That's the right answer")
            break
        elif cap.lower() == "exit":
            print("The correct answer was: " + capitals_dict[state] + "." + " " + "Goodbye...")
            break
        else:
            print("Sorry your answer is incorrect. Please try again or enter 'exit' to quit")
    else:
        print("Sorry you have entered an invalid state in USA. Please try again or enter 'exit' to quit")


# 3- write a program to take state as input from user and print the capital of the state using above dictionary.
# If the state is not there in dictionary then print "sorry , information not available"
capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}
state = input("Please enter name of any state in US: ")
state = state.title()
if state in capitals_dict:
    print(f"The capital of the state {state} is: {capitals_dict[state]}")
else:
    print("Sorry information is not available")
