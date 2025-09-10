from utils import PasswordManager

pas = PasswordManager()

str_ = pas.string_password(12)
pas.save_password(str_)
print(pas.filename)