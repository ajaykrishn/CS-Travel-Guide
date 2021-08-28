import webbrowser               #built-in module
import wikipedia                 #install by : pip install wikipedia
from PIL import Image           #install by : pip install Pillow
from review_mod import *             #program module
import mysql.connector as mysql  #install by : pip install mysql-connector-python
import time                   #built-in module


welcome()


con_check=1
while con_check:
    try:
        usr=input("Enter Username: ")
        psw=input("Enter Password: ")
        con=mysql.connect(host='localhost',user=usr,passwd=psw)
        curs=con.cursor()
        create_dbase(curs)
        print("\n\t\tWELCOME!")
        con_check=0
    except Exception as e:
        print(e)
        print("Please try again.\n")

op2=1

while op2:
    print('\nChoose an option from the below listed : \n\n 1. Information of a place \n 2. Hotel Bookings \n 3. Reviews \n 4. Exit. ')
    q=int(input("\n\nYour choice (1,2,3,4) : "))

    if q==1:
        try:
            infoplace=input("Enter the place you would like to know about : ")
            result=wikipedia.summary(infoplace, sentences=5)
            print(result)
            p_wiki=result.split()[0]
            print("\nReviews:")
            show_reviews(con,infoplace,p_wiki)
            ch=input("Do you want to add review?(y/n): ")
            if ch.lower()=="y":
                create(con,infoplace)
            print()
        except:
            print("Place is not available in our database.Please check spelling or other mistakes.")
        time.sleep(2)

    elif q==2:
        print('\n\nService is currently only supporting hotels in Kerala \nYou will be redirected to an external website')
        print("Please enter information asked below :")
        place=input("\nEnter Destination : ")
        adults=int(input("Enter total number of Adults : "))
        children=int(input("enter total number of children : "))
        x=("https://www.yatra.com/pwa/hotels/srp?roomRequests[0].id=1&roomRequests[0].noOfAdults={}&roomRequests[0].noOfChildren={}&source=BOOKING_ENGINE&pg=1&tenant=B2C&isPersnldSrp=1&city.name={}&city.code={}&state.name=KER&state.code=KER&country.name=India&country.code=IND".format(adults,children,place,place))
        webbrowser.open(x, new=1)
        time.sleep(2)

    elif q==3:
        op3=1
        while op3:
            print("\n\nEnter a : To write a review \nEnter b : To edit a review \nEnter c : To delete a review \nEnter d : Exit From this option.")
            op4=input("\n\nYour choice (a,b,c,d) : ")
            if op4=='a':
                p=input("Enter the Place: ")
                create(con,p)
            elif op4=="b":
                edit(con)
            elif op4=="c":
                delete(con)
            elif op4=="d":
                op3=0

            else:
                print("Kindly enter a valid option")
            time.sleep(1)
        time.sleep(2)
    elif q==4:
        op2=0

    else:
        print("Please enter a valid choice.")

curs.close()
con.close()

print("Thank you for using our Service.")
time.sleep(3)
