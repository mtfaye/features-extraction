# Features Calculations App 




This project is intended to be a walkthrough on the development of a machine learning project from end to end. It covers the creation of a tool (web application) that gathers data from several channel of communications such as emails, chats and text messages and shows a summary of interesting topics that are being treated across those different channels.

This is achieved with a statistical modeling technique that is able to convert text to numeric vectors in order to determines how important a word or a combination of words are by looking at how frequently they appear in a document. Please take the time to go through the notebooks as it contains in more details the explaination of my approach and the techniques used to extract information from the communication samples data. That should be necessary for reaching a full understanding of the project.


## Workflow:


#### 	1. Dataset Collection:
Recursively walking through the directory tree data folder to get access to the emails and scrapped the content from the eml files by using beautifulsoup and mbox. I have to mention that I only considered collecting data from 3 folders inside the communication samples directory; the chats folder, the sms folder and the inbox folder inside the emails. The reason is these 3 folders have different file format and I understand that one of the goal of this test task is to assess my ability to collect data from different source and file extension such as the eml files, the html files, the xml files or the mix of both so I made sure to collect data from those file extension. Also The emails folder has 10 x more files than the sms, chats, bbg and papota all combined together. There is a huge imbalance in term of potential information to retrieve across items and would not make sens to compare them as a whole, reason why to make it simple and save time on my preprocessing stage to only took data from the 3 folders mentioned above.


#### 	2. Preprocessing and Exploratory Data Analysis: 
The preprocessing and cleaning stage was quite straight forward. I applied some text cleaning techniques such as removing puctuation, multilanguage stop words removal, convert some characters to lowcase etc. The only challenge encoutered on this stage was when removing the chinese and hindu characters as they are not supported by the nltk librairies. 

For the exploratory stage, I took a look at the most common words and then created a word clouds visualization for each channel of communication. The findings was quite deceiving. Usually it is more interesting to perform some more analysis once the features are exposed. See notebook for more details.


#### 	3. Feature Engineering: 
Used TF-IDF Vectors to create bags of words, trigrams and a list of their scores and merge everything on a dataframe.


#### 	4. App Creation:

Used the analytic web framework Dash to build the web app that showcases the result. See the steps below to run it. 




## Repo content 

*	 src - All the excutable codes including the app.py file and the requirements.txt file.
		
*	 notebooks - The Ipyhton Notebooks for exploratory analysis and algorithms designing process.
		
*	 data - Serialized data.
		
*	 models - Saved models and will contains weights of an eventual machine learning algorithm.



## Run the app 




###### FIRST AND FOREMOST: 

Once you have access to the repository make sure to first open: 

	 __PATH_FILES__.py  

located inside:

	 ../behavox_assignment/src/
	 

then replace accordingly the absolute paths of your local directories. 



###### Follow these 6 steps from your terminal to run the app now.



     	1. git clone https://bitbucket.org/mtfaye/behavox_assignment.git
		
	    2. cd ../behavox_assignment
		
	    3. cd ../behavox_assignment/src/
		
	    4. source venv/bin/activate
		
	    5. pip install -r requirements.txt
		
	    6. python app.py

Enjoy!


## Who do I talk to? ###

* @author: Mouhameth T. Faye - tahafaye@hotmail.com