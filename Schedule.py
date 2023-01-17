import requests, json, time
from bs4 import BeautifulSoup
import pyfiglet, logging
from termcolor import colored
import Text
from datetime import datetime

COURSES = 'https://sis.rutgers.edu/soc/api/courses.json?year=2023&term=1&campus=NB'

def status(text):
    print(f"---------------[{text.upper()}]-----------------")

def ascii(text, color):
    print(colored(pyfiglet.figlet_format(text.upper()), color.lower()))

class Course:
    def __init__(self, courseJson):
        self.title = courseJson['title']
        self.fullCourseID = courseJson['courseString']
        self.synopsisURL = courseJson['synopsisUrl']
        self.courseSubject = courseJson['subjectDescription']
        self.openSections = courseJson['openSections']
        self.credits = courseJson['credits']
        self.howManySections = len(courseJson['sections'])
        self.howManyInstructors = len(courseJson['sections'][0]['instructors'])
        if(self.howManySections > 0):
            self.indexes = [] 
            self.status = []
            for x in range(self.howManySections):
                self.indexes.append(courseJson['sections'][x]['index'])
                self.status.append(courseJson['sections'][x]['openStatus'])
        else:
            self.indexes = []
            self.status = []

    def getTitle(self):
        return self.title
    def getFullCourseID(self):
        return self.fullCourseID
    def getOpenSections(self):
        return self.openSections
    def getIndexes(self):
        return self.indexes
    def getStatuses(self):
        return self.status
    def __str__(self):
        toString = f"[TITLE] : {self.title}\n[COURSE ID] : {self.fullCourseID}\n[SYNOPSIS URL] : {self.synopsisURL}\n[COURSE SUBJECT] : {self.courseSubject}\n[OPEN SECTIONS] : {self.openSections}\n[CREDITS] : {self.credits}\n[HOW MANY SECTIONS] : {self.howManySections}\n[HOW MANY INSTRUCTORS] : {self.howManyInstructors}\n[SECTIONS AVAILIBLE] : {self.indexes}\n[Status] : {self.status}\n"
        return toString

def getJsonFromURL(url):
    request = requests.get(url)
    coursesJson = json.loads(request.text)
    return coursesJson

def printLine():
    print('--------------------------------')

def getIndexOf(objArr, courseID):
        for x in range(len(objArr)):
            if(objArr[x].getFullCourseID() == courseID.upper()):
                return x
        return -1

def getArrCourses(coursesJson):
    coursesOA = []
    for x in range(len(coursesJson)):
        coursesOA.append(Course(coursesJson[x]))
    return coursesOA

def isIndexAvailable(objArr, courseID, targetIndex):
    for course in objArr:
        if (course.getOpenSections() > 0 and course.getFullCourseID() == courseID):
            if(course.getStatuses()[course.getIndexes().index(targetIndex)] == True):
                return True
    return False
    

# CourseName: coursesJson[0]['title']
# FullCourseID: coursesJson[0]['courseString']
# SynopsisURL: coursesJson[0]['synopsisUrl']
# CourseSubject: coursesJson[0]['subjectDescription']
# OpenSections: coursesJson[331]['openSections']
# Credits: coursesJson[331]['credits']
# HowManySections: len(coursesJson[331]['sections'])
# HowManyInstructors: len(coursesJson[331]['sections'][0]['instructors'])
# coursesJson[331]['sections'][0]['instructors'][0]['name']

if __name__ == '__main__':
    ascii("ru rah rah", "red")
    coursesArr = getArrCourses(getJsonFromURL(COURSES))
    status("courses retrieved successfully")
    while True:
        print(getIndexOf(coursesArr, "01:750:205"))
        print(coursesArr[getIndexOf(coursesArr, "01:750:205")])
        print("FOUND: ", isIndexAvailable(coursesArr, "01:750:205", "06629"))
        if( isIndexAvailable(coursesArr, "01:750:205", "06629")):
            break
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        printLine()

        time.sleep(1)

