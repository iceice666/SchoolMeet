

from main import MEET_driver
import multiprocessing as mp

import tkinter as tk


class MEET_Gui():
    class _Func():
        class _func():
            def start(self):
                self.m=MEET_driver()
                self.m.get_into_meet()
            def stop(self):
                self.m.quit_meet()
                self.m.close_driver()

        f = _func()
        def start(self):
            self.Process_MeetDriver=mp.Process(target=self.f.start)
            self.Process_MeetDriver.daemon=True
            self.Process_MeetDriver.start()

        def stop(self):
            Process_MeetDriverKiller=mp.Process(target=self.f.stop)
            Process_MeetDriverKiller.daemon=True
            Process_MeetDriverKiller.start()
            Process_MeetDriverKiller.join(60)

            if self.Process_MeetDriver.is_alive():
                self.Process_MeetDriver.kill()
                Process_MeetDriverKiller.kill()



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
    Btn_start.pack(side="left")

    Btn_stop = tk.Button(funcBtn, text="Stop", font=(
        "Microsoft JhengHei", 20), command=BtnFunc.stop)
    Btn_stop.pack(side="left")

    root.mainloop()
