# Features Calculation App 
This project is intended to be a walkthrough on the development of a tool (web application) that gathers text data from several directory and counts the value of a chosen feature of interest across the folders. This is achieved with a statistical modeling technique that is able to convert text to numeric vectors in order to determines how important a word or a combination of words are by looking at how frequently they appear in a document.


## Workflow


#### 	1. Dataset Collection:
Created 3 points of entry for the data injection and used the web scraping tool Beautiful Soup to scrape the body of messages for each channel of communication. 

![Corpus](src/assets/corpus.png)

The emails folder has more files than the sms, chats, bbg and papota all combined together. There is a huge imbalance in term of potential of information to retrieve across items.


#### 	2. Preprocessing and Exploratory Data Analysis: 
The preprocessing and cleaning stage is straight forward. The app apply some text cleaning techniques such as removing punctuation, multilanguage stop words removal, convert some characters to lowcase etc. 


![Words Cloud](src/assets/word_cloud.png)


#### 	3. Feature Engineering - TF-IDF Vectorizer: 
Used the bag of words analysis approach to tokenise the data and create trigrams.
Why TFIDF vectorizer? The goal is to scale down the impact of tokens that occur very frequently in the corpus because they  affects negatively the analysis. The tf-idf algorihtm is very efficient in reducing noise. 


#### 	4. App Creation:
Created the web app using the framework [Dash](https://plotly.com/dash/). 

## Repo content 

	├── .gitignore
	├── README.md
	│  
	├── data
	│   ├── immutable_input_data.mbox
	│   ├── raw.json
	│   ├── raw_corpus.json
	│   ├── raw_data.json
	│   └── term_matrix.json
	│  
	├── models
	│   └── tfidf.pickles
	│  
	├── src
	│   ├──__PATH_FILES__.py
	│   ├──__init__.py
	│   ├── app.py
	│   ├── assets
	│   │   └── sytlesheet.css
	│   ├── data_cleaning.py
	│   ├── data_loading.py
	│   ├── data_processing.py
	│   ├── features_extraction.py
	│   ├── requirements.txt



*	 data - Serialized data.

*	 models - Saved tf-ifdf parameters.

*	 src - The excutable codes including the requirements.txt file.
		
		
		
		


## Prerequisites

Make sure to have [pip](https://pip.pypa.io/en/stable/) and [Python3+](https://www.python.org/downloads/) installed in your local machine. 


## Set up and Run it

From comnand line:

1. Clone repo  ``` $ git clone https://bitbucket.org/mtfaye/behavox_assignment.git ```

2. Change directory ``` $ cd ../behavox_assignment/src/ ```
	  
3. Open file ``` __PATH_FILES__.py ```  and replace accordingly the absolute paths to connect the app with the data. 

4. Create a virtual environment venv, activate it and install the necessary dependencies.
		
	     $ python3 -m venv venv
		
	     $ source venv/bin/activate
		
	     $ pip install -r requirements.txt
	     
5. Run the app now.
		
	     $ python3 app.py






## Who do I talk to? ###

* @author: Mouhameth T. Faye - tahafaye@hotmail.com
