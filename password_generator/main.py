from utils import PasswordManager

pas = PasswordManager()

while True:
    str_ = pas.string_password(12)
    pas.save_password(str_)
    pas.show_password(filename='password.txt')
