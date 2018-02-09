def caesar(ciphertext):
    for i in range(26):
      s = ""
      for letter in ciphertext.lower():
          if letter != ' ':
              plainletter = ord(letter) + i
              if plainletter > ord('z'):
                  plainletter -= 26
              s += chr(plainletter)
          else:
              s += ' '
      print s
    print

def substitution(ciphertext):
    plaintext = ""
    for letter in ciphertext:
        if letter != ' ':
            plaintext += "-"
        else:
            plaintext += ' '
    print ciphertext
    print plaintext
    print
    while True:
        while True:
            ciphlet = raw_input("Input letter to replace: ").strip().upper()
            if len(ciphlet) == 1:
                break
        print ciphlet
        while True:
            plainlet = raw_input("Input replacement letter: ").strip().lower()
            if len(plainlet) == 1:
                break
        print plainlet
        print
        plain2 = ""
        for i in range(len(ciphertext)):
            if ciphertext[i] == ciphlet:
                plain2 += plainlet
            else:
                plain2 += plaintext[i]
        plaintext = plain2
        print ciphertext
        print plaintext
        print

if __name__== "__main__":
    ciphertext = raw_input("What is the ciphertext that you would like to decipher? ").upper()
    while True:
        cipher = raw_input("What kind of cipher is it? ").strip()
        try:
            eval(cipher + "(\"" + ciphertext + "\")")
            break
        except:
            print "Please choose a valid cipher (Caesar or substitution)."
            print
