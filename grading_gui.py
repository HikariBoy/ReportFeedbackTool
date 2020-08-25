# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:43:39 2020

@author: akeating
"""

#!/usr/bin/python3
from ctypes import *
import tkinter as tk
from tkinter import messagebox
#import tkinter.messagebox as  messagebox
import tkinter.font as tkFont
from tkinter.ttk import Progressbar
import yaml
import sys,os
 

__author__="Adrian Keating(UWA)"
__version__ = "0.1.1"
selections=[]


class MyError(tk.Toplevel):
    def __init__(self, message):
        tk.Toplevel.__init__(self)
        tk.Label(self, text=message).grid(row=0, column=0)
        tk.Button(self, command=self.destroy, text="OK").grid(row=1, column=0)
        self.lift()  # Puts Window on top
        self.grab_set()  # Prevents other Tkinter windows from being used


def showerror(string):
    MyError(string)
    
class ConfigError(Exception):
    pass

def allstates():
       print(list(lng.state()) )


class Checkbar(tk.Frame):
   def __init__(self, parent=None, picks=[],side="left", anchor="w", background='light yellow'):
      tk.Frame.__init__(self, parent,background='light yellow', )
      self.Frame1=tk.Frame
      self.vars = []
      self.listpicks=picks[::-1]  # COPIES and reverses the list and stores
      picks.reverse()  # reverse the list

      self.check_box_list=[]
      self.updatelist(picks)
      """
      for index,pick in enumerate(picks,start=0):
         var = tk.IntVar(value=flags[len(picks)-1-index])
         chk = tk.Checkbutton(self, borderwidth=3,text=pick, variable=var,background='white')
         chk.pack(side="bottom", anchor=anchor, expand="yes",pady=bd2scaled)
         self.vars.append(var)
      """
   def clearlist(self):
       for i in self.check_box_list:
            #if i.winfo_exists():    # Checks if the widget exists or not
            i.pack_forget()     # forget checkbutton
                # i.destroy()        # use destroy if you dont need those checkbuttons in future
       self.check_box_list=[]
       self.vars=[]
    
        
   def updatelist(self,picks):
       flags=[0]*len(picks)
       self.listpicks=picks[::-1]  # COPIES and reverses the list and stores
       #picks.reverse()  # reverse the list
       #print(self.check_box_list)
       #print(picks)
       self.clearlist()
       var=[]
       #picks.reverse()  # reverse the list
       #scale=2
       bd2scaled=int(2*scale)

       for index,pick in enumerate(picks,start=0):
         var = tk.IntVar(value=flags[len(picks)-1-index])
         starti=0
         endi=0
         NN=int(w/4)
         newpick=''
         while endi<len(pick):
             endi=starti+NN
             findspace=pick[endi:].split()
             if (len(findspace)>0):
                 extra=len(findspace[0])+1
             else:
                 extra=0
             endi=endi+extra
             if(endi<len(pick)):
                 newpick=newpick+pick[starti:endi]+'\n'
             else:
                 newpick=newpick+pick[starti:endi]
             starti=endi
         #if(endi>0):
         #    newpick=newpick[0:-1]
         chk = tk.Checkbutton(self, borderwidth=3,text=newpick, variable=var,background='light yellow',justify = "left")
         chk.pack( anchor='w')
         self.check_box_list.append(chk)
         self.vars.append(var)

       
   def state(self):
       statepicks=list(map((lambda var: var.get()), self.vars))
       statepicks.reverse()
       return statepicks


class RadioFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ###call the parent constructor
        tk.Frame.__init__(self, parent,bg="light blue", *args, **kwargs)
        self.parent = parent
        self.pack(fill="both", side="top",expand=True)
        N=len(Rubric)
        M=int(N/3)+1
        frame=[0]*M
        for indx in range(M):
            frame[indx]=tk.Frame(self,bg="light blue",bd=0,width=0)
            frame[indx].pack(fill="both",expand=True)
        frame1=tk.Frame(self,bg="white",bd=0,width=0) 
        frame2=tk.Frame(self,bg="white",bd=0,width=0)
        frame3=tk.Frame(self,bg="white",bd=0,width=0)
        #frame1.pack(fill="both",side="left",expand=True)
        frame1.pack(fill="both",expand=True)
        frame2.pack(fill="both",expand=True)
        frame3.pack(fill="both",expand=True)
        self.parent = parent
        for val, language in enumerate(Rubric):
            indx=int(val/3)
            tk.Radiobutton(frame[indx], 
                          text=language,
                          padx = 1, 
                          bg="light blue",
                          variable=v, 
                          command=ShowChoice,
                          value=val).pack(side="left")
        v.set(0)

        
class StartEndAppFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ###call the parent constructor
        tk.Frame.__init__(self, parent,bg="white", *args, **kwargs)
        self.parent = parent
        self.pack(fill="both", side="top",expand=True)
        frame1=tk.Frame(self,bg="white",bd=0,width=0)
        #frame1.pack(fill="both",side="left",expand=True)
        frame1.pack(fill="both",expand=True)
        self.parent = parent
        #frame2=tk.Frame(self,bg="white",bd=0,width=0)
        #frame2.pack(fill="both",side="left",expand=True)
        ###Create button
                ###Create button
        #GradingProgress.start_progressbar()
        #GradingProgress.update()
        bd5scaled=int(5*scale)
        bd12scaled=int(8*scale)
        width20scaled=int(20*scale)
        width5scaled=int(fontsize*.8)
        scaleheight=max(int(fontsize/9),1)
        #print("scale",scale)
        #print("lenaccept",len('Accept&Copy'))
        #print("lenacopy",len('copy'))
        self.btn =createButton('Accept&Copy',frame1,setText)
        #self.btn = tk.Button(frame1, text='Accept&Copy',bd=bd12scaled, width=11,height=scaleheight, relief="raised",command=setText)
        self.btn.pack({"side": "left"},expand=True)
        self.btn.pack(pady=1)
        #print(hlpbtnimg)
        btn1b =createButton('Copy',frame1,CopyText)
        #btn1b = tk.Button(frame1, text='Copy',bd=bd12scaled, width=4,height=scaleheight, relief="raised",command=CopyText)
        #btn2.pack(weight=1)
        btn1b.pack({"side": "left"},expand=True)
        btn1b.pack(pady=1)
        #hlpbtn = tk.Button(frame1, text='Help', bd=0,image=hlpbtnphoto, command=viewpdf)
        #hlpbtn.pack({"side": "left"},expand=True)
        #hlpbtn.pack(pady=5)
                ###Create button
        btn2=createButton('EXIT',frame1,gracefullexit,mybg="pink")
        #btn2 = tk.Button(frame1, text='EXIT',bg="pink",bd=bd12scaled, width=width5scaled,height=scaleheight, relief="raised",command=gracefullexit)
        #btn2.pack(weight=1)
        btn2.pack({"side": "right"},expand=True)
        btn2.pack(pady=1)
        #fm.pack(fill=BOTH, expand=YES)
        #print("about to exit")
        #return


def createButton(btn_name,frame, function,mybg='light grey'):
    w=len(btn_name)+2
    bdscaled=int(fontsize)
    scaleheight=max(int(fontsize/9),1)
    btn = tk.Button(frame, bg=mybg,text=btn_name,bd=bdscaled, width=w,height=scaleheight, relief="raised",command=function)
    return btn

    def increament(self):
        ii=GradingProgress.progress_var.get()
        #ii=GradingProgress.progress["value"]
        time.sleep(0.05)
        #GradingProgress["value"] = ii+10
        GradingProgress.progress_var.set(ii+1)
        print("prog"+str(GradingProgress.progress["value"]))
        GradingProgress.progress.update()
        return


def gracefullexit():
    root.destroy()
    root.quit()
    #exit()

def setText():
    #print('lng',lng.state())
    #print('ggg',radios.state())
    text=''
    localselections=lng.listpicks
    text=Rubric[v.get()]+':\n'
    for index,each in enumerate(lng.state()):
        if (each==1):
            text=text+localselections[index]+'\n'
    SearchParams.insert(tk.END, text)
# copy to the clipboard
    #root.withdraw()
    result=SearchParams.get("1.0", "end")
    #print(result)
    root.clipboard_clear()
    root.clipboard_append(result)
    CopyText
    #root.update()

def CopyText():
    result=SearchParams.get("1.0", "end")
    print(result)
    root.clipboard_clear()
    root.clipboard_append(result)
    #root.update()

def ShowChoice():
    selections=GradingConfigData['constants'][Rubric[v.get()]]
    lng.updatelist(selections)

def mymessagebox(title, text):
    localroot = tk.Tk()
    localroot.overrideredirect(1)
    localroot.withdraw()
    messagebox.showinfo(title, text)
    localroot.destroy()
    
if __name__ == '__main__':
   windll.shcore.SetProcessDpiAwareness(c_int(1))
   if getattr(sys, 'frozen', False): # Running as compiled
       running_dir = sys._MEIPASS + '\\'
       # Same path name than pyinstaller option
   else:
       running_dir = r'.\\' # Path name when run with Python interpreter
   
   root = tk.Tk()
   #root.overrideredirect(1) # To avoid a "flash" as the root window is created, use this slight variation on the accepted answer
   configfile='configList.yaml'
   
   #texto = tk.Toplevel(root)
   #showerror("Help!")
   try:
       with open(configfile,'r', encoding='utf8') as f:
        # utf-8 required to load accented text such as André-Marie Ampère
        #try:
            # with open(config, 'rt', encoding='utf8') as yml:
            # config_obj = yaml.load(yml)
            GradingConfigData = yaml.load(f, Loader=yaml.FullLoader)
            for eachvariable in  (GradingConfigData['constants'].keys()):
                print(eachvariable)
                locals()[eachvariable]=GradingConfigData['constants'][eachvariable]




       for indx in range(len(Rubric)):
         # check each value exists
         GradingConfigData['constants'][Rubric[indx]]

       
       #raise ConfigError(ErrorMsg)
       #sys.exit(0)
       #exit(1)         
       selections=GradingConfigData['constants'][Rubric[0]]
    
    
       if getattr(sys, 'frozen', False): # Running as compiled
           running_dir = sys._MEIPASS + '\\'
           # Same path name than pyinstaller option
       else:
           running_dir = r'.\\' # Path name when run with Python interpreter
    
       v = tk.IntVar()
    
       root.after(0, root.focus_force())
       root.wm_attributes('-fullscreen', 'False')
       root.call('wm', 'attributes', '.', '-topmost', '1')
    
       if (1):
           Wmain=root.winfo_screenwidth()
           Hmain=root.winfo_screenheight()
           print(Wmain,Hmain)
           
    
           # Get the reported DPI from the window's HWND
           dpi = windll.user32.GetDpiForWindow(root.winfo_id())
           # Print the DPI
           print('dpi',dpi/96)
    
           scale=1*Hmain*2/((dpi/96)*1800)
           #scale=1*Hmain/(1800)
           w=int(150*scale)
           h=int(660*w/1100)
           fontsize=int(9*scale)
           print("fontsize",fontsize)
           root.configure(width=w, height=h)  #root.geometry("300x200+300+300") app.geometry("300x100")
           Magnify=10
           root.option_add("*Font", "helvetica "+str(int(fontsize))+" bold")
           root.title('Grading Tool ('+str(__version__)+')/Dr. A. Keating, UWA, 2020')
           root.configure(background='white')
           radios=RadioFrame(root)
           GoQuit=StartEndAppFrame(root)
           GoQuit.pack(side="top")
           if(1):
               lng = Checkbar(root, selections )
               #print(lng.state())
               lng.state() #tgl = Checkbar(root, ['English','German'])
               lng.pack(side="top",  fill="x") #(fill="both", expand=True)
               #tgl.pack(side="left")
               bd2scaled=int(2*scale)
               lng.config(relief="groove", bd=bd2scaled)
           if(1):
               print(w)
               SearchParams = tk.Text(root,wrap=tk.WORD,width=int(w/4),height=10)
               SearchParams.pack({"side": "top"})
           root.lift()
           #root.update()
       root.mainloop()
   except (NameError) as error:
        #raise ConfigError('A key in the file '+configfile+' is not understood. Please edit the file, checking spelling and format')
        ErrorMsg='A key in the file '+configfile+' is not understood. Please edit the file, checking spelling and format'
        #print('A key in the file '+configfile+' is not understood')
        #sys.exit(os.EX_OK)
        root.withdraw() # don't show root window
        root.attributes('-topmost', True)
        messagebox.showinfo("CONFIG FILE ERROR", ErrorMsg)
        gracefullexit()
   except (FileNotFoundError) as error:
        #raise ConfigError('The File '+configfile+' Could not be found.  Check it has been placed in teh same directory as the main program.')
        #print('A key in the file '+configfile+' is not understood')
        ErrorMsg='The File '+configfile+' Could not be found.  Check it has been placed in the same directory as the main program.'
        root.withdraw() # don't show root window
        root.attributes('-topmost', True)
        messagebox.showinfo("CONFIG FILE ERROR", ErrorMsg)
        gracefullexit()
   except Exception as e:
        #raise ConfigError('An Error occurred when reading the file: '+configfile +'\nSpecific Error is:'+e)
        ErrorMsg='An Error occurred when reading the file: '+configfile +'\nSpecific Error for unknow parameter is: '+str(e)

        #texto = tk.Toplevel(root)
        #texto.withdraw()
        #texto.attributes('-topmost', True) # don't use topmost command
        root.withdraw() # don't show root window
        root.attributes('-topmost', True)
        messagebox.showinfo("CONFIG FILE ERROR", ErrorMsg)
        #texto.destroy()
        #messagebox.showinfo("CONFIG FILE ERROR", ErrorMsg)
        gracefullexit()
        
   except (KeyError) as e:
        ErrorMsg='The unknown parameter is :'+str(e)
        ErrorMsg='Unknown value in the file: '+configfile +'. Check spelling and format\n'+ErrorMsg
        #showerror(ErrorMsg) 
        root.withdraw() # don't show root window
        root.attributes('-topmost', True)
        messagebox.showinfo("CONFIG FILE ERROR", ErrorMsg)
        gracefullexit()