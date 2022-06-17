from tkinter import *
from tkinter import ttk
import page2
import page4


class Page3:
    def __init__(self, window):
        self.window = window
        self. window.title("REPORT AND LOG")
        self.window.geometry('1366x768')
        self.window.resizable(0, 0)
        self.window.state('zoomed')

        page2_Next_btn = ttk.Button(
            self.window, text='Next', command=self.admin_page)
        page2_Next_btn.place(x=1200, y=700, height=25, width=100)

        page2_Back_btn = ttk.Button(
            self.window, text='Back', command=self.second_page)
        page2_Back_btn.place(x=20, y=700, height=25, width=100)

    def second_page(self):
        win = Toplevel()
        page2.Page2(win)
        self.window.withdraw()
        win.deiconify()

    def admin_page(self):
        win = Toplevel()
        page4.Page4(win)
        self.window.withdraw()
        win.deiconify()


def page():
    window = Tk()
    Page3(window)
    window.mainloop()


if __name__ == "__main__":
    page()
