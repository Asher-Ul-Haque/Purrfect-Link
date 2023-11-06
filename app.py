#IMPORTS-
import customtkinter as ctk
import csv
import random
import datetime
import qrcode
from PIL import Image
from ctypes import windll, byref, sizeof, c_int

#= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

#FONTS AND COLORS AND IMAGES-
headingFont=('Cooper Black', 36, 'bold')
sidePanelFont=('Cooper Black', 25, 'bold')
subHeadingFont=('Cooper Black', 14)

#---------------------------------------
peach='#FFC0CB'
skyBlue='#87CEEB'

#---------------------------------------
whiteCatRaw=Image.open('whiteCat.png')
whiteCat=ctk.CTkImage(whiteCatRaw, size=(250,250))

whiteCatBlinkRaw=Image.open('whiteCatBlink.png')
whiteCatBlink=ctk.CTkImage(whiteCatBlinkRaw, size=(250,250))

orangeCatRaw=Image.open('orangeCat.png')
orangeCat=ctk.CTkImage(orangeCatRaw, size=(250,250))

orangeCatBlinkRaw=Image.open('orangeCatBlink.png')
orangeCatBlink=ctk.CTkImage(orangeCatBlinkRaw, size=(250,250))

shortRaw=Image.open('short.png')
short=ctk.CTkImage(shortRaw, size=(50,50))

longRaw=Image.open('long.png')
long=ctk.CTkImage(longRaw, size=(50,50))

homeRaw=Image.open('home.png')
home=ctk.CTkImage(homeRaw, size=(64, 64))

moonRaw=Image.open('moon.png')
moon=ctk.CTkImage(moonRaw, size=(64, 64))

sunRaw=Image.open('sun.png')
sun=ctk.CTkImage(sunRaw, size=(64, 64))

#= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

#SETTING UP THE ROOT
root=ctk.CTk()
root.geometry('500x400')
root.minsize(500,400)
root.maxsize(500, 400)
root.configure(fg_color='white')
root.title('Purrfect Link')
root.wm_iconbitmap('catIcon.ico')
try:
    HWND = windll.user32.GetParent(root.winfo_id())
    windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(0x0000FF)), sizeof(c_int))
except:
    pass

#= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

#VARIABLES-
title='Purrfect Link'
mode='light'
animatedTitle=''
cursor=0
chosenTask=-1
makeQrCode=0
qrCodeImage=whiteCatRaw
inputURL=ctk.StringVar()
longURL=ctk.StringVar(value='catURL/1234/this_Is_An_Example_Long_URL')
shortURL=ctk.StringVar(value='kittyURL/1234')
headers=['kitty', 'purr', 'cat', 'feline', 'paws', 'whisker', 'meow', 'pussyCat', 'litter', 'fur', 'claw']
enders=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '<', ',', '>', '.', '?']

#= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

#HEADING FRAME
titleLabel=ctk.CTkLabel(text='SAMPLE',
                        font=headingFont,
                        master=root,
                        text_color='red')

titleLabel.pack(side='top', pady=20)
def doNothing():
    pass

def animateHeading():
    global animatedTitle, title, cursor
    if animatedTitle!=title:
        titleLabel.configure(text=animatedTitle)
        animatedTitle+=title[cursor]
        root.after(100, animateHeading)
        cursor+=1
    else:
        root.after(100, doNothing)
        titleLabel.configure(text=title)

animateHeading()

#= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

#MASCOT
mascot=ctk.CTkLabel(image=orangeCat,
                    master=root,
                    fg_color='transparent',
                    text='')
mascot.place(x=20, y=140)

def animateMascot():
    global mode
    if mode=='light':
        mascot.configure(image=whiteCat)
        root.after(random.randint(50, 1000), animateMascot)
        if random.randint(0, 10)//2==0:
            mascot.configure(image=whiteCatBlink)
    else:
        mascot.configure(image=orangeCat)
        root.after(random.randint(50, 1000), animateMascot)
        if random.randint(0, 10)//2==0:
            mascot.configure(image=orangeCatBlink)
