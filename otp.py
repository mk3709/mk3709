from twilio.rest import Client
import random
from tkinter import *
from tkinter import messagebox
class otp_verifier(Tk):
    def _intit_(self):
        super().__init__()
        self.geometry("600x500")
        self.resizable(False,False)
        self.n=random.randit(1000,9999)
        self.client=Client("","")
        self.client.messages.create(to =[""],from_="",body=self.n)

    def labels(self):
        self.c=Canvas(self,bg="white",width=400,height=200)
        self.c.place(x=100,y=60)
        self.login_title=Label(self,text='OTP Verification',font="bold ,20 ",bg="white")
        self.login_title.place(x=210,y=90)
    def Entry(self):

        self.user_name=Text(self,borderwidth=2,highlighththickness=0,wrap='word',width=29,height=2)
        self.user_name.place(x=190,y=60)
    def Buttons(self):
        self.submitButtonImage=PhotoImage(file="submit.png")        
        self.submitButton=PhotoImage(self,image=self.submitButtonImage,comman=self.checkOTP,border=0)        
        self.submitButton.place(x=208,y=400)        
        
        self.resendOTPImage=PhotoImage(file="resendotp.png")
        self.resendOTP=Button(self,image=self.resendOTPImage,comman=self.checkOTP,border=0)        
        self.resendOTP.place(x=208,y=400)
    
    
    def checkOTP(self):
        try:
            self.userInput=int(self.User_Name.get(1.0,"end-1c")) 
            if self.userInput==self.n:
               messagebox.showinfo("showinfo","loginsuccess")
               self.n="done"
            elif self.n=="done":
                messagebox.showinfo("showinfo","already entered otp")
            else:
                messagebox.showinfo("showinfo","Invalid OTP")
        except:
                messagebox.showinfo("showinfo","Invalid OTP")

    def resendOTP(self):
            self.n=random.randit(1000,9999)
            self.client=Client("","")
            self.client.message.create(to=[""],from_="",body=self.n)





if __name__=="_main_":
    window=otp_verifier()
    window.Labels()
    window.Entry()
    window.Buttons()
    window.mainloop()






