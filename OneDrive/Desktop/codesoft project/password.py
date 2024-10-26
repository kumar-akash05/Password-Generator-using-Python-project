import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 for better security.")
        return None
    
 
    lower = string.ascii_lowercase   
    upper = string.ascii_uppercase   
    digits = string.digits      
    symbols = string.punctuation   

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_characters = lower + upper + digits + symbols
    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)
    return ''.join(password)

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        password = generate_password(length)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
