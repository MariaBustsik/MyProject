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
    screen3=Toplevel(screen, bg="pink")
    screen3.title("Авторизация")
    screen3.geometry("350x100")
    Label(screen3, bg="pink", fg="red", text="Авторизация удалась!").pack()
    Label(screen3, bg="pink", text= "").pack()
    Button(screen3, fg="purple", bg="light blue", text="OK", command=delete2).pack()

def password_not_recognized():
    global screen4
    screen4=Toplevel(screen, bg="pink")
    screen4.title("Ошибка авторизации!")
    screen4.geometry("350x100")
    Label(screen4, bg="pink", fg="red", text="Неверный пароль!").pack()
    Label(screen4, bg="pink", text= "").pack()
    Button(screen4, text="OK", fg="purple", bg="light blue", command=delete3).pack()
def user_not_found():
    global screen5
    screen5=Toplevel(screen, bg="pink")
    screen5.title("Ошибка авторизации!")
    screen5.geometry("350x100")
    Label(screen5, bg="pink", text="Пользователь не зарегистрирован!", fg="red",font=("Helvetica",11)).pack()
    Label(screen5, bg="pink", text= "").pack()
    Button(screen5, text="OK", fg="purple", bg="light blue",  command=delete4).pack()


 

def register_user():
    if not username.get() or not screen1.pass_str.get():
        Label(screen1, bg="pink", text="Заполните необходимые поля!", fg="red",font=("Helvetica",11)).pack()
    else:
        username_info=username.get()
        password_info=screen1.pass_str.get()

        file=open(username_info,"w")
        file.write(username_info+"\n")
        file.write(password_info)
        file.close()

        username_entry.delete(0,END)
        password_entry.delete(0, END)

        
        Label(screen1, text="Регистрация удалась!", bg="pink", fg="purple",font=("calibri",11)).pack()

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
    screen1=Toplevel(screen, bg="pink")
    screen1.title("Регистрация")
    screen1.geometry("300x250")
    
    global username
    global password
    global username_entry
    global password_entry
    
    screen1.pass_str = StringVar()
    username=StringVar()
    password=StringVar()

    Label(screen1, bg="light blue", text= "Введите необходимые данные").pack()
    Label(screen1, bg="pink", text= "").pack()
    Label(screen1, bg="light blue", text= "Логин *").pack()
    #global username_entry
    #global password_entry
    username_entry=Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, bg="light blue", text= "Пароль *").pack()
    password_entry=Entry(screen1, textvariable=screen1.pass_str)
    password_entry.pack()
    Label(screen1, bg="pink", text= "").pack()
    Button(screen1,bg="light blue", text="Создать пароль автоматически", width=25, height=1, command=generator).pack()
    Label(screen1, bg="pink", text= "").pack()
    Button(screen1, bg="light blue", text="Зарегистрироваться", width=25, height=1, command=register_user).pack()
    
def generator():
    
    password = ''
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    # Извлекаем из списка 12 произвольных значений
    password = ''.join([random.choice(ls) for x in range(12)])

    screen1.pass_str.set(password)

        

def login():
    global screen2
    screen2=Toplevel(screen, bg="pink")
    screen2.title("Авторизация")
    screen2.geometry("300x250")

    Label(screen2, bg="light blue", text= "Заполните поля ниже для авторизации").pack()
    Label(screen2, bg="pink", text= "").pack()

    global username_verify
    global password_verify

    username_verify=StringVar()
    password_verify=StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, bg="light blue", text= "Логин *").pack()
    username_entry1=Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, bg="pink", text="").pack()
    Label(screen2, bg="light blue", text= "Пароль *").pack()
    password_entry1=Entry(screen2, show="*", textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, bg="pink", text="").pack()
    Button(screen2, bg="light blue", text="Авторизация", width=10,height=1, command=login_verify).pack()

def main_screen():
    global screen
    screen=Tk()
    screen.geometry("400x600")
    img=PhotoImage(file="Spongebob.png").subsample(5)
    my_label=Label(screen, bg="light pink", image=img)
    my_label.place(relwidth=1,relheight=1)
    screen.title("Зачётное задание")
    Label(text="Система авторизации и регистрации 2.0", bg="light blue", fg="purple", width="300", height="2", font=("Impact", 15, "bold")).pack()
    Label(bg="light pink", text= "").pack()
    Button (text="Авторизация", height="2", width="30", font=("Helvetica"), fg="black", bg="light blue", command=login).pack()
    Label(bg="light pink", text="").pack()
    Button(text="Регистрация", height="2", width="30", font=("Helvetica"), fg="black", bg="light blue", command=register).pack()
    

    screen.mainloop()
main_screen()
