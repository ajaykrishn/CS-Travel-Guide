import os
import sys
import time
import subprocess

def install(name, file):
    target = "--target=" + os.getcwd() + "\\" + file
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', name , target ])

def installall():
    install("mysql-connector-python", "mysql" )
    install("wikipedia", "Wikipediam" )
    install("pwinput", "pwinput" )

while True:
    print("\tConfigure Program\n")
    print("These components need to be installed to use this program")
    print("1. Install all")
    print("2. Custom Installation")
    print("3. Exit")
    print()
    ch = input("Choice: ")
    print()
    
    if ch=='1':
        installall()
        print("-"*20)

    elif ch=='2':
        while True:
            print("\tCustom installation\n")
            print("1. mysql-connector-python")
            print("2. wikipedia")
            print('3. pwinput')
            print("4. Main menu")
            print()
            
            ch1=input("Choice: ")
    
            if ch1=='1':
                install("mysql-connector-python", "mysql" )
                print("-"*20)
            
            elif ch1=='2':
                install("wikipedia", "Wikipediam" )
                print("-"*20)
            
            elif ch1=='3':
                install("pwinput", "pwinput" )
                print("-"*20)
        
            elif ch1=='4':
                break
            
    elif ch=='3':
        print("Thank you")
        time.sleep(0.7)
        break
        
    else:
        print("Enter a valid choice.")
