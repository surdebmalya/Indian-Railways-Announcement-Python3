from tkinter import *
from tkinter import  messagebox
import sys
sys.path.append("C:/Users/surde/OneDrive/Desktop/Indian Railway Announcement Project/FinalProject/")
from pythonFiles import goingToNormalTrainMainPage
from pythonFiles import setDepartingTime
from pythonFiles import announcement

def deleteAll(root):
    list=root.pack_slaves()
    for l in list:
        l.pack_forget()

def backButtonClicked(root,SelectedLang):
    goingToNormalTrainMainPage.main(root,SelectedLang)

def clickTime(root,SelectedLang,trainNumber,trainName,upOrDown):
    setDepartingTime.main(root,SelectedLang,trainNumber,trainName,upOrDown)

def create(platformNumber,lastStation,timeStr,root,SelectedLang,trainNumber,trainName,upOrDown):
    if len(platformNumber)==0 or len(lastStation)==0:
        result=messagebox.showerror("Error!!!", "Until You Give Us Informations, We Can't Generate Announcement!!!")
    else:
        platformNo.delete(0,END)
        destination.delete(0,END)
        announcement.fullAnnouncement(SelectedLang,trainNumber,upOrDown,trainName,platformNumber,lastStation,timeStr)

def main(root,SelectedLang,trainNumber,trainName,upOrDown,finalTime):
    deleteAll(root)
    root.title("Normal Train Sub-settings")
    backButton=Button(root,text='<< Back',command=lambda:backButtonClicked(root,SelectedLang))
    backButton.pack(pady=(5,10))
    des0="All of the below are mandatory"
    label0=Label(root,text=des0)
    label0.pack(pady=(0,15))
    
    des3="1. Enter Departing Time"
    label3=Label(root,text=des3)
    label3.pack(pady=(0,0))
    des4="(Set Manually Or Press The 'Set Time' Button)"
    label4=Label(root,text=des4)
    label4.pack(pady=(0,5))
    timeEntry=Entry(root,width=9,borderwidth=5)
    timeEntry.insert(0,finalTime)
    timeEntry.pack(pady=(0,0))
    setTime=Button(root,text="Set Time",command=lambda:clickTime(root,SelectedLang,trainNumber,trainName,upOrDown))
    setTime.pack(pady=(0,15))
    des1="2. Enter Departing Platform Number"
    label1=Label(root,text=des1)
    label1.pack(pady=(0,5))
    global platformNo
    platformNo=Entry(root,width=7,borderwidth=5)
    platformNo.pack(pady=(0,10))
    des2="3. Enter Destination"
    label2=Label(root,text=des2)
    label2.pack(pady=(0,5))
    global destination
    destination=Entry(root,borderwidth=5)
    destination.pack(pady=(0,20))
    
    createAnnouncement=Button(root,text="Create The Announcement",padx=10,pady=5,command=lambda:create(platformNo.get(),destination.get(),timeEntry.get(),root,SelectedLang,trainNumber,trainName,upOrDown))
    createAnnouncement.pack()

if __name__=="__main__":
    main(root,SelectedLang,trainNumber,trainName,upOrDown,finalTime)
