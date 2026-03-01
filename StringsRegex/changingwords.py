#Nathalia é uma escritora que está revisando um texto para publicação. Durante o processo, ela percebeu que usou a palavra "bom" repetidamente, quando queria expressar algo mais forte, como "ótimo". Para economizar tempo, Nathalia quer substituir automaticamente todas as ocorrências da palavra "bom" por "ótimo" no texto.
#Ajude Nathalia a criar um programa que solicite um texto, a palavra que será substituída e a nova palavra. O programa deve exibir o texto com as alterações aplicadas.
text = input("Write the text for revision: ")
change_word = input("Write the word to be changed: ")
new_word = input("Write the new word: ")
replaced_text = text.replace(change_word, new_word)
print("Revised text:", replaced_text)