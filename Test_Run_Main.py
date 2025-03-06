import pandas as pd
import numpy as np
import time

# from Two_Chem_Efficient_Battery_Mass_Not_Pack import Two_Chem_Efficient_Battery_Mass_Not_Pack
from Test_Two_Chem_Efficient_Battery_Mass_Not_Pack import Two_Chem_Efficient_Battery_Mass_Not_Pack
from Two_Chemistries import Two_Chemistries
from Two_Chem_Efficient import Two_Chem_Efficient
from Check_battery_index_order import Check_Battery_Order



battery_1_index = 166
battery_2_index = 177

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

req_capacity = 35000
req_discharging_power = 100000
req_max_V = 400
req_min_V = 240
req_max_mass_battery = 200
req_charging_power = 75000

while multi_bat_success == 0:

    Check_battery_1_order = battery_data[f"battery_{battery_1_index}_index"][1] 

    print(f"Battery 1 Index: {battery_1_index} Battery 2 Index: {battery_2_index}")

    # print(f"Battery 1 Index: {battery_1_index} Battery 2 Index: {battery_2_index}")
    multi_bat_success, battery_1_series, battery_1_parallel, battery_2_series, battery_2_parallel, capacity, discharging_power, mass, charging_power = \
    Two_Chem_Efficient_Battery_Mass_Not_Pack(battery_data[f"battery_{battery_1_index}_index"], battery_data[f"battery_{battery_2_index}_index"],\
                                             req_capacity, req_discharging_power, req_max_V, req_min_V, req_max_mass_battery, req_charging_power)

    if multi_bat_success == 1:
        # print(f"Battery 1 Index: {battery_1_index} {battery_1_series}S {battery_1_parallel}P, Battery 2 Index: {battery_2_index} {battery_2_series}S {battery_2_parallel}P")
        
        # Check the battery indexes are the right way round
        check_battery_order = Check_Battery_Order (battery_data, battery_1_index, battery_2_index, battery_1_series, battery_1_parallel, \
                                                   battery_2_series, battery_2_parallel, capacity)
        
        print(f"Check Battery Order: {check_battery_order}")

        # successful_combinations.append([
        #     battery_1_index, battery_1_series, battery_1_parallel, 
        #     battery_2_index, battery_2_series, battery_2_parallel, 
        #     capacity, discharging_power, mass, charging_power
        # ])

        # print(successful_combinations)

        if check_battery_order == 0:
            battery_hold_index = battery_1_index
            battery_1_index_switched = battery_2_index
            battery_2_index_switched = battery_hold_index
        elif check_battery_order == 1:
            battery_1_index_switched = battery_1_index
            battery_2_index_switched = battery_2_index

        successful_combinations.append([
            battery_1_index_switched, battery_1_series, battery_1_parallel, 
            battery_2_index_switched, battery_2_series, battery_2_parallel, 
            capacity, discharging_power, mass, charging_power
        ])
        multi_bat_success = 0
        count_successful_combinations += 1

        print(successful_combinations)

    if battery_1_index == 166 and battery_2_index == 177:
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