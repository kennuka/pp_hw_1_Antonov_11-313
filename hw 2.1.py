morse_code_eng = {'A': '.- ','B': '-... ','C': '-.-. ',
        'D': '-.. ','E': '. ','F': '..-. ',
        'G': '--. ','H': '.... ',   'I': '.. ',
        'J': '.--- ','K': '-.- ',    'L': '.-.. ',
        'M': '-- ','N': '-. ',     'O': '--- ',
        'P': '.--. ','Q': '--.- ',   'R': '.-. ',
        'S': '... ','T': '- ',      'U': '..- ',
        'V': '...- ' ,'W': '.-- ',  'X': '-..- ',
        'Y': '-.-- ','Z': '--.. ',
        }
word = input('Напишите слово которое нужно перевести на код Морзе: ')
for translate in word:
        for letter in translate:
                print(morse_code_eng[letter],end=' ')