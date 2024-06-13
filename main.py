import hashlib


def hash_password(password):
    # Using a simple hashing function for demonstration purposes
    return hashlib.sha256(password.encode()).hexdigest()


def generate_password_hash():
    with open("10-million-password-list-top-10000.txt", "r") as passwords:
        with open("10-million-password-database.txt", "w") as file:
            for password in passwords:
                password = password.strip()  # Remove newline character
                hashed_password = hash_password(password)
                file.write(f"{hashed_password}:{password}\n")


# generate_password_hash()


# get 10-million-password-database
# Load the rainbow table
rainbow_table = {}
with open('10-million-password-database.txt', 'r') as file:
    for line in file:
        hashed_password, password = line.strip().split(':')
        rainbow_table[hashed_password] = password


# copy and paste here
database_password = [
    [
        2,
        "bishal",
        "bishaljoshi@gmail.com",
        "ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f"
    ],
    [
        3,
        "bishal",
        "biraj@gmail.com",
        "ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f"
    ],
    [
        4,
        "bishal",
        "bhes@gmail.com",
        "ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f"
    ],
    [
        5,
        "bishal",
        "apple@gmail.com",
        "ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f"
    ],
    [
        6,
        "bishal",
        "bishal@gmail.com",
        "ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f"
    ],
    [
        7,
        "bishal",
        "Bishal1@gmail.com",
        "ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f"
    ],
    [
        8,
        "Bhesh",
        "brthapa@maitriservices.com",
        "969fdf03e82fe9c964ed1f9177f5914246b0f30620a7c84180bbb42a65953224"
    ],
    [
        9,
        "shuii",
        "das@gmail.com",
        "c96b109b726f20c946827f22f508695bc2ffd871c63e4d168ef1b18316b12e51"
    ],
    [
        10,
        "spaudel",
        "spaudel@maitriservices.com",
        "9119a69c8a940be240612c9ff6177d5342332f052a5e1049938de3a010b75dfa"
    ],
    [
        11,
        "John Doe",
        "john@me.com",
        "ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f"
    ],
    [
        12,
        "John Doe",
        "john1@me.com",
        "ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f"
    ]
]

# filter the password and email
filtered_email_password = {
    data[2]: data[3] for data in database_password}


# Attempt to crack passwords using the rainbow table
cracked_passwords = {}
for username, hashed_password in filtered_email_password.items():
    if hashed_password in rainbow_table:
        cracked_passwords[username] = rainbow_table[hashed_password]

# Print the cracked passwords
if cracked_passwords:
    print("Cracked passwords:")
    for username, password in cracked_passwords.items():
        print(f"Username: {username}, Password: {password}")
else:
    print("No passwords cracked.")
