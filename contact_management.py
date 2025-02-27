# Description: This program is a simple contact management system that allows the user to add, search, and delete contacts.
# 1. Add a new contact
# 2. Search contact
# 3. Delete contact
# 4. Exit

# to add person
def add_person():
    name = input('Enter name: ')  
    age = input("Enter age: ")
    email = input('Enter email: ')

    person = {'name':name, 'age': age, 'email': email}
    return person

# to display 
def display_person(people):
    for i, person in enumerate(people):
        print(i+1,'-',person['name'], person['age'], person['email'])

# to search person
def search(people):
    search_name = input('Search the name: ')
    results = []

    for person in people:
        if search_name in person['name']:
            results.append(person)
    
    display_person(results)

# to delete person
def delete_person(people):
    display_person(people)

    while True:
        number_delete = input('Enter the number you want to delete: ')
        try:
            number = int(number_delete)
            if number<1 or number>len(people):
                print('Invalid number!')
            else:
                break
        except Exception as e:
            print(e)
        
    people.pop(number)
    print('delete successfull!\n')
    print('contact after deletion')
    display_person(people)

print()


def main(people):
    print("------Welcome to the Contact Managemet System---------")    
    while True:
        
        print("Contact size:",len(people))
        command = input("You can 'Add', 'Delete', 'Search' and 'Q' for quite: ").lower()

        if command == "add":
            person = add_person()
            people.append(person)
            print("person add successfully!")
        elif command == 'delete':
            delete_person(people)
        elif command == 'search':
            search(people)
        elif command == 'q':
            break
        else:
            print('Invalid input')
people = [ ]       
main(people)





"""
    
        while True:
        subjects = {
        # 'name':name,
        # 'class':clas,
        # 'facaulty': facaulty,
        # 'roll_no': roll_no,
        # 'subjects':{'maths': maths, 'computer': computer,'account': account, 'nepali': nepali, 'english': english, 'economics': economics 
    }
        sub_list = ['maths', 'computer','account','nepali','english','economics']
        for i in sub_list:
            while True:
                sub = input(f"marks of {i}:")
                try:
                    # maths = float(input('Enter marks of maths: '))
                    # computer = float(input('Enter marks of computer: '))
                    # account = float(input('Enter marks of account: '))
                    # nepali = float(input('Enter marks of nepali: '))
                    # english = float(input('Enter marks of english: '))
                    # economics = float(input('Enter marks of economics: '))
                    sub = float(sub)
                    subjects[i] == sub
                    if sub>100:
                        print("sorry! marks must be less than 100!")
                    break
                except:
                    print("InvalidInput! Input only number")

        return subjects
    """