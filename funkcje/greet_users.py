def greet_users(names):
    """Wyświetla proste powitanie każdemu użytkownikowi z listy"""
    for name in names:
        msg = f"Witaj {name.title()}, dobrze cię widzieć!"
        print(msg)

usernames = ['Kuba','Paweł','Wojtek','Piotrek']
greet_users(usernames)