import string
import secrets

print("======== Password Generator========")


length = int(input("Enter the desired length of the password: "))

if length < 8:
    print("Password length should be at least 8 characters for security reasons.")
else:
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(secrets.choice(characters) for i in range(length))

    print("\nGenerated password: ", password)

    print("Password generated successfully!")
