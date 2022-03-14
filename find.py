from itertools import count
from pickle import TRUE
from numpy import size
import pandas as pd
from datetime import datetime
import time
from dateutil.parser import parse


"""
            notInSiteMsp - the function check for specific site, if the tasks that in the portal not exist in the client file
@param equipment - List of the equipment name
@param activity - List of the TaskID from the portals .
@param sitename - the name of the site , using for searching
@param sitetasksID - List of the taskID from the client file.
@param tasksNotInMsp- the text file where the output will print.
@param site_number - represent the site that the USER want to check.
"""
def notInSiteMsp(equipment,activity,sitename,sitetasksID_list,tasksNotInMsp,site_number):
    flag=False
    counter=0
    for i in range(0,len(equipment)):
       
        if(sitename[i]==site_number):
            for k in range(0,len(sitetasksID_list)):
                if(sitetasksID_list[k]==activity[i]):
                    flag=TRUE
            if(flag == False):
                counter+=1
                tasksNotInMsp.write(activity[i]+'\n')
            flag=False
    tasksNotInMsp.write("total tasks that exist in mobideo but not in MSP"+str(counter))

"""
            findDuplicatesAllSites - the function check for all the duplicated tasks that exist in the portal.
@param Name_list - List of all the Activity Name from the portal.
@param equipment - List of all the equipment from the portals .
@param employee - the of all the employee from the site.
@param f - the file where the output will be printed.

"""
def findDuplicatesAllSites(Name_list,equipment,employee,f):
    counter=0
    print("total from poly "+ str(counter))
    for i in range(0,len(equipment)):
        print(i)
        for k in range(i,len(equipment)):
            if(i!=k and Name_list[i]==Name_list[k] and equipment[i]==equipment[k]and employee[i]==employee[k] ):
                counter+=1
                f.write(Name_list[i] +' '+ equipment[i]+' '+ employee[i]+ ' '+Name_list[i]+ "\n")
                f.write(Name_list[k] +' '+ equipment[k]+' '+employee[k]+' '+Name_list[k]+  "\n" )
                f.write("*******************"+ "\n")
             
    f.write(str(counter))
    f.write(" duplicated tasks founded")
    

"""
        checkStatusProblem- the function checks for all the tasks that their status not correct with regard to the current date.
        @param tasks_status - list of all the status of the tasks
        @param date_start - list of the date start for every task
        @paran activity - list of all the TaskID for printing to file the results.
"""
def checkStatusProblem(tasks_status,date_start,activity):
    tasksTimeError = open("tasksTimeError.txt","w")
    now = datetime.now()
    print("now =", now)
    dt_string = now.strftime("%m/%d/%Y")
    print("date and time =", dt_string)	
    d1=pd.to_datetime(dt_string)
    counter=0
    for i in range(0,len(tasks_status)):
        date_time_obj = date_start[i]
        d2=pd.to_datetime(date_time_obj)
        if(d1>d2 and tasks_status[i]=="Not started" ):
            tasksTimeError.write(activity[i])
            counter+=1
    tasksTimeError.write("total tasks : " + str(counter))



