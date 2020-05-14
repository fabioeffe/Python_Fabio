import tkinter as tkt 


def button():
    button1.config(text="Saving then!", fg='green') # with config you can change properties of the button
    save_data = True
    return save_data

def name_submit():
    print('Your name is {}'.format(e1.get()))

# create the window
root = tkt.Tk()
root.title("OCT shell")
root.iconbitmap('OCT_AGI_icon.ico')

photo= tkt.PhotoImage(file='wave.jpg')
w = tkt.Label(root,image=photo)
w.pack()

# # add a button
# button1 = tkt.Button(root, text = 'Log data?', command = button,padx=200, pady=100, bg = 'red', fg = 'blue')
# button1.pack(side=tkt.BOTTOM)

label1= tkt.Label(text='What is your name?',fg='blue')
e1 = tkt.Entry(root)
button1 = tkt.Button(text='Submit!',command=name_submit, fg='Blue')
label1.pack()
e1.pack()
button1.pack()

# frame1 = tkt.Frame(root)
# frame2 = tkt.Frame(root)

# label1 = tkt.Label(frame1, text='I am in frame one')
# button1 = tkt.Button(frame1, text='Button in frame 1')


# label2 = tkt.Label(frame2, text='I am in frame two')
# button2 = tkt.Button(frame2, text='Button in frame 2')

# label1.pack()
# label2.pack()
# button1.pack()
# button2.pack()
# frame1.pack(side=tkt.LEFT)
# frame2.pack(side=tkt.RIGHT)














root.mainloop() # this has to be at the bottom of the code
