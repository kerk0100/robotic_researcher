from RPA.Browser.Selenium import Selenium
from datetime import datetime

br = Selenium()


class Robot:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, my name is " + self.name)

    def say_goodbye(self):
        print("Goodbye, my name is " + self.name)

    def open_webpage(self, webpage, scientist):
        br.open_available_browser(webpage)
        date_born = br.find_element(locator="xpath://span[@class='bday']").get_attribute("textContent")
        date_died = br.find_elements(locator="xpath://td[@class='infobox-data']")[1].get_attribute("textContent")
        date_died = date_died[date_died.find("(")+1:date_died.find(")")]
        year_born = datetime.strptime(date_born, "%Y-%m-%d").year
        year_died = datetime.strptime(date_died, "%Y-%m-%d").year
        age = int(year_died) - int(year_born)
        first_paragraph = br.find_elements(locator="xpath://p")[1].get_attribute("textContent")
        scientist_data = {'Name': scientist, 'Age': age, 'First Paragraph': first_paragraph}
        return scientist_data

    def download_data(self, all_scientist_info):
        all_scientist_info.to_csv("scientist_info.csv")
        print("Scientist info has been saved to csv file with name: scientist_info.csv")
