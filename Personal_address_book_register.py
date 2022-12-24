import pymysql

con=pymysql.connect(host="localhost",user="root",password="password",db="addressbook",port=3406)

def userExits(uid):
   cmd1="select * from UserInfo where UserID='"+uid+"';"
   cursor=con.cursor()
   cursor.execute(cmd1)
   row_count=0
   results = cursor.fetchall()
   row_count = cursor.rowcount
   cursor.close()
   if row_count > 0:
    print("\nUserID already Exits Try Again!!!")
    exit()
    
def userDetails(uid):
   cmd1="select * from UserDetailInfo where UserID='"+uid+"';"
   cursor=con.cursor()
   cursor.execute(cmd1)
   results = cursor.fetchall()
   for x in results:
    print("\nS.No. {} User ID: {} First Name: {} Last Name: {} DOB : {} Address : {} Remarks : {}".format(x[6],x[0],x[1],x[2],x[3],x[4],x[5]))
   cursor.close()
   
   
def userExits2(uid,passw):
   cmd1="select * from UserInfo where UserID='"+uid+"' and password ='"+passw+"';"
   cursor=con.cursor()
   cursor.execute(cmd1)
   row_count=0
   results = cursor.fetchall()
   row_count = cursor.rowcount
   cursor.close()
   if row_count == 0:
    print("\nUser Details not Valid. Try Again!!!")
    exit()
def detailedregister(UserID):
   FirstName=input("\nEnter the First Name:  ")
   LastName=input("\nEnter the Last Name:  ")
   DOB=input("\nEnter the Date of Birth(dd-mm-yyyy):  ")
   Address=input("\nEnter the Address:  ")
   notes=input("\nEnter Remarks(If Any):  ")
   cursor1=con.cursor()
   cmd="insert into UserDetailInfo(userid, FirstName, LastName, DOB, Adderss, personalNote) values ('"+UserID+"','"+FirstName+"','"+LastName+"','"+DOB+"','"+Address+"','"+notes+"')"
   cursor1.execute(cmd)
   cursor1.close()

def register():
    while True:
        UserID=input("\nEnter a UserID:  ")
        try:
            if len(str(UserID)) >20 or len(str(UserID)) <3:
                raise Exception('Invalid Input')
            break
        except:
            print("Please enter a chars contains only alphabets and the chars between 3 to 20 long.\n")
            continue
    userExits(UserID)
    while True:
        UserName=input("\nEnter a UserName:  ")
        try:
            if len(str(UserName)) >30 or len(str(UserName)) <3:
                raise Exception('Invalid Input')
            break
        except:
            print("Please enter a chars contains only alphabets and the chars between 3 to 30 long.\n")
            continue
    while True:
        passw=input("\nEnter a Password:  ")
        try:
            if len(str(passw)) >20 or len(str(passw)) <3:
                raise Exception('Invalid Input')
            break
        except:
            print("Please enter a chars contains only alphabets and the chars between 3 to 20 long.\n")
            continue
    while True:
        PhoneNum=input("\nEnter a Phone Number:  ")
        try:
            if len(str(int(PhoneNum))) <10:
                raise Exception('Invalid Input')
            break
        except:
            print("Please enter a chars contains only digits and minimum 10 chars long\n")
            continue
    
    
    cursor1=con.cursor()
    cmd="insert into UserInfo values ('"+UserID+"','"+UserName+"','"+passw+"','"+PhoneNum+"')"
    cursor1.execute(cmd)
    cursor1.close()
    print("\nUser Registerd successfully!!!!!!\n Please provide Detail Info of user.")
    detailedregister(UserID)
   
def delete(UserID,sno):
   cursor1=con.cursor()
   cmd="DELETE FROM UserDetailInfo where userid ='{}' and sno= {};".format(UserID,sno)
   cursor1.execute(cmd)
   cursor1.close()   
   

def update(UserID,sno):
   print("1.\t Update Address\n2.\t Update Remarks\n3.\t Exit")
   option1=int(input("Enter the option:  "))
   if option1 not in [1,2,3]:
    print("\nNot a valid option. Try Again !!!")
    exit()
   if option1==1:
    cursor1=con.cursor()
    add=input("\nEnter the new Address:  ")
    cmd="update UserDetailInfo set Adderss='{}' where userid ='{}' and sno= {};".format(add,UserID,sno)
    cursor1.execute(cmd)
    cursor1.close()
   if option1==2:
    cursor1=con.cursor()
    add=input("\nEnter the new Remarks")
    cmd="update UserDetailInfo set personalNote='{}' where userid ='{}' and sno= {};".format(add,UserID,sno)
    cursor1.execute(cmd)
    cursor1.close()       
    
def operation1(option,UserID):
    if(option==1):
        userDetails(UserID)
    if(option==2):
        userDetails(UserID)
        d_sno=input("\n****Provide the S.No of the row item to be Updated: ")
        update(UserID,d_sno)
        print("\n")
        userDetails(UserID)
        print("\n1 row item Updated")
    if(option==3):
        detailedregister(UserID)
        print("1 row item Added")
    if(option==4):
        userDetails(UserID)
        d_sno=input("\n****Provide the S.No of the row item to be removed: ")
        delete(UserID,d_sno)
        print("\n")
        userDetails(UserID)
        print("\n1 row item Deleted")
    if(option==5):
        print('Exit success and thanks for using this app')
 
 
def operation(option):
    if(option==1):
        print("\t\t\t******** Login Page ********\t\t\t")
        print("Please Enter the below details")
        login()
    if(option==2):
        print("\t\t\t******** Registration Page ********\t\t\t")
        print("Please Enter the below details")
        register()  
def login():
   UserID=input("Enter a UserID:  ")
   Password=input("Enter a Password:  ")
   userExits2(UserID,Password)
   print("User Logged In successfully!!!!!!\n\n\n")
   
   print("Hi "+UserID+" , Please choose any of the below action!!!\n\n\n")
   
   print("1.\t View Details\n2.\t Edit Details\n3.\t Add Details\n4.\t Delete Details\n5.\t Exit")
   option1=int(input("\nEnter the option:  "))
   if option1 not in [1,2,3,4,5]:
    print("Not a valid option. Try Again !!!")
    exit()
   operation1(option1,UserID)



print("*"*100)
print("\t\t\t******** Personal Address Book Register ********\t\t\t")
print("*"*100)
print("1.\t Login\n2.\t Register\n3.\t Exit")
option=int(input("Enter the option:  "))
if option not in [1,2,3]:
    print("\nNot a valid option. Try Again !!!")
    exit()
 
    
operation(option)    
    

        
        
con.commit()
con.close()        