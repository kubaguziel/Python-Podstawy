message = "\nPodaj dodatki, jakie chcesz dodać do pizzy: "
message += "\nPo wprowadzeniu dodatków, napisz 'koniec'. "
while True:
    dodatek = input(message)
    if message == 'koniec':
        break
    else: 
        print(f"Dodałeś {dodatek} do pizzy!")