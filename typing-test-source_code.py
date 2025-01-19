from time import *
import random as r

def mistake(paratest,usertest):
    error=0
    for i in range(len(paratest.split())):
        try:
            if paratest.split()[i] != usertest.split()[i]:
                error=error+1
        except:
            error=error+1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay=time_e-time_s
    time_r=time_delay/60
    time_r_mins=round(time_r,2)
    speed=len(userinput.split())/time_r_mins
    return round(speed,2)



while True:
    print("ready to test: y/n ")
    check=input()
    if check=="y" or check=="Y":
        test=["The curious cat explored the dark attic, finding hidden treasures behind dusty boxes",
"She danced gracefully under the moonlight, her silhouette glowing in silver hues",
"In the quiet library, students studied diligently, surrounded by shelves of knowledge",
"The adventurous group hiked through dense forests, discovering breathtaking views of nature's beauty",
"Beneath the ocean waves, vibrant coral reefs housed countless colorful and exotic creatures"]

        test1=r.choice(test)
        print("    $$$$ TYPING SPEED TEST $$$$   ")
        print(" ")
        print("Type the following sentence:")
        print(test1)
        time_1=time()
        testinput=input("Start typing : ")
        time_2=time()

        print("Speed :" ,speed_time(time_1,time_2,testinput)," wpm")
        print("Error : ",mistake(test1,testinput))
    
    elif check=="n" or check=="N":
        print("Thank you!")
        break
    else:
        print("wrong input")