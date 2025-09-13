import secrets
import string
from rich.table import Table
from rich.console import Console


class PasswordManager:
    """
    A simple password manager:
    - Generate random passwords (letters, numbers, mixed)
    - Save passwords to a file
    - Show passwords in CLI with rich tables
    - Remove last password
    """

    def __init__(self, filename='password.txt', default_pass=12):
        self.filename = filename
        self.default_pass = default_pass

        # Initialize the file with a header if it does not exist
        with open(self.filename, 'w') as file:
            file.write('===== PASSWORDS =====\n')

    def __len__(self):
        # Return default password length
        return self.default_pass

    def __str__(self):
        # Return filename string
        return f"Password file: {self.filename}"

    def g_random_password(self, length=None):
        """Generate a random password with letters and digits"""
        if length is None:
            length = self.default_pass

        chars = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(chars) for _ in range(length))
        return password

    def save_password(self, password):
        """Save a password to the file"""
        try:
            with open(self.filename, 'a') as file:
                file.write(password + "\n")
            print("Password saved successfully.")
        except ValueError:
            print("Value Error: check the password length.")

    def number_password(self, length=None):
        """Generate a password only with digits"""
        if length is None:
            length = self.default_pass

        digits = string.digits
        password = ''.join(secrets.choice(digits) for _ in range(length))
        return password

    def string_password(self, length=None):
        """Generate a password only with letters"""
        if length is None:
            length = self.default_pass

        letters = string.ascii_letters
        password = ''.join(secrets.choice(letters) for _ in range(length))
        return password

    def show_password(self, filename='password.txt'):
        """Show all passwords in a table using rich"""
        console = Console()
        table = Table(title="PASSWORDS")

        table.add_column("ID", style="green")
        table.add_column("Password", style="red")

        with open(filename, 'r') as file:
            for i, line in enumerate(file, start=1):
                if line.strip():
                    pwd = line.strip()
                    table.add_row(str(i), pwd)

        console.print(table)

    def remove_password(self, filename='password.txt'):
        """Remove the last saved password"""
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()

            if len(lines) <= 1:  # Only header exists
                print("No password found. Please create one first.")
                return

            # Remove the last line
            lines = lines[:-1]

            with open(filename, 'w') as file:
                file.writelines(lines)

            print("Last password deleted successfully.")
        except FileNotFoundError:
            print("Password file not found.")

    def encrypt_password(self):
        """Placeholder for future encryption feature"""
        pass