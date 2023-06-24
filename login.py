#%%
import os
import json

class CheckValidation:
    def __init__(self, username, email, password):
        self.accounts = []
        self.username = username
        self.email = email
        self.password = password
        
    def get_account(self):
        accounts = []
        user_infor = os.listdir('users_infor')
        for i in range(len(user_infor)):
            with open ("users_infor/" + user_infor[i], "r") as f:
                data = json.loads(f.read())
                accounts.append(data)
        return accounts

    #checking whether the username existed.
    def check_username(self):
        self.accounts = self.get_account()
        if len(self.username) == 0:
            return "empty"
        if len(self.accounts) == 0 and len(self.username) >= 4:
            return True
        elif len(self.accounts) != 0 and len(self.username) >= 4:
            for i in range(len(self.accounts)):
                if self.username == self.accounts[i]['username']:
                    return "existed"
                else:
                    return True
        else:
            return "tooshort"
    #valid email contains "@" and "." characters   
    def check_email(self):
        self.accounts = self.get_account()
        if len(self.email) == 0:
            return "empty"
        if "@" in self.email and "." in self.email:
            for i in range(len(self.accounts)):
                if self.email == self.accounts[i]["email"]:
                    return "existed"
                else:
                    return True
        else:
            return False

    #valid password contains at least a number and an uppercase letter
    def check_password(self):
        if len(self.password) == 0:
            return "empty"
        number = [letter for letter in self.password if letter.isdigit()]
        upper = [letter for letter in self.password if letter.isupper()]
        if len(number) != 0 and len(upper) != 0:
            return True
        else:
            return False
        
    def existed_account(self):
        self.accounts = self.get_account()
        for i in range(len(self.accounts)):
            if self.username == self.accounts[i]["username"] and self.email == self.accounts[i]["email"] and self.password == self.accounts[i]["password"]:
                return False
            

#%%
#enter username:str, email:str, password:str => return an account is a dictionary containing id, username, email, password
# add account to users folder when user register
class Register:
    def __init__(self):
        self.accounts = []
        self.id = 1
    def check_infor(self, username:str, email:str, password:str):# check validation of  user information
        check_valid = CheckValidation(username, email, password)
        check_email = check_valid.check_email()
        check_username = check_valid.check_username()
        check_password = check_valid.check_password()
        return check_username, check_email, check_password
    
    def add_account(self, username:str, email:str, password:str):# add new acount to the storage database
        check_name, check_email, check_pass = self.check_infor(username, email, password)
        if check_name==True and check_email==True and check_pass==True:
            self.id = len(os.listdir('users_infor')) + self.id
            account = {'id': self.id,
                       'username': username,
                       'email': email,
                       'password': password}
            self.accounts.append(account)

            file_name = 'users_infor/' + str(self.id) + "_" + username + "_" + password + '.json'

            with open(file_name, 'w') as file:
                file.write(json.dumps(account))
                


#%%
#login your account
class LogIn(Register):
    def __init__(self, username, password):
        super().__init__()
        self.__username = username
        self.__password = password
        self.accounts = Register().accounts


    def check_infor(self, user):
        if self.get_username in str(user) and self.get_password in str(user):
            return True


    def login(self):
        users = os.listdir('users_infor')
        for user in users:
            self.check_infor(user=user)
            
    def get_password(self):
        return self.__password
    
    def set_password(self, password):
        self.__password = password

    def get_username(self):
        return self.__username
    

    def set_username(self, username):
        self.__username = username


#%%
# log = Register()
# log.add_account('acdk', '2002@gmail.com', 'jF2oijf')
# log.add_account('aeijf', '2002@gmail.com', '104jfoiJf')
# log.add_account('hdl', '0212@gmail.com', '505Ilu')
# print(LogIn('acdk', 'jF2oijf').login())
# print(Register().check_infor('acdk', '0212@gmail.com', '505Ilu'))
# print(CheckValidation('acdk', '2002@gmail.com', 'jF2oijf').existed_account())
# %%
