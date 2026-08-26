#READS
#READ
#READ
#!!!!!!!!!!!!!
#IF I EVER OPEN THIS REMEMBER TO START MYSQL IN WINDOWS SERVICES    




from tkinter import colorchooser
from tkinter import *
#import csv
from PIL import ImageTk, Image
from mysql.connector import connect

#from mysql.connector import cursor
#from mysql.connector import execute



#from tkmacosx import Button

try:
    mycon=connect(host='localhost',user='root',passwd='mysqlroot',database='project')
    mc=mycon.cursor()
except:
    host=input('Enter host:')
    user=input('Enter username:')
    password=input('Enter password:')
    mycon=connect(host=host,user=user,passwd=password)
    mc=mycon.cursor()
    
    mc.execute('create database project')
    mc.execute('use project')
    mc.execute('''create table Event_Details (
                Event_ID int primary key,
                Event_Name varchar(30),
                Event_Type varchar(30),
                Event_Location varchar(30),
                Event_Date date,
                Start_Time time,
                End_Time time,
                Number_of_Guests int,
                Flag_of_Completion char(1)''')
    mc.execute('''create table Login_Details (
                username varchar(30),
                password varchar(30))''')
    mc.execute('insert into login_details values ("administrator","administrator")')
    
root=Tk()

root.title('EVENT MANAGEMENT')

root.geometry('1050x500')

#root.configure(bg='#FFFFFF')

#Function to get the background colour from the user
def bg_colour_command():
    global bg_colour

    bg_colour = colorchooser.askcolor(title="Select Color")
    if bg_colour[1]:  
        welcome.configure(bg=bg_colour[1])
        welcome1.configure(bg=bg_colour[1])
        username_text.configure(bg=bg_colour[1])
        password_text.configure(bg=bg_colour[1])
        root.configure(bg=bg_colour[1])
        es1.configure(bg=bg_colour[1])
        es2.configure(bg=bg_colour[1])

#Function to get the text colour from the user
def text_colour_command():
    global text_colour
    
    text_colour = colorchooser.askcolor(title="Select Color")
    if text_colour[1]:  
        welcome.configure(fg=text_colour[1])
        welcome1.configure(fg=text_colour[1])
        username_text.configure(fg=text_colour[1])
        password_text.configure(fg=text_colour[1])    

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#This funtion gets called when the user presses the 'ok' button and it destroys the window that is displayed when you type the incorrect password or username
def incorrect_destroy():
    incorrect_window.destroy()

#This function checks with the database if the username and password exisits or not
def login_check():
    mc.execute('select * from login_details')
    details=mc.fetchall()
    f=False
    
    for i in details:
        if username.get()==i[0] and password.get()==i[1]:
            login_clicked()
            f=True
            
    if f==False:
        global incorrect_window
        global incorrect
        global ok
        incorrect_window= Toplevel()
        incorrect_window.configure(bg=bg_colour[1])
        incorrect = Label(incorrect_window,text = 'Incorrect username or password',font=("Arial", 30),fg=text_colour[1],bg=bg_colour[1]).grid(row=0,column=0,columnspan=2)
        ok = Button(incorrect_window,text='OK',command=incorrect_destroy,padx=15,pady=5).grid(row=1,column=0,padx=160)
            
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#This funtion destroys the logion page and shows the menu page
def login_clicked():

    #Funtion to call menu page
    start()

    #Destroying of previous page
    username.destroy()
    username_text.destroy()
    password_text.destroy()
    password.destroy()
    welcome.destroy()
    welcome1.destroy()
    start_submit.destroy()
    es1.destroy()
    es2.destroy()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#This funtion shows the login page of the program
