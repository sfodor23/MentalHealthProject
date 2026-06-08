#Import libraries
import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
import re
import string
import contractions
import wordninja

#Set up a dataframe of the initial data
Data = pd.read_csv("Input/SuicideDataset.csv")
Data = Data.iloc[0:len(Data) // 3].copy()
Data = Data.drop(columns=['Index'], errors='ignore')

#Extract a message from the initial data for later comparison 
OriginalMessage = Data['Text'][52]

#Set up non-Regex processing
nltk.download("stopwords")
Stopwords = nltk.corpus.stopwords.words('english')
Lemmatizer = WordNetLemmatizer()

#Set up Regex processing
EmailRegex = r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
RegexesToRemove = [EmailRegex, r'Subject:', r'Re:']

#Loop to process initial data
for i in range(0, len(Data)):
    #Define message and convert to string
    Message = str(Data['Text'][i])

    #Remove selected Regular Expressions
    for Regex in RegexesToRemove:
        Message = re.sub(Regex, '', Message)
    
    #Remove/edit contractions if possible (e.g. can't -> cannot)
    if Message:
        try:
            Message = contractions.fix(Message)
        except IndexError:
            Message = Message

    #Remove special characters
    Message = re.sub('[^a-zA-Z]', ' ', Message)

    #Make message entirely lowercase
    Message = Message.lower()

    #Split message into individual words
    Message = wordninja.split(Message)

    #Remove stop words and lemmatize remaining words (e.g. skies -> sky)
    Message = [Lemmatizer.lemmatize(Word) for Word in Message if not Word in set(Stopwords)]
    
    #Rejoin message into one string
    Message = ' '.join(Message)

    #Apply changes to the Dataframe
    Data.iloc[i, Data.columns.get_loc('Text')] = Message

    #Progression Check
    if i % 2500 == 0:
        print(f"{round((i/len(Data))*100, 1)}% Processed")

#Extract a message from the processed data for comparison
ProcessedMessage = Data['Text'][52]

#Compare initial message with processed message
print(f'Sample Original Message: "{OriginalMessage}"')
print(f'Sample Processed Message: "{ProcessedMessage}"')

#Export processed data as an accessible .csv file
Data.to_csv('Output/ProcessedData.csv')

