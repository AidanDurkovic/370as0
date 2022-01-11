import datetime
import sys

def convertInput(inString):
    inSplit = inString.split("-")
    outDate = datetime.date(inSplit[0],inSplit[1],inSplit[2])
    return outDate

gradeDates ={
    datetime.date(2022,1,21):5,
    datetime.date(2022,1,28):20,
    datetime.date(2022,2,11):5,
    datetime.date(2022,2,18):20,
    datetime.date(2022,3,11):5,
    datetime.date(2022,3,18):20,
    datetime.date(2022,4,1):5,
    datetime.date(2022,4,8):20
}

inDate = convertInput(sys.argv[1])
cumGrade = 0
for gradeDate in gradeDates:
    if inDate >= gradeDate:
        cumGrade += gradeDates[gradeDate]
    else:
        break

print(str(cumGrade) + "%")










