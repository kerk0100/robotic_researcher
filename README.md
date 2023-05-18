# Description
To run the program, enter commands: 
* ```pip3 install -r requirements.txt```
* ```python3 main.py```
* Note: program uses python 3.9.6
* Note: If you have conflicting versions, you may need sudo privileges: ```sudo pip3 install -r requirements.txt```

The program will tell the user what it is about to do (i.e. provide information about each scientist) and then
iterate through the list ```SCIENTISTS```. The program opens a headless Chrome browser, searches through the wikipedia
page for birth & death dates, as well as the first paragraph in the page. The program saves the Scientists' Name, Age, 
First Paragraph, and wiki URL to a pandas dataframe. The user is then given the option to save this dataframe to
a csv file. If yes, the path of the file is printed out to the user. The robot says goodbye. 


---




# Robotic Researcher
Welcome to Quandri's technical assignment. This assignment is meant to simulate the work
you would do working at Quandri building software robots. 

## Your task
The purpose of this software robot is to find key information about important scientists
and display it to the user.

When this robot is run, it should:

1. Introduce itself and explain the steps it's about to take.
2. Navigate to the wikipedia page of the scientists found in the list SCIENTISTS.
3. Retrieve the dates the scientists were born and died and calculate their age. Also, 
    retrieve the first paragraph of their wikipedia page.
4. Display all of this information to the user in an easily understood manner. 

## A few things to keep in mind
- This should be written as production level code. i.e. You would expect this code to
    pass a PR to get merged into main.
- As this is a software robot, it should not make use of any wikipedia API but it should 
    instead open a browser and navigate to wikipedia in the same manner a human would.
- The provided code can be added to, removed and changed as you see fit.
- Please use rpaframework to complete this task. Documentation for the provided 
    library can be found [here](https://rpaframework.org/#)

## Bonus
What other nifty features can you add to your robot? This is not required but is an
opportunity for you to have fun with your code and show your creativity.


## Submission
When you've completed the task, please email your project in a zip folder to 
jamieson@quandri.io with the subject line: `Robotic Researcher - Quandri Backend Python 
Interview`