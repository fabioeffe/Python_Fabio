import tkinter as tkt 
import os

# put all the functions here
def user_save_OCT_data(event):
    global save_data
    save_data = True
    save_button.config(text='Clicked!', fg='Black')
    save_display.config(text="Saving? "+ str(save_data), fg='Green') # maybe we could add how many frames are being saved here

save_data =  False

root = tkt.Tk()   #initialize the window
root.title("AGI OCT shell") 
root.iconbitmap("OCT_AGI_icon.ico") #insert the icon (form over function!)
root.geometry("1000x700") # define the window size

# Save button procedure
save_button = tkt.Button(root,text="Save data?", fg='Blue') # create the button
save_button.bind('<Button-1>',user_save_OCT_data) # link action to the button

save_display = tkt.Label(text="Saving? "+ str(save_data),fg='Blue')
save_display.bind('<Button-1>',user_save_OCT_data) # link action to the button


save_button.grid(row=0,column=0)
save_display.grid(row=0,column=1)



root.mainloop()     # this keeps the window active, it has tp be the last line!




