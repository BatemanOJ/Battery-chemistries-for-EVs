import pandas as pd
import math
import numpy as np


from Get_Data_From_Cell import Get_Data_Battery_Cell # row -3, column -2
# from Get_Data_From_Cell import Get_Data_EVs # row -2, colum -1
from Series_parallel_configuration import Series_Parallel_Config_EV 
from Range_Estimation import Range_Estimation_for_EVs
from Get_Data_From_Cell import Get_Battery_Data_Row # gets the row of data and puts it into an array -2 on the row number
from Two_Chemistries import Two_Chemistries
from Two_Chem_Efficient import Two_Chem_Efficient


# Load the Excel file
# battery_database = pd.read_excel("Battery database from open source_CellDatabase_v6.xlsx", sheet_name="RAW DATA")

# # Convert each row into a list
# batteries_as_arrays = battery_database.values.tolist()

battery_index = 11  # row -3
stat_index = 17  # column -2

cell_data = Get_Data_Battery_Cell(battery_index, stat_index)


EV_number = 3 # column number of the selected EV

# Gets the series and parallel cell configuration that meets the capacity and power requirements of the EV
series_values, parallel_values, max_cells_series, pack_capacity = Series_Parallel_Config_EV(EV_number)

# Prints the possible min series number for each parallel number that is possible 
# i.e. 20s 1p could have more than 20s up to the max number of series 

# print(f"Combinations found: {len(series_values)}")
# for i in range(len(series_values)):  # Loop through all available combinations
#     print(f"Combination {i+1}, Series: {series_values[i]} Parallel: {parallel_values[i]}, Max series: {max_cells_series}")


range_est_50kph, range_est_100kph = Range_Estimation_for_EVs(pack_capacity, EV_number)

# print(range_est_50kph, range_est_100kph)
battery_1_index = 1
battery_2_index = 2

# for i in range(1, 388):
#     battery_{i}_index = Get_Battery_Data_Row(i)

# battery_data = {f"battery_{i}_index": Get_Battery_Data_Row(i).tolist() for i in range(1, 388)}
print("Started")
battery_data = {}

battery_database = pd.read_excel("Battery database from open source_CellDatabase_v6.xlsx", sheet_name="RAW DATA")

i = 1
battery_data = {f"battery_{i}_index": battery_database.iloc[i].tolist() for i in range(388)}  # Adjusted for 387 rows



# success, battery_1_series, battery_1_parallel, battery_2_series, battery_2_parallel, capacity, power, mass = \
#     Two_Chem_Efficient(battery_data[f"battery_{battery_1_index}_index"], battery_data[f"battery_{battery_2_index}_index"], 135000, 511000, 459, 289, 540)
# print(f"Battery 1 Index: {battery_1_index} {battery_1_series}S {battery_1_parallel}P, Battery 2 Index: {battery_2_index} {battery_2_series}S {battery_2_parallel}P")

success = 0
count_successful_combinations = 0
successful_combinations = []


while success == 0:

    # print(f"Battery 1 Index: {battery_1_index} Battery 2 Index: {battery_2_index}")
    success, battery_1_series, battery_1_parallel, battery_2_series, battery_2_parallel, capacity, power, mass = \
    Two_Chem_Efficient(battery_data[f"battery_{battery_1_index}_index"], battery_data[f"battery_{battery_2_index}_index"], 135000, 511000, 459, 289, 540, 200000)

    if success == 1:
        print(f"Battery 1 Index: {battery_1_index} {battery_1_series}S {battery_1_parallel}P, Battery 2 Index: {battery_2_index} {battery_2_series}S {battery_2_parallel}P")
        
        successful_combinations.append([
            battery_1_index, battery_1_series, battery_1_parallel, 
            battery_2_index, battery_2_series, battery_2_parallel, 
            capacity, power, mass
        ])
        success = 0
        count_successful_combinations += 1

    if battery_2_index == 379 and battery_1_index == 5:
        break
    elif battery_2_index == 379:
        battery_1_index += 1
        battery_2_index = battery_1_index + 1
    else:
        battery_2_index += 1
    

    # print(f"Battery 1 Index: {battery_1_index} Battery 2 Index: {battery_2_index}")
    
    

# successful_combinations_store = [battery_1_index(1), battery_1_series(2), battery_1_parallel(3),
                                # battery_2_index(4), battery_2_series(5), battery_2_parallel(6),
                                # capacity(7), power(8), mass(9)]
        
print(count_successful_combinations)

if successful_combinations:
    max_capacity = max(combo[7] for combo in successful_combinations)
    max_capacity_row = max(successful_combinations, key=lambda x: x[7])
    print(max_capacity, max_capacity_row)





# success, battery_1_series, battery_1_parallel, battery_2_series, battery_2_parallel = \
#     Two_Chemistries(battery_1_index, battery_2_index, 75000, 200000, 250, 475, 360, 318)
# # print(f"Battery 1 Index: {battery_1_index} {battery_1_series}S {battery_1_parallel}P, Battery 2 Index: {battery_2_index} {battery_2_series}S {battery_2_parallel}P")

# while success == 0:
#     if battery_2_index == 388:
#         battery_1_index += 1
#         battery_2_index = battery_1_index
#     else:
#         battery_2_index += 1
    
#     success, battery_1_series, battery_1_parallel, battery_2_series, battery_2_parallel = \
#     Two_Chemistries(battery_1_index, battery_2_index, 75000, 200000, 250, 475, 360, 318)

#     print(f"Battery 1 Index: {battery_1_index} Battery 2 Index: {battery_2_index}")
    
#     if success == 1:
#         print(f"Battery 1 Index: {battery_1_index} {battery_1_series}S {battery_1_parallel}P, Battery 2 Index: {battery_2_index} {battery_2_series}S {battery_2_parallel}P")
#         break

# Two_Chemistries(required_cap, battery_1, battery_2, peak_power_required, min_pack_voltage, max_pack_voltage, pack_voltage, max_mass(kg))
# print(min_battery_1_only, min_battery_2_only)