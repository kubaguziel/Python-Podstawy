sandwich_orders = ['Mięsna','Wegetariańska','Ostra','Miesiany_miesiany']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"Przygotowano: {current_order}")
    finished_sandwiches.append(current_order)

print("\nGotowe zamówienia: ")
for orders in finished_sandwiches:
    print(f"\n{orders}")
