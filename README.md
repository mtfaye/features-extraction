# Communication featues calculations #

This project is intended to be a walkthrough on the development of a machine learning project from end to end. It covers the creation of a tool (web application) that gathers data from several channel of communications such as emails, chats and text messages and shows a summary of interesting topics that are being treated across those different channels.

This is achieved with a statistical modeling technique that is able to convert text to numeric vectors in order to determines how important a word or a combination of words is by looking at how frequently they appear in a document. Please take the time to go through the notebooks as it contains in much more details the explaination of my approach and the techniques used to extract information from the communication samples data. That should be necessary for reaching a full understanding of the project.


### The workflow consists of the following steps:

1. 			Dataset Collection: Recursively walking through the directory tree data folder to get access to the emails  folder and scrapped the messages from the eml files by using beautifulsoup. I have  I  
> 2. Exploratory Data Analysis: 
> 3. Feature Engineering
> 4. App Creation 



### Repo content ###

> 1.	 src - All the excutable source codes including the app.py file and the requirements.txt file.
> 2.	 notebooks - The Ipyhton Notebooks for exploratory analysis and algorithms designing process.
> 3.	 data - Serialized data.
> 4.	 tests - Empty for now but should contains the test files.
> 5.	 models - Saved models and weights
> [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)


### Run the app ###

> #### Follow these 6 steps from your terminal.
> 
>1. <pre><git clone https://bitbucket.org/mtfaye/behavox_assignment.git
>2.   	cd ../behavox_assignment>
>3.   	cd ../behavox_assignment/src>
>4.   	source venv/bin/activate>
>5.   	pip install -r requirements.txt>
>6.   	python app.py></pre>

>	    Enjoy!!!


### Contribution guidelines ###

>  Make tests


### Who do I talk to? ###

* @author: Mouhameth T. Faye