def welcome(): #welcome message
    print('\t\t\t\tWELCOME! \n\nThis program has been designed to help you find information regarding places \nWe hope this will be of help to you in finding what you are looking for! \n\t\t\t\t\t\t\t\t\tᴹᵃᵈᵉ ᵇʸ ᴬʲᵃʸ,ᴬᵐᵘʳᵗʰᵃ,ᴬʸᵈᶦⁿ\n')

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
	curs.execute("SELECT usr_name,REVIEWS,revdate,trvl_avl FROM Reviews WHERE Place in (%s,%s)",(place,pl_wiki))
	rev=curs.fetchall()
	if rev:
		for i in rev:
			print(i[0],'  ',i[2],'\n',i[1])
	else:
		print("No Reviews were Found.")
	print()
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

def status(conn,pl,plw):
    curs=conn.cursor()
    curs.execute("SELECT trvl_avl,rev_id FROM Reviews WHERE Place=%s or Place=%s GROUP BY revdate HAVING revdate=max(revdate);",(pl,plw))
    sta=curs.fetchall()[0][0]
    print("Current Status: ",sta)
    curs.close()


	
