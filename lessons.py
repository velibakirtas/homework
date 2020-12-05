'''
lineer algebra
introduction to python
statistics
probability
algorithm
'''


def choose_lesson():
    lessons = []
    counter = 1
    while counter < 6:
        lesson1 = input('Choose course: ')
        lessons.append(lesson1)
        if counter == 5:
            break
        check_continue = input('Will you choose another course?: (y/n)=')
        if check_continue == 'y':
            counter += 1
        elif check_continue == 'n':
            break
        print(lessons)
        return lessons
                      
    
def check_missing_lesson(): 
    how_course = choose_lesson()
    if len(how_course) < 3:
        return 'You failed in class'   
    else:
        if len(how_course) >= 3:
            return 'course selection is successful'    

   
                
