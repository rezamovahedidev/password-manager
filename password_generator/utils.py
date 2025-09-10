import secrets
import string

class PasswordManager():
    def __init__(self,filename='password.txt',default_pass= 12):
        self.filename = fname
        self.len = len_
        self.default_pass = default_pass 

        with open('password.txt','w') as file:
            file.write('=====PASSWORDS====\n')
    def g_random_password(self,len=None):
        if self.len == None:
           length =  self.default_pass
