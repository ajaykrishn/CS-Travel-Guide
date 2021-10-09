import os,sys
import mysql.connector as mysql

def Wiki():
    """Add wikipedia module and pwinput module file to Python path"""
    path = os.getcwd()
    wiki_path = path + r"\Wikipediam"
    pw_path = path + r"\pwinput"
    sys.path.append(wiki_path)
    sys.path.append(pw_path)
    
def create_rev(fname,curso):  #creating database from dump file
    fd = open(fname, 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        try:
            if command.strip() != '':
                curso.execute(command)
        except IOError as msg:
            print("Command skipped: ", msg)
          
def connectdb():
     usr=input("Enter Username: ")
     psw = pwinput.pwinput("Enter Password: ")
     con=mysql.connect(host='localhost',user=usr,passwd=psw)
     curs=con.cursor()
     create_dbase(curs)
     print("\nMySQL connection established ✅")
     return con

def create_dbase(curs):    #creating database
    curs.execute("SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'Review') AND (TABLE_NAME = 'Reviews')")
    c=curs.fetchone()[0]
    if c==0:
        curs.execute("Create Database Review")
        curs.execute("Use Review")
        path=os.getcwd().replace('\\','/')+"/review_reviews.sql"
        create_rev(path,curs)
    else:
        curs.execute("Use Review")
