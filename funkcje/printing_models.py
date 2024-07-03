def print_models(unprinted_designs, completed_models):
    """Symulujemy wydruk poszczególnych projektów, 
    dopóki pozostał jakikolwiek projekt na liście. 
    Każdy wydrukowany model zostaje przeniesiony na listę completed_models.
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Wydruk projektu: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Wyświetla modele, które zostały wydrukowane"""
    print("\nWydrukowane zostały następujące modele: ")
    for complete_model in completed_models:
        print(complete_model)


unprinted_designs = ['kot','popielniczka','stojak na słuchawki']
finished_designs = []

print_models(unprinted_designs[:],finished_designs) #dodanie [:] oznacza, że funkcja będzie korzystała z kopii listy, dzięki czemu nie zmieni jej zawartosci
show_completed_models(finished_designs)