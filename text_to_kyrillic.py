# kyrillic letters, do not touch
text_to_cyrillic = {
    'a': 'а', 'b': 'б', 'c': 'ц', 'd': 'д', 'e': 'е', 'f': 'ф', 'g': 'г',
    'h': 'х', 'i': 'и', 'j': 'й', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н',
    'o': 'о', 'p': 'п', 'q': 'қ', 'r': 'р', 's': 'с', 't': 'т', 'u': 'у',
    'v': 'в', 'w': 'ў', 'x': 'кс', 'y': 'ы', 'z': 'з',
    'A': 'А', 'B': 'Б', 'C': 'Ц', 'D': 'Д', 'E': 'Е', 'F': 'Ф', 'G': 'Г',
    'H': 'Х', 'I': 'И', 'J': 'Й', 'K': 'К', 'L': 'Л', 'M': 'М', 'N': 'Н',
    'O': 'О', 'P': 'П', 'Q': 'Қ', 'R': 'Р', 'S': 'С', 'T': 'Т', 'U': 'У',
    'V': 'В', 'W': 'Ў', 'X': 'КС', 'Y': 'Ы', 'Z': 'З'
}

def to_cyrillic(text):
    return ''.join(text_to_cyrillic.get(char, char) for char in text)

# configuration
normal_text = "your text"
cyrillic_text = to_cyrillic(normal_text)
print(cyrillic_text)
