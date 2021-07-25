characterCount = 0;
wordCount = 0;

testSentence = "Here we go. I don't want to get into it, but this is really needed.";
for i in testSentence:
    characterCount += 1;
    for j in i:
        print(i + " " + j)
        if i == " ":
            wordCount += 1;
            print('no')
        if j.isalpha:
            print('yes')
        
print(wordCount + 1)
print(characterCount)
