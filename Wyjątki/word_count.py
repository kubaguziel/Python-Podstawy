def count_words(filename):
    """Funkcja licząca ilość słów w danym pliku"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
        #print(f"Nie udało się odnaleźć pliku {filename}, ")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"Plik {filename} zawiera {num_words} słów.")

filename = ['alice.txt','little_women.txt','moby_dick.txt','sidhartha.txt']

for file in filename:
    count_words(file)