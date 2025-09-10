import pwd
import secrets
import string

class PasswordManager():
    '''
    a password manager return random passwords and save it
    '''
    def __init__(self,filename='password.txt',default_pass= 12):
        self.filename = fname
        self.len = len_
        self.default_pass = default_pass 

        with open('password.txt','w') as file:
            file.write('=====PASSWORDS====\n')
        
    def g_random_password(self,len=None):
        if self.len == None:
           length =  self.default_pass
        
        chars = string.ascii_letters + string.ascii_uppercase + string.digits
        passwords = ''.join(secrets.choice(chars) for _ in range(length))

        return passwords

    def save_password(self, password,service):
        '''
        save password to file txt
        '''
        print('====PASWORD SAVED===\n')

        with open(self.filename,'a') as file:
            file.write(self.filename, '\n')

    def number_password(self,len=None):
        if not self.len:
            lenght = self.default_pass
        
        number_pass = (string.digits **2) + (string.digits **2)
        passwords = ''.join(secrets.choice(number_pass) for _ in range(12))