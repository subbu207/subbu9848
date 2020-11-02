from tkinter import *
import random
def generateRandomIndex(start, end):
    index = random.randint(start, end)
    return index

def second_window(reg_num):
    def log_out():
        root.destroy()
        loginWindow()
        
    root = Tk()
    root.title("Welcome User")

    database = {"11915882":"Harshwardhan", "11915019":"Kethireddy Rishikreddy", "11914873":"Yerra Subbaya Naidu", "54321":"Student2","default":"Student"}
    
    photo = PhotoImage(file = "images/lpu_logo.png")
    lbl = Label(root, image = photo)
    lbl.image = photo
    lbl.pack(padx="80", pady="20")

    L1 = Label(text="Welcome "+str(reg_num)+" to Lovely Professional University")
    L1.pack(padx="20", pady="10")

    name = ""
    if reg_num in database.keys():
        name = database[reg_num]
    else:
        name = database["default"]

    L2 = Label(text="Name: "+name)
    L2.pack(pady="20")

    B1 = Button(text="Logout", command=log_out,bg="blue")
    B1.pack(pady="40")
    
    root.mainloop()
    
    
def loginWindow():
    
    def validateLogin():
        captchaValues = ["nvhoxdm","plbhxzxl","phxxjdrk","yhykemwr","zagxtwdx","nrtgdkwn","dpbaiajz","lucytpft","czchjiav","wvvjcfua"]
        captcha_val = captchaValues[random_num-1]
        reg_num = E1.get()
        captcha_entered = E2.get()
        if len(reg_num)<4 or not reg_num.isnumeric():
            L5.config(text="Enter valid registration number")
        else:   
            if captcha_val==captcha_entered:
                L5.config(text="Correct Captcha. You are logged in")
                top.destroy()
                second_window(reg_num)
            else:
                L5.config(text="Incorrect captcha. Please try again.")
        
    top = Tk()
    top.title("Student record")
    
    #L1 = Label(top,text="---- Captcha Generator ----",font = ( "bold" , 22 , ), fg="blue")
    #L1.grid(row=0, column=0, rowspan=2, columnspan=5)

    L2 = Label(top, text="Reg. No.")
    L2.grid(row=3, column=3, padx="20", pady="20")
    
    E1 = Entry(top, bd=1)
    E1.grid(row=3, column=4,padx="20", pady="20", ipadx="10", ipady="3")

    random_num = generateRandomIndex(1,10)

    photo = PhotoImage(file = "images/captcha"+str(random_num)+".PNG")
    lbl = Label(top, image = photo)
    lbl.image = photo
    lbl.grid(row=5, column=2,columnspan=3, rowspan=2, padx="50", pady="12")

    L3 = Label(top, text = "Type the code you see above")
    L3.grid(row=7, column=2, columnspan=5, pady="10")

    E2 = Entry(top, bd=1)
    E2.grid(row=8, column=2, ipady="6", columnspan=4, pady="8")

    B1 = Button(top, text="Submit", command=validateLogin, bg="blue", fg="white")
    B1.grid(row=9, column=2, columnspan=2, padx="10", pady="20")

    L4 = Label(top, text="Back to login page", fg="blue")
    L4.grid(row=9, column=4, columnspan=3)

    L5 = Label(top, text="")
    L5.grid(row=10, column=2, columnspan=4, pady="10")
    
    top.mainloop()

if __name__=="__main__":
    loginWindow()
    

