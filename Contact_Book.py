import sys
import sqlite3
from prettytable import from_db_cursor

# Connecting database
db = sqlite3.connect('contacts.db')
cursor = db.cursor()

# Declaring SQL database statements
def create():
    create = '''
    CREATE TABLE IF NOT EXISTS
    CONTACTS(Name TEXT, Number TEXT);
    '''
    cursor.execute(create)
    return

def select_all():
    select_all = '''
    SELECT * FROM CONTACTS;
    '''
    cursor.execute(select_all)
    print(from_db_cursor(cursor))
    return

def select_by_name():
    select_by_name = f'''
    SELECT * FROM CONTACTS WHERE Name = "{input('Enter name to search: ')}";
    '''
    cursor.execute(select_by_name)
    print(from_db_cursor(cursor))
    return

def select_by_number():
    select_by_number = f'''
    SELECT * FROM CONTACTS WHERE Number = "{input('Enter number to search: ')}";
    '''
    cursor.execute(select_by_number)
    print(from_db_cursor(cursor))
    return

def insert():
    insert = f'''
    INSERT INTO CONTACTS(Name,Number) VALUES("{input('Enter name to add: ')}","{input('Enter phone number: ')}");
    '''
    cursor.execute(insert)
    db.commit()
    return

def update_name():
    number = input('Enter number for which you want to update the name: ')
    update_name = f'''
    UPDATE CONTACTS SET Name = "{input('Enter new name: ')}" WHERE Number = "{number}";
    '''
    cursor.execute(update_name)
    db.commit()
    return

def update_number():
    name = input('Enter name for which you want to update the number: ')
    update_number = f'''
    UPDATE CONTACTS SET Number = "{input('Enter new number: ')}" WHERE Name = "{name}";
    '''
    cursor.execute(update_number)
    db.commit()
    return

def final_choice():
    final_choice = input('\nYou will not be able to restore this contact once deleted.\nDo you still want to continue? (yes/no)\n')
    if final_choice.lower() == 'yes':
        return True
    else:
        return False

def delete_by_name():
    delete_by_name = f'''
    DELETE FROM CONTACTS WHERE Name = "{input('Enter name for which you want to delete the contact: ')}";
    '''
    if final_choice() == True:
        cursor.execute(delete_by_name)
        db.commit()
        print('\nContact Deleted Successfully !!!')
    else:
        print('\nYour Contact was not deleted !!!\n')
    return

def delete_by_number():
    delete_by_number = f'''
    DELETE FROM CONTACTS WHERE Number = "{input('Enter number for which you want to delete the contact: ')}";
    '''
    if final_choice() == True:
        cursor.execute(delete_by_number)
        db.commit()
        print('\nContact Deleted Successfully !!!')
    else:
        print('\nYour Contact was not deleted !!!\n')
    return        

def delete_all():
    delete_all = f'''
    DELETE FROM CONTACTS;
    '''
    if final_choice() == True:
        cursor.execute(delete_all)
        db.commit()
        print('\nContact Deleted Successfully !!!')
    else:
        print('\nYour Contact was not deleted !!!\n')
    return   


# Driver Code - Main
print('\n!!! Welcome to the Contact Book !!!')

while True:
    print('''
    1 - Add Contact
    2 - Search Contact
    3 - Update Contact
    4 - Delete Contact
    5 - Exit from Contact Book
    ''')

    create()
    
    try:
        choice = int(input('Enter your choice to perform task: '))

        if choice == 1:
            insert()
            print('\nContact Added Succesfully !!!')

        elif choice == 2:
            print('''
            1 - Search Contact by Name
            2 - Search Contact by Number
            3 - See All Contacts
            ''')
            search_choice = int(input('Enter your choice how you want get contact: '))
            if search_choice == 1:
                select_by_name()
            elif search_choice == 2:
                select_by_number()
            else:
                select_all()

        elif choice == 3:
            print('''
            1 - Update Contact Name
            2 - Update Contact Number
            ''')
            update_choice = int(input('Enter your choice how you want to update the contact: '))
            if update_choice == 1:
                update_name()
            else:
                update_number()
            print('\nContact Updated Successfully !!!')

        elif choice == 4:
            print('''
            1 - Delete Contact by Name
            2 - Delete Contact by Number
            3 - Delete All Contacts
            ''')
            delete_choice = int(input('Enter your choice how you want to delete the contact: '))
            if delete_choice == 1:
                delete_by_name()
            elif delete_choice == 2:
                delete_by_number()
            else:
                delete_all()

        elif choice == 5:
            print('\n\n!!! Contact Book was closed succesfully !!!\n\n')
            # Saving and closing the databse
            db.commit()
            db.close()
            # Stopping the program execution
            sys.exit()

    except ValueError as error:
        print('\n\n!!!PLEASE, enter valid choices only !!!\n\n')