animateMascot()
#= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

#SLIDE PANELS
class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, startPos, endPos):
        super().__init__(master=parent,
                         height=50,
                         corner_radius=10,
                         fg_color='red')

        self.startPos=startPos
        self.endPos=endPos
        self.width=abs(endPos-startPos)
        self.pos=startPos
        self.atStart=True

        self.place(relx=self.startPos, y=75, relwidth=self.width)

    def animate(self):
        if self.atStart:
            self.animateForward()
        else:
            self.animateBackward()

    def animateForward(self):
        buttonShort.place_forget()
        buttonLong.place_forget()
        if self.pos > self.endPos:
            self.pos -=0.008
            self.place(relx=self.pos, relwidth=self.width, relheight=0.8)
            self.after(5, self.animateForward)
        else:
            self.atStart=False


    def animateBackward(self):
        if self.pos < self.startPos:
            self.pos +=0.008
            self.place(relx=self.pos, rely=0, relwidth=self.width, relheight=0.8)
            self.after(5, self.animateBackward)
        else:
            self.atStart=True
            buttonShort.place(x=300, y=100)
            buttonLong.place(x=300, y=250)
            answerEntry.place_forget()
            try:
                qrCodeImageLabel.place_forget()
            except:
                pass
            root.focus()
            urlEntry.delete(0, ctk.END)
#= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

#CHECK IF THE LINK HAS DEPRECATED
def deprecated(startDate):
  startDate = datetime.datetime.strptime(startDate, '%Y-%m-%d')
  endDate=datetime.datetime.now()
  endDate=str(endDate)[:10]
  endDate = datetime.datetime.strptime(endDate, '%Y-%m-%d')
  delta = endDate - startDate
  delta=str(delta)
  final=''
  for i in delta:
      if i==' ':
          return int(final)>=30
      else:
          final+=i


#= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

#THE SLIDE PANEL
sidePanel=SlidePanel(root, 1, 0.5)

panelHeading=ctk.CTkLabel(master=sidePanel,
                          text='TASK CHOSEN',
                          font=sidePanelFont,
                          text_color='white')
panelHeading.place(relx=0.5, y=20, anchor='center')

urlEntry=ctk.CTkEntry(master=sidePanel,
                      width=200,
                      height=30,
                      bg_color='transparent',
                      fg_color='white',
                      text_color='red',
                      placeholder_text='Enter URL here',
                      placeholder_text_color='purple',
                      corner_radius=5,
                      font=('Consolas', 14))
urlEntry.place(relx=0.5, y=120, anchor='center')

answerEntry=ctk.CTkEntry(master=sidePanel,
                      width=200,
                      height=30,
                      bg_color='transparent',
                      fg_color='white',
                      text_color='red',
                      placeholder_text='Your URL is',
                      placeholder_text_color='purple',
                      corner_radius=5,
                      font=('Consolas', 14),
                      state='readonly')
answerEntry.place_forget()

def backend():
    global shortURL, longURL, headers, qrCodeImage
#-----------------------------------------
    database = open('database.csv', 'r')
    reader = csv.reader(database)
