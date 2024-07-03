filename = "alice.txt"

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Plik o nazwie {filename} nie istnieje.")
else:
    #obliczenie przybliżonej liczy słów w pliku
    words = contents.split()
    num_words = len(words)
    print(f"\nPlik zawiera {num_words} słów. ")