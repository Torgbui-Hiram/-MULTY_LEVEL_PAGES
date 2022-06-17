from tkinter import *
from tkinter import ttk
import page2


class Page1:
    def __init__(self, window):
        self.window = window
        self. window.title("CREATING USER AND ACCESS CONTROL SYSTEM")
        self.window.geometry('1366x768')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        # =========== Login Frame==============
        Frame_login = Label(self.window)
        Frame_login.place(x=450, y=150, width=500, height=400)

        # Title & Subtitle
        title = Label(Frame_login, text="Login Here", font=(
            "Impact", 35, "bold"), fg="#6162FF").place(x=90, y=30)
        subtitle = Label(Frame_login, text="Member Login Area", font=(
            "Gougy old style", 15, "bold"), fg="#1d1d1d").place(x=90, y=100)

        # Username
        lbl_user = Label(Frame_login, text="Username", font=(
            "Gougy old style", 15, "bold"), fg="grey").place(x=90, y=140)
        username = Entry(Frame_login, font=(
            "Gougy old style", 15), bg="#E7E6E6")
        username.place(x=90, y=170, width=320, height=35)

        # User_password
        lbl_password = Label(Frame_login, text="Password", font=(
            "Gougy old style", 15, "bold"), fg="grey").place(x=90, y=210)
        password = Entry(Frame_login, font=(
            "Gougy old style", 15), bg="#E7E6E6", show='•')
        password.place(x=90, y=240, width=320, height=35)
        forget = Button(Frame_login, text=" forget password?", font=(
            "Gougy old style", 12), bd=0, cursor="hand2", fg="#6162FF").place(x=90, y=280)

        Submit = ttk.Button(Frame_login, text="Login", command=self.show_page,
                            cursor="hand2").place(x=90, y=320, width=180, height=40)

    def show_page(self):
        win = Toplevel()
        page2.Page2(win)
        self.window.withdraw()
        win.deiconify()


def page():
    window = Tk()
    Page1(window)
    window.mainloop()


if __name__ == "__main__":
    page()
