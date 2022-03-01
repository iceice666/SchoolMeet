

from main import MEET_driver

import tkinter as tk


class MEET_Gui():
    class _Func():
        def start(self):
            self.m=MEET_driver()
            self.m.get_into_meet()



    BtnFunc=_Func()

    MEET_States = "Offline"

    root = tk.Tk()
    root.title("SchoolMeet")

    # ^ States
    states = tk.Frame(root)
    states.pack()

    Label_MEET_States = tk.Label(
        states, text=MEET_States, font=("Microsoft JhengHei", 20))
    Label_MEET_States.pack()

    # ^ Profile
    profile = tk.Frame(root)
    profile.pack()

    Var_Email = tk.StringVar()
    Var_Pwd = tk.StringVar()

    Label_userEmail = tk.Label(profile, text="Email",
                               font=("Microsoft JhengHei", 20))
    Label_userEmail.grid(row=0, column=0)

    Entry_userEmail = tk.Entry(
        profile, width=25, textvariable=Var_Email, font=("Microsoft JhengHei", 20))
    Entry_userEmail.grid(row=0, column=1)

    Label_userPwd = tk.Label(profile, text="Password",
                             font=("Microsoft JhengHei", 20))
    Label_userPwd.grid(row=1, column=0)

    Entry_userPwd = tk.Entry(profile, show="*", width=25,
                             textvariable=Var_Pwd, font=("Microsoft JhengHei", 20))
    Entry_userPwd.grid(row=1, column=1)

    # ^ Functions' button

    funcBtn = tk.Frame(root)
    funcBtn.pack()


    Btn_start = tk.Button(funcBtn, text="Start",
                          font=("Microsoft JhengHei", 20),command= BtnFunc.start)
    Btn_start.pack()

    root.mainloop()