def actual_start():

    global text_colour
    text_colour=('','#FFFFFF')

    global bg_colour
    bg_colour=('','#323232')
    
    global welcome
    global welcome1
    welcome=Label(root,text = 'WELCOME',font=("Arial", 50))
    welcome1=Label(root,text = 'PLEASE ENTER USERNAME AND PASSWORD',font=("Arial", 40))
    welcome.grid(row=1,column=3,columnspan=3,pady=10)
    welcome1.grid(row=2,column=3,columnspan=3,padx=75,pady=20)

    global es1
    es1=Label(root,text='')
    es1.grid(row=6,column=4)

    global es2
    es2=Label(root,text='')
    es2.grid(row=9,column=4)
    
    global username
    global username_text
    global password
    global password_text

    username_text=Label(root,text='Enter Username',font=("Arial", 20))
    password_text=Label(root,text='Enter password',font=("Arial", 20))
    username_text.grid(row=4,column=4)
    password_text.grid(row=7,column=4)
    
    username = Entry(root , width=15)
    password = Entry(root , width=15,show='*')
    username.grid(row=5,column=4)
    password.grid(row=8,column=4)

    global start_submit
    start_submit = Button(root,text='Login',command=login_check,font=("Arial", 20),padx=20,pady=5)
    start_submit.grid(row=10,column=4)

    global edit_text_colour
    edit_text_colour=Button(root,text='Do you want to \n edit the text colour?',height=5,width=20,command=text_colour_command)
    edit_text_colour.grid(row=10,column=0,columnspan=4,padx=50)

    global edit_bg_colour
    edit_bg_colour=Button(root,text='Do you want to edit\n the background colour?',height=5,width=20,command=bg_colour_command)
    edit_bg_colour.grid(row=10,column=5,columnspan=4,padx=50)
   
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#This function is the start of the program aka the menu screen
def start():

    
    edit_text_colour.destroy()
    edit_bg_colour.destroy()
    
    global search_b
    global add_values_b
    global edit_values_b
    global delete_b

    global heading1
    heading1 = Label(root , text='EVENT MANAGEMENT' , font=("Arial", 50),fg=text_colour[1],bg=bg_colour[1])
    heading1.grid(row=1 , column=4,columnspan=5 ,sticky=N,padx=200,pady=25)
    
    global heading
    heading = Label(root , text='WHAT ACTION DO YOU WANNA PERFORM?' , font=("Arial", 30),fg=text_colour[1],bg=bg_colour[1])
    heading.grid(row=2 , column=4,columnspan=3 ,sticky=N,pady=25,padx=200)

    delete_b= Button(root  , text = 'Delete a value?' ,font=("Arial", 20) , command=delete_values,padx=10,pady=10)
    delete_b.grid(row=3 , column=4,pady=25)
    
    search_b= Button(root  , text = 'Search for a event?' ,font=("Arial", 20) , command=search,padx=10,pady=10)
    search_b.grid(row=4 , column=6,pady=30)

    add_values_b= Button(root , text = 'Add more values?' ,font=("Arial", 20) , command=add_values,padx=16,pady=10)
    add_values_b.grid(row=3 , column=6)

    edit_values_b = Button(root , text = 'Edit values?' ,font=("Arial", 20), command=edit_values,padx=25,pady=10)
    edit_values_b.grid(row=4 , column=4)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#This function will be called when you press the 'Go Back?' button after clicking 'Search for a event?' button
def back_pressed_s():

    
    s.destroy()
    s_val.destroy()
    s_b.destroy()
    heading_s.destroy()
    es6.destroy()
    showall.destroy()
    
    start()

    back.destroy()

#This function is the 'Go Back?' button which comes up when you press 'Search for a event?' button
def back_s():
    global back
    back= Button(root, text= 'Go Back?', command=back_pressed_s,padx=20,pady=10,font=("Arial", 15))
    back.grid(row=0,column=0,sticky=NW)

#This function will be called when you press the 'Go Back?' button after clicking 'Edit values?' button
def back_pressed_e():
    

    back.destroy()

    edit.destroy()
    edit_val.destroy()
    #e_b.destroy()
    es4.destroy()
    text_val.destroy()
    edit_head.destroy()
    edit_head_val.destroy()
    edit_command_button.destroy()
    
    drop_down_values.destroy()

    
    heading_e.destroy()

    start()
    

    
#This function is the 'Go Back?' button which comes up when you press 'Edit values?' button
def back_e():
    global back
    
    back= Button(root, text= 'Go Back?', command=back_pressed_e,padx=20,pady=10,font=("Arial", 15))
    back.grid(row=0,column=0,sticky=NW)

