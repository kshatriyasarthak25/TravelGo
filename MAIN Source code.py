import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='sarthak25',database='travel_booking')
c1=conn.cursor()
conn.autocommit = True

from time import gmtime, strftime
n=strftime("%a, %d %b %Y", gmtime())
n=str(n)
today=n[5:]


print('                 ','________TRAVEL DAILY welcomes U!!!!!!__________')
print()
print('                                   ',n)
print()
print('Press 1 to Login') 
print('Press 2 Create account')
print("press 3 delete account")
print('Press 4 to Exit')
print()
choice=int (input('Enter your choice='))


if choice ==1:
                print()
                a=int(input('Enter your phone number='))
                #Name of the person
                u=("select  name from accounts where phone_number = "+str(a)+";")
                c1.execute(u)
                #Wrong phone number[account doesn't exist]
                datan=c1.fetchall()
                s=c1.rowcount
                s=abs(s)   
                if s!= 1:
                    print()
                    print("***********************ACCOUNT DOESN'T EXIST************************")
                    print()
                    create=int(input("Press 32 to create account {{or}} Press 0 to exit="))
                    if create==32:
                        phone_number=int(input('Phone Number='))
                        name=str(input('Name='))
                        password =str(input( 'password[10]='))
                        c1.execute("insert into accounts(Phone_number,password,name )values(" + str(phone_number) +",'" +password  + "',' "+name+" ')")
                        conn.commit()
                        print('Account sucessfully Created')
                        import sys
                        sys.exit()
                    else:
                        import sys
                        sys.exit()
                    
                
                datan=datan[0]
                datan=list(datan)
                datan= datan[0]
                datan= str(datan)
               
                
            #selecting password
                y="select password from accounts where phone_number =({})".format(a)
                c1.execute(y)
                data=c1.fetchall()
                data=data[0]
                data=list(data)
                data=data[0]

                b=(input('Enter your password='))
                if b!=data:
                    print()
                    print("***********************INVALID PASSWORD**************************")
                conn.commit()
                    

        
                if b==data:
                    print()
                    print("LOGGED  IN !!!!!")
                    print()
                    print("HI",datan,"!!")
                    print()
                    print("What can I do for you?")
                    print()
                    print('12.Book for a board')
                    print('13.Bill verification')
                    print('14.My travel log')
                    print('0.Exit')
                    print()
                    choice1=int(input('Enter Your Choice='))
                    if choice1==0:
                        print()
                        print("Thank you , Visit again !!")
                        import sys
                        sys.exit()
                
                    if choice1==12:
                        your_location=input('Your_location=')
                        your_destination=input('Your_destination=')
                        time=input('time to start board=')
                        driver=input("driver gender preferences=")
                        urgency=input('urgency(yes/no)=')
                        c1.execute("insert into customer_bookings values(" + str(a) +",' " +  your_location + " ' ,'  "+your_destination+ " ' ,' "+time+ " ' ,' "+driver+" ' ,' "+urgency+" ',' "+today+" ' )")
                        conn.commit()
                        print()
                        print('********************************AT YOUR SERVICE AT',time,"********************************")
                        import sys
                        sys.exit()
                       
                        
                    if choice1==13:
                        Dist=int(input('distance travelled [km]='))
                        bill=Dist*5
                        print('your payment =Rs.',bill)
                    if choice1==14:                
                        c1.execute("select  your_destination,date_booked from customer_bookings where phone_number like '"+str(a)+"';")
                        data=c1.fetchall()
                        for row in data:
                               print(row[0],'-  {',row[1],'}')
                        conn.commit()
                        import sys
                        sys.exit()
                    if choice!=14 and 12 and 13:
                            print()
                            print()
                            print("********************INVALID CHOICE**********************")
                    import sys
                    sys.exit()
               

if choice==2:
    phone_number=int(input('Phone Number='))
    name=str(input('Name='))
    password =str(input( 'password[10]='))
    c1.execute("insert into accounts(Phone_number,password,name )values(" + str(phone_number) +",'" +str(password)  + "',' "+name+" ')")
    conn.commit()
    print('Account sucessfully Created')
    import sys
    sys.exit()

if choice==3:
    phone_number=int(input("enter your phone_number="))
    c1.execute("delete from customer_bookings where phone_number ="+str(phone_number)+";")
    c1.execute("delete from accounts where phone_number ="+str(phone_number)+";")
    conn.commit()
    print()
    print("**************************************SUCCESSFULLY ACCOUNT DELETED**************************************")
    import sys
    sys.exit()
    
if choice==4:
    import sys
    sys.exit()
   

if choice!=1 and 2 and 3:
    print()
    print()
    print("********************INVALID CHOICE**********************")
