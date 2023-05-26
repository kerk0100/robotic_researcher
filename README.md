# Robotic Researcher
To run the program, enter commands: 
* ```pip3 install -r requirements.txt```
* ```python3 main.py```
* Note: program uses python 3.9.6
* Note: If you have conflicting versions, you may need sudo privileges: ```sudo pip3 install -r requirements.txt```

The purpose of this software robot is to find key information about important scientists
and display it to the user.

The program will tell the user what it is about to do (i.e. provide information about each scientist) and then
iterate through the list ```SCIENTISTS```. The program opens a headless Chrome browser, searches through the wikipedia
page for birth & death dates, as well as the first paragraph in the page. The program saves the Scientists' Name, Age, 
First Paragraph, and wiki URL to a pandas dataframe. The user is then given the option to save this dataframe to
a csv file. If yes, the path of the file is printed out to the user. The robot says goodbye. 


---

