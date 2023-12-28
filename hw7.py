import re
def word(string):
    return re.findall(pattern=r'\b[-a-zA-Zа-яА-ЯёЁ]+\b', string=string)
def main():
    input = input()
    mch = word(put)
    print(len(mch))
if __name__ == '__main__':
    main()