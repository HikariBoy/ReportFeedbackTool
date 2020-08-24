# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:43:39 2020

@author: akeating
"""

#!/usr/bin/python3
from ctypes import *
import tkinter as tk
import tkinter.font as tkFont
from tkinter.ttk import Progressbar
import yaml
 

__author__="Adrian Keating(UWA)"
__version__ = "0.1.1"
selections=[]

def allstates():
       print(list(lng.state()) )


class Checkbar(tk.Frame):
   def __init__(self, parent=None, picks=[],side="left", anchor="w", background='white'):
      tk.Frame.__init__(self, parent,background='white', )
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
         chk = tk.Checkbutton(self, borderwidth=3,text=newpick, variable=var,background='white',justify = "left")
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
        tk.Frame.__init__(self, parent,bg="white", *args, **kwargs)
        self.parent = parent
        self.pack(fill="both", side="top",expand=True)
        N=len(Rubric)
        M=int(N/3)+1
        frame=[0]*M
        for indx in range(M):
            frame[indx]=tk.Frame(self,bg="white",bd=0,width=0)
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
        width5scaled=int(scale*10)
        self.btn = tk.Button(frame1, text='Accept&Copy',bd=bd12scaled, width=width5scaled*2,height=int(scale), relief="raised",command=setText)
        self.btn.pack({"side": "left"},expand=True)
        self.btn.pack(pady=1)
        #print(hlpbtnimg)
        btn1b = tk.Button(frame1, text='Copy',bd=bd12scaled, width=width5scaled,height=int(scale), relief="raised",command=CopyText)
        #btn2.pack(weight=1)
        btn1b.pack({"side": "left"},expand=True)
        btn1b.pack(pady=1)
        #hlpbtn = tk.Button(frame1, text='Help', bd=0,image=hlpbtnphoto, command=viewpdf)
        #hlpbtn.pack({"side": "left"},expand=True)
        #hlpbtn.pack(pady=5)
                ###Create button
        btn2 = tk.Button(frame1, text='EXIT',bd=bd12scaled, width=width5scaled,height=int(scale), relief="raised",command=gracefullexit)
        #btn2.pack(weight=1)
        btn2.pack({"side": "right"},expand=True)
        btn2.pack(pady=1)
        #fm.pack(fill=BOTH, expand=YES)
        #print("about to exit")
        #return




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
 
if __name__ == '__main__':
   windll.shcore.SetProcessDpiAwareness(c_int(1))
   if getattr(sys, 'frozen', False): # Running as compiled
       running_dir = sys._MEIPASS + '\\'
       # Same path name than pyinstaller option
   else:
       running_dir = r'.\\' # Path name when run with Python interpreter
   
   configfile='configList.yaml'
   with open(configfile,'r', encoding='utf8') as f:
        # utf-8 required to load accented text such as André-Marie Ampère
        try:
            # with open(config, 'rt', encoding='utf8') as yml:
            # config_obj = yaml.load(yml)
            GradingConfigData = yaml.load(f, Loader=yaml.FullLoader)
            for eachvariable in  (GradingConfigData['constants'].keys()):
                locals()[eachvariable]=GradingConfigData['constants'][eachvariable]

        except (NameError) as error:
            print('A key in the file '+configfile+' is not understood')
            raise
        except:
            raise
            
   selections=GradingConfigData['constants'][Rubric[0]]


   if getattr(sys, 'frozen', False): # Running as compiled
       running_dir = sys._MEIPASS + '\\'
       # Same path name than pyinstaller option
   else:
       running_dir = r'.\\' # Path name when run with Python interpreter
   root = tk.Tk()
   v = tk.IntVar()

   root.after(0, root.focus_force())
   root.wm_attributes('-fullscreen', 'False')
   root.call('wm', 'attributes', '.', '-topmost', '1')

   if (1):
       Wmain=root.winfo_screenwidth()
       Hmain=root.winfo_screenheight()
       scale=1*Hmain/1800
       w=int(200*scale)
       h=int(660*w/1100)
       fontsize=int(9*scale)
       root.configure(width=w, height=h)  #root.geometry("300x200+300+300")
       Magnify=10
       root.option_add("*Font", "helvetica "+str(fontsize)+" bold")
       root.title('Grading Tool ('+str(__version__)+') - By Dr. Adrian Keating (C) UWA, 2020')
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
