
# pass_fail.pys

def add_students_marks():
    """
    This add_students_marks function bascially to take students details and marks.
    Marks of are store in subjects variable where marks are store in dictionary format 
    """
    name = input('Enter your name: ').strip()
    clas = input('Enter your class: ').strip()
    facaulty = input('Enter your facaulty(Management, Science, Law, Humanities, Hotel Management): ').strip()
    roll_no = input('Enter your roll_no: ').strip()
    
    print()
    print("Enter marks of subjects (out of 100): ")

    subjects = {}
    sub_list = ['maths', 'computer','account','nepali','english','economics']
    for i in sub_list:
        while True:
            sub = input(f"marks of {i}:")
            try:
                sub = float(sub)
                if sub>100:
                    print("sorry! marks must be less than 100!")
                else:
                    subjects[i] = sub
                break
            except:
                print('Invalid input')
    print(subjects)
    print(len(subjects))
    return subjects
    # pass_fail(subjects)

def pass_fail(subjects):
    """
    1.this pass_fail function segregate the pass or fail subject 
    2. we set criteria to pass (pass>=27)
    3. we show total and percentage of user
    """
    pass_sub = []
    fail_sub = []
    total = 0
    # for visaya in all_subjects:
    #     for i in visaya:
    #         if float(visaya[i]) >= 27:
    #             pass_sub.append(i)
    #         else:
    #             fail_sub.append(i)
    for keys, values in subjects.items():
        if values>=27:
            pass_sub.append(keys)
        else:
            fail_sub.append(keys)
        total += values

    print()
    print("total marks: ", total,"out of 600")

    # percentage
    percentage = (total/600)*100
    print(f"percentage: {percentage}% out of 100%")

    # status
    if len(pass_sub) == 6:
        print("Congratulations! you have passed all the subjects.")
    else:
        print("Sorry! you have failed in following subjects: ", fail_sub,'\n')

def display_students_marks(all_subjects):
    """
    This function is used to display the marks of students
    """
    # subjects
    j = 0 
    for i in all_subjects:
        j += 1
        print(j,i)
def delete_students_marks(all_subjects):
    """
    This function is used to delete the marks of students
    """
    display_students_marks(all_subjects)
    delete = int(input("Enter the number to delete: ")) # exception handling must be here
    # all_subjects.pop(delete)
    del all_subjects[delete-1]

def search_students_marks(all_subjects):
    search_name = input("Enter student name to search: ").lower()
    for student in all_subjects:
        if search_name in student.get("name", "").lower(): # if values is availabe of corrrespond key it will retreive other wise " " to handle error
            # print(student)
            return student
    print("Student not found!")



# 1. get marks of subjects from user
# 2. return marks of subjects 

print() 
def main ():
    all_subjects = []

    print("X---------------Welcome to marks testing program--------------X")

    while True:
        print("Marks list size:",len(all_subjects))
        opinion = input("""
                        To add marks type 'add'
                        To delete marks type 'delete'
                        To search marks type 'search'
                        To exits type 'e'
                        """).lower()
        
        if opinion == 'add':
            subjects = add_students_marks()
            all_subjects.append(subjects)
            pass_fail(subjects)
        elif opinion == 'delete':
            delete_students_marks(all_subjects)
        elif opinion == 'search':
            search = search_students_marks(all_subjects)
            print(search)
        elif opinion == 'e':
            break
        else:
            print("InvalidInput!")

if __name__ == "__main__":
    main()   




