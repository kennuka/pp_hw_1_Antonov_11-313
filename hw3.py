morse = morse_alphabet = {
    'а': '.-',
    'б': '-..',
    'в': '.--',
    'г': '--.',
    'д': '-..',
    'е': '.',
    'ё': '.',
    'ж': '...-',
    'з': '--..',
    'и': '..',
    'й': '.---',
    'к': '-.-',
    'л': '.-..',
    'м': '--',
    'н': '-.',
    'о': '---',
    'п': '.--.',
    'р': '.-.',
    'с': '...',
    'т': '-',
    'у': '..-',
    'ф': '..-.',
    'х': '....',
    'ц': '-.-.',
    'ч': '---.',
    'ш': '----',
    'щ': '--.-',
    'ъ': '--.--',
    'ы': '-.--',
    'ь': '-..-',
    'э': '..-..',
    'ю': '..--',
    'я': '.---',
    ' ': '    '}
input = input('Введите ваш текст: ').lower()
new_text = ''
print('')
for sing in input:
    new_text += morse.get(sing, '    ') + ' '
print(new_text)
