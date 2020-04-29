from tkinter import *
from tkinter import  messagebox
import sys
sys.path.append("C:/Users/surde/OneDrive/Desktop/Indian Railway Announcement Project/FinalProject/")
from pythonFiles import goingToMainPage
from pythonFiles import normalTrainArriving
from pythonFiles import normalTrainDeparting

def deleteAll(root):
    list=root.pack_slaves()
    for l in list:
        l.pack_forget()

def backButtonClicked(root):
    goingToMainPage.main(root)

def clickedNext(root,SelectedLang,trainNumber,trainName,upOrDown,cat):
    if len(trainName)==0:
        result=messagebox.showerror("Error!!!", "Please Fill The Required Spaces.")
        main(root,SelectedLang)
    else:
        if  cat=="Arriving":
            normalTrainArriving.main(root,SelectedLang,trainNumber,trainName,upOrDown)
        else:
            normalTrainDeparting.main(root,SelectedLang,trainNumber,trainName,upOrDown)

def main(root,SelectedLang):
    deleteAll(root)
    root.title("Normal Train Settings")
    backButton=Button(root,text='<< Back',command=lambda:backButtonClicked(root))
    backButton.pack(pady=(5,5))

    mustDes="* Means, the input is must"
    label0=Label(root,text=mustDes)
    label0.pack(pady=(0,10))

    numberBox=Entry(root)
    numberBox.pack(pady=(0,5))
    platformNumberDes="1. Enter Train Number"
    label1=Label(root,text=platformNumberDes)
    label1.pack(pady=(0,15))

    name=Entry(root,width=25)
    name.pack(pady=(0,5))
    nameDes="2. Enter The Name Of The Train*"
    label2=Label(root,text=nameDes)
    label2.pack(pady=(0,15))

    updownDes="3. Direction Of The Train"
    label3=Label(root,text=updownDes)
    label3.pack(pady=(0,5))

    upOrdown=StringVar()
    upOrdown.set("UP")
    drop=OptionMenu(root,upOrdown,"UP","DOWN")
    drop.pack(pady=(0,15))

    categoryDes="4. Category Of The Train"
    label4=Label(root,text=categoryDes)
    label4.pack(pady=(0,5))

    categories=StringVar()
    categories.set("Arriving")
    dropMenu=OptionMenu(root,categories,"Arriving","Departing")
    dropMenu.pack(pady=(0,15))

    createButton=Button(root,
                        text="NEXT",
                        command=lambda:clickedNext(root,SelectedLang,numberBox.get(),name.get(),upOrdown.get(),categories.get()),
                        padx=15,pady=3)
    createButton.pack()

if __name__=="__main__":
    main(root,SelectedLang)
