import pandas as pd

csv_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data (1).csv")

# create the dictionary that'll hold the values of each fur colour #


counting_data = csv_data["Primary Fur Color"].value_counts()

grey_fur_count = counting_data.get('Gray')
red_fur_count = counting_data.get('Cinnamon')
black_fur_count = counting_data.get('Black')

squirrel_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_fur_count, red_fur_count, black_fur_count]
}

squirrel_data = pd.DataFrame(squirrel_dict)
squirrel_data.to_csv("new_squirrel_data.csv")

