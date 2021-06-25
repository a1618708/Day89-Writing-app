from tkinter import *
from tkinter import messagebox



timer = None
FONT = None
TIMELABELCOLOR = "#053742"


class WritingApp():
    def __init__(self):
        self.window = Tk()
        self.window.title("Dangerous Writing App")
        self.window.minsize(width=580, height=250)
        self.window.config(padx=0, pady=0)
        #add background image #
        self.background_image = PhotoImage(file="logo.png")
        self.background_label = Label(image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.count = 5
        self.compare2 = None
        self.show_time()
        self.text_area()





    def show_time(self):
        self.show_timeL = Label(text=f"Left {self.count} secs to delete your work", font=(FONT, 14, "bold"), fg=TIMELABELCOLOR )
        self.show_timeL.grid(row=0, column=1, sticky="e")


    def text_area(self):
        self.text = Text(width=85, height=20)
        self.text.insert(END, "Write down your work")
        self.text.grid(row=1, column=0, columnspan=2)
        self.text.bind("<Button-1>", self.delete_placeholder)


    def delete_placeholder(self, e):
        self.text.delete(1.0, END)
        self.compare1 = ""
        self.countdown()


    def countdown(self):
        global timer
        if self.count > 0:
            timer = self.window.after(1000, self.countdown,)
            self.compare2 = self.text.get(1.0, "end")

            if self.compare1 == self.compare2:
                self.count -= 1
                self.show_timeL.config(text=f"Left {self.count} secs to delete your work")
            else:
                self.compare1 = self.compare2
                self.count = 5
                self.show_timeL.config(text=f"Left {self.count} secs to delete your work")
        else:

            self.window.after_cancel(timer)
            self.reset()


    def reset(self):
        self.text.delete(1.0, END)
        messagebox.showinfo("Work Deleted", "Just let me reset all")
        self.window.destroy()
        self.__init__()


if __name__ == "__main__":
    app = WritingApp()
    app.window.mainloop()
