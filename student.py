student = 'Veli Bakirtas'

# isim kontrol
def check_name():
    counter = 1
    while counter < 4:
        name = input('Name and surname?: ')
        if name == student:
            print('Welcome')
            break        
        elif counter == 3:
            print('Please tyr again later')
            break
        else:
            counter += 1
            print('incorrect entry')
            
check_name()            


                        