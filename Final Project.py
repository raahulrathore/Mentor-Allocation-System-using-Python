from tkinter import *
from tkinter import messagebox
import time, os

#main window

root = Tk()
root.title("Supervisior Allocation Portal")
root.configure(background="cadetblue4")
root.resizable(width=False,height=False)
root.geometry("610x180+170+200")
l=Label(root,text="Welcome To Mentor Allocation System",font=('arial',25,'bold'),justify=CENTER,bg = 'cyan2')
l.grid(row=0,column=4,columnspan=4)

#registering new user
#norms : 
#l_attribute_section
#e_attribute_section

def new_user_student():
    root_new_user_student = Tk()
    root_new_user_student.title("Student Registration Portal")
    root_new_user_student.configure(background="cyan2")
    root_new_user_student.resizable(width=False,height=False )
    root_new_user_student.geometry("240x200+200+250")
    l.grid(row=1,column=4,columnspan=6)

    l_name_student = Label(root_new_user_student, text="Name",bg="cyan2")
    l_name_student.grid(row=0, sticky=W)

    e_name_student = Entry(root_new_user_student,bd=2)
    e_name_student.grid(row=0, column=1)

    l_reg_student = Label(root_new_user_student, text="Reg. No" ,bg="cyan2")
    l_reg_student.grid(row=1, sticky=W)

    e_reg_student = Entry(root_new_user_student,bd=2)
    e_reg_student.grid(row=1, column=1)

    l_special_student = Label(root_new_user_student, text="Specialization" ,bg="cyan2")
    l_special_student.grid(row=2, sticky=W)

    e_special_student = Entry(root_new_user_student,bd=2)
    e_special_student.grid(row=2, column=1)

    l_mobile_student = Label(root_new_user_student, text="Mobile No" ,bg="cyan2")
    l_mobile_student.grid(row=3, sticky=W)

    e_mobile_student = Entry(root_new_user_student,bd=2)
    e_mobile_student.grid(row=3, column=1)

    l_email_student = Label(root_new_user_student, text="Email" ,bg="cyan2")
    l_email_student.grid(row=4, sticky=W)

    e_email_student = Entry(root_new_user_student,bd=2)
    e_email_student.grid(row=4, column=1)

    l_password_student = Label(root_new_user_student, text="Password" ,bg="cyan2")
    l_password_student.grid(row=5, sticky=W)

    e_password_student = Entry(root_new_user_student,bd=2,show="#")
    e_password_student.grid(row=5, column=1)


    def student_register():
        #student credentials
        
        filename = e_name_student.get() + "_student.txt"
        file = open(filename, "w")
        file.write(
            e_name_student.get() + "\n" + e_reg_student.get() + "\n" + e_special_student.get() + "\n" + e_mobile_student.get() + "\n" + e_email_student.get())
        file.close()

        #stud password
        file_pass = open(e_name_student.get()+"_pass.txt", "w")
        file_pass.write(e_password_student.get())
        file_pass.close()
        

        file_1 = open("student_names.txt", "a")
        file_1.write(e_name_student.get()+"\n")
        file_1.close()
        messagebox.showinfo("SUCESS", "Congratulations! You've successfully registered")
        root_new_user_student.destroy()


    btn_register_student = Button(root_new_user_student, text="REGISTER",bd=4,bg="green3", command=student_register)
    btn_register_student.grid(row=6, column=0)

    btn_login_student = Button(root_new_user_student, text = 'LOGIN INSTEAD', bd=5,bg='orange1',command =login_page)
    btn_login_student.grid(row=6, column=1)

    btn_exit_student = Button(root_new_user_student, text = 'Exit', bd=5,bg='firebrick',command =root_new_user_student.destroy)
    btn_exit_student.grid(row=6, column=2)

    root_new_user_student.mainloop()