#This function will be called when you press the 'Go Back?' button after clicking 'Add more values?' button
def back_pressed_a():

    #deletion of all the texts and entry variables which appeared when you clicked 'Add more values?' button
    event_details.destroy()
    event_id.destroy()
    event_name.destroy()
    event_location.destroy()
    event_type.destroy()
    event_date.destroy()
    start_time.destroy()
    end_time.destroy()
    no_of_guests.destroy()
    flag_of_completion.destroy()
    event_id_value.destroy()
    event_name_value.destroy()
    event_location_value.destroy()
    event_type_value.destroy()
    event_date_value.destroy()
    start_time_value.destroy()
    end_time_value.destroy()
    no_of_guests_value.destroy()
    flag_of_completion_value.destroy()
    submit.destroy()
    es5.destroy()
    
    global heading1
    heading_a.destroy()
    start()
    
    back.destroy()

#This function is the 'Go Back?' button which comes up when you press 'Add more values?' button
def back_a():
    global back
    back= Button(root, text= 'Go Back?', command=back_pressed_a,padx=20,pady=10,font=("Arial", 15))
    back.grid(row=0,column=0,sticky=NW)


def back_d():
    global back
    back= Button(root, text= 'Go Back?', command=back_pressed_d,padx=20,pady=10,font=("Arial", 15))
    back.grid(row=0,column=0,sticky=NW)

    
def back_pressed_d():
    
    delete.destroy()
    delete_val.destroy()
    es3.destroy()
    delete_button.destroy()
    heading_d.destroy()

    start()
    
    back.destroy()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


##
##|‾‾‾‾‾‾\   |‾‾‾‾‾‾  |           |‾‾‾‾‾‾  ‾‾‾|‾‾‾  |‾‾‾‾‾‾
##|        |  |          |          |             |      |
##|        |  |——   |          |——      |      |——
##|        |  |          |          |             |      |
##|____/  |____  |____  |____     |      |____
##

 
def delete_window_destory():
    delete_window.destroy()
    
def delete_window_destory_confirmed():

    p=delete_val.get()
    
    mc.execute('delete from Event_Details where Event_Id={}'.format(p))
    mycon.commit()
    
    delete_window.destroy()

def confirm_delete():

    global delete_window
    
    delete_window = Toplevel()
    delete_window.configure(bg=bg_colour[1])
    delete_comfirm = Label(delete_window,text = 'Are you sure you want to delete this record?',font=("Arial", 30),fg=text_colour[1],bg=bg_colour[1]).grid(row=0,column=0,columnspan=2,pady=50)
    yes = Button(delete_window,text='YES',command=delete_window_destory_confirmed,padx=15,pady=5).grid(row=1,column=0,padx=50)
    no = Button(delete_window,text='NO',command=delete_window_destory,padx=15,pady=5).grid(row=1,column=1,padx=50)


def delete_values():

    back_d()

    heading1.destroy()
    heading.destroy()
    add_values_b.destroy()
    search_b.destroy()
    edit_values_b.destroy()
    delete_b.destroy()


    global heading_d
    
    heading_d = Label(root , text='EVENT MANAGEMENT' , font=("Arial", 50),fg=text_colour[1],bg=bg_colour[1])
    heading_d.grid(row=1 , column=2,columnspan=5 ,sticky=N,padx=100)

    global es3
    es3=Label(root,text='',bg=bg_colour[1])
    es3.grid(row=3,column=4,pady=50)
    
    global delete
    delete= Label(root , text ='Enter Event ID',font=("Arial", 30),fg=text_colour[1],bg=bg_colour[1])
    delete.grid(row=4,column=4)

    global delete_val
    delete_val= Entry(root , width=15)
    delete_val.grid(row=5,column=4)

    global delete_button
    delete_button=Button(root,text='Delete',padx=25,pady=5,font=("Arial", 20),command=confirm_delete)
    delete_button.grid(row=6,column=4,pady=20)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##
##|‾‾‾‾‾‾‾  |‾‾‾‾‾‾\  ‾‾‾‾|‾‾‾‾   ‾‾‾‾|‾‾‾‾
##|          |    	   |      |            |
##|——   |         |      |            |
##|          |         |      |            |
##|____  |____/ ___|___      |
##

