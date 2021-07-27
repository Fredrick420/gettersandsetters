import camelcase

c = camelcase.Camelcase()

def getUserSentence():
    userSentence = input("Enter your sentence")
    print(c.hump(userSentence))
getUserSentence()    