#----------------------------------------
    #Shorten a URL
    if chosenTask==0:

        def QRCodeMaking():
            qrCode = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H)
            qrCode.add_data(longURL.get())
            if mode=='light':
                qrCodeImage=whiteCatRaw.resize((64, 64))
                qring=qrCode.make_image(fill_color='red', back_color='transparent')
            elif mode=='dark':
                qrCodeImage=orangeCatRaw.resize((64, 64))
                qring=qrCode.make_image(fill_color='red', back_color='transparent')

            pos=((qring.size[0]-qrCodeImage.size[0])//2, (qring.size[1]-qrCodeImage.size[1])//2)
            qring.paste(qrCodeImage, pos)
            qring.save('QRcode.png')

            qrCodeRaw = Image.open('QRcode.png')
            qrCode = ctk.CTkImage(qrCodeRaw, size=(150, 150))
            qrCodeButton.place_forget()
            answerEntry.place_forget()
            taskButton.place_forget()
            qrCodeImageLabel.configure(image=qrCode)
            if mode=='dark':
                qrCodeImageLabel.configure(fg_color='black')
            qrCodeImageLabel.place(relx=0.5, y=225, anchor='center')

        longURL.set((urlEntry.get()))
        #a valid url
        if urlEntry.get().startswith('www.') or urlEntry.get().startswith('https://') or urlEntry.get().startswith('http://') or urlEntry.get().endswith('.com') or urlEntry.get().endswith('.in'):
            for i in reader:
                if longURL.get() == i[0] and not (deprecated(i[2])):
                    #URL existed already
                    shortURL.set(i[1])
                    longURL.set(i[0])
                    answerEntry.configure(textvariable=shortURL)
                    answerEntry.place(relx=0.5, y=250, anchor='center')
                    if makeQrCode==1:
                        QRCodeMaking()
                    return None
    #---------------------------------------
            #A pre-made URL doesnt exist
            urlExisted = True

            def makeNewUrl():
                global headers, enders
                temp = 'www.' + random.choice(headers)
                temp += '/'
                for i in range(4):
                    temp += random.choice(enders)
                return temp

            temp = makeNewUrl()
            if urlExisted != True:
                used=[]
                for i in reader:
                    used.append(i[1])
                while temp in used:
                    temp=makeNewUrl()
                shortURL.set(temp)
            database = open('database.csv', 'a', newline='')
            writer = csv.writer(database)
            date = str(datetime.datetime.now())[:10]
            writer.writerow([longURL.get(), temp, date])
            answerEntry.configure(textvariable=shortURL)
            if makeQrCode==1:
                QRCodeMaking()


        #invalid url
        else:
            error = ctk.CTkToplevel()
            error.attributes('-topmost', True)
            error.geometry('200x100')
            error.minsize(200, 100)
            error.maxsize(200, 100)
            error.configure(fg_color='white')
            error.title('Invalid URL')
            error.wm_iconbitmap('catIcon.ico')
            ctk.CTkLabel(master=error, text='').pack()
            ctk.CTkLabel(master=error,
                         text='InvalidURL',
                         font=('Consolas', 14),
                         text_color='red',
                         image=short,
                         compound='left').pack()
            ctk.CTkButton(master=error,
                          fg_color='red',
                          text_color='white',
                          text='Close',
                          corner_radius=10,
                          hover_color='#dd0000',
                          font=subHeadingFont,
                          height=8,
                          width=8,
                          anchor='e',
                          command=error.destroy).pack()
            error.focus()
            error.mainloop()
#---------------------------------------
    elif chosenTask==1:
        shortURL.set(urlEntry.get())
        for i in reader:
            if shortURL.get() == i[1] and not (deprecated(i[2])):
                print('The url is:  ', i[1], 'Depreacted:  ', deprecated(i[2]))
                # URL existed already
                longURL.set(i[0])
                answerEntry.configure(textvariable=longURL)
                answerEntry.place(relx=0.5, y=250, anchor='center')
                return None
        # ---------------------------------------
        # A pre-made URL doesnt exist
        error=ctk.CTkToplevel()
        error.attributes('-topmost', True)
        error.geometry('250x100')
        error.minsize(250, 100)
        error.maxsize(250, 100)
        error.configure(fg_color='white')
        error.title('Hiss')
        ctk.CTkLabel(master=error, text='').pack()
        ctk.CTkLabel(master=error,
                     text='Failed to find your link',
                     image=long,
                     compound='left',
                     font=('Consolas', 14),
                     text_color='red').pack()
        ctk.CTkButton(master=error,
                      fg_color='red',
                      text_color='white',
                      text='Close',
                      corner_radius=10,
                      hover_color='#dd0000',
                      font=subHeadingFont,
                      height=8,
                      width=8,
                      anchor='e',
                      command=error.destroy).pack()
        error.focus()
        error.mainloop()


    return None

taskButton=ctk.CTkButton(master=sidePanel,
                         fg_color='white',
                         text_color='red',
                         text='Convert',
                         corner_radius=10,
                         hover_color='#dedede',
                         font=subHeadingFont,
                         height=8,
                         width=8,
                         anchor='e',
                         command=backend)
taskButton.place(relx=0.5, y=200, anchor='center')

#= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

#MENU BUTTONS

def qrCodeClicked():
    global makeQrCode
    makeQrCode=1
    backend()

qrCodeButton = ctk.CTkButton(master=sidePanel,
                                 fg_color='white',
                                 text_color='red',
                                 text='Get QRcode',
                                 corner_radius=10,
                                 hover_color='#dedede',
                                 font=subHeadingFont,
                                 height=8,
                                 width=8,
                                 anchor='e',
                                 command=qrCodeClicked)
def shortenClicked():
    global chosenTask
    chosenTask=0
    panelHeading.configure(text='Shorten URL')
    taskButton.place(relx=0.2, y=200, anchor='center')
    qrCodeButton.place(relx=0.75, y=200, anchor='center')
    sidePanel.animate()

def lengthenClicked():
    global chosenTask
    chosenTask=1
    panelHeading.configure(text='Lengthen URL')
    sidePanel.animate()

buttonShort=ctk.CTkButton(master=root,
                          text_color='white',
                          fg_color='red',
                          text='Shorten URL',
                          corner_radius=10,
                          hover_color='#dd0000',
                          font=subHeadingFont,
                          height=100,
                          width=180,
                          anchor='e',
                          image=short,
                          compound='left',
                          command=shortenClicked)
buttonShort.place(x=300, y=100)

buttonLong=ctk.CTkButton(master=root,
                          text_color='white',
                          fg_color='red',
                          text='Lengthen URL',
                          corner_radius=10,
                          hover_color='#dd0000',
                          font=subHeadingFont,
                          height=100,
                          width=170,
                          anchor='e',
                          image=long,
                          compound='left',
                          command=lengthenClicked)
buttonLong.place(x=300, y=250)

#= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

#HOME BUTTON
homeButton=ctk.CTkButton(master=root,
                         fg_color='red',
                         text='',
                         corner_radius=10,
                         hover_color='#dd0000',
                         font=subHeadingFont,
                         anchor='e',
                         image=home,
                         width=10,
                         height=10,
                         command=sidePanel.animateBackward)
homeButton.place(x=20, y=3)

#= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

def modeChange():
    global mode
    if mode=='light':
        mode='dark'
        modeButton.configure(image=moon)
        root.configure(fg_color='#000000')
        try:
            HWND = windll.user32.GetParent(root.winfo_id())
            windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(0x000000)), sizeof(c_int))
        except:
            pass
    else:
        mode='light'
        modeButton.configure(image=sun)
        root.configure(fg_color='#ffffff')
        try:
            HWND = windll.user32.GetParent(root.winfo_id())
            windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(0x0000FF)), sizeof(c_int))
        except:
            pass


#DARKMODE/LIGHTMODE BUTTON
modeButton=ctk.CTkButton(master=root,
                          fg_color='transparent',
                          text='',
                          corner_radius=10,
                          hover_color='#dddddd',
                          height=10,
                          width=17,
                          anchor='e',
                          image=sun,
                          compound='left',
                          command=modeChange)
modeButton.place(x=400, y=3)

qrCodeImageLabel = ctk.CTkLabel(master=sidePanel,
                                            fg_color='white',
                                            text='',
                                            height=128,
                                            width=128,
                                            corner_radius=10)
#= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

#RUN
if __name__ == '__main__':
    root.mainloop()
