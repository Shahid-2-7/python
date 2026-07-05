totalMark = 0
database = {
    "shahid" : {
        "tamil": 87,
        "english": 89,
        "maths": 92,
        "science":87,
        "social science": 93,
        "computer science": 96,
        "hindi": 95,
        "gk": 90,
    },
    "anwer" : {
        "tamil": 87,
        "english": 89,
        "maths": 92,
        "science":87,
        "social science": 93,
        "computer science": 96,
        "hindi": 95,
        "gk": 89        
    }
}
condition = True
while condition:
    if len(database.keys()) >= 2:
        selectStudent = input("Select student: ")
        if selectStudent in database:
            student = selectStudent
            studentMarks = database[selectStudent]
            print(student)
            print(studentMarks)
        else:
            print("Student was not found!")
            break
    while True:
        try:
            print("1 - Show all subject marks\n2 - Show average mark\n3 - Show passed and failed subjects\n4 - Search for a specfic subject's mark\n5 - Update a subject mark\n6 - Exit")
            select_menu = int(input("Select => "))
            match select_menu:
                case 1:
                    for sub,mark in database[selectStudent].items():
                        print (sub, ":", mark)
                case 2:
                    totalMark = 0
                    for avg in database[selectStudent].values():
                        totalMark += avg
                    avgMarks = round(totalMark / 8)
                    print("Average marks of", student,":", avgMarks)
                case 3:
                    for sub, mark in database[selectStudent].items():
                        if mark >= 32:
                            print(sub,":",mark,"Result: PASS")
                        else:
                            print(sub,":",mark,"Result: FAIL!")
                case 4:
                    selectSubject = input("Select subject : ")
                    for sub, mark in database[selectStudent].items():
                        if selectSubject == sub:
                            print(sub,":",mark)
                case 5:
                    selectSubjectToUpdate = input("Select a subject to update : ")
                    if selectSubjectToUpdate in database[selectStudent]:
                        print(selectSubjectToUpdate,"has been found!")
                        newMark = int(input("Enter updated marks : "))
                        database[selectStudent][selectSubjectToUpdate] = newMark
                        print("Marks updated successfully!\nUpdated marks for",selectSubjectToUpdate,":",newMark)
                    else:
                        print("Subject was not found!")
                case 6:
                    condition = False
                    break
                case _:
                    print("Invalid Input given!")
        except Exception:
            print("Error has been thrown, please try again")

