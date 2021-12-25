#GOODPASSWORD
#Filip Rokita
#www.filiprokita.com

#import
import tkinter as tk
import string
import random
from tkinter import messagebox

#def
def work():
    length = lengthVar.get()

    if length < 4:
        messagebox.showerror(title='GOODPASSWORD', message='Password cannot be shorter than 4 characters! Try again.')
    else:
        while True:
            initial_password = generate_password(length)
            if check_password(initial_password) == 1:
                password = initial_password
                break
        displaypass(password)


def generate_password(password_length):
    characters = string.digits + string.ascii_lowercase + string.ascii_uppercase + special
    result = "".join(random.choice(characters) for i in range(password_length))
    return result


def check_password(input_password):
    has_digits = 0
    has_ascii_lowercase = 0
    has_ascii_uppercase = 0
    has_special = 0

    for i in range (len(input_password)):
        for j in range(len(string.digits)):
            if input_password[i] == string.digits[j]: has_digits = 1
        for j in range(len(string.ascii_lowercase)):
            if input_password[i] == string.ascii_lowercase[j]: has_ascii_lowercase = 1
        for j in range(len(string.ascii_uppercase)):
            if input_password[i] == string.ascii_uppercase[j]: has_ascii_uppercase = 1
        for j in range(len(special)):
            if input_password[i] == special[j]: has_special = 1
    score = has_digits + has_ascii_lowercase + has_ascii_uppercase + has_special

    if score == 4:
        return 1
    else:
        return 0


def displaypass(password_to_display):
    dp = tk.Tk()
    dp.title('GOODPASSWORD')
    dp.geometry('300x100')
    dp.resizable(False, False)
    
    passwordL = tk.Label(dp, text=f'Your new password is:\n\n{password_to_display}'); passwordL.pack()
    copyB = tk.Button(dp, text='Copy to clipboard', command=copy(password_to_display)); copyB.pack(pady=10)

    dp.mainloop()


def copy(text_to_copy):
    cp = tk.Tk()
    cp.clipboard_clear()
    cp.clipboard_append(text_to_copy)
    cp.destroy()



#main
root = tk.Tk()
root.title('GOODPASSWORD')
root.geometry('300x120')
root.resizable(False, False)
    
special = "!@#$%^&*()-_=+"
lengthVar = tk.IntVar()

lengthL = tk.Label(root, text='LENGTH'); lengthL.pack()
lengthE = tk.Entry(root, textvariable=lengthVar, justify=tk.CENTER); lengthE.pack()
generateB = tk.Button(root, text='GENERATE', command=work); generateB.pack(pady=10)
authorL = tk.Label(root, text='www.filiprokita.com'); authorL.pack()

root.mainloop()