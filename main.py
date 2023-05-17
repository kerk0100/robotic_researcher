from robotics import Robot
import pandas as pd

# SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]
SCIENTISTS = ["Albert Einstein"]

robot = Robot("Quandrinaut")


def introduce_yourself():
    robot.say_hello()


def farewell_yourself():
    robot.say_goodbye()


def get_webpage(url, scientist):
    data = robot.open_webpage(url, scientist)
    return data


def ask_to_download(all_scientist_info):
    answer = input("Would you like to download this data as a csv? Y/N")
    if answer == "Y":
        robot.download_data(all_scientist_info)
    else:
        return


def main():
    introduce_yourself()
    all_scientist_info = pd.DataFrame(columns=["Name", "Age", "First Paragraph"])
    for scientist in SCIENTISTS:
        first_name = scientist.split(" ")[0]
        last_name = scientist.split(" ")[1]
        url = 'https://en.wikipedia.org/wiki/' + first_name + "_" + last_name
        get_data = get_webpage(url, scientist)
        all_scientist_info.loc[len(all_scientist_info)] = get_data
    ask_to_download(all_scientist_info)
    farewell_yourself()


if __name__ == "__main__":
    main()
