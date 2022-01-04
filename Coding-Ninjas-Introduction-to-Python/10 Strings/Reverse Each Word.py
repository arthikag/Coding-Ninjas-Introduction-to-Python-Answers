def reverseWordSentence(Sentence):
  
    words = Sentence.split(" ")
      
    newWords = [word[::-1] for word in words]
      
    newSentence = " ".join(newWords)
  
    return newSentence
  
# Driver's Code 
Sentence = input()
print(reverseWordSentence(Sentence))