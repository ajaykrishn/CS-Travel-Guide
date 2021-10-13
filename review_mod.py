"""Module name : review_mod.py
   All functions related with accessing and manipulating
   reviews"""

import os       # built-in module
import sys      # built-in module
import random   # built-in module


def Wiki():  # Add wikipedia to Python path
    path = os.getcwd()
    wiki_path = path + r"\Wikipediam"
    sys.path.append(wiki_path)


Wiki()
import wikipedia     # Only import after appending to path


def welcome():  # welcome message
    print("\t\t\t\tWELCOME! \n")
    wel1 = "This program has been designed to help you find information "
    wel2 = "regarding places in Kerala.We hope this will be of help to you "
    wel3 = "in finding what you are looking for!\t\t\t\t\n"
    wel = wel1 + wel2 + wel3
    print(wel)

def info(conn, infoplace):   # Show Reviews
    result = wikipedia.summary(infoplace, sentences=5)
    print(result)
    p_wiki = result.split()[0]
    status(conn, infoplace, p_wiki)
    print("\nReviews:")
    show_reviews_info(conn, infoplace, p_wiki)
    ch = input("Do you want to add review?(y/n): ")
    if ch.lower() == "y":
        create(conn, infoplace)
    print()


def attrofday(conn):      # Attraction of the day
    curs = conn.cursor()
    query = 'SELECT DISTINCT Place FROM reviews'
    curs.execute(query)
    placesl = curs.fetchall()
    places = []
    for i in placesl:
        places.append(i[0])
    attraction = random.choice(places)
    info(conn, attraction)
    curs.close()


def create(conn, place):  # for writing reviews
    f = 2
    curs = conn.cursor()
    while f != 1:
        m = input('Write your review here: ')
        ctad = input("Current restrictions(Skip if not available): ")
        name = input("Enter Your name: ")
        curs.execute("SELECT max(rev_id) FROM Reviews")
        n = curs.fetchone()[0]
        print("Reference id for editing or deleting your review is: ", n + 1)
        t = (n + 1, name, place, m, ctad)
        sql1 = 'INSERT INTO Reviews(rev_id,usr_name,Place,Reviews,trvl_avl) '
        sql2 = "values(%s,%s,%s,%s,%s)"
        sql = sql1 + sql2
        curs.execute(sql, t)
        conn.commit()
        f = int(input('Enter zero to quit. '))
        f = f + 1
    curs.close()


def show_reviews_info(conn, place, pl_wiki):     # for displaying reviews
    curs = conn.cursor()
    sql = "SELECT usr_name,REVIEWS,revdate,trvl_avl FROM Reviews WHERE Place in (%s,%s)"
    curs.execute(sql, (place, pl_wiki))
    rev = curs.fetchall()
    if rev:
        for i in rev:
            print(i[0], '  ', i[2], '\n', i[1])
    else:
        print("No Reviews were Found.")
    print()
    curs.close()


def edit(conn):     # for editing reviews previously entered
    curs = conn.cursor()
    a = int(input("Enter Review Id for the review you would like to edit: "))
    show_reviews(conn, a, 'edit')
    b = input("Enter new review: ")
    ctad = input("Current restrictions(Skip if not available): ")
    s = ("Update Reviews set Reviews=%s, trvl_avl=%s where rev_id=%s")
    curs.execute(s, (b, ctad, a))
    if curs.rowcount == 0:
        print("The reference id entered does not exist.Enter a valid id")
    else:
        print("Review has been updated")
    conn.commit()
    curs.close()


def delete(conn):        # for deleting reviews previously entered
    curs = conn.cursor()
    d = int(input("Enter the reference id for the review you would like to delete: "))
    s = ('Delete from Reviews where rev_id=%s')
    curs.execute(s, (d,))
    if curs.rowcount == 0:
        print("The reference id entered does not exist.Enter a valid id.")
    else:
        print("Review has been deleted")
    conn.commit()
    curs.close()


def status(conn, pl, plw):  # show status of a place if available
    curs = conn.cursor()
    query1 = "SELECT trvl_avl,rev_id,usr_name,revdate FROM Reviews WHERE Place=%s "
    query2 = "or Place=%s GROUP BY revdate HAVING revdate=max(revdate)"
    query = query1 + query2            # query cut short to compensate hard copy 
    curs.execute(query, (pl, plw))
    dat = curs.fetchall()
    if dat:
        sta = dat[0][0]
        date = dat[0][3]
        name = dat[0][2]
        if sta != "Data not available":
            print("Current Status ( last updated on", date, 'by', name, ') :', sta)
        else:
            print("Current Status: (Please add through reviews)")
    else:
        print("Current Status: (Please add through reviews)")
    curs.close()


def show_reviews(conn, id, mode="d"):  # show reviews according to revid
    curso = conn.cursor()
    curso.execute("SELECT Reviews,Place FROM Reviews WHERE rev_id=%s", (id,))
    r = curso.fetchone()
    if r:
        place, rev = r[1], r[0]
        if mode == 'edit':  # show reviews in edit op
            print("Old review of", place, ":", rev)
        elif mode == 'd':  # show reviews according to id
            print("Your review of", place, ":", rev)
    else:
        if mode == 'd':
            print("Review id doesn't exist")
    curso.close()
