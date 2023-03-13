def word_count(sentece):
    
    # Remove special chars and punctuation
    table = str.maketrans("", "", ",.'\"")
    sentece = sentece.translate(table)
    
    contDict = {}
    for palavra in sentece.split(" "):
        #print(f"Palavra: {palavra}")
        if palavra in contDict:
            contDict[palavra] += 1
        else:
            contDict[palavra] = 1

    # Order Dict Larger to smaller
    contDict = dict(sorted(contDict.items(), key=lambda item: item[1], reverse=True))

    # Get first 3 largest elements
    countAux = 0
    dictAux = {}
    for palavra, qtde in contDict.items():
        countAux += 1
        dictAux[palavra] = qtde        
        if countAux == 3:
            break
        
    return dictAux

if __name__ == "__main__":
    sentence = "Aqui vai uma frase que pode ter palavras repetidas ou nao, se nao houver palavras repetidas nao tem problema."
    print(word_count(sentence))