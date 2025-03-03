import pandas as pd
import numpy as np
import time

# from Two_Chem_Efficient_Battery_Mass_Not_Pack import Two_Chem_Efficient_Battery_Mass_Not_Pack
from Test_Two_Chem_Efficient_Battery_Mass_Not_Pack import Two_Chem_Efficient_Battery_Mass_Not_Pack
from Two_Chemistries import Two_Chemistries
from Two_Chem_Efficient import Two_Chem_Efficient


battery_1_index = 174
battery_2_index = 223

# for i in range(1, 388):
#     battery_{i}_index = Get_Battery_Data_Row(i)

# battery_data = {f"battery_{i}_index": Get_Battery_Data_Row(i).tolist() for i in range(1, 388)}
print("Started")
battery_data = {}

battery_database = pd.read_excel("Battery database from open source_CellDatabase_v6.xlsx", sheet_name="RAW DATA")

i = 1
battery_data = {f"battery_{i}_index": battery_database.iloc[i].tolist() for i in range(388)}  # Adjusted for 387 rows

print("Battery Data Imported")

#############################################################

# Checks using battery mass not pack mass

multi_bat_success = 0
count_successful_combinations = 0
successful_combinations = []

start_time = time.time()

while multi_bat_success == 0:

    # print(f"Battery 1 Index: {battery_1_index} Battery 2 Index: {battery_2_index}")
    multi_bat_success, battery_1_series, battery_1_parallel, battery_2_series, battery_2_parallel, capacity, discharging_power, mass, charging_power = \
    Two_Chem_Efficient_Battery_Mass_Not_Pack(battery_data[f"battery_{battery_1_index}_index"], battery_data[f"battery_{battery_2_index}_index"], 75000, 250000, 459, 289, 320, 160000)

    if multi_bat_success == 1:
        # print(f"Battery 1 Index: {battery_1_index} {battery_1_series}S {battery_1_parallel}P, Battery 2 Index: {battery_2_index} {battery_2_series}S {battery_2_parallel}P")
        
        successful_combinations.append([
            battery_1_index, battery_1_series, battery_1_parallel, 
            battery_2_index, battery_2_series, battery_2_parallel, 
            capacity, discharging_power, mass, charging_power
        ])
        multi_bat_success = 0
        count_successful_combinations += 1

    if battery_1_index == 1 and battery_2_index == 379:
        break
    elif battery_2_index == 379:
        battery_1_index += 1
        battery_2_index = battery_1_index + 1
    else:
        battery_2_index += 1
      

    # print(f"Battery 1 Index: {battery_1_index} Battery 2 Index: {battery_2_index}")

# successful_combinations_store = [battery_1_index(1), battery_1_series(2), battery_1_parallel(3),
                                # battery_2_index(4), battery_2_series(5), battery_2_parallel(6),
                                # capacity(7), discharging_power(8), mass(9), charging_power(10)]

end_time = time.time()  # End timer

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")
        
print(count_successful_combinations)

if successful_combinations:
    max_capacity_row = max(successful_combinations, key=lambda x: x[7])
    print(max_capacity_row)

#############################################################