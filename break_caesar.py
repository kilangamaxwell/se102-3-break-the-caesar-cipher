import re
import string

def encrypt_char(char, key):
  #Describes character encryption with support for casing and punctuation
  cap_state = []
  if char in string.punctuation + ' ':
    return char

  if char == char.upper():
    cap_state.append(True)
  else:
    cap_state.append(False)
  char = char.lower()
  nchar = ord(char) + key
  if nchar < 97:
    nchar = chr(122 - (96 - nchar))
  elif nchar > 122:
    nchar = chr((nchar - 122) + 96)
  else:
    nchar = chr(nchar)
  if cap_state[0] == True:
    nchar = nchar.upper()
  return nchar

def encrypt_caesar(text, key):
  #Describes text encryption
  ntext = text
  n_text = ''
  for ch in ntext:
    nchar = encrypt_char(ch, key)
    n_text += nchar
  return n_text

def decrypt_char(ci_char, key):
  #Describes character decryption, casing and punctuation
  cap_state = []
  if ci_char in string.punctuation + ' ':
    return ci_char

  if ci_char == ci_char.upper():
    cap_state.append(True)
  else:
    cap_state.append(False)
  ci_char = ci_char.lower()
  nci_char = ord(ci_char) - key
  if nci_char < 97:
    nci_char = 122 - (96 - nci_char)
    nci_char = chr(nci_char)
  elif nci_char > 122:
    nci_char = (nci_char - 122) + 96
    nci_char = chr(nci_char)
  else:
    nci_char = chr(nci_char)
  if cap_state[0] == True:
    nci_char = nci_char.upper()
  return nci_char

def decrypt_caesar(ciphertext, key):
  #Describes text decryption
  ntext = ciphertext
  o_text = ''
  for ch in ntext:
    o_char = decrypt_char(ch, key)
    o_text += o_char
  return o_text


MESSAGE = """
Jylbujm nby gimn zugiom nblyy qilxm onnylyx ch fcnylunoly, "Yn no, Vlony?" (Ypyh sio, Vlonom?) nbcm yrjlymmcih bum wigy xiqh ch bcmnils ni gyuh nby ofncguny vynlusuf vs ihy'm wfimymn zlcyhx. Nbcm mwyhy, ch qbcwb nby wihmjclunilm ch nby Myhuny ummummchuny Wuymul, cm ihy iz nby gimn xluguncw gigyhnm ih nby Mbueymjyulyuh mnuay. Nby uoxcyhwy bum domn qcnhymmyx nby ulliauhwy uhx bovlcm iz u lofyl qbi bum mioabn, qcnbch u lyjovfcw, ni vywigy u gihulwb, wigjulcha bcgmyfz ni nby aixm. Vlonom, u zlcyhx iz Wuymul uhx syn u guh qbi fipym Ligy (uhx zlyyxig) gily, bum dichyx nby wihmjclunilm ch nby ummummchuncih, u vynlusuf qbcwb cm wujnolyx vs nby nblyy qilxm uvipy ch nbcm zugiom Mbueymjyuly koiny.
"""

def main():
  #print(encrypt_char('y', 3))
  #print(decrypt_caesar('b', 3))
  for key in range(1, 27):
    print(str(key) + "\n" + decrypt_caesar(MESSAGE, key) + "\n")
  

if __name__ == "__main__":
  main()
