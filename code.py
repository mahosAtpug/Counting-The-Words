def countWordsFromFile():
    fileName = input("Please Enter The Name of The File : ")
    file = open(fileName , "r")
    numberOfWords = 0
    for line in file:
        words = line.split()
        numberOfWords = numberOfWords + len(words)

    print("Total Number of Words In Your Selected File Are :" , numberOfWords)

countWordsFromFile()
