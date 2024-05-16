import random
import string

from kiwisolver import strength

def generate_password(length,strength):
    if strength == "low":
        characters = string.ascii_letters + string.digits
    elif strength == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif strength == "high":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
    else:
        print("Invalid input")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    strength = input("Enter the password strength level (low, medium, high): ").lower()
    
    password = generate_password(length,strength)
    if password:
        print("Generated Password:", password)
if __name__ == "__main__":
    main()