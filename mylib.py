import book
import member
import transaction
import report
while(True):
 print("="*80)
 print("\t\t\t------Library Management System------\n")
 print("="*80)
 print("\t\t\t\tEnter Your Choice\n\t\t\t\t1.Book Details\n\t\t\t\t2.Member 
Details\n\t\t\t\t3.Transaction\n\t\t\t\t4.Report\n\t\t\t\t5.Exit")
 choice = int(input())
 if choice == 1:
 while(True):
 print("\t\t\t\tEnter Your Choice\n\t\t\t\t1.Add Book Details\n\t\t\t\t2. Edit 
Book Details\
 \n\t\t\t\t3. Delete A Book\n\t\t\t\t4. Search A Book\n\t\t\t\t5. Update A 
Book\
 \n\t\t\t\t6. Back To Main Menu")
 ch = int(input())
 if ch==1:
 book.book_input()
 elif ch==2:
 book.book_edit()
 elif ch==3:
 book.book_delete()
 elif ch==4:
 book.book_search()
 elif ch==5:
 book.book_update()
 elif ch==6:
 break
 elif choice ==2:
 while(True):
 print("\t\t\t\tEnter Your Choice\n\t\t\t\t1.Add Member Details\n\t\t\t\t2. Edit 
Member Details\
 \n\t\t\t\t3. Delete A Member\n\t\t\t\t4. Search A 
Member\n\t\t\t\t5. Back To Main Menu")
 ch = int(input())
 if ch==1:
 member.member_input()
 elif ch==2:
 member.member_edit()
 elif ch==3:
 member.member_delete()
 elif ch==4:
 member.member_search()
 elif ch==5:
 break
 elif choice == 3:
 while(True):
 print("\t\t\t\tEnter Your Choice\n\t\t\t\t1.Issue Book\n\t\t\t\t2. Return 
Book\n\t\t\t\t3. Back To Main Menu")
 ch = int(input())
 if ch==1:
 transaction.book_issue()
 elif ch==2:
 transaction.book_return()
 elif ch==3:
 break
 
 elif choice == 4:
 while(True):
 print("\t\t\t\tEnter Your Choice\n\t\t\t\t1.Book Details\n\t\t\t\t2. Member 
Details\
 \n\t\t\t\t3. Issue Details\n\t\t\t\t4. Return Details\n\t\t\t\t5. Best Reading 
Book (Chart)\
 \n\t\t\t\t6. Back To Main Menu")
 ch = int(input())
 if ch==1:
 report.book_output()
 elif ch==2:
 report.member_output()
 elif ch==3:
 report.issue_output()
 elif ch==4:
 report.return_output()
 elif ch==5:
 report.col_chart()
 elif ch==6:

 break
 elif choice == 5:
 break
‘BOOK’ MODULEimport mysql.connector as sqlt
import pandas as pd
from tabulate import tabulate
con = sqlt.connect(host = "localhost", user = "root", passwd = "sanjay", database = "library")
cursor = con.cursor()
def book_input():
 try:
 bookid=input("Enter Book Id")
 bname = input("Enter Book Name")
 author = input("Enter Author Name")
 price = float(input("Enter Price"))
 copies = int(input("Enter No of Copies"))
 qry = "insert into book values({},'{}','{}',{},{},{});".format(bookid, bname, author, price, 
copies,copies)
 cursor.execute(qry)
 con.commit()
 print("added successfully..")
 except:
 print("Error.. Worng Entry")
def book_edit():
 x=int(input("Enter Book ID"))
 qry="select * from book where bookid = {};".format(x)
 cursor.execute(qry)
 r=cursor.fetchone()
 if r:
 y=float(input("Enter New Price"))
 qry = "update book set price = {} where bookid = {};".format(y,x)
 cursor.execute(qry)
 con.commit()
 print("Edited Successfully.")
 
 else:
 print("Wrong Book ID")
def book_update():
 x=int(input("Enter Book ID"))
 qry="select * from book where bookid = {};".format(x)
 cursor.execute(qry)
 r=cursor.fetchone()
 print("Present Copies- ",r[4])
 print("Present Remaining Copies- ",r[5])
 if r:
 y=float(input("Enter No of New Copies"))
 qry = "update book set copies = {}, rem_copies = {} where bookid = 
{};".format(r[4]+5,r[5]+5,x)
 cursor.execute(qry)
 con.commit()
 print("Updated Successfully.")
 qry="select * from book where bookid = {};".format(x)
 df = pd.read_sql(qry,con)
 print("New Updated Book Details")
 print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = False))
 else:
 print("Wrong Book ID")
def book_delete():
 x=int(input("Enter Book ID"))
 qry="select * from book where bookid = {};".format(x)
 cursor.execute(qry)
 r=cursor.fetchone()
 if r:
 qry = "delete from book where bookid = {};".format(x)
 cursor.execute(qry)
 con.commit()
 print("deleted Successfully.")
 
 else:
 print("Wrong Book ID")
def book_search():
 x=int(input("Enter Book ID"))
 qry="select * from book where bookid = {};".format(x)
 cursor.execute(qry)
 r=cursor.fetchone()
 if r:
 
 df = pd.read_sql(qry,con)
 print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = False))

 
 else:
 print("Wrong Book ID")
‘MEMBER’ MODULEimport book
import mysql.connector as sqlt
import pandas as pd
from tabulate import tabulate
con = sqlt.connect(host = "localhost", user = "root", passwd = "sanjay", database = "library")
cursor = con.cursor()
def member_input():
 try:
 memberid=int(input("Enter Member Id"))
 mname = input("Enter Member Name")
 madd = input("Enter member Address")
 phone = input("Enter Phone No")
 
 qry = "insert into member values({},'{}','{}','{}');".format(memberid, mname, madd, phone)
 cursor.execute(qry)
 con.commit()
 print("added successfully..")
 except:
 print("Error...")
def member_edit():
 x=int(input("Enter Member ID"))
 qry="select * from member where memberid = {};".format(x)
 cursor.execute(qry)
 r=cursor.fetchone()
 if r:
 y=input("Enter New Address")
 qry = "update member set madd = '{}' where memberid = {};".format(y,x)
 cursor.execute(qry)
 con.commit()
 print("Edited Successfully.")
 
 else:
 print("Wrong Member ID")
def member_delete():

 x=int(input("Enter Member ID"))
 qry="select * from member where memberid = {};".format(x)
 cursor.execute(qry)
 r=cursor.fetchone()
 if r:
 qry = "delete from member where memberid = {};".format(x)
 cursor.execute(qry)
 con.commit()
 print("deleted Successfully.")
 
 else:
 print("Wrong member ID")
def member_search():
 x=int(input("Enter Member ID"))
 qry="select * from member where memberid = {};".format(x)
 cursor.execute(qry)
 r=cursor.fetchone()
 if r:
 
 df = pd.read_sql(qry,con)
 print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = False))
 
 else:
 print("Wrong Member ID")
