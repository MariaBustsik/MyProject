from tkinter import *
from tkinter import messagebox
import os
import random, string



    

def delete2():
    screen.destroy()

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

def login_sucess():
    global screen3
    screen3=Toplevel(screen)
    screen3.title("Авторизация")
    screen3.geometry("150x100")
    Label(screen3, text="Авторизация удалась!").pack()
    Button(screen3, text="OK", command=delete2).pack()

def password_not_recognized():
    global screen4
    screen4=Toplevel(screen)
    screen4.title("Ошибка авторизации!")
    screen4.geometry("150x100")
    Label(screen4, text="Неверный пароль!").pack()
    Button(screen4, text="OK", command=delete3).pack()
def user_not_found():
    global screen5
    screen5=Toplevel(screen)
    screen5.title("Ошибка авторизации!")
    screen5.geometry("350x50")
    Label(screen5, text="Пользователь не зарегистрирован!").pack()
    Button(screen5, text="OK", command=delete4).pack()



def Generator():
    global screen6
    screen6=Toplevel(screen)
    screen6.title("Генератор пароля 2.0")
    screen6.geometry("500x100")
    Label(screen6, text = "Скопируйте полученный пароль:" , font ='arial 15 bold').pack()
    
 
    pass_len = IntVar()
    length = Spinbox(screen6, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).pack()
    pass_str = StringVar()
    password = ''

    for x in range (0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)
    Entry(screen6 , textvariable = pass_str).pack()    
  
 

def register_user():
    if not username.get() or not password.get():
        Label(screen1, text="Заполните необходимые поля!", fg="green",font=("calibri",11)).pack()
    else:
        username_info=username.get()
        password_info=password.get()

        file=open(username_info,"w")
        file.write(username_info+"\n")
        file.write(password_info)
        file.close()

        username_entry.delete(0,END)
        password_entry.delete(0, END)


        Label(screen1, text="Регистрация удалась!", fg="green",font=("calibri",11)).pack()

def login_verify():
    username1=username_verify.get()
    password1=password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)


    list_of_files=os.listdir()
    if username1 in list_of_files:
        file1=open(username1, "r")
        verify=file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            password_not_recognized()
    else:
        user_not_found()



def register():
    global screen1
    screen1=Toplevel(screen)
    screen1.title("Регистрация")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry

    username=StringVar()
    password=StringVar()

    Label(screen1, text= "Введите необходимые данные").pack()
    Label(screen1, text= "").pack()
    Label(screen1, text= "Логин *").pack()
    global username_entry
    global password_entry
    username_entry=Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text= "Пароль *").pack()
    password_entry=Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text= "").pack()
    Button(screen1,text="Создать пароль автоматически", width=25, height=1, command=Generator).pack()
    Label(screen1, text= "").pack()
    Button(screen1,text="Зарегистрироваться", width=25, height=1, command=register_user).pack()
    
    

def login():
    global screen2
    screen2=Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")

    Label(screen2, text= "Заполните поля ниже для авторизации").pack()
    Label(screen2, text= "").pack()

    global username_verify
    global password_verify

    username_verify=StringVar()
    password_verify=StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text= "Логин *").pack()
    username_entry1=Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2,text="").pack()
    Label(screen2, text= "Пароль *").pack()
    password_entry1=Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2,text="").pack()
    Button(screen2, text="Авторизация", width=10,height=1, command=login_verify).pack()

def main_screen():
    global screen
    screen=Tk()
    screen.geometry("400x600")
    img=PhotoImage(file="Spongebob.png").subsample(5)
    my_label=Label(screen,image=img)
    my_label.place(relwidth=1,relheight=1)
    screen.title("Зачётное задание")
    Label(text="Система авторизации и регистрации 2.0", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text= "").pack()
    Button (text="Авторизация", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Регистрация", height="2", width="30", command=register).pack()
    

    screen.mainloop()
main_screen()
