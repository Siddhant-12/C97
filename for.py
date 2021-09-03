introString=input("enter a string")
characterCount=0
wordCount=0

for i in introString:
    characterCount=characterCount+1
    if(i==" "):
        wordCount=wordCount+1

print(characterCount)
print(wordCount)