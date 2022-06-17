from tkinter import *
from tkinter import ttk
import page3


class Page4:
    def __init__(self, window):
        self.window = window
        self. window.title("ADMINISTRATOR SYSTEM")
        self.window.geometry('1366x768')
        self.window.resizable(0, 0)
        self.window.state('zoomed')

        page2_Back_btn = ttk.Button(
            self.window, text='Back', command=self.admin_page)
        page2_Back_btn.place(x=1200, y=700, height=25, width=100)

    def admin_page(self):
        win = Toplevel()
        page3.Page3(win)
        self.window.withdraw()
        win.deiconify()


def page():
    window = Tk()
    Page4(window)
    window.mainloop()


if __name__ == "__main__":
    page()
