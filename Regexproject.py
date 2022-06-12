import re


phoneRegex= re.compile(r'''
(((\d\d\d)|((\d\d\d)))?                 #area code(opt)
(\s|-)                    #dirst seperator
\d\d\d                   #first 3 digits
-                    #seperator
\d\d\d\d                    #last 4 digits
((ext(\.)?\s|x)                  #extension word part (opt)
(\d{2,5}))?)               #extension number part(opt)
''', re.VERBOSE)

emailRegex= re.compile(r'''
[a-zA-Z0-9_.+]+             #namepart with plus underscore and dot    square brackets means dont need divide 
@                           #@ symbol
[a-zA-Z0-9_.+]+             #domain name part
''', re.VERBOSE)

text = '''Instructor: Dr. Stephanie Kerr
Lecture Time: NA - Posted on Moodle every Monday 
Discussion Groups: T & R 1:15-2:30pm
Office Hours: Mondays 2:30-3:30pm by appointment 
Email Address: stephanie.kerr@concordia.ca (514)-218-3555
TA: Issam Banifadel issam.banifadel@gmail.com 514-929-5858'''

phoneNumbers= phoneRegex.findall(text)
emailadresses= emailRegex.findall(text)
allPhoneNbs= []
for phoneNumber in phoneNumbers:
    allPhoneNbs.append(phoneNumber[0])
results= '\n'.join(allPhoneNbs) + '\n'+ '\n'.join(emailadresses)
print(results)