import random
import string

def generate_password(length):
    if length < 4:
        return "Password too short! Must be at least 4 characters."

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_chars = letters + digits + symbols

    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    password += [random.choice(all_chars) for _ in range(length - 3)]
    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    print("Welcome to the Random Password Generator!")
    try:
        user_length = int(input("Enter password length (min 4): "))
        pwd = generate_password(user_length)
        print("✅ Your secure password is:", pwd)
    except ValueError:
        print("❌ Please enter a valid number.")
