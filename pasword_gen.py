import random
import string
import pyfiglet

def gen_password(length):
    if length < 8:
        print("!!!! Password should be at least of 8 characters.!!!!")
        return None
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password
def main():
    ascii_banner = pyfiglet.figlet_format("Pasword Generator")
    print(ascii_banner)
    length = int(input("Enter the length of the password: "))
    print("Your Password is : ", gen_password(length))

main()