def command_edit():
    global stored
    global event_id_get
    global edited_val

    event_id_get=edit_val.get()
    stored=drop_down_stored.get()
    edited_val=edit_head_val.get()

    if stored == 'Event_Name':
        mc.execute('update Event_Details set Event_Name = "{}" where Event_Id={}'.format(edited_val,event_id_get))
    elif stored == 'Event_Location':
        mc.execute('update Event_Details set Event_Location = "{}" where Event_Id={}'.format(edited_val,event_id_get))
    elif stored == 'Event_Type':
        mc.execute('update Event_Details set Event_Type = "{}" where Event_Id={}'.format(edited_val,event_id_get))
    elif stored == 'Event_Date':
        mc.execute('update Event_Details set Event_Date = "{}" where Event_Id={}'.format(edited_val,event_id_get))
    elif stored == 'Start_Time':
        mc.execute('update Event_Details set Start_Time = "{}" where Event_Id={}'.format(edited_val,event_id_get))
    elif stored == 'End_Time':
        mc.execute('update Event_Details set End_Time = "{}" where Event_Id={}'.format(edited_val,event_id_get))
    elif stored == 'Number_of_Guests':
        mc.execute('update Event_Details set Number_of_Guests = {} where Event_Id={}'.format(edited_val,event_id_get))
    elif stored == 'Flag_of_Completion':
        mc.execute('update Event_Details set Flag_of_Completion = "{}" where Event_Id={}'.format(edited_val,event_id_get))

    mycon.commit()

    

#function which shows 'Edit values?' menu which that button['Edit Values?'] gets clicked
def edit_values():

    back_e()

    heading1.destroy()
    heading.destroy()
    add_values_b.destroy()
    search_b.destroy()
    edit_values_b.destroy()
    delete_b.destroy()

    global heading_e
    
    heading_e = Label(root , text='EVENT MANAGEMENT' , font=("Arial", 40),fg=text_colour[1],bg=bg_colour[1])
    heading_e.grid(row=1 , column=2,columnspan=5 ,sticky=N,padx=140)

    global es4
    es4=Label(root,text='',bg=bg_colour[1])
    es4.grid(row=2,column=4,pady=5)

    global edit
    edit= Label(root , text ='Enter Event ID',font=("Arial", 20),fg=text_colour[1],bg=bg_colour[1])
    edit.grid(row=3,column=4,padx=40)

    global edit_val
    edit_val= Entry(root , width=15)
    edit_val.grid(row=4,column=4,padx=40)

    global text_val
    text_val=Label(root,text='Which value to be edited?',font=("Arial", 30),fg=text_colour[1],bg=bg_colour[1])
    text_val.grid(row=5,column=4,pady=30)

    global drop_down_stored
    global drop_down_values

    options=['event_name' , 'event_location', 'event_type', 'event_date', 'start_time', 'end_time', 'no_of_guests', 'flag_of_completion']
    drop_down_stored= StringVar()
    drop_down_stored.set('Event_Name')
    drop_down_values= OptionMenu(root,drop_down_stored,'Event_Name' , 'Event_Location', 'Event_Type', 'Event_Date', 'Start_Time', 'End_Time', 'Number_of_Guests', 'Flag_of_Completion')
    drop_down_values.grid(row=6,column=4,padx=40)

    global edit_head
    global edit_head_val
    global edit_command_button 

    edit_head=Label(root,text='Enter edited value:',font=("Arial", 20),fg=text_colour[1],bg=bg_colour[1])
    edit_head_val=Entry(root)
    edit_command_button=Button(root,text='Make changes?',font=("Arial", 20),padx=15,pady=5,command=command_edit)
    
    edit_head.grid(row=11,column=4,pady=10,padx=40)
    edit_head_val.grid(row=12,column=4,padx=40)
    edit_command_button.grid(row=13,column=4,padx=40)
 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##
