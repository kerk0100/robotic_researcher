from robotics import Robot
import pandas as pd

SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]
WIKI_URL = 'https://en.wikipedia.org/wiki/'

robot = Robot("Quandrinaut")


# robot says hello to user
def introduce_yourself():
    robot.say_hello()


# robot says goodbye to user
def farewell_yourself():
    robot.say_goodbye()


# robot gets data from webpage and displays to user
def get_data(url, scientist):
    data = robot.get_data_from_webpage(url, scientist)
    return data


# robot asks if user wants to save the data
def ask_to_download(all_scientist_info):
    answer = input("Would you like to save this data as a csv? Y/N \n")
    if answer == "Y":
        robot.download_data(all_scientist_info)
    else:
        print("Data not saved.")
        return


def main():
    introduce_yourself()

    # create df to save the data collected on each scientist
    all_scientist_info = pd.DataFrame(columns=["Name", "Age", "First Paragraph", "URL"])

    # iterate through all scientists to collect data on each
    for scientist in SCIENTISTS:
        print("Collecting data for: " + scientist + "...")
        # create the URL
        first_name = scientist.split(" ")[0]
        last_name = scientist.split(" ")[1]
        url = WIKI_URL + first_name + "_" + last_name

        # get data on scientist
        data = get_data(url, scientist)

        # save data to df
        all_scientist_info.loc[len(all_scientist_info)] = data

    ask_to_download(all_scientist_info)
    farewell_yourself()


if __name__ == "__main__":
    main()
