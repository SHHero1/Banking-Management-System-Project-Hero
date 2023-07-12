from Admin import Admin
from User import User

def main():
    hero = User('1111', 'hero', 'hero@gmail.com', '4321') # User
    hero.create_account('1111', 'hero', 'hero@gmail.com', '4321') # User
    hero.deposit(5000)
    hero.check_balance() # User

    fahmid = User('1112', 'fahmid', 'fahmid@gmail.com', '4322') # User
    fahmid.create_account('1112', 'fahmid', 'fahmid@gmail.com', '4322') # User

    
    hero.deposit(4000) # User

    shourov = Admin('1234', 'shourov', 'shourov@gmail.com', '5432') # Admin
    shourov.create_account('1234', 'shourov', 'shourov@gmail.com', '5432') # Admin
    shourov.check_total_balance() # Admin

    fahmid.deposit(30000) # User
    fahmid.check_balance() # User

    shourov.check_total_balance() # Admin

    sakib = Admin('1235', 'Sakib', 'sakib@gmail.com', '5433') # Admin
    sakib.create_account('1235', 'Sakib', 'sakib@gmail.com', '5433') # Admin
    sakib.check_total_balance() # Admin

    fahmid.check_balance() # User

    fahmid.withdraw(1000) # User
    fahmid.check_balance() # User

    fahmid.transfer(hero, 5000) # User
    hero.check_balance() # User

    sakib.check_transaction() # Admin
    sakib.check_total_balance() # Admin

    hero.take_loan(5000) # User
    hero.check_balance() # User

    sakib.check_total_balance() # Admin

    fahmid.check_balance() # User

    shourov.toggle_loan_feature(False) # Admin

    hero.take_loan(5000) # User
    fahmid.take_loan(5000) # User
    fahmid.check_balance() # User
    hero.check_balance() # User

    shourov.check_total_loan() # Admin
    shourov.check_transaction() # Admin

    hero.check_transaction_history() # User
    fahmid.check_transaction_history() # User

if __name__ == '__main__':
    main()