##|‾‾‾‾‾‾‾‾ |‾‾‾‾‾‾‾‾       / \      |‾‾‾‾‾| |‾‾‾‾‾‾‾‾ |        |
##|           |               /   \     |      | |           |        |
##|_____ |____      /     \    |___| |           |____|
##          | |             /__ _\   |\       |           |        |
##          | |            /         \  |  \     |           |        |
##_____| |_____ /           \ |    \   |_____ |        |
##


def close():
    c.destroy()
    
def close1():
    d.destroy()

def close2():
    e.destroy()


def command_search():
    f=True
    
    mc.execute('select * from Event_Details')
    a=mc.fetchall()
    try:
        b=s_val.get()
        q=int(b)
        m=len(a)
        n=len(a[0])
    
        for i in range(m):
            if q==a[i][0]:
                f=True

                global c
                c=Toplevel()
                c.configure(bg=bg_colour[1])

                lis=['Event ID','Event Name','Event Location','Event Type','Event Date','Starting Time','Ending Time','Number of Guests','Flag of Completion']
            
                for j in range(len(lis)):
                    v = Entry(c, width=16 ,fg='lightblue', font=('Arial', 16, 'bold'))
                    v.grid(row=0, column=j)
                    v.insert(END, lis[j])
                    v.config(state='readonly')  # Make the entry widget read-only
   
                for j in range(n):
                    v = Entry(c, width=16 ,fg='lightblue', font=('Arial', 16, 'bold'))
                    v.grid(row=1, column=j)
                    v.insert(END, a[i][j])
                    v.config(state='readonly')
                     
                g=Button(c,text='Close window',command=close).grid(row=2,column=4,columnspan=2)

                break
            
            if b!=a[i][0]:
                f=False
        
        if f==False:

            global d
            d=Toplevel()
            m=Label(d,text='Record not found',font=("Arial", 20),fg=text_colour[1]).grid(row=0,column=0,columnspan=2)
            n=Button(d,text='Close window',command=close1,font=("Arial", 20)).grid(row=1,column=0)
    except:
        global o
        o=Toplevel()
        g=Label(o,text='Please enter Event ID',bg=bg_colour[1],fg=text_colour[1],font=("Arial", 40))
        h=Button(o,text='Close',command=close_o, padx=20, pady = 10,font=("Arial", 30))
        g.pack()
        h.pack()
                
def close_o():
    o.destroy()

            
def showall():

    mc.execute("select * from Event_Details")
    a=mc.fetchall()
    m=len(a)
    n=len(a[0])
    
    global e
    e=Toplevel()
    e.configure(bg=bg_colour[1])


    lis=['Event ID','Event Name','Event Location','Event Type','Event Date','Starting Time','Ending Time','Number of Guests','Flag of Completion']
        
    try:
        for i in range(len(lis)):
            v = Entry(e, width=16 ,fg='lightblue', font=('Arial', 16, 'bold'))
            v.grid(row=0, column=i)
            v.insert(END, lis[i])
            v.config(state='readonly')  # Make the entry widget read-only
   
    
    
        for i in range(m):
            for j in range(n):
                v = Entry(e, width=16 ,fg='lightblue', font=('Arial', 16, 'bold'))
                v.grid(row=i+1, column=j)
                v.insert(END, a[i][j])
                v.config(state='readonly')  # Make the entry widget read-only
    except:
        for i in range(len(lis)):
            v = Entry(e, width=16 ,fg='lightblue', font=('Arial', 16, 'bold'))
            v.grid(row=0, column=i)
            v.insert(END, lis[i])
            v.config(state='readonly')  # Make the entry widget read-only
   
    
    
        for i in range(m):
            for j in range(n):
                v = Entry(e, width=16 ,fg='lightblue', font=('Arial', 16, 'bold'))
                v.grid(row=i+1, column=j)
                v.insert(END, a[i][j])
                v.config(state='readonly')  # Make the entry widget read-only


    g=Button(e,text='Close window',command=close2).grid(row=m+1,column=4,columnspan=2)

            
