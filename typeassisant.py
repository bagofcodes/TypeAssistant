import os

print("\n*******************************************************************************************************************************************************************************************************************\n")
print("                                                                                             Welcome to Type Assistant\n\n")
print("\n*******************************************************************************************************************************************************************************************************************\n")

print("Hi I am Anshu the Genie.....I am at your service.....!!!")

i=1
while True:
    if(i==1):
        print("What can I do for you My Master...!!!!: " , end =" ")
    else:
        print("What next should I do for you My Master...!!! ", end = " ")
    i+=1

    command=input().lower()

    if("launch" in command or "run" in command or "execute" in command or "play" in command or "open" in command or "surf" in command):
        if("browser" in command or "chrome" in command or "internet" in command or "net" in command):
            os.system("chrome")
        elif("photoshop" in command or "photo editor" in command or "graphics maker" in command):
            os.system("Photoshop")
        elif("program editor" in command or "program writer" in command or "code" in command or "vs code" in command or "program" in command):
            os.system("Code")
        elif("text editor" in command or "editor" in command or "notepad" in command or "notebook" in command):
            os.system("notepad")
        elif("media player" in command or "song player" in command or "wmplayer" in command or "player" in command and "vlc" not in command and "video" not in command):
            os.system("wmplayer")
        elif("vlc" in command or "video player" in command):
            os.system("vlc")
        elif("android studio" in command or "app developement software" in command or "studio" in command or "android app maker" in command or "android" in command):
            os.system("studio64")
        
        #System Apps

        elif("calculator" in command or "calc" in command or "mathematical operations" in command or "calculate" in command or "calculation" in command or "addition" in command or "subtraction" in command or "multiplication" in command or "division" in command or "sum" in command or "difference" in command):
            os.system("calc")
        elif("excel" in command or "sheet" in command):
            os.system("EXCEL")
        elif("word" in command or "document" in command or "winword" in command):
            os.system("WINWORD")
        elif("powepoint" in command or "ppt" in command or "presentation" in command):
            os.system("POWERPNT")
        else:
            print("Sorry I could fulfill your wish....!!!! Please Ask for something else....!!!")

    elif("browser" in command or "chrome" in command or "internet" in command or "net" in command):
        os.system("chrome")
    elif("photoshop" in command or "photo editor" in command or "graphics maker" in command):
        os.system("Photoshop")
    elif("program editor" in command or "ide" in command or "program writer" in command or "code" in command or "vs code" in command):
        os.system("Code")
    elif("text editor" in command or "editor" in command or "notepad" in command or "notebook" in command):
        os.system("notepad")
    elif("media player" in command or "song player" in command or "wmplayer" in command or "player" in command and "vlc" not in command and "video" not in command):
        os.system("wmplayer")
    elif("vlc" in command or "video player" in command):
        os.system("vlc")
    elif("android studio" in command or "app developement software" in command or "studio" in command or "android app maker" in command or "android" in command):
        os.system("studio64")
    
    #System Apps

    elif("calculator" in command or "calc" in command or "mathematical operations" in command or "calculate" in command or "calculation" in command or "addition" in command or "subtraction" in command or "multiplication" in command or "division" in command or "sum" in command or "difference" in command):
        os.system("calc")
    elif("excel" in command or "sheet" in command):
        os.system("EXCEL")
    elif("word" in command or "document" in command or "winword" in command):
        os.system("WINWORD")
    elif("powepoint" in command or "ppt" in command or "presentation" in command):
        os.system("POWERPNT")
    elif("exit" in command or "stop" in command):
        print("It was nice serving you Master....!!!... Have a nice Day...!!!")
        break
    else:
        print("Sorry I could fulfill your wish....!!!! Please Ask for something else....!!!")

    
        

        









       
