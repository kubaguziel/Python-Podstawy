nicknames = []
if nicknames:
    for nickname in nicknames:
        if nickname == 'admin':
            print("Witaj, admin! Czy chcesz przejrzeć dzisiejszy raport?")
        else:
            print(f"Witaj, {nickname.title()}! Dziękujemy że ponownie się zalogowałeś.")
else: 
    print("Lista użytkowników jest pusta.")
