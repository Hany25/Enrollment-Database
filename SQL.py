
import mysql.connector
from mysql.connector import errorcode

        
try:
  mysql_connection = mysql.connector.connect(host="localhost", user='root', passwd="Student123", database='fname_inf2070_projec_yiting')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Incorrect Username and/or Password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Specified schema does not exist")
  else:
    print("err")
else:
  print("DB and Schema connections were successful")
no=0
while no==0:
  qweqwe=input("would you like to start, y or n")
  if qweqwe=="n":
    no=1
  if qweqwe=="y":
    z=0
    while z==0:
        print("what would you like to do, please type as shown")
        action=(input("(add_student, change_class, change_grade, remove_student, unenroll_student,delete_student, reenroll)"))
        if action.isdigit()==False:
            action.lower()
            if action=="add_student" or action=="change_class" or action=="change_grade" or action=="remove_student" or action=="unenroll_student" or action=="delete_student" or action=="reenroll":
                z=1

    if action=="add_student":
            student_id=0
            templist=[]
            user_input=""
            good=0
            name=""
            randomvar=[]
            x=0
            randomlist=[]
            fk_student_time=0
            mysql_cursor = mysql_connection.cursor()
            mysql_query=("select time_name from times")
            mysql_cursor.execute(mysql_query)
            while not name:
              name=input("name?").strip().capitalize()
            for time_name in mysql_cursor:
              randomvar.append(time_name)
            while x==0:
                for i in range(len(randomvar)):
                  print(randomvar[i][0])
                user_input=str(input("period? Choose from option above")).upper()
                for i in range(len(randomvar)):
                  if randomvar[i][0]==user_input:
                    x=1
            if user_input:
                randomlist=[user_input]
                mysql_query=("select timeID from times where time_name=(%s)")
                mysql_cursor.execute(mysql_query, randomlist)
                randomvar.clear()
                for timeID in mysql_cursor:
                  randomvar.append(timeID)
                mysql_query =('Select Count(studentID) as student_row_count from students')
                mysql_cursor.execute(mysql_query)
                for (student_row_count) in mysql_cursor:
                    if int(student_row_count[0]) == 0:
                        student_id=1
                        print("Your studentID is", str(student_id))
                    else:
                        mysql_query =("select max(studentID) as Max_studentID From students")
                        mysql_cursor.execute(mysql_query)
                        for (max_studentID) in mysql_cursor:
                            student_id = int(max_studentID[0]) + 1 
                        print("Your studentID is", str(student_id))
                    student_name=("Student_"+str(student_id))
                random_var=[student_id,student_name,randomvar[0][0], 1]
                
            if student_name and student_id>0 and randomvar[0][0]>0:
                mysql_query= ("Insert Into students values (%s, %s, %s, %s)")
                mysql_cursor.execute(mysql_query, random_var)
                mysql_connection.commit()
                good=1
                
            if good==1:
                module=[]
                randomvar=0
                eid=0
                eid_list=[]
                varry=[]
                mysql_query=("select compsci_name from compsci")
                mysql_cursor.execute(mysql_query)
                for compsci_name in mysql_cursor:
                  varry.append(compsci_name)
                while randomvar==0:
                  for i in range(len(varry)):
                    print(varry[i][0])
                  classes=input("what Class Choose from option above: ")
                  if classes.isdigit():
                      classes=int(classes)
                      for i in range(len(varry)):
                        if classes==int(varry[i][0]):
                          randomvar=1
                          secondvar=[classes]
                mysql_query=("select compsciID from compsci where compsci_name=(%s)")
                mysql_cursor.execute(mysql_query, secondvar)
                varry.clear()
                for compsciID in mysql_cursor:
                  varry.append(compsciID)
            
                second_randomvar=[varry[0][0]]
                mysql_query=("select MC_ID from modules_compsci where fk_MC_CSID=(%s)")
                mysql_cursor.execute(mysql_query, second_randomvar)
                for MC_ID in mysql_cursor:
                    module.append(MC_ID)
                mysql_query=("Select count(EID) as eid_row_count from enrollment")
                mysql_cursor.execute(mysql_query)
                for (eid_row_count) in mysql_cursor:
                    if int(eid_row_count[0])==0:
                        eid=1
                        eid_list.append(eid)
                        print("Your EID is", str(eid))
                    else:
                        mysql_query=("select max(EID) as max_eid from enrollment")
                        mysql_cursor.execute(mysql_query)
                    for (max_eid) in mysql_cursor:
                          eid= int(max_eid[0]) + 1
                    for j in range(5):
                            eid_list.append(eid)
                            eid+=1
                    print("Your EID is", str(eid_list))
                module.sort()
                eid_list.sort()
                for i in range(5):
                  randomlist=[student_id, module[i][0], 0, 0, 0, eid_list[i]]
                  mysql_query=("insert into enrollment values (%s, %s, %s, %s, %s, %s)")
                  mysql_cursor.execute(mysql_query, randomlist)
                  mysql_connection.commit()
                  randomlist.clear()
             
    elif action=="change_class":
            module=[]
            randomvar=0
            eid=0
            eid_list=[]
            y=0
            savingstuff=[]
            varry=0
            saving=[]
            yiting_t=[]
            counter1=0
            randomlist=[]
            listdam=[]
            noname=[]
            counterreal=0
            neededlist=[]
            savingmodule=[]
            savingmcid=[]
            y=0
            varry=0
            
            while y==0:
                  student_id=input("what is your student ID")
                  if student_id.isdigit():
                      y=1
                      student_id=int(student_id)
            mysql_cursor = mysql_connection.cursor()
            mysql_query=("select max(studentID) as Max_studentID From students")
            mysql_cursor.execute(mysql_query)
            for (Max_studentID) in mysql_cursor:
                    varry=int(Max_studentID[0])
            if student_id>varry:
                    print("sorry you are not in our school")
            elif student_id<=varry:
              rand=[student_id]
              mysql_query=("select inorout from students where studentID=(%s)")
              mysql_cursor.execute(mysql_query, rand)
              rand.clear()
              for inorout in mysql_cursor:
                  rand.append(inorout)
              if rand[0][0]==1:
                student_idremove=[student_id]
                mysql_query=("select EID from enrollment where fk_MCS_S=(%s)")
                mysql_cursor.execute(mysql_query, student_idremove)
                asdqwe=0
                for EID in mysql_cursor:
                  saving.append(EID)

                for i in range(len(saving)):
                      if saving[i][0]%5==1 or saving[i][0]==1:
                        listdam.append(saving[i][0])
                        listdam=[saving[i][0]]
                        mysql_query=("select fk_MCS_MC from enrollment where EID=(%s)")
                        mysql_cursor.execute(mysql_query, listdam)
                        for fk_MCS_MC in mysql_cursor:
                          noname.append(fk_MCS_MC)
                        rando=[noname[0][0]]
                        noname.clear()
                        mysql_query=("select fk_MC_CSID from modules_compsci where MC_ID=(%s)")
                        mysql_cursor.execute(mysql_query, rando)
                        for fk_MC_CSID in mysql_cursor:
                          noname.append(fk_MC_CSID)
                        rando=[noname[0][0]]
                        mysql_query=("select compsci_name from compsci where compsciID=(%s)")
                        mysql_cursor.execute(mysql_query, rando)
                        noname.clear()
                        for compsci_name in mysql_cursor:
                          noname.append(compsci_name)
                        jk=0
                        while jk==0:
                          for i in range(len(noname)):
                            print(noname[i][0])
                            userasd=input("please choose an option(spell exactly as it says)")
                            for i in range(len(noname)):
                                if noname[i][0]==userasd:
                                  savingclassreal=userasd
                                  jk=1
                asdqwe=0

                if asdqwe==0:
                      sighlist=[]
                      pleasebedone=[]
                      randomlist=[userasd]
                      rando.clear()
                      mysql_query=("select compsciID from compsci where compsci_name=(%s)")
                      mysql_cursor.execute(mysql_query,randomlist)
                      for compsciID in mysql_cursor:
                        rando.append(compsciID)
                      randomlist=[rando[0][0]]
                      mysql_query=("select MC_ID from modules_compsci where fk_MC_CSID=(%s)")
                      mysql_cursor.execute(mysql_query, randomlist)
                      rando.clear()
                      for MC_ID in mysql_cursor:
                        neededlist.append(MC_ID)
                      for i in range(len(neededlist)):
                        randomlist=[neededlist[i][0],student_id]
                        mysql_query=("select EID from enrollment where fk_MCS_MC=(%s) and fk_MCS_S=(%s)")
                        mysql_cursor.execute(mysql_query, randomlist)
                        rando.clear()

                        for EID in mysql_cursor:
                          
                          rando.append(EID)
                        for s in range(len(rando)):
                            randomlist=[rando[s][0]]
                            mysql_query=("select project from enrollment where EID=(%s)")
                            mysql_cursor.execute(mysql_query, randomlist)
                            for project in mysql_cursor:
                              yiting_t.append(project)
                            for i in range(len(yiting_t)):
                              if yiting_t[i][0]!=0:
                                  counter1+=1
                            yiting_t.clear()
                            mysql_query=("select Test from enrollment where EID=(%s)")
                            mysql_cursor.execute(mysql_query, randomlist)
                            for Test in mysql_cursor:
                              yiting_t.append(Test)
                            for i in range(len(yiting_t)):
                              if yiting_t[i][0]!=0:
                                counter1+=1
                            yiting_t.clear()
                            mysql_query=("select Classwork from enrollment where EID=(%s)")
                            mysql_cursor.execute(mysql_query, randomlist)
                            for Classwork in mysql_cursor:
                              yiting_t.append(Classwork)
                            for i in range(len(yiting_t)):
                              if yiting_t[i][0]!=0:
                                counter1+=1
                            if counter1>0:
                              counterreal+=1
                            if counter1==0:
                              sighlist.append(rando[s][0])
                            if 0<counter1<3:
                              pleasebedone.append(rando)
                            if counter1==3:
                              randomlistqwe=[rando[s][0]]
                              mysql_query=("select fk_MCS_MC from enrollment where EID=(%s)")
                              mysql_cursor.execute(mysql_query, randomlistqwe)
                              randomlistqwe.clear()
                              for fk_MCS_MC in mysql_cursor:
                                randomlistqwe.append(fk_MCS_MC)
                              for i in range(len(randomlistqwe)):
                                savingmcid.append(randomlistqwe[i][0])
                            counter1=0
                            yiting_t.clear()
                      randomvar123=1
                      if len(pleasebedone)!=0:
                        counterreall=""
                        randomvar123=0
                        print("Please finish your module before changing")
                      if randomvar123==1:
                        if counterreal==0:
                          mysql_query=("delete from enrollment where fk_MCS_S=(%s)") 
                          mysql_cursor.execute(mysql_query, student_idremove)
                          mysql_connection.commit()
                          varry=[]
                          
                          mysql_query=("select compsci_name from compsci")
                          mysql_cursor.execute(mysql_query)
                          for compsci_name in mysql_cursor:
                            varry.append(compsci_name)
                          while randomvar==0:
                            for i in range(len(varry)):
                              print(varry[i][0])
                            classes=input("what Class Choose from option above: ")
                            if classes.isdigit():
                                classes=int(classes)
                                for i in range(len(varry)):
                                  if classes==int(varry[i][0]):
                                    randomvar=1
                                    secondvar=[classes]
                          mysql_query=("select compsciID from compsci where compsci_name=(%s)")
                          mysql_cursor.execute(mysql_query, secondvar)
                          varry.clear()
                          for compsciID in mysql_cursor:
                            varry.append(compsciID)
                    
                          second_randomvar=[varry[0][0]]
                          mysql_query=("select MC_ID from modules_compsci where fk_MC_CSID=(%s)")
                          mysql_cursor.execute(mysql_query, second_randomvar)
                          for MC_ID in mysql_cursor:
                              module.append(MC_ID)
                          print("Your EID are",saving)
                          saving.sort()
                          eid_list.sort()
                          for i in range(5):
                            randomlist=[student_id, module[i][0], 0, 0, 0, saving[i][0]]
                            mysql_query=("insert into enrollment values (%s, %s, %s, %s, %s, %s)")
                            mysql_cursor.execute(mysql_query, randomlist)
                            mysql_connection.commit()
                            randomlist.clear()

                        if counterreal!=0 and counterreal!="":
                            varry=[]
                            randomvar=0
                            mysql_query=("select compsci_name from compsci")
                            mysql_cursor.execute(mysql_query)
                            for compsci_name in mysql_cursor:
                              varry.append(compsci_name)
                            randrandlist=[]
                            for i in range(len(varry)):
                              randrandlist.append(varry[i][0])
                            randrandlist.remove(userasd)
                            while randomvar==0:
                              for i in range(len(randrandlist)):
                                print(randrandlist[i])
                              classes=input("what Class Choose from option above: ")
                              if classes.isdigit():
                                  classes=int(classes)
                                  for i in range(len(randrandlist)):
                                    if classes==int(randrandlist[i]):
                                      randomvar=1
                                      secondvar=[classes]
                            mysql_query=("select compsciID from compsci where compsci_name=(%s)")
                            mysql_cursor.execute(mysql_query,secondvar)
                            secondvar.clear()
                            for compsciID in mysql_cursor:
                              secondvar.append(compsciID)
                            idk2=[secondvar[0][0]]
                            mysql_query=("select fk_MC_MID from modules_compsci where fk_MC_CSID=(%s)")
                            mysql_cursor.execute(mysql_query,idk2)
                            thirdvar=[]
                            for fk_MC_MID in mysql_cursor:
                              thirdvar.append(fk_MC_MID)
                            actualsaveboth=[]
                            actualsaveone=[]
                            mysql_query=("select fk_MC_MID from modules_compsci where MC_ID=(%s)")
                            mysql_cursor.execute(mysql_query, savingmcid)
                            idk=[]
                            for fk_MC_MID in mysql_cursor:
                              idk.append(fk_MC_MID)
                            for i in range(len(idk)):
                              savingmodule.append(idk[i][0])
                            for i in range(len(savingmodule)):
                              for l in range(len(thirdvar)):
                                if savingmodule[i]==thirdvar[l][0]:
                                  actualsaveboth.append(savingmodule[i])
                            for i in range(len(actualsaveboth)):
                              for t in range(len(savingmodule)):
                                if actualsaveboth[i]!=savingmodule[t]:
                                  actualsaveone.append(savingmodule[t])
                            print(actualsaveone)
                            neededmodules=[]
                            for i in range(len(thirdvar)):
                              neededmodules.append(thirdvar[i][0])
                            for i in range(len(actualsaveboth)):
                              neededmodules.remove(actualsaveboth[i])
                            otherlist=[]
                            for i in range(len(neededmodules)):
                              finallist=[neededmodules[i],idk2[0]]
                              print(finallist)
                              mysql_query=("select MC_ID from modules_compsci where fk_MC_MID=(%s) and fk_MC_CSID=(%s)")
                              mysql_cursor.execute(mysql_query,finallist)
                              for MC_ID in mysql_cursor:
                                otherlist.append(MC_ID)
                              print(otherlist)
                            mysql_query=("select max(EID) as EID From enrollment")
                            mysql_cursor.execute(mysql_query)
                            for (EID) in mysql_cursor:
                                    varry=int(EID[0])+1
                            for i in range(len(otherlist)):
                              finallist=[student_id,otherlist[i][0],0,0,0, varry]
                              mysql_query=("insert into enrollment values (%s, %s, %s, %s, %s, %s)")
                              mysql_cursor.execute(mysql_query, finallist)
                              mysql_connection.commit()
                              varry+=1
                              randomlist.clear()
                            print(sighlist)
                            for i in range(len(sighlist)):
                                finalistlist=[sighlist[i]]
                                mysql_query=("delete from enrollment where EID=(%s)")
                                mysql_cursor.execute(mysql_query, finalistlist)
                                mysql_connection.commit()

                            counterreal==""
                            sdf=1

                       

                      
    elif action=="delete_student":
            y=0
            varry=0
            while y==0:
                student_id=input("what is your student ID")
                if student_id.isdigit():
                    y=1
                    student_id=int(student_id)
            mysql_cursor = mysql_connection.cursor()
            mysql_query=("select max(studentID) as Max_studentID From students")
            mysql_cursor.execute(mysql_query)
            for (Max_studentID) in mysql_cursor:
              
                varry=int(Max_studentID[0])
            if student_id>varry:
                print("sorry you are not in our school")
            elif student_id<=varry:
                rand=[student_id]
                mysql_query=("select inorout from students where studentID=(%s)")
                mysql_cursor.execute(mysql_query, rand)
                rand.clear()
                for inorout in mysql_cursor:
                  rand.append(inorout)
                if rand[0][0]==0:
                  student_idremove=[student_id]
                  mysql_query=("delete from enrollment where fk_MCS_S=(%s)")
                  mysql_cursor.execute(mysql_query, student_idremove)
                  mysql_connection.commit()
                  mysql_query=("delete from students where studentId=(%s)")
                  mysql_cursor.execute(mysql_query, student_idremove)
                  mysql_connection.commit()
                  print("you are removed from the school")
                elif rand[0][0]==1:
                  print("sorry you are enrolled in are school please reenroll to be removed")
                
    elif action=="unenroll_student":
          y=0
          varry=0
          while y==0:
                student_id=input("what is your student ID")
                if student_id.isdigit():
                    y=1
                    student_id=int(student_id)
          mysql_cursor = mysql_connection.cursor()
          mysql_query=("select max(studentID) as Max_studentID From students")
          mysql_cursor.execute(mysql_query)
          for (Max_studentID) in mysql_cursor:
                varry=int(Max_studentID[0])
          if student_id>varry:
                print("sorry you are not in our school")
          elif student_id<=varry:
                rand=[student_id]
                student_idremove=[0,student_id]
                mysql_query=("select inorout from students where studentID=(%s)")
                mysql_cursor.execute(mysql_query, rand)
                rand.clear()
                for inorout in mysql_cursor:
                  rand.append(inorout)
                if rand[0][0]==1:
                  mysql_query=("UPDATE students SET inorout = (%s) WHERE studentID=(%s)")
                  mysql_cursor.execute(mysql_query, student_idremove)
                  mysql_connection.commit()
                  print("you are removed from the school")
                elif rand[0][0]==0:
                  print("sorry you are already unenrolled")
                  
    elif action=="reenroll":
          y=0
          varry=0
          while y==0:
                student_id=input("what is your student ID")
                if student_id.isdigit():
                    y=1
                    student_id=int(student_id)
          mysql_cursor = mysql_connection.cursor()
          mysql_query=("select max(studentID) as Max_studentID From students")
          mysql_cursor.execute(mysql_query)
          for (Max_studentID) in mysql_cursor:
                varry=int(Max_studentID[0])
          if student_id>varry:
                print("sorry you are not in our school")
          elif student_id<=varry:
                student_idremove=[1,student_id]
                rand=[student_id]
                mysql_query=("select inorout from students where studentID=(%s)")
                mysql_cursor.execute(mysql_query, rand)
                rand.clear()
                for inorout in mysql_cursor:
                  rand.append(inorout)
                if rand[0][0]==1:
                  mysql_query=("UPDATE students SET inorout = (%s) WHERE studentID=(%s)")
                  mysql_cursor.execute(mysql_query, student_idremove)
                  mysql_connection.commit()
                  print("you are removed from the school")
                elif rand[0][0]==0:
                  print("sorry you are already unenrolled")


      
    elif action=="change_grade":
          y=0
          varry=0
          modulelist=[]
          randomlist=[]
          middlelist=[]
          listextra=[]
          m=0
          d=0
          l=0
          while y==0:
                student_id=input("what is your student ID")
                if student_id.isdigit():
                    y=1
                    student_id=int(student_id)
          mysql_cursor = mysql_connection.cursor()
          mysql_query=("select max(studentID) as Max_studentID From students")
          mysql_cursor.execute(mysql_query)
          for (Max_studentID) in mysql_cursor:
                varry=int(Max_studentID[0])
          if student_id>varry:
                print("sorry your are not in are school")
          elif student_id<=varry:
            student_idremove=[1,student_id]
            rand=[student_id]
            mysql_query=("select inorout from students where studentID=(%s)")
            mysql_cursor.execute(mysql_query, rand)
            rand.clear()
            for inorout in mysql_cursor:
                  rand.append(inorout)
            if rand[0][0]==1:
                student_idcheck=[student_id]
                mysql_query=("select fk_MCS_MC from enrollment where fk_MCS_S=(%s)")
                mysql_cursor.execute(mysql_query, student_idcheck)
                for (fk_MCS_MC) in mysql_cursor:
                  modulelist.append(fk_MCS_MC)
                for i in range(5):
                  listrandom=[modulelist[i][0]]
                  mysql_query=("select fk_MC_MID from modules_compsci where MC_ID=(%s)")
                  mysql_cursor.execute(mysql_query, listrandom)
                  for fk_MCS_MC in mysql_cursor:
                    randomlist.append(fk_MCS_MC)
                  listrandom.clear()
                for i in range(5):
                  listrandom=[randomlist[i][0]]
                  mysql_query=("select Module_name from modules where modulesID=(%s)")
                  mysql_cursor.execute(mysql_query, listrandom)
                  for Module_name in mysql_cursor:
                    middlelist.append(Module_name)
                  listrandom.clear()
                while m==0:
                  print(middlelist)
                  print("Plese capitalize")
                  var=input("Please choose which module")
                  for i in range(len(middlelist)):
                    if middlelist[i][0]==var:
                      m=1
                listrandom=[var]
                mysql_query=("select modulesID from modules where Module_name=(%s)")
                mysql_cursor.execute(mysql_query, listrandom)
                listrandom.clear()
                for modulesID in mysql_cursor:
                  listrandom.append(modulesID)
                listrandom2=[listrandom[0][0]]
                mysql_query=("select MC_ID from modules_compsci where fk_MC_MID=(%s)")
                mysql_cursor.execute(mysql_query, listrandom2)
                listrandom2.clear()
                listrandom.clear()
                for (MC_ID) in mysql_cursor:
                  listrandom.append(MC_ID)
                for i in range(len(listrandom)):
                  for k in range(len(modulelist)):
                    if modulelist[k][0]==listrandom[i][0]:
                      listextra=[modulelist[k][0]]
                      inconvient=listextra[0]

                listrandom.clear()
                keepgoing=0
                pop=0
                while keepgoing==0:
                  pop=0
                  while pop==0:
                    print("would you like to change classwork, project or test")
                    user=input("please choose option exact as shown above")
                    if user=="classwork" or user=="project" or user=="test":
                      pop=1
                  listrandom=[inconvient, student_id]
                  if user=="classwork":
                    mysql_query=("select Classwork from enrollment where fk_MCS_MC=(%s) and fk_MCS_S=(%s)")
                    mysql_cursor.execute(mysql_query, listrandom)
                    listrandom2.clear()
                    for Classwork in mysql_cursor:
                      listrandom2.append(Classwork)
                    while d==0:
                      print("Current grade in classwork is ",listrandom2[0][0])
                      randomstuff=input("what would you like your grade to be")
                      if randomstuff.isdigit():
                        randomstuff=int(randomstuff)
                        if randomstuff>100:
                          print("Im sorry your grade cannot be above 100")
                          randomstuff=""
                        elif randomstuff<=100:
                          d=1
                    listextra=[randomstuff, listrandom[0], listrandom[1]]
                    mysql_query=("UPDATE enrollment SET Classwork = (%s) WHERE fk_MCS_MC=(%s) and fk_MCS_S=(%s)")
                    mysql_cursor.execute(mysql_query, listextra)
                    mysql_connection.commit()
                    listextra.clear()
                    listrandom2.clear()
                    d=0
                  if user=="project":
                    mysql_query=("select project from enrollment where fk_MCS_MC=(%s) and fk_MCS_S=(%s)")
                    mysql_cursor.execute(mysql_query, listrandom)
                    listrandom2.clear()
                    for project in mysql_cursor:
                      listrandom2.append(project)
                    while d==0:
                      print("Current grade in project is ",listrandom2[0][0])
                      randomstuff=input("what would you like your grade to be")
                      if randomstuff.isdigit():
                        randomstuff=int(randomstuff)
                        if randomstuff>100:
                          print("Im sorry your grade cannot be above 100")
                          randomstuff=""
                        elif randomstuff<=100:
                          d=1
                    listextra=[randomstuff, listrandom[0], listrandom[1]]
                    mysql_query=("UPDATE enrollment SET project = (%s) WHERE fk_MCS_MC=(%s) and fk_MCS_S=(%s)")
                    mysql_cursor.execute(mysql_query, listextra)
                    mysql_connection.commit()
                    listextra.clear()
                    listrandom2.clear()
                    d=0
                  if user=="test":
                    mysql_query=("select Test from enrollment where fk_MCS_MC=(%s) and fk_MCS_S=(%s)")
                    mysql_cursor.execute(mysql_query, listrandom)
                    listrandom2.clear()
                    for Test in mysql_cursor:
                      listrandom2.append(Test)
                    while d==0:
                      print("Current grade in test is ",listrandom2[0][0])
                      randomstuff=input("what would you like your grade to be")
                      if randomstuff.isdigit():
                        randomstuff=int(randomstuff)
                        if randomstuff>100:
                          print("Im sorry your grade cannot be above 100")
                          randomstuff=""
                        elif randomstuff<=100:
                          d=1
                    listextra=[randomstuff, listrandom[0], listrandom[1]]
                    mysql_query=("UPDATE enrollment SET Test = (%s) WHERE fk_MCS_MC=(%s) and fk_MCS_S=(%s)")
                    mysql_cursor.execute(mysql_query, listextra)
                    mysql_connection.commit()
                    listextra.clear()
                    listrandom2.clear()

                  users=input("keepgoing yes or no")
                  if users=="yes":
                    keepgoing=0
                  elif users=="no":
                    keepgoing=1
                  print("successful")
                
                
                
                  
mysql_connection.close()


