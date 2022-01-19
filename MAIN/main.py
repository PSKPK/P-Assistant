from kivy.app import App
from kivy.config import Config
Config.set('graphics','resizable',True)
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
import datetime
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import os
from kivy.clock import Clock
from kivy.core.window import Window
from kivymd.app import MDApp

folder='/storage/emulated/0/Trial1Files/'
OldNameOfFile=""
OldText=""
firsttime=1
pcheck=0
FileListString=""
badsol=["13","9","5","1","15","10","6","2","15","11","7","3"," ","12","8","4"]
solution=["13","9","5","1","14","10","6","2","14","11","7","3"," ","12","8","4"]
moredec=1
ans=0
#requirements = python3,kivy,kivymd,wikipedia,sdl2_ttf==2.0.15,requests,chardet,idna,urllib3,certifi,soupsieve,beautifulsoup4

class MyLayout(FloatLayout):
    def ButtonMaker(self):
        self.Wikib=Button(
            text="WikiPedia",size_hint=(.35,.15),pos_hint={"x":.09,"y":.6})
        self.WriteB=Button(
            text="Press here to \nwrite a note",size_hint=(.35,.15),pos_hint={"x":.6,"y":.6})
        self.NoteB=Button(
            text="Press here to view\n a written note",size_hint=(.35,.15),pos_hint={"x":.09,"y":.2})
        self.SWB=Button(
            text="Press here for \nStop-Watch",size_hint=(.35,.15),pos_hint={"x":.6,"y":.2})
        self.GameB=Button(
            text="Game Blocks",size_hint=(.35,.15),pos_hint={"x":.09,"y":.4})
        self.CalcB=Button(
            text="Calculator",size_hint=(.35,.15),pos_hint={"x":.6,"y":.4})

        self.GameRB=Button(
            text="Restart",font_size=30,pos_hint={"x":0.15,"y":0.05},size_hint=(.3,.15))
        self.GameQuitButton=Button(
            text="Quit",font_size=30,pos_hint={"x":0.55,"y":0.05},size_hint=(.3,.15))
        self.GameLeftBor=Button(
            text=" ",pos_hint={"x":0.17,"y":0.28},size_hint=(.01,.64),background_color=(0.5,0.5,1,1))
        self.GameRightBor=Button(
            text=" ",pos_hint={"x":0.83,"y":0.28},size_hint=(.01,.64),background_color=(0.5,0.5,1,1))
        self.GameTopBor=Button(
            text=" ",pos_hint={"x":0.15,"y":0.92},size_hint=(0.71,0.01),background_color=(.5,.5,1,1))
        self.GameBotBor=Button(
            text=" ",pos_hint={"x":0.15,"y":0.27},size_hint=(0.71,0.01),background_color=(.5,.5,1,1))

        self.STOPWATCHStartB=Button(
            text="Start",size_hint=(.25,.20),pos_hint={"x":.04,"y":.3})
        self.STOPWATCHStopB=Button(
            text="Stop",size_hint=(.25,.20),pos_hint={"x":.36,"y":.3})
        self.STOPWATCHCloseB=Button(
            text="Close",size_hint=(.25,.20),pos_hint={"x":.68,"y":.3})
        self.STOPWATCHPauseB=Button(
            text="Pause",size_hint=(.25,.20),pos_hint={"x":.2,"y":.05})
        self.STOPWATCHResetB=Button(
            text="Reset",size_hint=(.25,.20),pos_hint={"x":.53,"y":.05})
        self.STOPWATCHDisp=TextInput(
            text=" 00:00:00:00",size_hint=(.9,.3),font_size='125sp',readonly=True,pos_hint={"x":.05,"y":.6})
        self.TimeBTime=Button(
            text="The time is :",background_color=(0,0,0,1),font_size=40,pos_hint={"x":0,"y":.3})
        self.TimeBCloseB=Button(
            text="Click to close",size_hint=(.2,.2),pos_hint={"x":.35,"y":.2})
        self.WriteBNameB=Label(
            text="Enter name of file here : (or Enter name of already\n existing file to edit beforen entering text)",size_hint=(1,.09),color=(0,0,0,1),pos_hint={"x":0.01,"y":.93})
