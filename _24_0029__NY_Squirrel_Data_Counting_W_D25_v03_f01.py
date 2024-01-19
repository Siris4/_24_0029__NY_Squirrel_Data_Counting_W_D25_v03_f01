
import pandas

# TODO: Create a small table within a csv file (named "squirrel_count.csv")
# It will contain, as the Column heading names: Fur color (shown in the Dataset as "Primary Fur color" column)

# TODO: Determine how many of each 3 colors there are. Count them
# Should generate a table within a filename named: "squirrel_count.csv" that looks like; Fur color (shown in the Dataset as "Primary Fur color" column):

# Create a new dataframe:

'''
,Fur Color,Count
0,Gray,2473
1,Cinnamon,392
2,Black,103
'''

squirrel_data_file = pandas.read_csv("2018_Central_Park_Squirrel_Census_Squirrel_Data.csv")
# print(squirrel_data_file["Primary Fur Color"])
fur_column = squirrel_data_file["Primary Fur Color"]

count_black_fur = 0
count_gray_fur = 0
count_cinnamon_fur = 0

# counting black fur:
for each_iteration in fur_column:
    if each_iteration == "Black" or each_iteration == "black":
        count_black_fur += 1
    if each_iteration == "Gray" or each_iteration == "gray" or each_iteration == "Grey" or each_iteration == "grey":
        count_gray_fur += 1
    if each_iteration == "Cinnamon" or each_iteration == "cinnamon" or each_iteration == "Cinamon" or each_iteration == "cinamon":
        count_cinnamon_fur += 1

# print(f"Black fur count: {count_black_fur}")
# print(f"Gray fur count: {count_gray_fur}")
# print(f"Cinnamon fur count: {count_cinnamon_fur}")

#Create DataFrame from scratch:
data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [count_gray_fur, count_cinnamon_fur, count_black_fur]
}

data_frame = pandas.DataFrame(data_dict)
print(data_frame)

data_frame.to_csv("squirrel_count.csv")