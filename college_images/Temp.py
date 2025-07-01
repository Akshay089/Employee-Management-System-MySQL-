from tkinter import*								
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Management System")

        #Variables
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_designation=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_EmployeeId=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_country=StringVar()
        self.var_ctc=StringVar()
        

        #Title
        lbl_title=Label(self.root,text='____EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',37,'bold'),fg='blue',bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=50)

        #logo
        img_logo=Image.open('college_images/employee.png')
        img_logo=img_logo.resize((50,50))
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=300,y=0,width=50,height=50)

        #Images 
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=160)

        #IMAGE1
        img1=Image.open('college_images/img.jpg')
        img1=img1.resize((540,160))
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)

        #IMAGE2
        img2=Image.open('college_images/Emp.webp')
        img2=img2.resize((540,160))
        self.photo2=ImageTk.PhotoImage(img2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=540,y=0,width=540,height=160)

        #IMAGE
        img3=Image.open('college_images/image.png')
        img3=img3.resize((540,160))
        self.photo3=ImageTk.PhotoImage(img3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=1080,y=0,width=540,height=160)

        #MAIN FRAME
        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        main_frame.place(x=10,y=220,width=1500,height=560)

        #UPPER FRAME
        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information',font=('times new roman',18,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1480,height=270)

        #Labels and input fields 
        #Department
        lbl_dep=Label(upper_frame,text='Department:',font=('arial',12,'bold'),fg='black',bg='white')
        lbl_dep.grid(row=0,column=0,padx=4,sticky=W)

        combo_dept=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial',11,'bold'),width=17,state='readonly')
        combo_dept['value']=('Select Department','HR','Finance','Sales','Marketing','Quality','Maintanance','IT','Design','Production')
        combo_dept.current(0)
        combo_dept.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #NAME
        lbl_name=Label(upper_frame,text='Name:',font=('arial',12,'bold'),fg='black',bg='white')
        lbl_name.grid(row=0,column=2,padx=4,pady=7,sticky=W)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,font=('arial',11,'bold'),width=22)
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        #Designation
        lbl_dep=Label(upper_frame,text='Designation:',font=('arial',12,'bold'),fg='black',bg='white')
        lbl_dep.grid(row=2,column=0,padx=4,sticky=W)

        combo_desig=ttk.Combobox(upper_frame,textvariable=self.var_designation,font=('arial',11,'bold'),width=17,state='readonly')
        combo_desig['value']=('Select Designation','Senior Executive','Senior Manager','Manager','Associate Manager','Team Leader','Sr.Software Engineer','Software Engineer','Associate Software Engineer','Designer')
        combo_desig.current(0)
        combo_desig.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        #Email
        lbl_mail=Label(upper_frame,text='Email:',font=('arial',12,'bold'),fg='black',bg='white')
        lbl_mail.grid(row=2,column=2,padx=4,pady=7,sticky=W)

        txt_mail=ttk.Entry(upper_frame,textvariable=self.var_email,font=('arial',11,'bold'),width=22)
        txt_mail.grid(row=2,column=3,padx=2,pady=7)

        #Address
        lbl_address=Label(upper_frame,text='Address:',font=('arial',12,'bold'),fg='black',bg='white')
        lbl_address.grid(row=3,column=0,padx=4,sticky=W)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,font=('arial',11,'bold'),width=22)
        txt_address.grid(row=3,column=1,padx=2,pady=7)

        #MARRIED STATUS
        lbl_status=Label(upper_frame,text='Married Status:',font=('arial',12,'bold'),fg='black',bg='white')
        lbl_status.grid(row=4,column=2,padx=4,pady=7,sticky=W)

        com_status=ttk.Combobox(upper_frame,textvariable=self.var_married,font=('arial',11,'bold'),width=17,state='readonly')
        com_status['value']=('Married','Unmarried')
        com_status.current(0)
        com_status.grid(row=4,column=3,padx=5,pady=7,sticky=W)

        #DOB
        lbl_dob=Label(upper_frame,text='DOB:',font=('arial',12,'bold'),fg='black',bg='white')
        lbl_dob.grid(row=3,column=2,padx=4,pady=7,sticky=W)

        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,font=('arial',11,'bold'),width=22)
        txt_dob.grid(row=3,column=3,padx=2,pady=7)

        #DOJ
        lbl_doj=Label(upper_frame,text='DOJ:',font=('arial',12,'bold'),fg='black',bg='white')
        lbl_doj.grid(row=3,column=5,padx=5,pady=7,sticky=W)

        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,font=('arial',11,'bold'),width=22)
        txt_doj.grid(row=3,column=6,padx=2,pady=7)

        #EmployeeId

        #com_txt_card=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb,font=('arial',11,'bold'),width=17,state='readonly')
        #com_txt_card['value']=('Select ID Proof','Aadhar Card','PAN Card','Driving licence','Passport','Election Card')
        #com_txt_card.current(0)
        #com_txt_card.grid(row=5,column=0,padx=2,pady=7,sticky=W)        
        lbl_gen=Label(upper_frame,text='EmployeeId',font=('arial',12,'bold'),fg='black',bg='white')
        lbl_gen.grid(row=5,column=0,padx=2,pady=7,sticky=W)

        txt_card=ttk.Entry(upper_frame,textvariable=self.var_EmployeeId,font=('arial',11,'bold'),width=22)
        txt_card.grid(row=5,column=1,padx=2,pady=7)

        #GENDER
        lbl_gen=Label(upper_frame,text='Gender:',font=('arial',12,'bold'),fg='black',bg='white')
        lbl_gen.grid(row=4,column=0,padx=4,sticky=W)

        combo_gen=ttk.Combobox(upper_frame,textvariable=self.var_gender,font=('arial',11,'bold'),width=17,state='readonly')
        combo_gen['value']=('Male','Female')
        combo_gen.current(0)
        combo_gen.grid(row=4,column=1,padx=2,pady=10,sticky=W)

        #MOBILE
        lbl_mobile=Label(upper_frame,text='Mobile No.:',font=('arial',12,'bold'),fg='black',bg='white')
        lbl_mobile.grid(row=0,column=5,padx=5,pady=7,sticky=W)

        txt_mobile=ttk.Entry(upper_frame,textvariable=self.var_mobile,font=('arial',11,'bold'),width=22)
        txt_mobile.grid(row=0,column=6,padx=2,pady=7)

        #COUNTRY
        lbl_country=Label(upper_frame,text='Country:',font=('arial',12,'bold'),fg='black',bg='white')
        lbl_country.grid(row=2,column=5,padx=5,pady=7,sticky=W)

        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,font=('arial',11,'bold'),width=22)
        txt_country.grid(row=2,column=6,padx=2,pady=7)

        #CTC
        lbl_ctc=Label(upper_frame,text='CTC:',font=('arial',12,'bold'),fg='black',bg='white')
        lbl_ctc.grid(row=5,column=2,padx=4,pady=7,sticky=W)

        txt_ctc=ttk.Entry(upper_frame,textvariable=self.var_ctc,font=('arial',11,'bold'),width=22)
        txt_ctc.grid(row=5,column=3,padx=2,pady=7)

        #IMAGE
        img4=Image.open('college_images/logo.jpg')
        img4=img4.resize((220,220))
        self.photo4=ImageTk.PhotoImage(img4)

        self.img_4=Label(upper_frame,image=self.photo4)
        self.img_4.place(x=1000,y=0,width=220,height=220)

        #FRAME FOR BUTTONS
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1230,y=10,width=170,height=210)

        btn_add=Button(button_frame,text="SAVE",command=self.add_data,font=('arial',11,'bold'),width=13,bg='blue',fg='white')
        btn_add.grid(row=1,column=2,padx=18,pady=10)

        btn_delete=Button(button_frame,text="REMOVE",command=self.delete_data,font=('arial',11,'bold'),width=13,bg='blue',fg='white')
        btn_delete.grid(row=2,column=2,padx=18,pady=8)

        btn_update=Button(button_frame,text="UPDATE",command=self.update_data,font=('arial',11,'bold'),width=13,bg='blue',fg='white')
        btn_update.grid(row=3,column=2,padx=18,pady=9)

        btn_clear=Button(button_frame,text="CLEAR",command=self.reset_data,font=('arial',11,'bold'),width=13,bg='blue',fg='white')
        btn_clear.grid(row=4,column=2,padx=18,pady=10)


        #DOWN FRAME
        down_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information Table',font=('times new roman',18,'bold'),fg='red')
        down_frame.place(x=10,y=280,width=1480,height=270)

        #SEARCH FRAME
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text='Search Employee',font=('times new roman',14,'bold'),fg='blue')
        search_frame.place(x=0,y=0,width=1470,height=60)

        search_by=Label(search_frame,font=('arial',11,'bold'),fg='white',bg='red',text="Search By:")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        #SEARCH
        self.var_com_search=StringVar()
        com_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=('arial',11,'bold'),width=17,state='readonly')
        com_search['value']=('Select Option','Name','Phone','employeeid')
        com_search.current(0)
        com_search.grid(row=0,column=1,padx=5,sticky=W) 

        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,font=('arial',11,'bold'),width=22)
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(search_frame,text="SEARCH",command=self.search_data,font=('arial',11,'bold'),width=13,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=5)

        btn_showAll=Button(search_frame,text="Show All",command=self.fetch_data,font=('arial',11,'bold'),width=13,bg='blue',fg='white')
        btn_showAll.grid(row=0,column=4,padx=5)

        #________________TABLE_________________
        #TABLE FRAME
        table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.empinfo=ttk.Treeview(table_frame,column=("dep","name","designation","email","address","married","DOB","DOJ","EmployeeId","Gender","mobile","country","CTC",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.empinfo.xview)
        scroll_y.config(command=self.empinfo.yview)

        self.empinfo.heading("dep",text="Department")
        self.empinfo.heading('name',text='Name')
        self.empinfo.heading('designation',text='Designation')
        self.empinfo.heading('email',text='Email')
        self.empinfo.heading('address',text='Address')
        self.empinfo.heading('married',text='Married Status')
        self.empinfo.heading('DOB',text='DOB')
        self.empinfo.heading('DOJ',text='DOJ')
        self.empinfo.heading('EmployeeId',text='EmployeeId')
        self.empinfo.heading('Gender',text='Gender')
        self.empinfo.heading('mobile',text='Phone')
        self.empinfo.heading('country',text='Country')
        self.empinfo.heading('CTC',text='CTC')
        
        self.empinfo['show']='headings'
    
        self.empinfo.column("dep",width=100)
        self.empinfo.column("name",width=100)
        self.empinfo.column("designation",width=100)
        self.empinfo.column("email",width=100)
        self.empinfo.column("address",width=70)
        self.empinfo.column("married",width=80)
        self.empinfo.column("DOB",width=100)
        self.empinfo.column("DOJ",width=100)
        self.empinfo.column("EmployeeId",width=100)
        self.empinfo.column("Gender",width=100)
        self.empinfo.column("mobile",width=100)
        self.empinfo.column("country",width=100)
        self.empinfo.column("CTC",width=100)
        

        self.empinfo.pack(fill=BOTH,expand=1)
        self.empinfo.bind("<ButtonRelease>",self.get_cursor)
        

        self.fetch_data()

    #_______________Fuctions_______________________    
    def add_data(self):
            if self.var_dep.get()=="" or self.var_email.get()=="":
                messagebox.showerror('Error','All Fields are required')
            else:
                try:
                    conn=mysql.connector.connect(host='localhost',username='root',password='W7301@jqir#',database='ems')
                    my_cursor=conn.cursor()
                    my_cursor.execute('insert into empinfo values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                        self.var_dep.get(),
                                                                                        self.var_name.get(),
                                                                                        self.var_designation.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_married.get(),
                                                                                        self.var_dob.get(),
                                                                                        self.var_doj.get(),
                                                                                        self.var_EmployeeId.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_mobile.get(),
                                                                                        self.var_country.get(),
                                                                                        self.var_ctc.get()

                                                                                    ))
                    conn.commit()
                    self.fetch_data()    #--->To add data immediately
                    conn.close()
                    messagebox.showinfo('Success','Employee has been added!',parent=self.root)
                except Exception as es:
                    messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)                                                                   
    #FETCH Function
    def fetch_data(self):
                conn=mysql.connector.connect(host='localhost',username='root',password='W7301@jqir#',database='ems')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from empinfo')
                data=my_cursor.fetchall()       #-->Variable to store the data
                if len(data)!=0:
                    self.empinfo.delete(*self.empinfo.get_children())
                    for i in data:
                        self.empinfo.insert("",END,values=i)
                    conn.commit
                conn.close()
    
    #Get Cursor
    def get_cursor(self,event=""):
        cursor_row=self.empinfo.focus()
        content=self.empinfo.item(cursor_row)
        data=content['values']

        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designation.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_EmployeeId.set(data[8])
        self.var_gender.set(data[9])
        self.var_mobile.set(data[10])
        self.var_country.set(data[11])
        self.var_ctc.set(data[12])

    def update_data(self):
            if self.var_dep.get()=="" or self.var_email.get()=="":
                messagebox.showerror('Error','All Fields are required')
            else:
                try:
                    update=messagebox.askyesno('Update','Are you sure to update this Employee data')
                    if update>0:
                        conn=mysql.connector.connect(host='localhost',username='root',password='W7301@jqir#',database='ems')
                        my_cursor=conn.cursor()
                        my_cursor.execute('update empinfo set Department=%s,Name=%s,Designation=%s,Email=%s,Address=%s,Married_Status=%s,DOB=%s,DOJ=%s,Gender=%s,Phone=%s,Country=%s,CTC=%s where EmployeeId=%s',(
                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                    self.var_designation.get(),
                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                    self.var_married.get(),
                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                    self.var_doj.get(),
                                                                                                                                                                                                                                                                                                                                  
                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                    self.var_mobile.get(),
                                                                                                                                                                    self.var_country.get(),
                                                                                                                                                                    self.var_ctc.get(),
                                                                                                                                                                    self.var_EmployeeId.get()              
                                                                                                                                                                ))
                    else:
                        if not update:
                           return
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo('Success','Updated Successfully',parent=self.root)        
                except Exception as es:
                        messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    #DELETE
    def delete_data(self):
        if self.var_EmployeeId.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure to delete this Employee data')
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='W7301@jqir#',database='ems')
                    my_cursor=conn.cursor()
                    sql='delete from empinfo where EmployeeId=%s'
                    value=(self.var_EmployeeId.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()    #--->To add data immediately
                conn.close()
                messagebox.showinfo('Delete','Employee has been Deleted!',parent=self.root)
            except Exception as es:
                    messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    
    #RESET
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_name.set("")
        self.var_designation.set("Select Designation")
        self.var_email.set("")
        self.var_address.set("")
        self.var_married.set("Married")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_EmployeeId.set("")
        self.var_gender.set("Male")
        self.var_mobile.set("")
        self.var_country.set("")
        self.var_ctc.set("")


############################# SEARCH ####################################
    def search_data(self):
        if self.var_com_search.get()=='' or self.var_search.get()=='':
            messagebox.showerror('Error','Please select option')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='W7301@jqir#',database='ems')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from empinfo where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'")) #-->from empinfo where ' +str-->Here,i.e Spacing is must before and after single quote(')
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.empinfo.delete(*self.empinfo.get_children())
                    for i in rows:
                        self.empinfo.insert("",END,values=i)
                conn.commit
                conn.close()
            except Exception as es:
                    messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()

