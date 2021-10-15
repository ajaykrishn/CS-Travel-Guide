"""Module name : Project.py
   Main project framework"""


import os                 # built-in module
import time               # built-in module
import booking            # built-in module
from review_mod import *  # program module
from dtbs_mod import *    # program module

welcome()             # Welcome message

print("Please Enter your Mysql Credintials to continue:")

while True:
    try:
        con = connectdb()  # Connect to Mysql
        break
    except Exception as e:
        print("Msg:", e)      # Display encountered error
        print("Something went wrong.Please try again.\n")

time.sleep(0.5)       # Display connection status
os.system("cls")      # Clear terminal screen

while True:
    print('\n\t\tMain Menu\n\nChoose an option from the below listed : \n')
    print(' 1. Reviews of places \n 2. Your Reviews ')
    print(' 3. Hotel Bookings \n 4. Attraction of the day ')
    print(' 5. Exit ')
    q = input("\n\nYour choice (1,2,3,4) : ")

    if q == '1':
        try:
            infoplace = input("Enter the place you would like to know about : ")
            info(con, infoplace)     # Show reviews
        except Exception as e:
            print("Error code:", e)
        time.sleep(0.5)

    elif q == '2':
        while True:
            print("\n\t\tReviews\n\nEnter an option from the below listed : \n")
            print("Enter a : To write review \nEnter b : To edit a review ")
            print("Enter c : To delete a review \nEnter d : To view previous reviews ")
            print("Enter e : Exit this option")
            op4 = input("\n\nYour choice (a,b,c,d,e) : ")

            if op4.lower() == 'a':
                p = input("Enter the Place: ")
                create(con, p)

            elif op4.lower() == "b":
                edit(con)
                time.sleep(0.5)

            elif op4.lower() == "c":
                delete(con)
                time.sleep(0.5)

            elif op4.lower() == "d":
                id = int(input("Enter the reference id: "))
                show_reviews(con, id)
                time.sleep(1)

            elif op4.lower() == 'e':
                break

            else:
                print("Kindly enter a valid option")
                time.sleep(0.5)

        time.sleep(0.7)
    
    elif q == '3':
        print("\n\nEnter the website you would like to do your hotel booking in : ")
        print(" 1. Yatra\n 2. Easemytrip\n 3. Exit \n\n")

        while True:
            choice = input("Your response :")
            if choice == "1":
                booking.yatra()
                break
            elif choice == "2":
                booking.easemytrip()
                break
            elif choice == "3":
                break
            else:
                print("Sorry , please enter a valid option")
                time.sleep(0.5)

    elif q == '4':
        attrofday(con)

    elif q == '5':
        break

    else:
        print("Please enter a valid choice.")

con.close()

print("Thank you for using our service")
time.sleep(1.5)