def showall1():

    mc.execute("select * from Event_Details")
    a=mc.fetchall()
    m=len(a)
    n=len(a[0])
    
    global e
    e=Toplevel()
    e.configure(bg=bg_colour[1])

    lis=['Event ID','Event Name','Event Location','Event Type','Event Date','Starting Time','Ending Time','Number of Guests','Flag of Completion']
        
    try:
        for i in range(len(lis)):
            v = Entry(e, width=16 ,fg='lightblue', font=('Arial', 16, 'bold'))
            v.grid(row=0, column=i)
            v.insert(END, lis[i])
            v.config(state='readonly')  # Make the entry widget read-only
   
    
    
        for i in range(m):
            for j in range(n):
                v = Entry(e, width=16 ,fg='lightblue', font=('Arial', 16, 'bold'))
                v.grid(row=i+1, column=j)
                v.insert(END, a[i][j])
                v.config(state='readonly')  # Make the entry widget read-only
    except:
        for i in range(len(lis)):
            v = Entry(e, width=16 ,fg='lightblue', font=('Arial', 16, 'bold'))
            v.grid(row=0, column=i)
            v.insert(END, lis[i])
            v.config(state='readonly')  # Make the entry widget read-only
   
    
    
        for i in range(m):
            for j in range(n):
                v = Entry(e, width=16 ,fg='lightblue', font=('Arial', 16, 'bold'))
                v.grid(row=i+1, column=j)
                v.insert(END, a[i][j])
                v.config(state='readonly')  # Make the entry widget read-only
            
    g=Button(e,text='Close window',command=close2).grid(row=m+1,column=4,columnspan=2)




def search():
    
    back_s()

    heading1.destroy()
    heading.destroy()
    add_values_b.destroy()
    search_b.destroy()
    edit_values_b.destroy()
    delete_b.destroy()

    global heading_s

    heading_s = Label(root , text='EVENT MANAGEMENT' , font=("Arial", 50),fg=text_colour[1],bg=bg_colour[1])
    heading_s.grid(row=1 , column=1,columnspan=5 ,sticky=N,padx=150,pady=0)

    global es6
    es6=Label(root,text='',bg=bg_colour[1])
    es6.grid(row=2,column=4,pady=30)
    
    #This 'values' list will be used to get the values from mysql server for searching for a particular event
    values=[]
    
    #Text variable
    global s
    s= Label(root , text ='Enter Event ID',font=("Arial", 30),fg=text_colour[1],bg=bg_colour[1])
    s.grid(row=3,column=3 )

    #Value variable below text variable
    global s_val
    s_val= Entry(root , width=15)
    s_val.grid(row=4,column=3)

    global s_b
    s_b=Button(root,text='Search?',font=("Arial", 20),padx=10,pady=5,command=command_search)
    s_b.grid(row=6,column=3,pady=25)

    global showall
    showall=Button(root,text='Show all records',font=("Arial", 20),padx=10,pady=5,command=showall1)
    showall.grid(row=8,column=3)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##
##     /\     |‾‾‾‾‾‾\  |‾‾‾‾‾‾\
##    /  \    |        | |        |
##   /    \   |        | |        |
## /‾‾‾‾‾‾\  |        | |        |
##/         \ |____/ |____/
##


