# Virtual Assistant - Cubic
Virtual Assistant using Artificial Intelligence - Cubic. 
This project is based on Neural Network.
Implemented with Python using PyTorch, enables natural language understanding and responsive interactions with users through neural network training.
<_____Run Cubic.py File_____>

Summary of Project :

Listen.py ----->
This code imports the speech_recognition library and defines a function named "Listen" that listens to the user's voice input from a microphone, recognizes the speech using Google's speech recognition API, and returns the recognized text as a string. If the API fails to recognize the speech or if there is no speech input, an empty string is returned.

Speak.py ----->
This code imports the pyttsx3 library for text-to-speech synthesis and defines a Say function that takes a string argument and converts it to speech using the pyttsx3 library. The function initializes the pyttsx3 engine, sets the speech rate and voice, and then calls the say method of the engine to generate the speech output. Finally, the function calls the runAndWait method of the engine to ensure that the speech output is played before the function terminates. The Say function is called with the string "Hello, I am Cubic" as an argument.

Brain.py ----->
This code defines a neural network model using the PyTorch deep learning framework. It first imports the nn module from the torch library.
The NeuralNet class inherits from the nn.Module class, which is the base class for all neural network modules in PyTorch. The class takes in three parameters during initialization: the input size, hidden size, and number of output classes for the network.
The class defines three fully connected layers (l1, l2, and l3), each with a ReLU activation function. The forward() function specifies the forward pass of the network, taking in an input tensor x and returning the output tensor out.
Overall, this code defines a simple feedforward neural network with two hidden layers, making it suitable for various classification tasks.

intents.json ----->
This is a JSON file containing intents for a virtual assistant, with tags for greeting, goodbye, health, identity, day, time, date, Wikipedia search, and Google search. Each intent has a set of patterns that the assistant can recognize and a set of responses to provide to the user.

Task.py ----->
This code defines several functions for executing different types of queries:
Time() function returns the current time using the datetime module and uses the Say() function to speak the time.
Date() function returns the current date using the datetime module and uses the Say() function to speak the date.
Day() function returns the current day using the datetime module and uses the Say() function to speak the day.
NonInputExecution(query) function takes a query as input and executes it based on its content. If the query contains the word "time", it calls the Time() function. If it contains the word "date", it calls the Date() function. If it contains the word "day", it calls the Day() function.
InputExecution(tag,query) function takes a tag and a query as input and executes the query based on its tag. If the tag contains the word "wikipedia", it uses the wikipedia module to search for a summary of the query and uses the Say() function to speak the summary. If the tag contains the word "google", it uses the pywhatkit module to search for the query on Google.

NeuralNetwork.py ----->
This code defines several functions used in natural language processing (NLP). It first imports the numpy and nltk libraries, and specifically the PorterStemmer class from the nltk.stem.porter module.
The tokenize() function uses the nltk library to tokenize a sentence into a list of words. The stem() function uses the PorterStemmer class to stem a word by removing any suffixes and converting it to lowercase.
The bag_of_words() function creates a bag of words representation of a tokenized sentence, using the stem() function to stem each word. It first creates an array of zeros with the same length as the total number of words in the vocabulary. It then iterates through each word in the vocabulary, setting the corresponding element in the array to 1 if the word appears in the tokenized sentence.
Overall, these functions are useful for pre-processing natural language text data before using it for various NLP tasks such as sentiment analysis, text classification, and more.

Train.py ----->
This code is for training a neural network model to understand and classify different intents in natural language using the intents.json file. It starts by reading the data from the intents.json file, tokenizing and stemming the words in the data, and creating a bag of words. Then, the data is split into x_train and y_train for training the neural network. The model is defined and trained using a DataLoader and CrossEntropyLoss. Finally, the model is saved in a TrainData.pth file for future use.

TrainData.pth ----->
The TrainData.pth file appears to be a trained model data file that contains information such as input size, hidden size, output size, all words, tags, and model state for a neural network model used by the virtual assistant. This file is likely loaded and used by the code to initialize and configure the neural network model for processing user queries and generating appropriate responses based on the intents and patterns defined in the intents.json file.

Cubic.py ----->
This code implements a chatbot named "Cubic" that uses a trained neural network model to understand and respond to user inputs.
The code first imports the necessary modules such as random, json, torch, and custom modules Brain, NeuralNetwork, Listen, Speak, and Task. It then loads a pre-trained model from a saved file and sets up the chatbot's main loop.
Within the main loop, the chatbot listens for user input using the Listen() function and tokenizes the input using the tokenize() function from the NeuralNetwork module. It then converts the tokenized input to a bag of words representation using the bag_of_words() function. The bag of words representation is then passed to the trained neural network model, which predicts the appropriate response tag.
If the predicted response tag has a probability greater than 0.75, the chatbot selects a random response from the corresponding intent in the intents.json file. If the response contains keywords like "time", "date", "day", "wikipedia", or "google", the chatbot calls the corresponding functions NonInputExecution() or InputExecution() from the Task module to perform the corresponding tasks or searches. Otherwise, the chatbot uses the Say() function from the Speak module to convert the response to speech and speak it.
The chatbot continues to loop and listen for user input until the user enters "bye" to exit the program.
