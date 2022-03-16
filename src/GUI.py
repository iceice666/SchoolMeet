

from main import MEET_driver
import multiprocessing as mp

import tkinter as tk

from selenium.common.exceptions import WebDriverException
import sys

class MEET_Gui():
    class _Func():
        class _func():
            m = MEET_driver()

            def start(self, email, password):
                self.m.get_into_meet(email, password)

            def stop(self):
                if self.m.fetch_state() == self.m.INACTIVE:
                    return
                self.m.quit_meet()
                self.m.close_driver()

            def exit(self):
                try:
                    self.m.close_driver()
                except WebDriverException:
                    pass

                sys.exit(0)

        f = _func()

        def start(self):
            try:
                if self.Process_MeetDriver.is_alive:
                    return
            except AttributeError:
                pass

            self.Process_MeetDriver = mp.Process(target=self.f.start, args=(
                MEET_Gui.Var_Email.get(), MEET_Gui.Var_Pwd.get()))
            self.Process_MeetDriver.daemon = True
            self.Process_MeetDriver.start()

        def stop(self):
            try:
                if self.Process_MeetDriverKiller.is_alive:
                    return
            except AttributeError:
                pass

            self.Process_MeetDriverKiller = mp.Process(target=self.f.stop)
            self.Process_MeetDriverKiller.daemon = True
            self.Process_MeetDriverKiller.start()
            self.Process_MeetDriverKiller.join(60)

        def exit(self):
            pe = mp.Process(target=self.f.exit)
            pe.start()
            pe.join()

    BtnFunc = _Func()

    root = tk.Tk()
    root.title("SchoolMeet")

    # ^ States
    states = tk.Frame(root)
    states.pack()


    Label_MEET_States = tk.Label(
        states, font=("Microsoft JhengHei", 20))
    Label_MEET_States.pack()

    # ^ Profile
    profile = tk.Frame(root)
    profile.pack()

    Var_Email = tk.StringVar(value="@kmhjh.kh.edu.tw")
    Var_Pwd = tk.StringVar(value="12345678")

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

    Btn_start = tk.Button(funcBtn, text="Start", font=(
        "Microsoft JhengHei", 20), command=BtnFunc.start)
    Btn_start.pack(side="left")

    Btn_stop = tk.Button(funcBtn, text="Stop", font=(
        "Microsoft JhengHei", 20), command=BtnFunc.stop)
    Btn_stop.pack(side="left")

    Btn_exit = tk.Button(funcBtn, text="Exit", font=(
        "Microsoft JhengHei", 20), command=BtnFunc.exit)
    Btn_exit.pack(side="left")

    def __init__(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    r = MEET_Gui()
