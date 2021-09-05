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
    print('\n\t\t𝐌𝐚𝐢𝐧 𝐌𝐞𝐧𝐮\n\n𝐂𝐡𝐨𝐨𝐬𝐞 𝐚𝐧 𝐨𝐩𝐭𝐢𝐨𝐧 𝐟𝐫𝐨𝐦 𝐭𝐡𝐞 𝐛𝐞𝐥𝐨𝐰 𝐥𝐢𝐬𝐭𝐞𝐝 : \n\n 1. 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧 𝐨𝐟 𝐚 𝐩𝐥𝐚𝐜𝐞 \n 2. 𝐇𝐨𝐭𝐞𝐥 𝐁𝐨𝐨𝐤𝐢𝐧𝐠𝐬 \n 3. 𝐑𝐞𝐯𝐢𝐞𝐰𝐬 \n 4. 𝐄𝐱𝐢𝐭 ')
    q=int(input("\n\nYour choice (𝟏,𝟐,𝟑,𝟒) : "))

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
        print("\n\n𝐄𝐧𝐭𝐞𝐫 𝐭𝐡𝐞 𝐰𝐞𝐛𝐬𝐢𝐭𝐞 𝐲𝐨𝐮 𝐰𝐨𝐮𝐥𝐝 𝐩𝐫𝐞𝐟𝐞𝐫 𝐭𝐨 𝐝𝐨 𝐲𝐨𝐮𝐫 𝐇𝐨𝐭𝐞𝐥 𝐁𝐨𝐨𝐤𝐢𝐧𝐠 𝐢𝐧 : \n 1. 𝐘𝐚𝐭𝐫𝐚\n 2. 𝐄𝐚𝐬𝐞𝐦𝐲𝐭𝐫𝐢𝐩\n 3. 𝐄𝐱𝐢𝐭 \n\n")
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
            print("\n\n𝐄𝐧𝐭𝐞𝐫 a : 𝐓𝐨 𝐰𝐫𝐢𝐭𝐞 𝐚 𝐫𝐞𝐯𝐢𝐞𝐰 \n𝐄𝐧𝐭𝐞𝐫 b : 𝐓𝐨 𝐞𝐝𝐢𝐭 𝐚 𝐫𝐞𝐯𝐢𝐞𝐰 \n𝐄𝐧𝐭𝐞𝐫 c : 𝐓𝐨 𝐝𝐞𝐥𝐞𝐭𝐞 𝐚 𝐫𝐞𝐯𝐢𝐞𝐰 \n𝐄𝐧𝐭𝐞𝐫 d : 𝐄𝐱𝐢𝐭 𝐅𝐫𝐨𝐦 𝐭𝐡𝐢𝐬 𝐨𝐩𝐭𝐢𝐨𝐧")
            op4=input("\n\n𝐘𝐨𝐮𝐫 𝐜𝐡𝐨𝐢𝐜𝐞 (𝐚,𝐛,𝐜,𝐝) : ")
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

print("𝑻𝒉𝒂𝒏𝒌 𝒚𝒐𝒖 𝒇𝒐𝒓 𝒖𝒔𝒊𝒏𝒈 𝒐𝒖𝒓 𝑺𝒆𝒓𝒗𝒊𝒄𝒆.")
time.sleep(3)
