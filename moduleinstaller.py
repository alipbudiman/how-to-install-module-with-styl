import os, sys

__author__ = "> Alif Budiman"
__idline__  = "\n> ID Line: alifbudimanwahabbi"
__status__ = "\n> Send bug if you find it!!!"

"""
CREDIT ________________________________

⌬   Creat with ❤️ by Alip
⌬   find me on LINE or IG
⌬   ID: alifbudimanwahabbi 
⌬   ID LINE: alifbudimanwahabbi
⌬   Whatsapp +6282113791904
⌬   You can DM me for any ask something or give a littlebit donations
⌬   Copyright 2021 by Alip  FXG TEAMS

# Free to use, all credits belong to me.
# Feel free to report bugs :)

"""

class CekINS(object):
    def __init__(self,pathfile=[],pipmodule=[],appmodule=[]):
        taskdone = []
        for file in pathfile:
            if file != str:
                cekfile = os.path.isfile(file)
                if cekfile:
                    pass
                    #pint(file, " in directory")
                else:
                    print(file, " not in directory")
                    #os.system("wget blabla..") < or something else
            else:
                print("Type data must string")
                continue
        print("Task1 done")
        taskdone.append("Task1 done")
        for pipers in pipmodule:
            if file != str:
                if pipers in sys.modules:
                    pass
                    #pint(file, " alredy installed")
                else:
                    #pint(file, " not installed")
                    try:
                        os.system(f"pip3 install {pipers}")
                        #os.system(f"sudo pip3 install {pipers}")
                        #os.system(f"pip install {pipers}")
                    except:
                        print(f"Oops... something went wrong with {pipers}")
                        continue
            else:
                print("Type data must string")
        print("Task2 done")
        taskdone.append("Task2 done")
        for modulers in appmodule:
            if modulers != str:
                cekapp = os.popen(f"which {modulers}").read()
                if cekapp:
                    pass
                    #pint(file, " alredy installed")
                else:
                    #pint(file, " not installed")
                    try:
                        os.system(f"apt install {cekapp}")
                    except:
                        print(f"Oops... something went wrong with {cekapp}")
                        continue
            else:
                print("Type data must string")
        print("Task3 done")
        taskdone.append("Task3 done")
        
        scoop_me_ice_cram = [__author__,__idline__,__status__]
        if scoop_me_ice_cram != []:
            for wanna_ice_cream in scoop_me_ice_cram:
                print(wanna_ice_cream)
        else:
            print("i'm mad woth u :(")
        
        print(taskdone)

# examples of use

myfile = ["CODING TEST/readme.md"]
mypipmodule = ["numpy"]
myappmodule = ["zip","unzip"]

CekINS(pathfile=myfile,pipmodule=mypipmodule,appmodule=myappmodule)
