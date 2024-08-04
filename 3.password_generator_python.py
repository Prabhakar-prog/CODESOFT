import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.sample(characters, length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired length of your password: "))
            if length <= 0:
                print("Length must be greater than zero. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer length.")
    
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
