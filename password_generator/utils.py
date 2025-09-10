import secrets
import string

class PasswordManager():
    
    '''
    a password manager return random passwords and save it
    '''

    
    def __init__(self,filename='password.txt',default_pass= 12):
        self.filename = filename
        self.default_pass = default_pass 

        with open(self.filename,'w') as file:
            file.write('=====PASSWORDS====\n')

    def __len__(self) :
        self.default_pass

    def __str__(self):
        self.filename


    def g_random_password(self,lentgh=None):
        if lentgh is None:
           lentgh =  self.default_pass
        else:
            chars = string.ascii_letters + string.ascii_uppercase + string.digits
            passwords = ''.join(secrets.choice(chars) for _ in range(lentgh))

        return passwords

    def save_password(self, password):
        '''
        save password to file txt
        '''
        try:
            print('password created succesfullly')
            with open(self.filename,'a') as file:
                file.write(password)
        except ValueError:
            print('Value Error check the the lenght or password')


    def number_password(self,lenght=None):
        if lenght is None:
            lenght = self.default_pass
        
        number_pass = string.digits + string.digits
        passwords = ''.join(secrets.choice(number_pass) for _ in range(lenght))
        
        return passwords

    def string_password(self,lenght=None):
        if lenght is None:
            lenght = self.default_pass

        string_pass = string.ascii_letters + string.ascii_uppercase + string.ascii_lowercase
        passwords = ''.join(secrets.choice(string_pass) for _ in range(lenght))

        return passwords
