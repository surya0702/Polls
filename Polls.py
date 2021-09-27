counter={} # A Dictonary to store the values of options given by the user
options=[] # Options for the poll given by the User
userCount=0 # No of users who answered the Poll
question=""

def ResultPrinter(): # Prints the Poll options and the percentage of times they were selected
    print('\n\n'+question)
    print('The Results of the Poll is :')
    for option in options:
        percentage=(counter[option]/userCount)*100 if option in counter else 0
        percentage="{:.2f}".format(percentage)
        print(option+'\t\t'+str(percentage)+"%")

# Intro Message
print("Hello there! Welcome to Polls.")
print("Please select the mode of Poll")
pollModes=['1) Yes/No Poll','2) Normal Poll','3) Quiz Mode'] # Poll Modes available
print(",".join(pollModes))
while 1: # Iterating untill the user inputs an available mode number
    try:
        mode=int(input("Enter the Poll Number you want to chose : ")) # Poll Mode selected by the user
        if mode in [1,2,3]:
            break
        else:
            raise Exception
    except:
        print("Please enter a valid Input") # For invalid Poll mode selected by user 
question=input("Enter the Poll Question : ") # Question for the poll
if mode!=1:
    print("Enter the options with a space in between them") # Options for the Poll question
    while 1: # Iterating untill the user input options for the Poll
        try:
            options=input().split() 
            if len(options)<2: # Raising an exception if options given by the user are less than 2
                raise Exception
            break
        except:
            print("Please enter the options with a space in between them")
    while mode!=2: # Prompting the user to enter a Correct_Option in case of Quiz Mode Poll
        try:
            correctOption=input("Enter the correct option : ")
            if correctOption not in options: # If Correct_Option is not present in the available options given by the user.
                raise Exception
            break
        except: # If the user inputs anything wrong.
            print("Please enter a Correct option which is available in Options")
else:
    options=['Yes','No'] # Rewriting the options list if the mode selected is Yes/No Mode.

#Users Part
print("\n\n")
print(question) # Question of the Poll
for i in range(len(options)): # Options for the Question based on the Poll Mode
    print("("+str(i+1)+")"+options[i])

while 1: # Interating untill the user either prompts to leave the poll or if he selected the correct option in case of Quiz Mode.
    try:
        userInput=int(input("Select the number corresponding to your answer : ")) # Users input for the Poll question
        uInput=options[userInput-1]
        userCount+=1 # Increasing the user count for every Loop
        if uInput in counter: # Incrementing the value of the options which are choosen by the users.
            counter[uInput]+=1
        else:
            counter[uInput]=1
        if mode==3 : # In case of Quiz Mode we check the users input with the Correct_Option available
            if uInput==correctOption: # If both are same, prints the Congratulations message.
                print("Congratulations! Your answer is correct.")
                break
            else: # Otherwise prints the Wrong_answer message
                print("Wrong Answer!")
    except: # If the users inputs any wrong input
        print("Please select an option which is available!")

    try: # Asking the user if he would like to continue the poll or not.
        print("Would you like to continue? : Yes/No")
        exiter=input()
        if (exiter).lower()=="no": # If the user wants to Quit from the poll, Prints the Results of the poll.
            ResultPrinter()
            break
    except:
        continue
