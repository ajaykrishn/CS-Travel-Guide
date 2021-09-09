import time,os               #built-in modules
from review_mod import *             #program module
import booking
from dtbs_mod import *        #program module
try:
    import wikipedia                 # by pip install wikipedia
except:
    inst_wiki()                 #option to install module
    import wikipedia

welcome()
print("Please Enter your Mysql Credintials to continue:")

while True:
    try:
        con=connectdb()
        break
    except Exception as e:
        print(e)
        print("Something went wrong.Please try again.\n")
os.system("cls")

while True:
    print('\n\t\tMain Menu\n\nChoose an option from the below listed : \n\n 1. Information of place \n 2. Hotel bookings \n 3. Reviews \n 4. Exit ')
    q=input("\n\nYour choice (1,2,3,4) : ")

    if q=='1':
        try:
            infoplace=input("Enter the place you would like to know about : ")#view reviews
            result=wikipedia.summary(infoplace, sentences=5)
            print(result)
            p_wiki=result.split()[0]
            status(con,infoplace,p_wiki)
            print("\nReviews:")
            show_reviews_info(con,infoplace,p_wiki)
            ch=input("Do you want to add review?(y/n): ")
            if ch.lower()=="y":
                create(con,infoplace)
            print()
        except Exception as e:
            print("Error code:",e)
        time.sleep(0.5)

    elif q=='2':
        print("\n\nEnter the website you would like to do your hotel booking in : \n 1. Yatra\n 2. Easemytrip\n 3. Exit \n\n")
        while True:
            choice=input("Your response :")
            if choice=="1":
                booking.yatra()
                break
            elif choice=="2":
                booking.easemytrip()
                break
            elif choice=="3":
                break
            else:
                print("Sorry , please enter a valid option")
                time.sleep(0.5)


    elif q=='3':
        while True:
            print("\n\nEnter a : To write review \nEnter b : To edit a review \nEnter c : To delete a review \nEnter d : To view previous reviews \nEnter e : Exit this option")
            op4=input("\n\nYour choice (a,b,c,d,e) : ")
            if op4.lower()=='a':
                p=input("Enter the Place: ")
                create(con,p)
                op3=0
            elif op4.lower()=="b":
                edit(con)
                op3=0
            elif op4.lower()=="c":
                delete(con)
                op3=0
            elif op4.lower()=="d":
                id=int(input("Enter the reference id"))
                show_reviews(con,id)
                time.sleep(1)
                op3=0
            elif op4.lower()=='e':
                break
            else:
                print("Kindly enter a valid option")
                time.sleep(0.5)
        time.sleep(0.7)
    elif q=='4':
        break

    else:
        print("Please enter a valid choice.")

con.close()

print("Thank you for using our service")
time.sleep(1.5)
