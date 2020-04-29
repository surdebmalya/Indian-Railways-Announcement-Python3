from tkinter import *
import sys
sys.path.append("C:/Users/surde/OneDrive/Desktop/Indian Railway Announcement Project/FinalProject/")
from pythonFiles import proxyNormalTrainDeparting

def deleteAll(root):
    list=root.pack_slaves()
    for l in list:
        l.pack_forget()

def finalSet(hour,minute,amOrPm,root,SelectedLang,trainNumber,trainName,upOrDown):
    finalTime=""
    finalTime+=hour
    finalTime+=":"
    temp=str(minute)
    finalTime+=temp
    finalTime+=" "
    finalTime+=amOrPm

    proxyNormalTrainDeparting.main(root,SelectedLang,trainNumber,trainName,upOrDown,finalTime)
        
def main(root,SelectedLang,trainNumber,trainName,upOrDown):
    deleteAll(root)
    root.title("Set The Departing Time")
    root.iconbitmap("Icon/clock.ico")

    des0="1. Set Hour"
    label0=Label(root,text=des0)
    label0.pack(pady=(20,7))
    hour=StringVar()
    hour.set("10")
    drop0=OptionMenu(root,hour,
                     "1","2","3","4","5","6","7","8","9","10","11","12")
    drop0.pack(pady=(0,30))

    des1="2. Set Minute"
    label1=Label(root,text=des1)
    label1.pack(pady=(0,0))
    des11="(Set The Minutes By Slider)"
    label2=Label(root,text=des11)
    label2.pack(pady=(0,3))
    horizontal=Scale(root,from_=0,to=59,orient=HORIZONTAL)
    horizontal.pack(pady=(0,30))
    des2="3. Set AM/PM"
    label3=Label(root,text=des2)
    label3.pack(pady=(0,7))
    
    amOrpm=StringVar()
    amOrpm.set("AM")
    drop1=OptionMenu(root,amOrpm,"AM","PM")
    drop1.pack(pady=(0,30))

    setButton=Button(root,text="Set",
                     command=lambda:finalSet(hour.get(),
                                             horizontal.get(),amOrpm.get(),
                                             root,SelectedLang,trainNumber,trainName,upOrDown))
    setButton.pack()
    
if __name__=="__main__":
    main(root,SelectedLang,trainNumber,trainName,upOrDown)
