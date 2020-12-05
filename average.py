import lessons
course_list = lessons.choose_lesson() # seçilen dersler listesi
#choose_exam = input('Choose a course for the exam: ')
for i in course_list:
    choose_exam = input('Choose a course for the exam: ')
    if i == choose_exam:
        pass
        break
    else:
        print('Please select again')
        