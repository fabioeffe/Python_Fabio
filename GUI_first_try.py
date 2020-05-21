import tkinter as tkt 
import os
print (os.getcwd())

def button(event):
    button1.config(text="Saving then!", fg='green') # with config you can change properties of the button
    save_data = True
    return save_data

def name_submit(event): # if using the method .bind then you need to put 'event'
    print('Your name is {}'.format(e1.get()))

def foo(event):
    print('Working just fine!')

def click_counter():
    global counter
    counter+=1
    button_counter.config(text=counter)


counter = 0    
# create the window
root = tkt.Tk()
root.title("OCT shell")
root.iconbitmap("OCT_AGI_icon.ico") #insert the icon (not really useful)
root.geometry("1000x700") # define teh window size

photo= tkt.PhotoImage(file = "wave_move.gif")
w = tkt.Label(root,image=photo)
# w.grid(row=1,column=0)

# # add a button
# button1 = tkt.Button(root, text = 'Log data?', command = button,padx=200, pady=100, bg = 'red', fg = 'blue')
# button1.pack(side=tkt.BOTTOM)

label1= tkt.Label(text='What is your name?',fg='blue')
e1 = tkt.Entry(root)
button1 = tkt.Button(text='Submit!', fg='Blue')
button1.bind('<Button-1>',name_submit)
# button1.bind('<Button-1>',button)
# root.bind('<Return>',foo)

button2=tkt.Button(root,text='Click me!',command=click_counter)
button_counter= tkt.Label(root, text=counter)

label1.grid(row=0,column=0, sticky=tkt.E)
e1.grid(row=0,column=1)
button1.grid(row=0,column=2,pady=100)

button2.grid(row=1,column=0)
button_counter.grid(row=1,column=1,pady=100)
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
