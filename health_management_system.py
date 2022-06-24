def getdate():
    import datetime
    return datetime.datetime.now()
try:
    file = open("text_files/sampleFile.txt","a")
    file.close
except:
    import os
    os.mkdir("text_files")
str1 = "diet"
str2="exercise"
familyMembers = ["member1","member2","member3","member4","member5","member6","member7","member8","member9"]
familyMembersOriginal = familyMembers.copy()
print("THIS PROGRAM IS THE HEALTH MANAGEMENT SYSTEM OF RAM NIWAS FAMILY...")
try:
    for member in familyMembers:
        file = open(f"text_files/{member}_{str1}.txt","a")
        file.close()
        file2 = open(f"text_files/{member}_{str2}.txt","a")
        file2.close()
except:
    pass
def log():
    print("Whose data do you want to log?\n")
    counter=0
    for member in familyMembers:
        print(f"Enter \'{counter}\' to log the data of {member}.")
        counter+=1
    user_input = int(input("=>"))
    memberName = familyMembers[user_input]
    diet_or_exercise = int(input("Type \'1\' to log \"diet\" and \'2\' to log \"exercise\":-\n"))
    if diet_or_exercise == 1:
        diet = input("Please enter the diet:-\n")
        file = open(f"text_files/{memberName}_diet.txt","a")
        var1=str(getdate())
        file.write("["+var1+"]"+"\t\t"+diet+"\n")
        file.close()
    elif diet_or_exercise == 2:
        exercise = input("Please enter the exercise:-\t")
        file=open(f"text_files/{memberName}_exercise.txt","a")
        var2=str(getdate())
        file.write("["+var2+"]"+"\t\t"+exercise+"\n")
        file.close()
def retrieve():
    print("Whose data do you want ot retrieve?")
    counter=0
    for member in familyMembers:
        print(f"Enter \'{counter}\' to retrieve the data of \"{member}\".")
        counter+=1
    user_input=int(input("=>"))
    memberName = familyMembers[user_input]
    diet_or_exercise = int(input("Press \'1\' to retrieve \"diet\" and \'2\' to retrieve \"exercise\":-\n"))
    if diet_or_exercise == 1:
        file=open(f"text_files/{memberName}_diet.txt")
        for line in file:
            print(line,end="")
        file.close()
    elif diet_or_exercise == 2:
        file=open(f"text_files/{memberName}_exercise.txt")
        for line in file:
            print(line,end="")
        file.close()
y_n = "y"
while y_n == "y":
    var = int(input("Type \'1\' to \"log\" data and \"2\" to retrieve it:-\n"))
    if var==1:
        log()
    elif var==2:
        retrieve()
    y_n = input("\nPress \'y\' to perform some function again and press any other key to exit the program.\n")
print("THANKS FOR USING OUR PROGRAM, HAVE A NICE DAY AHEAD!!!")
input()