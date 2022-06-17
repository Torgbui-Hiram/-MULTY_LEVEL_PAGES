from tkinter import *
from tkinter import ttk
import page1
import page3


class Page2:
    def __init__(self, window):
        self.window = window
        self. window.title("MANAGEMENT RECORD SYSTEM")
        self.window.geometry('1366x768')
        self.window.resizable(0, 0)
        self.window.state('zoomed')

        page2_Next_btn = ttk.Button(
            self.window, text='Next', command=self.next_page)
        page2_Next_btn.place(x=1200, y=700, height=25, width=100)

        page2_Back_btn = ttk.Button(
            self.window, text='Logout', command=self.first_page)
        page2_Back_btn.place(x=20, y=700, height=25, width=100)

    def first_page(self):
        win = Toplevel()
        page1.Page1(win)
        self.window.withdraw()
        win.deiconify()

    def next_page(self):
        win = Toplevel()
        page3.Page3(win)
        self.window.withdraw()
        win.deiconify()


def page():
    window = Tk()
    Page2(window)
    window.mainloop()


if __name__ == "__main__":
    page()
