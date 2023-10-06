import random
import string

class PasswordGenerator:
    def __init__(self):
        self.character_sets = {
            "lowercase": string.ascii_lowercase,
            "uppercase": string.ascii_uppercase,
            "digits": string.digits,
            "special": string.punctuation
        }

    def generate_password(self, length, include=None, exclude=None, min_strength=3):
        if length < 6:
            raise ValueError("Password length should be at least 6 characters.")

        if include is None:
            include = list(self.character_sets.keys())

        character_set = ''.join([self.character_sets[char] for char in include if char in self.character_sets])

        if exclude is not None:
            character_set = ''.join([char for char in character_set if char not in exclude])

        if len(character_set) < min_strength:
            raise ValueError("Password strength  not met with the selected character set.")

        password = ''.join(random.choice(character_set) for _ in range(length))
        return password

def main():
    password_generator = PasswordGenerator()

    while True:
        try:
            length = int(input("Enter the desired password length (at least 6): "))
            if length < 6:
                print("Password length should be at least 6 characters. Please try again.")
                continue

            include = input("Enter character types to include (lowercase, uppercase, digits, special), separated by commas (default: all): ").split(',')
            exclude = input("Enter characters to exclude (e.g., !&*@#$%): ")

            min_strength = int(input("Enter minimum password strength (number of character types): "))

            password = password_generator.generate_password(length, include=include, exclude=exclude, min_strength=min_strength)

            print("Generated Password:", password)
            break
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
