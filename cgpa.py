# Python3 script to calculate CGPA for Anna University B.E CSE Regulation 2013
# Date  : 17-February-2018
# Author: Sivarama Subramanian

def getSem():
    try:
        return int(input("Enter your Semester(1-8): "))
    except:
        # most probably entered value is not a number
        return -1

def getChoice():
    try:
        return int(input("1.GPA\n2.CGPA\nEnter your choice(1 or 2): "))
    except:
        # most probably entered value is not a number
        return -1


grade_points={
                'S':10,
                'A':9,
                'B':8,
                'C':7,
                'D':6,
                'E':5,
                'U':0,
                'UA':0
}

semesters=[
            [   # Semester 1
            #('subject code','subject name',credits for the subject)
                ('HS6151',' Technical English – I ',4),
                ('MA6151',' Mathematics – I ',4),
                ('PH6151',' Engineering Physics – I ',3),
                ('CY6151',' Engineering Chemistry – I ',3),
                ('GE6151',' Computer Programming',3),
                ('GE6152',' Engineering Graphics ',4),
                ('GE6161',' Computer Practices Laboratory ',2),
                ('GE6162',' Engineering Practices Laboratory',2),
                ('GE6163',' Physics and Chemistry Laboratory - I ',1)
            ],
            [   # Semester 2
                ('HS6251',' Technical English – II ',4),
                ('MA6251',' Mathematics – II ',4),
                ('PH6251',' Engineering Physics – II ',3),
                ('CY6251',' Engineering Chemistry – II ',3),
                ('CS6201',' Digital Principles and System Design',3),
                ('CS6202',' Programming and Data Structures I ',3),
                ('GE6262',' Physics and Chemistry Laboratory - II  ',1),
                ('CS6211',' Digital Laboratory',2),
                ('CS6212',' Programming and Data Structures Laboratory - I',2)
            ],
            [   # Semester 3
                ('MA6351',' Transforms and Partial Differential Equations ',4),
                ('CS6301',' Programming and Data Structure II ',3),
                ('CS6302',' Database Management Systems ',3),
                ('CS6303',' Computer Architecture ',3),
                ('CS6304',' Analog and Digital Communication ',3),
                ('GE6351',' Environmental Science and Engineering ',3),
                ('CS6311',' Programming and Data Structures Laboratory - II',2),
                ('GE6312',' Database Management Systems Laboratory ',2),
            ],
            [   # Semester 4
                ('MA6453',' Probability and Queueing Theory ',4),
                ('CS6551',' Computer Networks ',3),
                ('CS6401',' Operating Systems ',3),
                ('CS6304',' Design and Analysis of Algorithms ',3),
                ('EC6504',' Microprocessor and Microcontroller ',3),
                ('CS6403',' Software Engineering  ',3),
                ('CS6411',' Networks Laboratory ',2),
                ('CS6412',' Microprocessor and Microcontroller Laboratory ',2),
                ('CS6413',' Operating Systems Laboratory ',2),
            ],
            [   # Semester 5
                ('MA6566',' Discrete Mathematics ',4),
                ('CS6501',' Internet Programming ',4),
                ('CS6502',' Object Oriented Analysis and Design ',3),
                ('CS6503',' Theory of Computation ',3),
                ('CS6504',' Computer Graphics ',3),
                ('CS6511',' Case Tools Laboratory ',2),
                ('CS6512',' Internet Programming Laboratory ',2),
                ('CS6513',' Computer Graphics Laboratory ',2)
            ],
            [   # Semester 6
                ('CS6601',' Distributed Systems ',3),
                ('IT6601',' Mobile Computing ',3),
                ('CS6660',' Compiler Design ',3),
                ('IT6502',' Digital Signal Processing ',4),
                ('CS6659',' Artificial Intelligence ',3),
                ('CS6001 or GE6757 or IT6702 or CS6002 or IT6004',' Elective I ',3),
                ('CS6611',' Mobile Application Development Laboratory ',2),
                ('CS6612',' Compiler Laboratory ',2),
                ('GE6674',' Communication and Soft Skills - Laboratory ',2),
            ],
            [   # Semester 7
                ('CS6701',' Cryptography and Network Security ',3),
                ('CS6702',' Graph Theory and Applications ',3),
                ('CS6703',' Grid and Cloud Computing ',3),
                ('CS6704',' Resource Management Techniques ',3),
                ('CS6003 or CS6004 or CS6005 or BM6005 or IT6801',' Elective II ',3),
                ('IT6005 or EC6703 or CS6006 or CS6007 or IT6006',' Elective III ',3),
                ('CS6711',' Security Laboratory ',2),
                ('CS6712',' Grid and Cloud Computing Laboratory ',2)
            ],
             [   # Semester 8
                ('CS6801',' Multi – Core Architectures and Programming  ',3),
                ('CS6008 or CS6009 or IT6011 or CS6010',' Elective IV ',3),
                ('MG6088 or GE6075 or CS6011 or CS6012',' Elective V ',3),
                ('CS6811',' Project Work  ',6),
             ]
]

