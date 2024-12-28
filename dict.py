 
student = {'name': 'zoe'

           }
student['ph'] = 1234
student['address'] = 'xyz'
student['id'] = 'zoe@gmail.com'
student['ph'] = 1234567
student['pho'] = 1234
del student['pho']
print(student)
for i in student:
    print(i)
for i in student.keys():
    print(i)
for i in student.values():
    print(i)
if 'zoe' in student.values():
    print('yes')
    
#hw: dictionary with:
#country:
#capital:
#currency
#language
    