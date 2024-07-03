#import pizza

# można też tak, wtedy zaimportujemy tylko jedną funkcję z danego pliku/modułu
# from pizza import make_pizza
#lub
from pizza import make_pizza as mp 
#co zmieni nam nazwę funkcji

mp('salami','cheese','ananas')