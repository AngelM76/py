def main():

    crypt("new.txt", letters = {'A':'p', 'B':'7', 'C':'a', 'D':'#', 'E':'g', 'F':'€', 'G':'s', 'H':'o', 'I':'x', 'J':'&', 'K':'*', 'L':'+',
             'M':'f', 'N':'^', 'O':'q', 'P':')', 'Q':'/', 'R':'!', 'S':'0', 'T':'i', 'U':'%', 'V':'e', 'W':'1',
             'X':'b', 'Y':'r', 'Z':'3', 'a':'B', 'b':'-', 'c':':', 'd':'O', 'e':'Y', 'f':'5', 'g':'Q', 'h':'P', 'i':'4',
             'j':'(', 'k':'[', 'l':'¨', 'm':'M', 'n':'J', 'o':'"', 'p':'Z', 'q':'`', 'r':'8', 's':'2', 't':'6', 'u':'9',
             'v':'N', 'w':'H', 'x':'X', 'y':'D', 'z':'?'})
    decrypt("krypterad.txt", letters = {'p':'A', '7':'B', 'a':'C', '#':'D', 'g':'E', '€':'F', 's':'G', 'o':'H', 'x':'I', '&':'J', '*':'K', '+':'L',
             'f':'M', '^':'N', 'q':'O', ')':'P', '/':'Q', '!':'R', '0':'S', 'i':'T', '%':'U', 'e':'V', '1':'W',
             'b':'X', 'r':'Y', '3':'Z', 'B':'a', '-':'b', ':':'c', 'O':'d', 'Y':'e', '5':'f', 'Q':'g', 'P':'h', '4':'i',
             '(':'j', '[':'k', '¨':'l', 'M':'m', 'J':'n', '"':'o', 'Z':'p', '`':'q', '8':'r', '2':'s', '6':'t', '9':'u',
             'N':'v', 'H':'w', 'X':'x', 'D':'y', '?':'z'})

def crypt(file, letters):
    f = open(file, 'r')

    encrypted = ""
    for line in f:
        for letter in line:
            if letter in letters:
                encrypted += letters[letter]
            else:
                encrypted += letter
    f.close()
    f = open("krypterad.txt", "w")
    f.write(encrypted)
    f.close()

def decrypt(file, letters):
    f = open(file, 'r')

    decrypted = ""
    for line in f:
        for letter in line:
            if letter in letters:
                decrypted += letters[letter]
            else:
                decrypted += letter
    f.close()
    f = open("decrypterad.txt", "w")
    f.write(decrypted)
    f.close()

main()