‘TRANSACTION MODULEimport book
import mysql.connector as sqlt
import pandas as pd
from tabulate import tabulate
con = sqlt.connect(host = "localhost", user = "root", passwd = "sanjay", database = "library")
cursor = con.cursor()
def book_issue():
 q = "select max(issueid) from issue;"
 cursor.execute(q)
 r = cursor.fetchone()[0]
 if r:
 issueid = r+1
 else:
 issueid = 1
 x=int(input("Enter Member ID"))
 q1 = "select * from member where memberid = {};".format(x)
 cursor.execute(q1)
 r=cursor.fetchone()
 if r:
 y =int(input("Enter Book ID"))
 q2 = "select bookid, rem_copies from book where bookid = {};".format(y)
 cursor.execute(q2)
 r=cursor.fetchone()
 if r:
 if r[1] > 0:
 issuedate = input("Enter Issue Date")
 copies = int(input("Enter No of Copies"))
 remcopies = r[1] - copies
 q3 = "insert into issue values({},'{}',{},{},{});".format(issueid, issuedate, x, y,copies)
 cursor.execute(q3)
 q4 = "update book set rem_copies = {} where bookid = {};".format(remcopies,y)
 cursor.execute(q4)
 con.commit()
 print("Book Issued...")
 else:
 print("Book is Not Available")
 else:
 print("Wrong Book ID ")
 
 else: 
 print("Wrong Memeber Id")
def book_return():
 q = "select max(returnid) from returns;"
 cursor.execute(q)
 r = cursor.fetchone()[0]
 if r:
 reutrnid = r+1
 else:
 returnid = 1
 x=int(input("Enter Member ID"))
 q1 = "select * from member where memberid = {};".format(x)
 cursor.execute(q1)
 r=cursor.fetchone()
 if r:
 y =int(input("Enter Book ID"))
 q2 = "select bookid, rem_copies from book where bookid = {};".format(y)
 cursor.execute(q2)


 r=cursor.fetchone()
 if r:
 
 returndate = input("Enter return Date")
 copies = int(input("Enter No of Copies"))
 remcopies = r[1] + copies
 q3 = "insert into returns values({},'{}',{},{},{});".format(returnid, returndate, x, y,copies)
 cursor.execute(q3)
 q4 = "update book set rem_copies = {} where bookid = {};".format(remcopies,y)
 cursor.execute(q4)
 con.commit()
 print("Book Returned...")
 
 else:
 print("Wrong Book ID ")
 
 else: 
 print("Wrong Memeber Id")
‘REPORT’ MODULEimport mysql.connector as sqlt
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
con = sqlt.connect(host = "localhost", user = "root", passwd = "sanjay", database = "library")
cursor = con.cursor()
def book_output():
 df = pd.read_sql("select * from book",con)
 print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = False))
def member_output():
 df = pd.read_sql("select * from member",con)
 print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = False))
def return_output():
 df = pd.read_sql("select * from returns",con)
 print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = False))
def issue_output():
 df = pd.read_sql("select * from issue",con)
 print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = False))
def col_chart():
 q = "select bookid, count(copies) as totalcopies from issue group by bookid;"
 df = pd.read_sql(q,con)
 print(df)
 plt.bar(df.bookid, df.totalcopies)
 plt.xlabel("BookID")
 plt.ylabel("Copies Issued")
 plt.title("Best Reading Book")
 plt.xticks(df.bookid)
 plt.show()