def request_for_supervisor():

    root_request_supervisor = Tk()

    l_name_supervisor = Label(root_request_supervisor, text="Name")
    l_name_supervisor.grid(row=0, sticky=W)

    e_name_supervisor = Entry(root_request_supervisor)
    e_name_supervisor.grid(row=0, column=1)

    l_UID_supervisor = Label(root_request_supervisor, text="UID")
    l_UID_supervisor.grid(row=1, sticky=W)

    e_UID_supervisor = Entry(root_request_supervisor)
    e_UID_supervisor.grid(row=1, column=1)

    l_special_supervisor = Label(root_request_supervisor, text="Specialization")
    l_special_supervisor.grid(row=2, sticky=W)

    e_special_supervisor = Entry(root_request_supervisor)
    e_special_supervisor.grid(row=2, column=1)

    l_mobile_supervisor = Label(root_request_supervisor, text="Mobile No")
    l_mobile_supervisor.grid(row=3, sticky=W)

    e_mobile_supervisor = Entry(root_request_supervisor)
    e_mobile_supervisor.grid(row=3, column=1)

    l_email_supervisor = Label(root_request_supervisor, text="Email")
    l_email_supervisor.grid(row=4, sticky=W)

    e_email_supervisor = Entry(root_request_supervisor)
    e_email_supervisor.grid(row=4, column=1)

    l_password_supervisor = Label(root_request_supervisor, text="Password")
    l_password_supervisor.grid(row=5, sticky=W)

    e_password_supervisor = Entry(root_request_supervisor,show="*")
    e_password_supervisor.grid(row=5, column=1)

                               

    def supervisor_register():
        filename = e_name_supervisor.get() + "_supervisor.txt"
        file = open(filename, "w")
        file.write(
            e_name_supervisor.get() + "\n" + e_UID_supervisor.get() + "\n" + e_special_supervisor.get() + "\n" + e_mobile_supervisor.get() + "\n" + e_email_supervisor.get() + "\n" + e_password_supervisor.get())
        file.close()
        messagebox.showinfo("REGISTER", "Supervisor details have successfully registered")

    btn_register_supervisor = Button(root_request_supervisor, text="REGISTER",bg="green3" ,command=supervisor_register)
    btn_register_supervisor.grid(row=6, column=1)

    root_request_supervisor.title("NEW USER SUPERVISOR")
    root_request_supervisor.mainloop()



