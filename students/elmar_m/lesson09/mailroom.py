#!/usr/bin/env python3

'''
file: mailroom.py
elmar_m / 22e88@mailbox.org
Lesson09: OOP mailroom program 
'''

import sqlite3


class Donor:

    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        self.uid = '{}_{}'.format(fname, lname) 


class Collection:

    def __init__(self):
        self.db= sqlite3.connect('BLABLA.db')
        self.cursor = self.db.cursor()

    def _create_table(self):
        ''' Other columns like e.g. date of donation could be 
            inserted anytime without breaking the class interface
        '''
        self.cursor.execute("create table mailroom (donation_ID INTEGER PRIMARY KEY AUTOINCREMENT, donor TEXT, donation INT DEFAULT 0)")
        # self.db.close()
        return True

    def add_donor(self, donor):
        self.cursor.execute("insert into mailroom (donor) values(?)", (donor,)) 
        self.db.commit()
        # self.db.close()

    def add_donation(self, donor, amount):
        self.cursor.execute("insert into mailroom (donor, donation) values(?, ?)", (donor, amount)) 
        self.db.commit()
    #    self.db.close()


    def get_donations(self, donor):
        # self.cursor.execute("select * from mailroom where donor = ?", (donor,))
        self.cursor.execute("select donation from mailroom where donor = ?", (donor,))
        # self.db.close()
        return self.cursor.fetchall()


    def get_average_donation(self, donor):
        pass


    def get_number_of_donations(self, donor):
        pass

    
    def sum_up_donations(self, donor):
        pass
    

    #def report(self):      # ?? das hier oder oben die Einzelfunktionen?
    #    pass               # ?? oder dies hier nutzt die Einzelfunktionen,
                            # welche dann nur 'intern' sind?

    #def send_mails(self):  # hier oder draussen?
    #    pass


    def get_all_donors(self):
        self.cursor.execute("select donor from mailroom")
        donors = set(self.cursor.fetchall())
        return donors
        

    def check_existence(self, donor):
        self.cursor.execute("select * from mailroom where donor = ?", (donor,))
        if self.cursor.fetchall():
            return True
        else:
            return None




def efunc():
    return 'exiting'

def fakefunc():
    pass

def list_donors():
    db = Collection()
    for i in db.get_all_donors():
        print('\t{} {}'.format('Nice person:', i)) 

def list_donations():
    donor = input('Please enter name of donor: ') 
    db = Collection()
    for i in db.get_donations(donor):
        print('\t{} donated: {}'.format(donor, i)) 

def add():
    while True: 
        donor = input('Please enter donor name: ')
        if not donor.isalpha():
            print('>> only alphabetical characters in donor name allowed, please try again')
            continue
        else:
            break
    amount = input('Please enter donation amount: ')
    db = Collection()
    db.add_donation(donor, amount)

    #if db.check_existence(donor):   
    #    print('{} found in database'.format(donor))
    #    db.add_donation(donor, amount)
    #else:
    #    print('{} NOT FOUND in database, will be added'.format(donor))
    #    db.add_donation(donor, amount)
        
    
#def add():
#    while True: 
#        dname = input('>> Please give donor name: ')
#        if not dname.isalpha():
#            print('>> only alphabetical characters in donor name allowed, please try again')
#            continue
#        else:
#            break
#    if dname in donors:
#        print('>>', dname, 'already in list')
#        return add_amount(dname)
#        # add_amount(dname)
#        # return True
#    
#    else:
#        print('>>', dname, 'not in list, adding it')
#        return add_amount(dname)
#        # add_amount(dname)
#        # return True

    


def menu(prompt, dispatcher):
    try:
        while True:
            response = input(prompt)
            if dispatcher[response]() == 'exiting':
                break
    except KeyError:
        print('\n\tSorry, unknown option:', response, '\n')
        menu(prompt, dispatcher)


if __name__ == '__main__':

    prompt = '\
    \nPlease choose an option:\
    \n\t1: list donors\
    \n\t2: list donations of a donor\
    \n\t3: add donor and / or donation\
    \n\t4: send thankyou mail\
    \n\t5: show report\
    \n\t6: quit program\n\n'

    dispatcher = {
        '1' : list_donors,
        '2' : list_donations,
        '3' : add,
        # '4' : thankyou,
        '4' : fakefunc,
        # '5' : report,
        '5' : fakefunc,
        '6' : efunc,
        }

    print('\n*** Welcome to OOP mailroom. ***')
    menu(prompt, dispatcher)
    print('\n***Thanks for using OOP mailroom. Goodbye.***\n')


