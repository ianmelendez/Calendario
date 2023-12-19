from tkinter import *
import calendar

def showCalender():
    gui = Tk()
    gui.config(background='white')
    gui.title("Calendario")
    gui.geometry("600x600")
    year = int(year_field.get())
    gui_content= calendar.calendar(year)
    calend_total = Label(gui, text= gui_content, font= "Consolas 10 bold")
    calend_total.grid(row=5, column=1,padx=20)
    gui.mainloop()

if __name__=='__main__':
    new = Tk()
    new.config(background='grey')
    new.title("Calendario")
    new.geometry("250x140")
    cal = Label(new, text="Calendario",bg='white',font=("times", 28, "bold"))
    year = Label(new, text="Introduce un año", bg='dark grey')
    year_field=Entry(new)
    button = Button(new, text='Muestra Calendario',
fg='Black',bg='Blue',command=showCalender)
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    new.mainloop()
    