#            text="Enter name of file here : (or Enter name of already existing file to edit before entering text)",size_hint=(1,.09),background_color=(100,100,100,1),pos_hint={"x":0.01,"y":.9})
        self.WriteBTIB=Button(
            text="Enter text here :",size_hint=(1,.09),background_color=(0,0,0,1),pos_hint={"x":0.01,"y":.78})
        self.WriteBSubmitB=Button(
            text="Save",size_hint=(.4,.1),pos_hint={"x":0.07,"y":.1})
        self.WriteBCloseB=Button(
            text="Close",size_hint=(.4,.1),pos_hint={"x":.53,"y":.1})
        self.WriteBTI=TextInput(
            font_size=30,size_hint=(.95,.55),pos_hint={"x":0.02,"y":.25},multiline=True)
        self.WriteBName=TextInput(
            font_size=20,size_hint=(.95,.07),pos_hint={"x":0.02,"y":.85})
        self.WriteBp=Button(
            text="Empty name error...",background_color=(0,0,0,1),size_hint=(.4,.08),pos_hint={"x":0.3,"y":0.01})
        self.NoteBName=TextInput(
            text="Select a file name from below files",font_size=20,size_hint=(.95,.07),pos_hint={"x":.02,"y":.85})
        self.NoteBNameB=Button(
            text="Enter name of file here :",size_hint=(1,.09),background_color=(0,0,0,1),pos_hint={"x":0.01,"y":.9})
        self.NoteBTextData=TextInput(
            font_size=20,size_hint=(.95,.55),pos_hint={"x":0.02,"y":.25},readonly=True,multiline=True)
        self.NoteBTextDataB=Button(
            text="Data of files :",size_hint=(1,.09),background_color=(0,0,0,1),pos_hint={"x":0.01,"y":.78})
        self.NoteBSubmitB=Button(
            text="Submit",size_hint=(.4,.1),pos_hint={"x":0.07,"y":.13})
        self.NoteBCloseB=Button(
            text="Close",size_hint=(.4,.1),pos_hint={"x":0.53,"y":.13})
        self.NoteBDeleteB=Button(
            text="Delete this",size_hint=(.38,.09),pos_hint={"x":0.3,"y":0.02})
        self.NoteBp=Button(
            text="Empty name error...",background_color=(0,0,0,1),size_hint=(.4,.1),pos_hint={"x":0.3,"y":0.02})
        self.CalcQuitB=Button(
            text="Back",size_hint=(.15,.05),pos_hint={"x":.1,"y":.9})
        self.WikiReqInp=TextInput(
            text="Search here",size_hint=(.56,.1),pos_hint={"x":.02,"y":.8})
        self.WikilinesInp=TextInput(
            text=str(self.Wikilines),size_hint=(.2,.1),pos_hint={"x":.58,"y":.8})
        self.WikiReqOut=TextInput(
            text="Result here",size_hint=(.96,.7),pos_hint={"x":.02,"y":.1})
        self.WikiReqB=Button(
            text="Search",size_hint=(.2,.1),pos_hint={"x":.78,"y":.8},on_press=self.WikiSearch)
        self.WikiQuitB=Button(
            text="Back",size_hint=(.15,.07),pos_hint={"x":.02,"y":.9},on_press=self.WikiQuit)

        self.CalcB1=Button(text=str(0),font_size=70,size_hint=(.15,.1),pos_hint={"x":.26,"y":.09},on_press=self.UpdateBar)
        self.CalcB2=Button(text=".",font_size=120,size_hint=(.15,.1),pos_hint={"x":.1,"y":.09},on_press=self.UpdateBar)
        self.CalcB3=Button(text="=",font_size=80,size_hint=(.15,.1),pos_hint={"x":.42,"y":.09},on_press=self.UpdateBar)
        self.CalcB4=Button(text="+",font_size=80,size_hint=(.15,.1),pos_hint={"x":.58,"y":.42},on_press=self.UpdateBar)
        self.CalcB5=Button(text="-",font_size=80,size_hint=(.15,.1),pos_hint={"x":.58,"y":.31},on_press=self.UpdateBar)
        self.CalcB6=Button(text="*",font_size=80,size_hint=(.15,.1),pos_hint={"x":.58,"y":.2},on_press=self.UpdateBar)
        self.CalcB7=Button(text="/",font_size=80,size_hint=(.15,.1),pos_hint={"x":.58,"y":.09},on_press=self.UpdateBar)
        self.CalcB8=Button(text="(",font_size=80,size_hint=(.15,.1),pos_hint={"x":.74,"y":.42},on_press=self.UpdateBar)
        self.CalcB9=Button(text=")",font_size=80,size_hint=(.15,.1),pos_hint={"x":.74,"y":.31},on_press=self.UpdateBar)
        self.CalcB10=Button(text="x^(y)",size_hint=(.15,.1),pos_hint={"x":.74,"y":.2},on_press=self.UpdateBar)
        self.CalcB11=Button(text="e^(x)",size_hint=(.15,.1),pos_hint={"x":.74,"y":.09},on_press=self.UpdateBar)
        self.CalcB12=Button(text="More\ndecimals\nOn",font_size=30,size_hint=(.15,.1),pos_hint={"x":.74,"y":.53},on_press=self.UpdateDec)
        self.CalcB13=Button(text="log(a,base)",font_size=30,size_hint=(.15,.1),pos_hint={"x":.26,"y":.53},on_press=self.UpdateBar)
        self.CalcB14=Button(text=",",font_size=80,size_hint=(.15,.1),pos_hint={"x":.58,"y":.53},on_press=self.UpdateBar)
        self.CalcB15=Button(text="sqrt(x)",size_hint=(.15,.1),pos_hint={"x":.1,"y":.53},on_press=self.UpdateBar)
        self.CalcB16=Button(text="pi",font_size=40,size_hint=(.073,0.1),pos_hint={"x":.42,"y":.53},on_press=self.UpdateBar)
        self.CalcB17=Button(text="e",font_size=40,size_hint=(.075,0.1),pos_hint={"x":.495,"y":.53},on_press=self.UpdateBar)
        self.CalcB18=Button(text="Clear",size_hint=(.15,.05),pos_hint={"x":.74,"y":.8},on_press=self.ClearCalcBar)
        self.CalcB19=Button(text="Clear All",font_size=35,size_hint=(.15,.05),pos_hint={"x":.74,"y":.85},on_press=self.ClearCalcBarAll)
        self.CalcTextBar=TextInput(text="",readonly=True,font_size=50,multiline=True,size_hint=(.64,.1),pos_hint={"x":.1,"y":.8})

        self.HomePage1List=[
            self.Wikib,self.WriteB,self.NoteB,self.SWB,self.GameB,self.CalcB]
        self.STOPWATCHList=[
            self.STOPWATCHStartB,self.STOPWATCHStopB,self.STOPWATCHCloseB,self.STOPWATCHPauseB,self.STOPWATCHResetB,self.STOPWATCHDisp]
        self.WikiBList=[
            self.WikiReqInp,self.WikilinesInp,self.WikiReqOut,self.WikiQuitB,self.WikiReqB]
        self.WriteBList=[
            self.WriteBNameB,self.WriteBTIB,self.WriteBName,self.WriteBTI,self.WriteBSubmitB,self.WriteBCloseB]
        self.NoteBList=[
            self.NoteBNameB,self.NoteBName,self.NoteBTextDataB,self.NoteBTextData,self.NoteBSubmitB,self.NoteBCloseB,self.NoteBDeleteB]
        self.GameDispList=[
            self.GameBotBor,self.GameTopBor,self.GameLeftBor,self.GameRightBor,self.GameRB,self.GameQuitButton]
        self.CalcButtonList=[
            Button(text=str(i+1),font_size=70,size_hint=(.15,.1),pos_hint={"x":0.1+0.16*(i%3),"y":0.2+(0.11*(i//3))},on_press=self.UpdateBar) for i in range(9)]
        self.CalcDispList=[
            self.CalcQuitB,self.CalcTextBar]
        for j in range(1,20):
            exec("self.CalcDispList.append(self.CalcB{num})".format(num=j))
        self.Winbutton=Button(text="YOU WON!!!",font_size=80,pos_hint={"x":.2,"y":.3},size_hint=(.6,.6))
        self.GameButtonList=[Button(text=str(b),font_size=40,pos_hint={"x":b//4*(0.15)+(0.21),"y":b%4*(0.15)+(0.3)},size_hint=(0.14,.14)) for b in range(1,16)]
        self.GameButtonList.append(Button(text=" ",font_size=40,pos_hint={"x":0.21,"y":0.3},size_hint=(.14,.14)))
    def BindButtons(self):
        self.SWB.bind(on_press=self.StopWatchPress)
        self.Wikib.bind(on_press=self.WikiBPress)
        self.WriteB.bind(on_press=self.WriteBPress)
        self.NoteB.bind(on_press=self.NoteBPress)
        self.STOPWATCHStartB.bind(on_press=self.OnStart)
        self.STOPWATCHStopB.bind(on_press=self.OnStop)
        self.STOPWATCHResetB.bind(on_press=self.OnReset)
        self.STOPWATCHPauseB.bind(on_press=self.OnPause)
        self.STOPWATCHCloseB.bind(on_press=self.StopWatchClose)
        self.TimeBCloseB.bind(on_press=self.TimeBClose)
        self.WriteBCloseB.bind(on_press=self.WriteBClose)
        self.WriteBSubmitB.bind(on_press=self.Saveandwrite)
        self.NoteBSubmitB.bind(on_press=self.OpenFile)
        self.NoteBCloseB.bind(on_press=self.NoteBClose)
        self.NoteBDeleteB.bind(on_press=self.NoteBDelete)
        self.GameB.bind(on_press=self.Game)
        self.Winbutton.bind(on_press=self.GameShuffleButtons)
        self.GameRB.bind(on_press=self.GameShuffleButtons)
        self.GameQuitButton.bind(on_press=self.QuitGame)
        for b in self.GameButtonList:
            b.bind(on_press=self.Move)
        self.CalcB.bind(on_press=self.Calc)
        self.CalcQuitB.bind(on_press=self.CalcQuit)
    def AddHomePage1(self):
        for b in self.HomePage1List:
            self.add_widget(b)
    def RemHomePage1(self):
        for b in self.HomePage1List:
            self.remove_widget(b)

    def __init__(self,**kwargs):
        super(MyLayout,self).__init__(**kwargs)
        self.Wikilines=6
        self.ButtonMaker()
        self.BindButtons()
        self.AddHomePage1()
        global folder
        if not os.path.exists(folder):
            os.makedirs(folder)

    def StopWatchPress(self,button):
        self.RemHomePage1()
        self.STOPWATCHpause=0
        self.STOPWATCHstop=0
        Clock.unschedule(self.increment_STOPWATCHtime)
        self.STOPWATCHtime=["00","00","00","0"]
        self.STOPWATCHDisp.text=" 00:00:00:00"
        for b in self.STOPWATCHList:
            self.add_widget(b)
    def WikiBPress(self,button):
        self.RemHomePage1()
        for b in self.WikiBList:
            self.add_widget(b)
    def WriteBPress(self,button):
        self.RemHomePage1()
        global firsttime
        firsttime=1
        for b in self.WriteBList:
            self.add_widget(b)
    def NoteBPress(self,button):
        self.RemHomePage1()
        global folder
        FileList=os.listdir(os.path.join(folder))
        global FileListString
        FileListString="Names of all files are : \n"
        for k in FileList:
            if k[-4:]==".txt":
                FileListString=FileListString+k+"\n"
        self.NoteBTextData.text=FileListString
        for b in self.NoteBList:
            self.add_widget(b)

    def StopWatchClose(self,button):
        for b in self.STOPWATCHList:
            self.remove_widget(b)
        self.AddHomePage1()
    def TimeBClose(self,button):
        self.remove_widget(self.TimeBCloseB)
        self.remove_widget(self.TimeBTime)
        self.AddHomePage1()
    def Saveandwrite(self,button):
        global OldNameOfFile
        global OldText
        global firsttime
        global folder
        if firsttime==1 or (OldNameOfFile!=self.WriteBName.text.strip() or OldText!=self.WriteBTI.text):
            file="new"
            NameOfFile=self.WriteBName.text.strip()
        else:
            file="old"
        if file=="old":
            return
        global pcheck
        OldNameOfFile=NameOfFile
        if NameOfFile=="":
            if pcheck==0:
                self.add_widget(self.WriteBp)
                pcheck=1
            return
        if NameOfFile!="":
            self.remove_widget(self.WriteBp)
            pcheck=0
        if NameOfFile[-4:]==".txt":
            NameOfFile=NameOfFile[:-4]
        try:
            NewF=open(os.path.join(folder,NameOfFile+".txt"),"r")
            if self.WriteBTI.text=="":
                self.WriteBTI.text=NewF.read()
            NewF.close()
        except:
            pass
        NewF=open(os.path.join(folder,NameOfFile+".txt"),"w")
        self.WriteBName.text=NameOfFile
        Text=self.WriteBTI.text
        OldText=Text
        NewF.write(Text)
        NewF.close()
        firsttime=0
        return
    def WriteBClose(self,button):
        for b in self.WriteBList:
            self.remove_widget(b)
        global pcheck
        global OldNameOfFile
        global firsttime
        firsttime=1
        OldNameOfFile=""
        self.WriteBName.text=""
        self.WriteBTI.text=""
        if pcheck==1:
            pcheck=0
            self.remove_widget(self.WriteBp)
        self.AddHomePage1()
    def OpenFile(self,button):
        global FileListString
        NameOfFile=self.NoteBName.text.strip()
        global pcheck
        global folder
        if NameOfFile=="":
            if pcheck==0:
                self.add_widget(self.NoteBp)
                pcheck=1
            return
        if NameOfFile!="":
            self.remove_widget(self.NoteBp)
            pcheck=0
        try:
            if NameOfFile[-4:]==".txt":
                NameOfFile=NameOfFile[:-4]
            NewF=open(os.path.join(folder,NameOfFile+".txt"),"r")
            self.NoteBTextData.text=NewF.read()
        except :
            self.NoteBTextData.text=FileListString
            self.NoteBName.text="No Such File.. Select a name from below files.."
    def NoteBDelete(self,button):
        global folder
        NameOfFile=self.NoteBName.text.strip()
        if NameOfFile[-4:]==".txt":
            NameOfFile=NameOfFile[:-4]
        try:
            os.remove(os.path.join(folder,NameOfFile+".txt"))
        except:
            pass
        FileList=os.listdir(os.path.join(folder))
        global FileListString
        FileListString="Names of all files are : \n"
        for k in FileList:
            if k[-4:]==".txt":
                FileListString=FileListString+k+"\n"
        self.NoteBTextData.text=FileListString
        self.NoteBName.text="Select a file name from below files"
    def NoteBClose(self,button):
        for b in self.NoteBList:
            self.remove_widget(b)
        global pcheck
        global FileListString
        FileListString=""
        self.NoteBName.text="Select a file name from below files"
        if pcheck==1:
            pcheck=0
            self.remove_widget(self.NoteBp)
        self.AddHomePage1()
    def increment_STOPWATCHtime(self,interval):
        if int(self.STOPWATCHtime[3])<75:
            self.STOPWATCHtime[3]=str(int(self.STOPWATCHtime[3])+2)
        else:
            self.STOPWATCHtime[3]=str(int(self.STOPWATCHtime[3])+4)
        if int(self.STOPWATCHtime[3])>90:
            self.STOPWATCHtime[2]=str(int(self.STOPWATCHtime[2])+1)
            self.STOPWATCHtime[3]="00"
        if self.STOPWATCHtime[2]=="60":
            self.STOPWATCHtime[1]=str(int(self.STOPWATCHtime[1])+1)
            self.STOPWATCHtime[2]="00"
            self.STOPWATCHtime[3]="30"
        if self.STOPWATCHtime[1]=="60":
            self.STOPWATCHtime[0]=str(int(self.STOPWATCHtime[0])+1)
            self.STOPWATCHtime[1]="00"
        if self.STOPWATCHtime[0]=="24":
            self.STOPWATCHtime=["00","00","00","00"]
        for k in range(4):
            if int(self.STOPWATCHtime[k])<10:
                self.STOPWATCHtime[k]="0"+str(int(self.STOPWATCHtime[k]))
        self.STOPWATCHDisp.text=" "
        for k in range(4):
            self.STOPWATCHDisp.text+=self.STOPWATCHtime[k]
            if k<3: self.STOPWATCHDisp.text+=":"
    def OnPause(self,button):
        self.STOPWATCHpause=1
        Clock.unschedule(self.increment_STOPWATCHtime)
    def OnReset(self,button):
        Clock.unschedule(self.increment_STOPWATCHtime)
        self.STOPWATCHtime=["00","00","00","00"]
        self.STOPWATCHDisp.text=" 00:00:00:00"
        self.STOPWATCHpause=0
    def OnStart(self,button):
        Clock.unschedule(self.increment_STOPWATCHtime)
        if self.STOPWATCHpause==0 and self.STOPWATCHstop!=1:
            self.STOPWATCHtime=["00","00","00","00"]
            self.STOPWATCHDisp.text=" 00:00:00:00"
        elif self.STOPWATCHstop==1:
            self.STOPWATCHtime=["00","00","00","00"]
            self.STOPWATCHDisp.text=" 00:00:00:00"
        Clock.schedule_interval(self.increment_STOPWATCHtime,0.02)
        self.STOPWATCHpause=0
        self.STOPWATCHstop=0
    def OnStop(self,button):
        Clock.unschedule(self.increment_STOPWATCHtime)
        self.STOPWATCHstop=1
        self.STOPWATCHpause=0
    def Game(self,button):
        self.RemHomePage1()
        self.GameShuffleButtons(Button())
        for b in self.GameDispList:
            self.add_widget(b)
    def AddButtons(self):
        for b in self.GameButtonList:
            if b.text==" ":
                b.background_color=(1,1,1,0.5)
            else:
                b.background_color=(1,1,1,1)
            self.add_widget(b)
    def CheckWin(self):
        for k in range(16):
            if solution[k]!=self.GameButtonList[k].text and badsol[k]!=self.GameButtonList[k].text:
                return
        if self.GameButtonList[4].text=="15":
            self.Winbutton.text="This board cannot be \nsolved further more\nSO YOU WIN!!!"
            self.Winbutton.font_size=30
        else:
            self.Winbutton.text="YOU WIN!!!"
            self.Winbutton.font_size=80
        self.add_widget(self.Winbutton)
    def GameShuffleButtons(self,button):
        try:
            for b in self.GameButtonList:
                self.remove_widget(b)
        except:
            pass
        try:
            self.remove_widget(self.Winbutton)
        except:
            pass
        from random import shuffle
        shuffle(self.GameButtonList)
        for b in range(len(self.GameButtonList)):
            self.GameButtonList[b].pos_hint={"x":b//4*(0.15)+(0.21),"y":b%4*(.15)+.3}
        self.AddButtons()
    def Move(self,Button):
        now=-1
        change=-1
        for l in range(len(self.GameButtonList)):
            if self.GameButtonList[l].text==Button.text:
                now=l
                break
        if self.GameButtonList[now].text==" ":
            return
        temp=[now-4,now-1,now+1,now+4]
        if now%4==0:
            temp.remove(now-1)
        if (now+1)%4==0:
            temp.remove(now+1)
        for k in temp:
            if k>-1 and k<16:
                if self.GameButtonList[k].text==" ":
                    change=k
                    break
        if change>-1 and now>-1 :
            self.GameButtonList[now].text,self.GameButtonList[change].text=self.GameButtonList[change].text,self.GameButtonList[now].text
            self.GameButtonList[now].background_color,self.GameButtonList[change].background_color=self.GameButtonList[change].background_color,self.GameButtonList[now].background_color
        for b in (self.GameButtonList[now],self.GameButtonList[change]):
            self.remove_widget(b)
            self.add_widget(b)
        if self.GameButtonList[5].text=="10" and self.GameButtonList[10].text=="7":
            self.CheckWin()
    def QuitGame(self,button):
        try:
            for b in self.GameDispList:
                self.remove_widget(b)
        except:pass
        try:
            for b in self.GameButtonList:
                self.remove_widget(b)
        except:pass
        try:
            self.remove_widget(self.Winbutton)
        except:pass
        self.AddHomePage1()
    def Calc(self,button):
        self.RemHomePage1()
        for b in self.CalcButtonList:
            self.add_widget(b)
        for b in self.CalcDispList:
            self.add_widget(b)
    def UpdateBar(self,button):
        tobeadded=button.text
        if tobeadded=="e^(x)":
            self.CalcTextBar.text=self.CalcTextBar.text+"e^("
        elif tobeadded=="log(a,base)":
            self.CalcTextBar.text=self.CalcTextBar.text+"log("
        elif tobeadded=="sqrt(x)":
            self.CalcTextBar.text=self.CalcTextBar.text+"sqrt("
        elif tobeadded=="x^(y)":
            self.CalcTextBar.text=self.CalcTextBar.text+"**("
        elif tobeadded!="=" and tobeadded!="x^(y)":
            self.CalcTextBar.text=self.CalcTextBar.text+tobeadded
        else:
            try:
                while "e^(" in self.CalcTextBar.text:
                    start=self.CalcTextBar.text.find("e^(")
                    end=self.CalcTextBar.text.find(")",start)
                    part=self.CalcTextBar.text[start+3:end]
                    self.CalcTextBar.text=self.CalcTextBar.text.replace("e^("+part+")","exp("+part+")")
                k="ans="+self.CalcTextBar.text
                global ans
                exec(k,globals())
                global moredec
                if moredec==0:
                    p=str(ans).find(".")
                    if p>-1:
                        try:
                            ans=str(ans)[:p+4]
                        except:
                            ans=ans
                self.CalcTextBar.text=str(ans)
                try:
                    flag=1
                    for k in self.CalcTextBar.text.split('.')[1]:
                        if k=='0':
                            flag=1
                        else:
                            flag=0
                            break
                    if flag==1:
                        self.CalcTextBar.text=self.CalcTextBar.text.split('.')[0]
                except:
                    pass
            except Exception as e:
                self.CalcTextBar.text="Invalid input"
    def WikiQuit(self,button):
        self.WikiReqInp.text="Search here"
        self.WikiReqOut.text="Result here"
        for b in self.WikiBList:
            self.remove_widget(b)
        self.AddHomePage1()
    def WikiSearch(self,button):
        query=self.WikiReqInp.text.strip()
        lineskk=self.WikilinesInp.text.strip()
        if lineskk=="":
            self.Wikilines=6
            self.WikilinesInp.text=str(self.Wikilines)
        else:
            try:
                self.Wikilines=int(lineskk)
            except:
                self.WikiReqOut.text="\n\t\t\tImproper pages number input"
                return
        try:
            import wikipedia
            self.WikiReqOut.text=wikipedia.summary(query,sentences=self.Wikilines).strip()
        except Exception as e:
            if e.__class__.__name__=="ConnectionError":
                self.WikiReqOut.text="\n\t\t\tNo internet connection..\n\t\t\tPlease check your network and retry"
            else: self.WikiReqOut.text='''
            Oops.. unable to find information for given query..
            Try asking in a different way'''

    def UpdateDec(self,Button):
        if Button.text[-1]=="n":
            Button.text=Button.text[:-2]+"Off"
        else:
            Button.text=Button.text[:-3]+"On"
        global moredec
        if moredec==1:
            moredec=0
        else:
            moredec=1
    def ClearCalcBar(self,button):
        if len(self.CalcTextBar.text)>0:
            self.CalcTextBar.text=self.CalcTextBar.text[:-1]
    def ClearCalcBarAll(self,button):
        self.CalcTextBar.text=""
    def CalcQuit(self,button):
        self.CalcTextBar.text=""
        for b in self.CalcButtonList:
            self.remove_widget(b)
        for b in self.CalcDispList:
            self.remove_widget(b)
        self.AddHomePage1()
class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Green"
        return MyLayout()

if __name__=="__main__":
    demo=DemoApp()
    demo.run()
