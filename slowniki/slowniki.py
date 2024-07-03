alien_0 = {'color': 'zielony', 'points':5}   #inicjalizacja słownika

print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0          #dodawanie pary klucz-wartość do słownika
alien_0['y_position'] = 25
print(alien_0)
alien_0['color'] = 'żółty'         #modyfikacja wartości słownika
print(alien_0)
alien_0['speed'] = 'średnio'
print(f"Początkowa wartość x-position: {alien_0['x_position']}")
if alien_0['speed'] == 'wolno': 
    x_increment = 1
elif alien_0['speed'] == 'średnio':
    x_increment = 2
else:
    x_increment = 3
#nowe położenie to suma dotychczasowegho położenia i wartości x_increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"Nowa wartość x_position: {alien_0['x_position']}")
alien_0['speed'] = 'szybko'
