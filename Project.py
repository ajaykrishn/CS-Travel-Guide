import webbrowser               #built-in module
import wikipedia                 #install by : pip install wikipedia
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
        print("\nMySQL connection established ✅")
        con_check=0
    except Exception as e:
        print(e)
        print("Please try again.\n")

op2=1

while op2:
    print('\n\t\tMain Menu\n\nChoose an option from the below listed : \n\n 1. Information of place \n 2. Hotel bookings \n 3. Reviews \n 4. Exit ')
    q=int(input("\n\nYour choice (1,2,3,4) : "))

    if q==1:
        try:
            infoplace=input("Enter the place you would like to know about : ")
            result=wikipedia.summary(infoplace, sentences=5)
            print(result)
            p_wiki=result.split()[0]
            status(con,infoplace,p_wiki)
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
        bk=1
        print("\n\nEnter the website you would like to do your hotel booking in : \n 1. Yatra\n 2. Easemytrip\n 3. Exit \n\n")
        while bk:
            choice=input("Your response :")
            if choice=="1":
                place=input("\nEnter Destination : ")
                adults=int(input("Enter total number of Adults : "))
                children=int(input("Enter total number of children : "))
                yatra=("https://www.yatra.com/pwa/hotels/srp?roomRequests[0].id=1&roomRequests[0].noOfAdults={}&roomRequests[0].noOfChildren={}&source=BOOKING_ENGINE&pg=1&tenant=B2C&isPersnldSrp=1&city.name={}&city.code={}&state.name=KER&state.code=KER&country.name=India&country.code=IND".format(adults,children,place,place))
                print("You are being redirected")
                webbrowser.open(yatra, new=1)
                bk=0
            elif choice=="2":
                destination=input("Enter your Destination : ")
                checkin=input("Enter Check-in date in format DD/MM/YYYY : ")
                checkout=input("Enter Check-out date in format DD/MM/YYYY : ")
                pax=input("Enter number of adults : ")
                rooms=input("Enter number of rooms required : ")
                easemytrip=("https://hotels.easemytrip.com/newhotel/Hotel/HotelListing?e=202193214436&city={},%20India&cin={}&cOut={}&Hotel=NA&Rooms={}&pax={}".format(destination,checkin,checkout,rooms,pax))
                print("You are being redirected")
                webbrowser.open(easemytrip,new=1)
                bk=0
            elif choice=="3":
                bk=0
            else:
                print("Sorry , please enter a valid option")

            time.sleep(2)


    elif q==3:
        op3=1
        while op3:
            print("\n\nEnter a : To write review \nEnter b : To edit a review \nEnter c : To delete a review \nEnter d : Exit this option")
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

print("Thank you for using this service")
time.sleep(3)
