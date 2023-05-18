from RPA.Browser.Selenium import Selenium
from datetime import datetime
import os
import textwrap

br = Selenium()


class Robot:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, my name is " + self.name)
        print("I will provide you with some information about famous scientists.")
        print("I will tell you which scientist I am collecting data for, their age, and a paragraph about them.")
        print("At the end of my research, I will give you the option to save the data as a csv file.")
        print("Here we go!")
        print('_' * 40)

    def say_goodbye(self):
        print("Goodbye.")

    def get_data_from_webpage(self, webpage, scientist):
        # open browser in background
        br.open_headless_chrome_browser(webpage)

        # find birth and death dates
        date_born = br.find_element(locator="xpath://span[@class='bday']").get_attribute("textContent")
        date_died = br.find_elements(locator="xpath://td[@class='infobox-data']")[1].get_attribute("textContent")
        date_died = date_died[date_died.find("(")+1:date_died.find(")")]
        year_born = datetime.strptime(date_born, "%Y-%m-%d").year
        year_died = datetime.strptime(date_died, "%Y-%m-%d").year
        age = int(year_died) - int(year_born)

        # find first paragraph
        paragraphs = br.find_elements(locator="xpath://p")
        first_paragraph = "Could not find first paragraph."
        for p in paragraphs:
            if p.text:
                first_paragraph = textwrap.dedent(p.text).strip()
                break

        # print data to user
        print("Age: " + str(age))
        print("Info: " + textwrap.fill(first_paragraph, width=80))
        print('_' * 40)

        # save data for df
        scientist_data = {'Name': scientist, 'Age': age, 'First Paragraph': first_paragraph, 'URL': webpage}
        return scientist_data

    # save df to csv file and print out file path to user
    def download_data(self, all_scientist_info):
        all_scientist_info.to_csv("scientist_info.csv")
        file_path = os.getcwd()
        print("Scientist info has been saved to csv file:" + file_path + "/scientist_info.csv")