def login_page():

    root_login_page = Tk()
    
    l_username_login = Label(root_login_page, text="User Name")
    l_username_login.grid(row=0, sticky=W)
   

    e_username_login = Entry(root_login_page)
    e_username_login.grid(row=0, column=1)

    l_password_login = Label(root_login_page, text="Password")
    l_password_login.grid(row=1, sticky=W)

    e_password_login = Entry(root_login_page,show="*")
    e_password_login.grid(row=1, column=1)

    
    def login_now():

        def student():
            root_student = Tk()
            def new_message():
                try:
                    n_file_name = e_username_login.get()+"_new_messages.txt"
                    file_new = open(n_file_name,"r")
                    noti = ""
                    for i in file_new.readlines():
                        noti=noti+i
                    file_new.close()
                    os.remove(e_username_login.get()+"_new_messages.txt")
                    file_messages = open(e_username_login.get()+"_messages.txt", "a")
                    file_messages.write(noti)
                    file_messages.close()

                    messagebox.showinfo("NOTIFICATIONS", noti)
                except:
                    messagebox.showinfo("NOTIFICATIONS", "There are no new messages")


            btn_noti = Button(root_student, text="New Message", command=new_message)
            btn_noti.grid(row=0)

            def old_messages():
                try:
                    file_old_message = open(e_username_login.get() + "_messages.txt", "r")
                    lines = ""
                    for i in file_old_message.readlines():
                        lines = lines + i

                    messagebox.showinfo("ALL MESAAGES", lines)
                except:
                    messagebox.showinfo("ALL MESSAGES", "There are no messages")

            btn_messages = Button(root_student, text="Messages", command=old_messages)
            btn_messages.grid(row=0, column=1)

            root_student.title("STUDENT")
            root_student.mainloop()


           # pass

        def supervisor():
            root_supervisor = Tk()
            e_student_search = Entry(root_supervisor)
            e_student_search.grid(row=0)

            def search():
                try:
                    f_name = e_student_search.get()+"_student.txt"
                    file_search = open(f_name,"r")
                    details = ""
                    for i in file_search.readlines():
                        details = details+i+"\n"

                    file_search.close()
                    messagebox.showinfo(e_student_search.get()+" Details", details)
                except:
                    messagebox.showinfo("ERRORR!!!!!!!!!!1", "404 NOT FOUND!\n"+"There is no student named "+e_student_search.get())

            btn_search = Button(root_supervisor, text="SEARCH", command=search)
            btn_search.grid(row=0, column=1)

            def show():
                file_show = open("student_names.txt", "r")
                show_name = ""
                for i in file_show.readlines():
                    show_name = show_name + i + "\n"
                file_show.close()

                messagebox.showinfo("STUDENTS NAMES", show_name)

            btn_show_students = Button(root_supervisor, text="Show Students", command=show)
            btn_show_students.grid(row=1)

            def select():
                root_select = Tk()

                l_student_name = Label(root_select, text="Enter student name: ")
                l_student_name.grid(row=0, sticky=W)

                e_student_name = Entry(root_select)
                e_student_name.grid(row=0, column=1)

                l_message = Label(root_select, text="Enter a message: ")
                l_message.grid(row=1, sticky=W)

                e_message = Entry(root_select)
                e_message.grid(row=1, column=1, ipadx=50, ipady=15)
                

                def send():
                    try:
                        check = open(e_student_name.get()+"_student.txt","r")
                        check.close()
                        file_send = open(e_student_name.get()+"_new_messages.txt","a")
                        file_send.write(time.ctime()+"\tFrom: "+e_username_login.get()+"\n\t"+e_message.get()+"\n")
                        file_send.close()
                        messagebox.showinfo("SUCCESSFUL", "Message successfully sent")
                    except:
                        messagebox.showinfo("ERRORRR!!!", "101 NOT ROUND \n"+"There is no student named "+e_student_name.get())


                btn_send = Button(root_select, text="SEND", command=send)
                btn_send.grid(row=2,column=1)

                root_select.title("SELECT STUDENT")
                root_select.mainloop()

            btn_select_student = Button(root_supervisor, text="Select Student",bd=4,bg="powder blue", command=select)
            btn_select_student.grid(row=1, column=1)

            root_supervisor.title("SUPERVISOR")
            root_supervisor.mainloop()

        filename_1 = e_username_login.get() + "_student.txt"
        filename_2 = e_username_login.get() + "_supervisor.txt"
        try:
            file = open(filename_1, "r")
            file.close()
            file_pass = open(e_username_login.get()+"_pass.txt", "r")
            passcode_1 = file_pass.readlines()[0]
            file_pass.close()
            if str(passcode_1) == str(e_password_login.get()):
                student()
            else:
                messagebox.showinfo("ACCESS DENIED", "Wrong password")
        except:
            try:
                file = open(filename_2, "r")
                passcode_2 = file.readlines()[5]
                if str(passcode_2) == str(e_password_login.get()):
                    supervisor()
                else:
                    messagebox.showinfo("ACCESS DENIED!!", "Invalid  Password")
            except:
                messagebox.showinfo("Invalid", "No record for %s" % e_username_login.get())

                

    btn_login_login = Button(root_login_page, text="LOGIN NOW",bd=4,bg="green3", command=login_now)
    btn_login_login.grid(row=2,column=0,rowspan=1)

    btn_new_user_login = Button(root_login_page, text="NEW USER",bd=4,bg="orange1", command=new_user_student)
    btn_new_user_login.grid(row=2, column=1)

    
    btn_new_user_exit = Button(root_login_page, text="EXIT",bd=4,bg="firebrick", command=root_login_page.destroy)
    btn_new_user_exit.grid(row=2,column=2)


    root_login_page.title("LOGIN PAGE")
    root_login_page.mainloop()

    


btn_login = Button(root, text="LOGIN",bd=4,bg="green3", command=login_page)
btn_login.grid(row=30,column=5)

btn_new_user = Button(root, text="NEW USER",bd=4,bg="orange1", command=new_user_student)
btn_new_user.grid(row=30,column=6)

btn_request = Button(root, text="REQUEST FOR SUPERVISOR",bd=4,bg="blue2", command=request_for_supervisor)
btn_request.grid(row=30,column=7)


btn_exit = Button(root, text="EXIT",bd=4,bg="firebrick", command=root.destroy)
btn_exit.grid(row=34,column=6)


root.mainloop()
