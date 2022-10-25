import time # Just Curious if the Thonny IDE has a time module

SuperUser = ["Admin", ]
User = ["King", "Bob"]
NewUser = []

Yes = ["Yes", "Yeah", "Yea", "Sure", "Yup", "Yuppers", "Ok", "Okay", "Maybe", "Totally", "I do", "Y", " Yes", " Yeah",
           " Yea", " Sure", " Yuppers", " Ok", " Okay", " Maybe", " Totally", " I do", " Y", "yes", "yeah", "yea",
           "sure", "yup", "yuppers", "ok", "okay", "maybe", "totally", "i do", "y", " yes", " yeah", " yea", " sure",
           " yup", " yuppers", " ok", " okay", " maybe", " totally", " i do", " y", "I'm ready", "i'm ready", " I'm ready",
           " i'm ready"] # Word Bank

print("1. Add a new user\n" +
"2. Modify an existing user\n" +
"3. Change a user's role \n" +
"4. Delete a user's role \n" +
"5. Delete a user \n" +
"6. Exit the system \n" +
"7. Display Users \n")

def MenuFun():
    Menu = str(input("Please choose an option: ")) # Default for Menu
    if Menu == "1": # Option 1
        NewUser = input("Please enter a new user name: ")
        User.append(NewUser)
        print(User[-1])
        MenuFun()
    elif Menu == "2": #Option 2
        print(User)
        NewUser = str(input("Who do you want to change: "))
        if NewUser in User:
            ChangeUser = input("Your old name is " + NewUser + " Please enter a new user name: ")
            User.remove(NewUser)
            User.append(ChangeUser)
            print(User)
            MenuFun()
        else:
            MenuFun()
    elif Menu == "3": # Option 3
        print("This is a list of our Users - " + str(User))
        print("This is a list of our Super Users - " + str(SuperUser))
        NewUser = input("Who would you like to change: ")
        if NewUser in SuperUser:
                print("Sorry that person is already a Super User! \n")
                MenuFun()
        elif NewUser in User: 
            ChangeUser = input("Would you like to make that person a super user: ")
            if ChangeUser in Yes:
                SuperUser.append(NewUser)
                print("Ok done! \n")
                MenuFun()
            else:
                MenuFun()
            print("Done \n")
            MenuFun()
        else:
            print("Sorry that is not an option! \n")
            MenuFun()
    elif Menu == "4": # Option 4
        print(SuperUser)
        NewUser = input("Please choose whose Super role you wish to delete: ")
        if NewUser in SuperUser:
            SuperUser.remove(NewUser)
            print(NewUser + " is now a regular user. To make further changes you must delete their account.")
            print(SuperUser)
            MenuFun()
        else:
            print("Sorry that is not an option \n")
            MenuFun()
    elif Menu == "5": # Option 5
        print(User)
        NewUser = input("Whom would you like to delete: ")
        if NewUser in User:
            User.remove(NewUser)
            print("Account has been deleted \n")
            print(User)
            MenuFun()
    elif Menu == "6": # Option 6
        print("See you next time! \n")
        time.sleep(1)
        exit()
    elif Menu == "7": # Option 7
        print(User)
        print(SuperUser)
        MenuFun()
    else:
        MenuFun()
MenuFun()
