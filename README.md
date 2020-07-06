# Question-Answering-System

Developed a model that takes user query as an input and answers the query by matching the user question with predefined questions using cosine similarity.
Also created a basic Graphical User Interface using Tkinter.

stored 20 questions and answers in seperate lists.
defined stopwords. words that carry no inherent meaning are excluded such as "a, the, and" e.t.c

saved all the words in the questions in a list (without stopwords).
assigned unique numeric values to each unique words in the questions through CountVectorizer and transofrmed the results into an array. 
Used cosine similarity to compare the similarity between the predefined questions.

cosine similarity = a/(√b x √c)        where a=count of all the common 1's,    b=count of all 1's in first qs,  c= count of 1's in second qs

User is prompted to ask the question. 
stopwords are removed and the words are stored in a list.
compares cosine similarity between user question and default questions

GUI:
root is defined and canvas is 1080x1920.
customized background image is used.
Working frame of question and user input space are defined.
a button is added and the answer space is defined.
