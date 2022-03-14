from cgitb import text

from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox

#from click import command
from numpy import place
import find
import pandas as pd

window=Tk()
window.geometry("400x500")
window.title("MOBIDEO CSS HELPER")

def activate():
    filename=fd.askopenfilename()
    data = pd.read_csv(filename, encoding='utf-8')
    Name_list = data["Activity Name"].tolist()
    equipment=data["Equipment"].tolist()
    employee=data["Employee"].tolist()
    f = open("duplicatesInAllSites.txt", "w") #the file to output the result
    find.findDuplicatesAllSites(Name_list,equipment,employee,f)
    messagebox.showinfo("file with data created")
    
def chooseFile(label):
    filename=fd.askopenfilename()
    label.config(text=filename)

def findstrange(urlalltasks,urlsite,siteNmber):
     sitenum=siteNmber[:-1]
     sitedata = pd.read_csv(urlsite, encoding='utf-8')
     tasksNotInMsp = open("TasksNotInMsp.txt","w")
     sitetasks=sitedata["TaskID"].tolist()
     alldata = pd.read_csv(urlalltasks, encoding='utf-8')
     equipment=alldata["Equipment"].tolist()
     activity=alldata["Activity ID"].tolist()
     sitename=alldata["Site_Name"].tolist()
     find.notInSiteMsp(equipment,activity,sitename,sitetasks,tasksNotInMsp,sitenum) 
     messagebox.showinfo("done")

def checkStatus(allsitesurl):
    data = pd.read_csv(allsitesurl, encoding='utf-8')
    date_start=data["Planned Start"].tolist()
    tasks_status=data["Status"].tolist()
    activity=data["Activity ID"].tolist()
    find.checkStatusProblem(tasks_status,date_start,activity)
    messagebox.showinfo("done")


find_dup_btn=Button(window,text="find all duplicates",height = 3, width = 16,command=activate)
find_dup_btn.place(relx=0.2,rely=0.1)

find_strange_tasks=Button(window,text="Find strange tasks",height = 3, width = 16,command=lambda: findstrange(label_all_tasks['text'],label_file['text'],site_name.get("1.0",END)))
find_strange_tasks.place(relx=0.20,rely=0.6)



label_all_tasks=Label(window,text="No file")
label_all_tasks.place(relx=0.20 , rely=0.40)

add_all_tasks=Button(window,text="Add all tasks",command= lambda :chooseFile(label_all_tasks))
add_all_tasks.place(relx=0.20,rely=0.35)

label_file=Label(window,text="No file")
label_file.place(relx=0.20 , rely=0.5)

add_file=Button(window,text="Add file to check",command=lambda :chooseFile(label_file))
add_file.place(relx=0.20,rely=0.45)

site_name=Text(window,height=1,width=4)
site_name.delete("1.0",END)
site_name.insert(END,"0")
site_name.place(relx=0.55 , rely= 0.45)

tasks_status_btn=Button(window,text="find status eror",height = 3, width = 16,command=lambda :checkStatus(label_all_tasks['text']))
tasks_status_btn.place(relx =0.20 , rely =0.80 )

window.mainloop()