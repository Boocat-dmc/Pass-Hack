import os 
from random import randint

pas=input("send password: ")

keys=["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h"
      ,"i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
      ]
pwd = ""
while(pwd!=pas):
    pwd=""
    for i in range(len(pas)):
        guessPass=keys[randint(0,4)]
        pwd=str(guessPass)+str(pwd)
        print(pwd)
        print("attacking... please wait!")
        os.system("cls")

print(f"the pas is:{pwd}")