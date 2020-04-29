from tkinter import *
from tkinter import  messagebox
import sys
sys.path.append("C:/Users/surde/OneDrive/Desktop/Indian Railway Announcement Project/FinalProject/")
from pythonFiles import goingToMainPage
from pythonFiles import announcement

def deleteAll(root):
    list=root.pack_slaves()
    for l in list:
        l.pack_forget()
        
def backButtonClicked(root):
    goingToMainPage.main(root)

def createAnnouncement(SelectedLang,platformNumber):
    if len(platformNumber)==0:
        result=messagebox.showerror("Error!!!", "Please Enter The Platform Number Through Which The Train Will Pass")
    else:
        inputBox.delete(0,END)
        announcement.main(SelectedLang,platformNumber,1)
        
def main(root,SelectedLang):
    deleteAll(root)
    root.title("Through Train Settings")
    backButton=Button(root,text='<< Back',command=lambda:backButtonClicked(root))
    backButton.pack(pady=(10,110))

    global inputBox    
    inputBox=Entry(root,borderwidth=5)
    inputBox.pack(pady=(0,25))
    description="Enter The Passing Platform Number"
    platformNumberLabel=Label(root,text=description)
    platformNumberLabel.pack(pady=(0,100))
    
    createButton=Button(root,text="Create The Announcement!!!",command=lambda:createAnnouncement(SelectedLang,inputBox.get()))
    createButton.pack()

if __name__=="__main__":
    main(root,SelectedLang)
