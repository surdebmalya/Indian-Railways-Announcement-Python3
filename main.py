from tkinter import *
from pythonFiles import throughTrain
from pythonFiles import normalTrain
from pythonFiles import goingToMainPage
from pythonFiles import announcement
from pythonFiles import normalTrainArriving
from pythonFiles import normalTrainDeparting
from pythonFiles import setDepartingTime
from pythonFiles import proxyNormalTrainDeparting

def ClickedToProceed(root,SelectedLang, TrainCategory):
    if TrainCategory==1:
        throughTrain.main(root,SelectedLang)
    else:
        normalTrain.main(root,SelectedLang)

def main():
    root=Tk()

    root.geometry("400x370")
    root.minsize(400,370)
    root.maxsize(400,370)
    root.title("Indian Railway Announcement App")
    root.iconbitmap("Icon/icon.ico")

    frame1=LabelFrame(root,text="Select The Language",padx=10,pady=10)
    frame1.pack(padx=50,pady=25)
    l=IntVar()
    l.set("3")
    Radiobutton(frame1,text="Bengali",variable=l,value=1).pack()
    Radiobutton(frame1,text="Hindi",variable=l,value=2).pack()
    Radiobutton(frame1,text="Indian-English",variable=l,value=3).pack()

    frame2=LabelFrame(root,text="Select Train Category",padx=10,pady=10)
    frame2.pack(padx=50,pady=(0,50))
    c=IntVar()
    c.set("2")
    Radiobutton(frame2,text="Through Train",variable=c,value=1).pack()
    Radiobutton(frame2,text="Normal Train",variable=c,value=2).pack()

    proceedButton=Button(root,text="Click Here To Proceed",command=lambda:ClickedToProceed(root,l.get(),c.get()))
    proceedButton.pack()

    root.mainloop()

if __name__=="__main__":
    main()
