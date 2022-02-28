
"""
from main import MEET_driver

m=MEET_driver()
m.get_into_meet()
input()
m.quit_meet()
"""
import tkinter as tk


MEET_States="Offline"

root=tk.Tk()
root.title("WELCOME")


#^States
states=tk.Frame(root)
states.pack()

Label_MEET_States = tk.Label(
    states, text=MEET_States, font=("Microsoft JhengHei", 20))
Label_MEET_States.pack()

#^ Profile
profile=tk.Frame(root)
profile.pack()

Var_Email=tk.StringVar()
Var_Pwd=tk.StringVar()

Label_userEmail=tk.Label(profile,text="Email",font=("Microsoft JhengHei", 20))
Label_userEmail.grid(row=0,column=0)

Entry_userEmail = tk.Entry(
    profile, width=25, textvariable=Var_Email, font=("Microsoft JhengHei", 20))
Entry_userEmail.grid(row=0, column=1)

Label_userPwd = tk.Label(profile, text="Password",font=("Microsoft JhengHei", 20))
Label_userPwd.grid(row=1, column=0)

Entry_userPwd = tk.Entry(profile, show="*", width=25,
                         textvariable=Var_Pwd, font=("Microsoft JhengHei", 20))
Entry_userPwd.grid(row=1, column=1)


root.mainloop()