def add_values():

    #Back button being called when 'Add more values?' button is pressed
    back_a()

    heading.destroy()    
    add_values_b.destroy()
    search_b.destroy()
    edit_values_b.destroy()
    delete_b.destroy()

    global heading_a
    heading1.destroy()
    
    heading_a = Label(root , text='EVENT MANAGEMENT' , font=("Arial", 50),fg=text_colour[1],bg=bg_colour[1])
    heading_a.grid(row=1 , column=1,columnspan=5 ,sticky=N,padx=150,pady=0)

    global es5
    es5=Label(root,text='',bg=bg_colour[1])
    es5.grid(row=2,column=4,pady=0)

    
    #Text variables which pop up when you press add values button
    global event_id
    global event_name
    global event_location
    global event_type
    global event_date
    global start_time
    global end_time
    global no_of_guests
    global flag_of_completion

    global event_details

    event_details = Label(root , text='Event Details',font=("Arial", 43),fg=text_colour[1],bg=bg_colour[1])
    event_details.grid(row=4 , column = 0, columnspan=2)
    
    event_id = Label(root , text='Event ID',font=("Arial", 20),fg=text_colour[1],bg=bg_colour[1])
    event_name = Label(root , text='Event Name',font=("Arial", 20),fg=text_colour[1],bg=bg_colour[1])
    event_location = Label(root , text='Event Location',font=("Arial", 20),fg=text_colour[1],bg=bg_colour[1])
    event_type = Label(root , text='Event Type',font=("Arial", 20),fg=text_colour[1],bg=bg_colour[1])
    event_date = Label(root , text='Event Date',font=("Arial", 20),fg=text_colour[1],bg=bg_colour[1])
    start_time = Label(root , text='Starting Time',font=("Arial", 20),fg=text_colour[1],bg=bg_colour[1])
    end_time = Label(root , text='Ending Time',font=("Arial", 20),fg=text_colour[1],bg=bg_colour[1])
    no_of_guests = Label(root , text='Number of Guests',font=("Arial", 20),fg=text_colour[1],bg=bg_colour[1])
    flag_of_completion = Label(root , text='Flag of Completion',font=("Arial", 20),fg=text_colour[1],bg=bg_colour[1])

    event_id.grid(row=5 , column=0)
    event_name.grid(row=6 , column=0)
    event_location.grid(row=7 , column=0)
    event_type.grid(row=8, column=0)
    event_date.grid(row=9,column=0)
    start_time.grid(row=10 , column=0)
    end_time.grid(row=11 , column=0)
    no_of_guests.grid(row=12 , column=0)
    flag_of_completion.grid(row=13 , column=0)

    #value variables to get the values from the user which are below the text variables
    global event_id_value
    global event_name_value
    global event_location_value
    global event_type_value
    global event_date_value
    global start_time_value
    global end_time_value
    global no_of_guests_value
    global flag_of_completion_value
    
    event_id_value = Entry(root , width=15)
    event_name_value = Entry(root , width=15)
    event_location_value = Entry(root , width=15)
    event_type_value =  Entry(root , width=15)
    event_date_value = Entry(root , width=15)
    start_time_value = Entry(root , width=15)
    end_time_value = Entry(root , width=15)
    no_of_guests_value = Entry(root , width=15)
    flag_of_completion_value = Entry(root , width=15)
    
    event_id_value.grid(row=5 , column=1)
    event_name_value.grid(row=6 , column=1)
    event_location_value.grid(row=7 , column=1)
    event_type_value.grid(row=8 , column = 1)
    event_date_value.grid(row=9 , column = 1)
    start_time_value.grid(row=10 , column=1)
    end_time_value.grid(row=11 , column=1)
    no_of_guests_value.grid(row=12 , column=1)
    flag_of_completion_value.grid(row=13 , column=1)
    
    #submit button
    global submit
    submit= Button(root , text='Submit details', command=get_values , padx=20, pady = 15)
    submit.grid(row=8 , column = 2,rowspan=2)


def get_values():
    
    try:
        
        a=int(event_id_value.get())
        b=str(event_name_value.get())
        c=str(event_location_value.get())
        d=str(event_type_value.get())
        e=str(event_date_value.get())
        f=str(start_time_value.get())
        g=str(end_time_value.get())
        h=int(no_of_guests_value.get())
        i=str(flag_of_completion_value.get())
        
        mc.execute('insert into Event_Details values ({},"{}","{}","{}","{}","{}","{}",{},"{}")'.format(a,b,c,d,e,f,g,h,i))
        mycon.commit()
    
        event_id_value.delete(0,END)
        event_name_value.delete(0,END)
        event_location_value.delete(0,END)
        event_type_value.delete(0,END)
        event_date_value.delete(0,END)
        start_time_value.delete(0,END)
        end_time_value.delete(0,END)
        no_of_guests_value.delete(0,END)
        flag_of_completion_value.delete(0,END)

    except:
        global p
        p=Toplevel()
        p.configure(bg=bg_colour[1])
        a=Label(p,text='Please enter a value for every field',bg=bg_colour[1],fg=text_colour[1],font=("Arial", 40))
        b=Button(p,text='Close',command=close_p, padx=20, pady = 10)
        a.pack()
        b.pack()

def close_p():
    p.destroy()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

actual_start()

root.mainloop()
