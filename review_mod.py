def welcome(): #welcome message
    print('Welcome Aboard to Travel Guide.This program has been designed to help you find information regarding places in the state of Kerala,India,accomodation as per your needs and reviews about destinations you are looking for.We hope this will be of help to you in finding what you are looking for!")  

def create_dbase(curs):
    curs.execute("SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'Review') AND (TABLE_NAME = 'Reviews')")
    c=curs.fetchone()[0]
    if c==0:
        curs.execute("Create Database Review")
        curs.execute("Use Review")
        curs.execute("Create table Reviews(rev_id int primary key,usr_name varchar(30),Place varchar(50),Reviews varchar(250))")
        curs.execute("Insert into Reviews values(1000,'admin','test','test_review')")
    else:
        curs.execute("Use Review")

def create(conn,place):   #for writing reviews
    f=2
    curs=conn.cursor()
    while f!=1:
        m=input('Write your review here: ')
        name=input("Enter Your name: ")
        curs.execute("SELECT max(rev_id) FROM Reviews")
        n=curs.fetchone()[0]
        print("Reference id for editing or deleting your review is: ",n+1)
        t=(n+1,name,place,m)
        s='insert into Reviews values(%s,%s,%s,%s)'
        curs.execute(s,t)
        conn.commit()
        f=int(input('Enter zero to quit '))
        f=f+1
    curs.close()

def show_reviews(conn,place,pl_wiki):  #for displaying reviews
	curs=conn.cursor()
	curs.execute("SELECT usr_name,REVIEWS FROM Reviews WHERE Place in (%s,%s)",(place,pl_wiki))
	rev=curs.fetchall()
	if rev:
		for i in rev:
			print(i[0],':',i[1])
	else:
		print("No Reviews were Found.")
	curs.close()

def edit(conn):     #for editing reviews previously entered
    curs=conn.cursor()
    a=int(input("Enter Review Id for the review you would like to edit: "))
    b=input("Enter new review: ")
    s=("Update Reviews set Reviews=%s where rev_id=%s")
    curs.execute(s,(b,a))
    if curs.rowcount==0:
        print("The reference id entered does not exist.Enter a valid id")
    else:
        print("Review has been updated")
    conn.commit()
    curs.close()


def delete(conn): #for deleting reviews previously entered
    curs=conn.cursor()
    d=int(input("Enter the reference id for the review you would like to delete: "))
    s=('Delete from Reviews where rev_id=%s')
    curs.execute(s,(d,))
    if curs.rowcount==0:
          print("The reference id entered does not exist.Enter a valid id.")
    else:
        print("Review has been deleted")
    conn.commit()
    curs.close()



	