# dictionary to store the grades of the user
# 'subject name'    -       string       - is used as key
# (grade , credits) - (string,int) tuple - is the stored value
input_grades={}

# function to calculate CGPA till a given semester
def calcCGPA(semester):
    # for each semester
    for sem_no in range(semester):
        # for each subject in the semester
        for subject_code,subject,credits in semesters[sem_no]:
            # get the grade
            grade=input("Enter your grade in %s %s: "%(subject_code,subject)).upper()
            # validate the grade , if invalid get again
            while grade not in grade_points:
                grade=input("Enter your grade (eg: \'S\',\'A\' etc. ) in %s %s"%(subject_code,subject)).upper()
            # store the grade with the subject name
            input_grades[subject]=(grade,credits)

    #initialize the variable used to calculate GPA
    gradepointsum=0;
    creditsum=0;
    #initialize the variable used to calculate CGPA
    CGPAgradepointsum=0;
    CGPAcreditsum=0;

    # for each semester
    for sem_no in range(semester):
        print("\nSemester %d\n "%(sem_no+1))
        # for each subject in the semester
        for subject_code,subject,credits in semesters[sem_no]:
            # retrieve the grade for the subject
            grade = input_grades[subject][0]
            # calculate grade points for the subject
            gradepoint=  grade_points[grade]
            # print the grade and subject
            print("Grade in %s %s is %s"%(subject_code,subject,grade))
            # if it is not an arrear, include it in calculation of GPA & CGPA
            if grade !='U' and grade !='UA':
                gradepointsum+=(gradepoint*credits);
                creditsum+=credits
                CGPAgradepointsum+=(gradepoint*credits);
                CGPAcreditsum+=credits

        # print the results
        print("GPA for Semester %d is %f "%(sem_no+1,(gradepointsum/creditsum)))
        print("CGPA upto Semester %d is %f \n"%(sem_no+1,(CGPAgradepointsum/CGPAcreditsum)))
        # initialize GPA variables to zero for next semester
        # but keep the CGPA variables as it is
        gradepointsum=0
        creditsum=0

# function to calculate GPA for a given semester
def calcGPA(sem_no):
        # for each subject in the semester
        for subject_code,subject,credits in semesters[sem_no]:
            # get the grade
            grade=input("Enter your grade in %s %s: "%(subject_code,subject)).upper()
            # validate the grade , if invalid get again
            while grade not in grade_points:
                grade=input("Enter your grade (eg: \'S\',\'A\' etc. ) in %s %s"%(subject_code,subject)).upper()
            # store the grade with the subject name
            input_grades[subject]=(grade,credits)

        #initialize the variable used to calculate GPA
        gradepointsum=0;
        creditsum=0;

        # for each subject in the semester
        for subject_code,subject,credits in semesters[sem_no]:
            # retrieve the grade for the subject
            grade = input_grades[subject][0]
            # calculate grade points for the subject
            gradepoint=  grade_points[grade]
            print("Grade in %s %s is %s"%(subject_code,subject,grade))
            # if it is not an arrear, include it in calculation of GPA
            if grade !='U' and grade !='UA':
                gradepointsum+=(gradepoint*credits);
                creditsum+=credits

        # print the results
        print("GPA for Semester %d is %f "%(sem_no+1,(gradepointsum/creditsum)))


if __name__=='__main__':
    # get user's choice for calculating GPA or CGPA
    choice = getChoice()
    # while user's choice is invalid
    while choice < 1 or choice > 2:
        # prompt for a valid choice
        choice = getChoice()

    # get the semester for which GPA is to be calculated
    # or upto which the CGPA is to calculated
    semester = getSem()
    # while semester is invalid
    while semester < 1 or semester > 8:
        # prompt for a valid semester
        semester=getSem()

    if choice==1:
        # if user's choice is to calculate GPA,
        # call calcGPA(semester - 1)
        # array index starts from zero, hence pass 'semester - 1'
        calcGPA(semester-1)
    else:
        # else user chose to calculate CGPA
        # call calcCGPA(semester)
        # range(n) is used in calcCGPA() it iterates from 0 to n-1
        # so no need to pass 'semester - 1' as the argument
        calcCGPA(semester)