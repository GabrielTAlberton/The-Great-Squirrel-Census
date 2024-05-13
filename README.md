# The-Great-Squirrel-Census
[Code challenge] In this code challenge we're going to use the Pandas library to try and get some specific information of a .csv file.

To-do's: create a .csv file that contains the total number of grey, red and black squirrels.


#Update:
Challenge solved and i like to tackle the way that i got hold of the total number for each fur color using this:


counting_data = csv_data["Primary Fur Color"].value_counts()

grey_fur_count = counting_data.get('Gray')

red_fur_count = counting_data.get('Cinnamon')

black_fur_count = counting_data.get('Black')

but this would also worked: 

black_squirrels_count = len(csv_data[csv_data["Primary Fur Color"] == "Black"]

