import csv
#enables python to parse csv info using this built in function
Yes = ["y","Y","yes","Yes","YES"]
No = ["n","N","no","No","NO"]
Head = ["Name","Age","Contact","E-mail id"]
no = 1
def StuAdminWrite(StuInfo_list):
    with open("Student_Data.csv","a+",newline = "") as StuData:
        StuWrite = csv.writer(StuData)
        if StuData.tell() == 0:
            StuWrite.writerow(Head)
        StuWrite.writerow(StuInfo_list)
def StuAdminRead():
    with open("Student_Data.csv","r") as StuData:
        StuRead = csv.reader(StuData)
        for i,row in enumerate(StuRead):
            print(f"{i} | {row[0]} | {row[1]} | {row[2]} | {row[3]}")
#ensures the loop makes the user input info until the condition is met/broken
while True:
    StuInfo = input(f"Welcome! You are student #{no} ! Please enter your details in this format, seperated by space :- Name Age Contact E-mail id:\n")
    StuInfo_list = StuInfo.split(" ")
    print(f"The values you have entered are : ?\nName: {StuInfo_list[0]}\nAge: {StuInfo_list[1]}\nPhnNo: {StuInfo_list[2]}\nEmail: {StuInfo_list[3]}")
    y_n = input(" Do you wish to proceed with these values? \n If Yes then press y, if No then press n:\n")
    if y_n in Yes:
        x = StuAdminWrite(StuInfo_list)
    elif y_n in No:
        print("Please enter the correct values :")
        continue
    MoreStu = input("Do you wish to add more Students?(y/n)\n")
    if MoreStu in Yes:
        no+=1
    elif MoreStu in No:
        break

StuFileRead()
