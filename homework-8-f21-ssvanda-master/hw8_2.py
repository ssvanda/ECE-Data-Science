from helper import remove_punc
import numpy as np
import string
import nltk
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
nltk.download('punkt')

#Clean and stem the contents of a document
#Takes in a file name to read in and clean
#Return a list of words, without stopwords and punctuation, and with all words stemmed
# NOTE: Do not append any directory names to doc -- assume we will give you
# a string representing a file name that will open correctly
def read_and_clean_doc(doc) :
    #1. Open document, read text into *single* string
    with open(doc,'r') as myfile:
        docString = myfile.read()
    #2. Tokenize string using nltk.tokenize.word_tokenize
    doc_tokens = word_tokenize(docString)
    #3. Filter out punct1uation from list of words (use remove_punc)
    doc_tokens_no_punc = remove_punc(doc_tokens)
    #4. Make the words lower case
    for i in range(len(doc_tokens_no_punc)):
        doc_tokens_no_punc[i] = doc_tokens_no_punc[i].lower()

    #5. Filter out stopwords
    # go through words from 27, check if in stop or not, make list thats not stop words
    stop = stopwords.words('english')
    doc_tokens_clean = []
    for n in doc_tokens_no_punc:
        if not(n) in stop:
            doc_tokens_clean.append(n)

    #6. Stem words
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    doc_tokens_clean_stem = [stemmer.stem(x) for x in doc_tokens_clean]
    doc_tokens_clean_lem  = [lemmatizer.lemmatize(x) for x in doc_tokens_clean_stem] 
    words = doc_tokens_clean_lem
    

    return doc_tokens_clean_stem
    
#Builds a doc-word matrix for a set of documents
#Takes in a *list of filenames*
#
#Returns 1) a doc-word matrix for the cleaned documents
#This should be a 2-dimensional numpy array, with one row per document and one 
#column per word (there should be as many columns as unique words that appear
#across *all* documents. Also, Before constructing the doc-word matrix, 
#you should sort the wordlist output and construct the doc-word matrix based on the sorted list
#
#Also returns 2) a list of words that should correspond to the columns in
#docword
def build_doc_word_matrix(doclist) :
    #1. Create word lists for each cleaned doc (use read_and_clean_doc)
    wordlist = []
    cleanedDoc = []

    for doc in doclist:
        cleanedDoc.append(read_and_clean_doc(doc))
    doclist = cleanedDoc    
    #read_and_clean_doc(doc)
    for doc in doclist:
        for word in doc:
            if(not(word in wordlist)):
                wordlist.append(word)
   
    wordlist.sort()
    #2. Use these word lists to build the doc word matrix
    docword = []
    for doc in doclist:
        doc_vec = [0]*len(wordlist) #Each document is represented as a vect or of word occurrences
        for word in doc:
            ind = wordlist.index(word)
            doc_vec[ind] += 1 #Increment the corresponding word index
        docword.append(doc_vec)   
    docword = np.array(docword)

    return docword, wordlist
    
#Builds a term-frequency matrix
#Takes in a doc word matrix (as built in build_doc_word_matrix)
#Returns a term-frequency matrix, which should be a 2-dimensional numpy array
#with the same shape as docword
def build_tf_matrix(docword) :
    #fill in
    tf = []
    row = len(docword)
    col = len(docword[0])
    rowSum = np.sum(docword, axis=1)
    for rowNum in range(row):
        myRow = []
        for colNum in range(col):
            value = docword[rowNum][colNum]
            myRow.append(value / rowSum[rowNum])
        tf.append(myRow)
    tf = np.array(tf)

    


    return tf
    
#Builds an inverse document frequency matrix
#Takes in a doc word matrix (as built in build_doc_word_matrix)
#Returns an inverse document frequency matrix (should be a 1xW numpy array where
#W is the number of words in the doc word matrix)
#Don't forget the log factor!
def build_idf_matrix(docword) :
    #fill in
    idf = []
    tf = build_tf_matrix(docword)
    idf = tf.reshape(1,10)
    
    return idf
    
#Builds a tf-idf matrix given a doc word matrix
def build_tfidf_matrix(docword) :
    #fill in
    tfidf = []

    

    return tfidf
    
#Find the three most distinctive words, according to TFIDF, in each document
#Input: a docword matrix, a wordlist (corresponding to columns) and a doclist 
# (corresponding to rows)
#Output: a dictionary, mapping each document name from doclist to an (ordered
# list of the three most common words in each document
def find_distinctive_words(docword, wordlist, doclist) :
    distinctive_words = {}
    #fill in
    #you might find numpy.argsort helpful for solving this problem:
    #https://docs.scipy.org/doc/numpy/reference/generated/numpy.argsort.html
    


    distinctiveWords = {}
    #fill in
    #you might find numpy.argsort helpful for solving this problem:
    

    
    return distinctive_words

if __name__ == '__main__':
    from os import listdir
    from os.path import isfile, join, splitext
    
    ### Test Cases ###
    directory='lecs'
    path1 = join(directory, '1_vidText.txt')
    path2 = join(directory, '2_vidText.txt')
    
    # Uncomment and recomment ths part where you see fit for testing purposes
    
    print("*** Testing read_and_clean_doc ***")
    print(read_and_clean_doc(path1)[0:5])
    
    print("*** Testing build_doc_word_matrix ***") 
    doclist =[path1, path2]
    docword, wordlist = build_doc_word_matrix(doclist)
    print(docword.shape)
    print(len(wordlist))
    print(docword[0][0:10])
    print(wordlist[0:10])
    print(docword[1][0:10])
    
    print("*** Testing build_tf_matrix ***") 
    tf = build_tf_matrix(docword)
    print(tf[0][0:10])
    print(tf[1][0:10])
    print(tf.sum(axis =1))
    
    print("*** Testing build_idf_matrix ***") 
    idf = build_idf_matrix(docword)
    print(idf[0][0:10])
    '''
    print("*** Testing build_tfidf_matrix ***") 
    tfidf = build_tfidf_matrix(docword)
    print(tfidf.shape)
    print(tfidf[0][0:10])
    print(tfidf[1][0:10])
    print("*** Testing find_distinctive_words ***")
    print(find_distinctive_words(docword, wordlist, doclist))
    '''
