#language translator
#all vowels are converted to a g
#vowels--> g

#for example:
#dog-->dgg
#cat-->cgt

def translator(phrase):
    translation = ""

    #looping through the phrase to change the vowel

    for letter in phrase:
        if letter in "AEIOUaeiou":
        #if letter.lower() in "aeiou":
            if letter.isupper():
               translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translator(input("Enter a phrase: ")))