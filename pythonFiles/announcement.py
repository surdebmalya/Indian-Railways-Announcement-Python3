from gtts import gTTS
import os
import random
import time

def fullAnnouncement(SelectedLang,trainNumber,upOrDown,trainName,platformNumber,lastStation,timeStr):
    if SelectedLang==1:
        langCode='bn'
    elif SelectedLang==2:
        langCode='hi'
    else:
        langCode='en-in'

    period=timeStr[-2]+timeStr[-1]
    timeStr=timeStr[:-3]
    tempList=timeStr.split(':')
    hour=tempList[0]
    minute=tempList[1]

    if len(trainNumber)==0:
        if langCode=='en-in':
            mainText="Please pay attaintion, "+upOrDown+" "+trainName+", will depart from platform number "+platformNumber+", for destination "+lastStation+", at "+hour+" hours "+minute+" minutes "+period+"."
        elif langCode=='bn':
            mainText="অনুগ্রহ করে শুনুন, "+upOrDown+" "+trainName+", প্ল্যাটফর্ম নম্বর "+platformNumber+" থেকে গন্তব্য স্টেশান "+lastStation+" এর উদ্দেশ্যে "+period+" এর "+hour+" টা বেজে "+minute+" মিনিটের সময় রওনা দেবে."
        else:
            mainText="कृपया सुनिए, "+upOrDown+" "+trainName+", प्लेटफार्म नंबर "+platformNumber+" से "+lastStation+" के लिए, "+hour+" घंटे "+minute+" मिनट "+period+" पर प्रस्थान करेगी."
    else:
        finalTrainNumber=""
        for i in range(len(trainNumber)):
            finalTrainNumber=finalTrainNumber+" "+trainNumber[i]
        if langCode=='en-in':
            mainText="Please pay attaintion, Train number "+finalTrainNumber+", "+upOrDown+" "+trainName+", will depart from platform number "+platformNumber+", for destination "+lastStation+", at "+hour+" hours "+minute+" minutes "+period+"."
        elif langCode=='bn':
            mainText="অনুগ্রহ করে শুনুন, ট্রেন নম্বর "+finalTrainNumber+", "+upOrDown+" "+trainName+", প্ল্যাটফর্ম নম্বর "+platformNumber+" থেকে গন্তব্য স্টেশান "+lastStation+" এর উদ্দেশ্যে "+period+" এর "+hour+" টা বেজে "+minute+" মিনিটের সময় রওনা দেবে."
        else:
            mainText="कृपया सुनिए, ट्रेन नंबर "+finalTrainNumber+", "+upOrDown+" "+trainName+", प्लेटफार्म नंबर "+platformNumber+" से "+lastStation+" के लिए, "+hour+" घंटे "+minute+" मिनट "+period+" पर प्रस्थान करेगी."
        
    output=gTTS(text=mainText,lang=langCode,slow=False)
    path="C:/Users/surde/OneDrive/Desktop/IndianRailwayAnnouncementProject/FinalProject/sounds/"
    output.save(path+"SecondPart.mp3")
    randomList=[1,2]
    toss=random.choice(randomList)
    if toss==1:
        os.system("start "+path+"IntroductiveSounds/KringKring.mp3")
    elif toss==2:
        os.system("start "+path+"IntroductiveSounds/RingRangRong.mp3")
    time.sleep(3)
    os.system("start "+path+"SecondPart.mp3")

def arrivingTrain(SelectedLang,trainNumber,trainName,upOrDown,platformNumber):
    if SelectedLang==1:
        langCode='bn'
    elif SelectedLang==2:
        langCode='hi'
    else:
        langCode='en-in'
    if len(trainNumber)!=0:
        finalTrainNumber=""
        for i in range(len(trainNumber)):
            finalTrainNumber=finalTrainNumber+" "+trainNumber[i]
        if langCode=='en-in':
             mainText="Please pay attaintion, Train number "+finalTrainNumber+", "+upOrDown+" "+trainName+", is arriving to the platform number "+platformNumber+"."
        elif langCode=='bn':
            mainText="অনুগ্রহ করে শুনুন, ট্রেন নম্বর "+finalTrainNumber+", "+upOrDown+" "+trainName+", প্ল্যাটফম নম্বর "+platformNumber+" এ আছ্ছে."
        else:
            mainText="कृपया सुनिए, ट्रेन नंबर "+ finalTrainNumber +", "+ upOrDown +" "+ trainName + ", प्लेटफॉर्म नंबर " +platformNumber+" आ रही है।"
    else:
        if langCode=='en-in':
             mainText="Please pay attaintion, "+upOrDown+" "+trainName+", is arriving to the platform number "+platformNumber+"."
        elif langCode=='bn':
            mainText="অনুগ্রহ করে শুনুন, "+upOrDown+" "+trainName+", প্ল্যাটফম নম্বর "+platformNumber+" এ আছ্ছে."
        else:
            mainText="कृपया सुनिए, "+ upOrDown +" "+ trainName + ", प्लेटफॉर्म नंबर " +platformNumber+"पर आ रही है।"                        
    output=gTTS(text=mainText,lang=langCode,slow=False)
    path="C:/Users/surde/OneDrive/Desktop/IndianRailwayAnnouncementProject/FinalProject/sounds/"
    output.save(path+"SecondPart.mp3")
    randomList=[1,2]
    toss=random.choice(randomList)
    if toss==1:
        os.system("start "+path+"IntroductiveSounds/KringKring.mp3")
    elif toss==2:
        os.system("start "+path+"IntroductiveSounds/RingRangRong.mp3")
    time.sleep(3)
    os.system("start "+path+"SecondPart.mp3")
    
def announcementForThroughTrain(langCode,platformNumber):
    if langCode=='en-in':
        mainText="Please pay attention, a thru train will pass from platform number "+platformNumber+", passengers are requested to maintain a safe distance. Thanks."
    elif langCode=='bn':
        mainText="অনুগ্রহ করে শুনুন, একটি থ্রু ট্রেনটি প্ল্যাটফর্ম নম্বর "+platformNumber+"থেকে পাস করবে, যাত্রীদের একটি নিরাপদ দূরত্ব বজায় রাখতে অনুরোধ করা হছ্ছে. ধন্যবাদ."
    else:
        mainText="कृपया ध्यान दें, एक थ्रू ट्रेन प्लेटफॉर्म नंबर "+platformNumber+"से गुजरेगी, यात्रियों से अनुरोध है कि वे एक सुरक्षित दूरी बनाए रखें। धन्यवाद।"
    output=gTTS(text=mainText,lang=langCode,slow=False)
    path="C:/Users/surde/OneDrive/Desktop/IndianRailwayAnnouncementProject/FinalProject/sounds/"
    output.save(path+"SecondPart.mp3")
    randomList=[1,2]
    toss=random.choice(randomList)
    if toss==1:
        os.system("start "+path+"IntroductiveSounds/KringKring.mp3")
    elif toss==2:
        os.system("start "+path+"IntroductiveSounds/RingRangRong.mp3")
    time.sleep(3)
    os.system("start "+path+"SecondPart.mp3")

def main(SelectedLang,platformNumber,code):
    if SelectedLang==1:
        langCode='bn'
    elif SelectedLang==2:
        langCode='hi'
    else:
        langCode='en-in'
    if code==1:
        announcementForThroughTrain(langCode,platformNumber)
    
if __name__=="__main__":
    main(SelectedLang,platformNumber,code)
