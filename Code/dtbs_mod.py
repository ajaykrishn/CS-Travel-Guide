"""Module Name : dtbs_mod.py
   All functions related to Mysql connections 
   and database creations."""

import os                        # built-in module
import pwinput.pwinput as pw     # pip install pwinput
import mysql.connector as mysql  # pip install mysql-connector-python


def connectdb():              # Connect to Mysql
    usr = input("Enter Username: ")
    psw = pw.pwinput("Enter Password: ")
    con = mysql.connect(host='localhost', user=usr, passwd=psw)
    curs = con.cursor()
    create_dbase(curs)
    print("\nMySQL connection established ✅")
    return con


def create_dbase(curs):  # Creating database in Mysql
    sql1 = "SELECT count(*) FROM information_schema.TABLES WHERE "
    sql2 = "(TABLE_SCHEMA = 'Review') AND (TABLE_NAME = 'Reviews')"
    sql = sql1 + sql2
    curs.execute(sql)
    c = curs.fetchone()[0]
    if c == 0:
        curs.execute("Create Database Review")
        curs.execute("Use Review")
        path = os.getcwd().replace('\\', '/') + "/review_reviews.sql"
        create_rev(path, curs)
    else:
        curs.execute("Use Review")

         
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
