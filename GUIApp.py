from tkinter import *
import tkinter.messagebox


def calculate():
    length = int(entry1.get())
    width = int(entry2.get())
    price_per_sqr = int(entryPerSqr.get())
    area = length * width
    price = area * price_per_sqr
    unit = v.get()
    if unit == 0:
        answer_label['text'] = 'The total amount for the customer to pay is ${} for {}ft^2'.format(price, area)
    elif unit == 1:
        dis_value = int(entryDis.get())
        discount_amount = price * dis_value / 100
        final_dis_amount = price - discount_amount
        answer_label['text'] = 'The discounted amount is ${}\n' \
                               'The total amount for the customer to pay is ${} for {}ft^2' \
            .format(discount_amount, final_dis_amount, area)


def enable():
    global labelDis
    global entryDis
    labelDis.config(state='normal')
    entryDis.config(state='normal')


def disable():
    global labelDis
    global entryDis
    labelDis.config(state='disabled')
    entryDis.config(state='disabled')


def about():
    tkinter.messagebox.showinfo("About", "This is square feet calculator app\nMade by Njteh Keledjian")


root = Tk()

menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu)

menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Exit", command=quit)

helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About", command=about)

label1 = Label(root, text="Enter room length(ft):")
label2 = Label(root, text="Enter room width(ft):")

entry1 = Entry(root)
entry2 = Entry(root)

label1.grid(row=0, column=0, padx=(75, 0))
label2.grid(row=1, column=0, padx=(75, 0))

entry1.grid(row=0, column=1, padx=(0, 75))
entry2.grid(row=1, column=1, padx=(0, 75))

perSqr = Label(root, text="Enter price per square feet($):")
entryPerSqr = Entry(root)

perSqr.grid(row=2, column=0, padx=(75, 0))
entryPerSqr.grid(row=2, column=1, padx=(0, 75))

v = IntVar()
radioDis = Radiobutton(root, text="With Discount", padx=20, value=1, variable=v, command=enable)
radioNoDis = Radiobutton(root, text="No Discount", padx=20, value=0, variable=v, command=disable)

radioDis.grid(row=3, column=0, padx=(75, 0))
radioNoDis.grid(row=3, column=1, padx=(0, 75))

labelDis = Label(root, text="Enter discount amount in %", state='disabled')
entryDis = Entry(root, state='disabled')
labelDis.grid(row=4, column=0, padx=(75, 0))
entryDis.grid(row=4, column=1, padx=(0, 75))

calc_button = Button(text='Calculate', command=calculate)
calc_button.grid(row=5, column=0, columnspan=4)

answer_frame = LabelFrame(text='Result', height=100)
answer_frame.grid(row=6, column=0, columnspan=4, sticky='nesw')

answer_label = Label(answer_frame, text='')
answer_label.grid(row=0, column=0)

root.mainloop()
