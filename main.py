import random


def generate_random_password(number, length):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£#$%&*.?0123456789'
    
    passwords = []

    for pwd in range(number):
        password = ''

        for i in range(length):
            password += random.choice(chars)
        
        passwords.append(password)

    return passwords


def main():
    print("=-=" * 12)
    print("Password Generator")
    print("=-=" * 12)

    number = int(input("\nAmount of passwords to generate: "))
    length = int(input("Input your password length: "))

    passwords = generate_random_password(number, length)

    print("\nHere are your passwords:")

    for password in passwords:
        print(password)


if __name__ == '__main__':
    main()