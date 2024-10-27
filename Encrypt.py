while True:
  print("Hello , please choose your option:\n\t 1)Encrypt\n\t 2)Decrypt\n\t 3)Exit")
  choise = input("your choise is:")
  
  if choise == "1" or choise == "Encrypt" :
    text = input("your text:")
    Encrypt_text = ""
    for x in text :
      c = ord(x) * 3 - 4 + 6 
      Encrypt_text += chr(c)
    print("Encrypt text: ", Encrypt_text)
    print("*" * 30 + "\n")


  elif choise == "2" or choise == "Decrypt" :
     Encrypt_text = input("your Decrypt text:")
     text = ""
     for x in Encrypt_text :
      c = ((ord(x) - 6) + 4 ) // 3
      text += chr(c)
     print("Encrypt text: ", text)
     print("*" * 30 + "\n")
  
  elif choise == "3" or choise == "Exit" :
    print("See You Again !")
    print("*" * 30 + "\n")
  
  else:
    print("your choise is wrong !")
    print("*" * 30 + "\n")