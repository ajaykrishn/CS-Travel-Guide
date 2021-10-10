""""""

import os
import sys
from pwinput import pwinput
import mysql.connector as mysql


def Wiki():  # Add wikipedia and pwinput module to Python path
    path = os.getcwd()
    wiki_path = path + r"\Wikipediam"
    pw_path = path + r"\pwinput"
    sys.path.append(wiki_path)
    sys.path.append(pw_path)


def create_rev(fname, curso):  # Create Tables in Mysql from dump file
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


def connectdb():              # Connect to Mysql
    usr = input("Enter Username: ")
    psw = pwinput.pwinput("Enter Password: ")
    con = mysql.connect(host='localhost', user=usr, passwd=psw)
    curs = con.cursor()
    create_dbase(curs)
    print("\nMySQL connection established ✅")
    return con


def create_dbase(curs):  # Creating database in Mysql
    curs.execute(
        "SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'Review') AND (TABLE_NAME = 'Reviews')")
    c = curs.fetchone()[0]
    if c == 0:
        curs.execute("Create Database Review")
        curs.execute("Use Review")
        path = os.getcwd().replace('\\', '/') + "/review_reviews.sql"
        create_rev(path, curs)
    else:
        curs.execute("Use Review")
