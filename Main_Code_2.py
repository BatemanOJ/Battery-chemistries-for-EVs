import pandas as pd
import math
import numpy as np
import time


from Get_Data_From_Cell import Get_Data_Battery_Cell # row -3, column -2
# from Get_Data_From_Cell import Get_Data_EVs # row -2, colum -1
from Series_parallel_configuration import Series_Parallel_Config_EV 
from Range_Estimation import Range_Estimation_for_EVs
from Get_Data_From_Cell import Get_Battery_Data_Row # gets the row of data and puts it into an array -2 on the row number
from Two_Chemistries import Two_Chemistries
from Two_Chem_Efficient import Two_Chem_Efficient
from Two_Chem_Efficient_Battery_Mass_Not_Pack import Two_Chem_Efficient_Battery_Mass_Not_Pack
from One_Chem_Comparison import One_Chem_Comparison


# Load the Excel file
# battery_database = pd.read_excel("Battery database from open source_CellDatabase_v6.xlsx", sheet_name="RAW DATA")

# # Convert each row into a list
# batteries_as_arrays = battery_database.values.tolist()

battery_index = 11  # row -3
stat_index = 17  # column -2

# cell_data = Get_Data_Battery_Cell(battery_index, stat_index)


EV_number = 3 # column number of the selected EV

# Gets the series and parallel cell configuration that meets the capacity and power requirements of the EV
# series_values, parallel_values, max_cells_series, pack_capacity = Series_Parallel_Config_EV(EV_number)

# Prints the possible min series number for each parallel number that is possible 
# i.e. 20s 1p could have more than 20s up to the max number of series 

# print(f"Combinations found: {len(series_values)}")
# for i in range(len(series_values)):  # Loop through all available combinations
#     print(f"Combination {i+1}, Series: {series_values[i]} Parallel: {parallel_values[i]}, Max series: {max_cells_series}")


# range_est_50kph, range_est_100kph = Range_Estimation_for_EVs(pack_capacity, EV_number)

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

print("Battery Data Imported")

# success, battery_1_series, battery_1_parallel, battery_2_series, battery_2_parallel, capacity, power, mass = \
#     Two_Chem_Efficient(battery_data[f"battery_{battery_1_index}_index"], battery_data[f"battery_{battery_2_index}_index"], 135000, 511000, 459, 289, 540)
# print(f"Battery 1 Index: {battery_1_index} {battery_1_series}S {battery_1_parallel}P, Battery 2 Index: {battery_2_index} {battery_2_series}S {battery_2_parallel}P")


#############################################################

# # Checks using pack mass not battery mass

# multi_bat_success = 0
# count_successful_combinations = 0
# successful_combinations = []

# start_time = time.time()

# while multi_bat_success == 0:

#     # print(f"Battery 1 Index: {battery_1_index} Battery 2 Index: {battery_2_index}")
#     multi_bat_success, battery_1_series, battery_1_parallel, battery_2_series, battery_2_parallel, capacity, discharging_power, mass, charging_power = \
#     Two_Chem_Efficient(battery_data[f"battery_{battery_1_index}_index"], battery_data[f"battery_{battery_2_index}_index"], 75000, 250000, 459, 289, 520, 160000)

#     if multi_bat_success == 1:
#         # print(f"Battery 1 Index: {battery_1_index} {battery_1_series}S {battery_1_parallel}P, Battery 2 Index: {battery_2_index} {battery_2_series}S {battery_2_parallel}P")
        
#         successful_combinations.append([
#             battery_1_index, battery_1_series, battery_1_parallel, 
#             battery_2_index, battery_2_series, battery_2_parallel, 
#             capacity, discharging_power, mass, charging_power
#         ])
#         multi_bat_success = 0
#         count_successful_combinations += 1

#     if battery_2_index == 379 and battery_1_index == 378:
#         break
#     elif battery_2_index == 379:
#         battery_1_index += 1
#         battery_2_index = battery_1_index + 1
#     else:
#         battery_2_index += 1
      

#     # print(f"Battery 1 Index: {battery_1_index} Battery 2 Index: {battery_2_index}")

# # successful_combinations_store = [battery_1_index(1), battery_1_series(2), battery_1_parallel(3),
#                                 # battery_2_index(4), battery_2_series(5), battery_2_parallel(6),
#                                 # capacity(7), discharging_power(8), mass(9), charging_power(10)]

# end_time = time.time()  # End timer

# elapsed_time = end_time - start_time
# print(f"Elapsed time: {elapsed_time:.6f} seconds")
        
# print(count_successful_combinations)

# if successful_combinations:
#     max_capacity_row = max(successful_combinations, key=lambda x: x[7])
#     print(max_capacity_row)


#############################################################

# Checks using battery mass not pack mass

multi_bat_success = 0
count_successful_combinations = 0
successful_combinations = []

start_time = time.time()

req_capacity = 75000
req_discharging_power = 250000
req_max_V = 459
req_min_V = 275
req_max_mass = 400
req_charging_power = 160000

while multi_bat_success == 0:

    # print(f"Battery 1 Index: {battery_1_index} Battery 2 Index: {battery_2_index}")
    multi_bat_success, battery_1_series, battery_1_parallel, battery_2_series, battery_2_parallel, capacity, discharging_power, mass, charging_power = \
    Two_Chem_Efficient_Battery_Mass_Not_Pack(battery_data[f"battery_{battery_1_index}_index"], battery_data[f"battery_{battery_2_index}_index"],\
                                             req_capacity, req_discharging_power, req_max_V, req_min_V, req_max_mass, req_charging_power)

    if multi_bat_success == 1:
        # print(f"Battery 1 Index: {battery_1_index} {battery_1_series}S {battery_1_parallel}P, Battery 2 Index: {battery_2_index} {battery_2_series}S {battery_2_parallel}P")
        
        successful_combinations.append([
            battery_1_index, battery_1_series, battery_1_parallel, 
            battery_2_index, battery_2_series, battery_2_parallel, 
            capacity, discharging_power, mass, charging_power
        ])
        multi_bat_success = 0
        count_successful_combinations += 1

    if battery_1_index == 378 and battery_2_index == 379:
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


# single_bat_success = 0
# count_successful_batteries = 0
# successful_batteries = []


# while single_bat_success == 0:

#     # print(f"Battery 1 Index: {battery_1_index} Battery 2 Index: {battery_2_index}")
#     multi_bat_success, battery_1_series, battery_1_parallel, capacity, discharging_power, mass, charging_power = \
#     One_Chem_Comparison(battery_data[f"battery_{battery_1_index}_index"], 75000, 300000, 459, 289, 1100, 200000)
#     # battery_1, req_capacity, peak_power_req, max_pack_V_allowed, min_pack_V_allowed, max_mass, peak_charge_power_req

#     if single_bat_success == 1:
#         # print(f"Battery 1 Index: {battery_1_index} {battery_1_series}S {battery_1_parallel}P, Battery 2 Index: {battery_2_index} {battery_2_series}S {battery_2_parallel}P")
        
#         successful_batteries.append([
#             battery_1_index, battery_1_series, battery_1_parallel,
#             capacity, discharging_power, mass, charging_power])
        
#         single_bat_success = 0
#         count_successful_batteries += 1

#     if battery_1_index == 379:
#         break
#     else:
#         battery_1_index += 1
    

#     # print(f"Battery 1 Index: {battery_1_index} Battery 2 Index: {battery_2_index}")
    
# print(count_successful_batteries)

# if successful_batteries:
#     max_capacity_row_single_bat = max(successful_batteries, key=lambda x: x[7])
#     print(max_capacity_row_single_bat)



#############################################################



# success, battery_1_series, battery_1_parallel, battery_2_series, battery_2_parallel = \
#     Two_Chemistries(battery_1_index, battery_2_index, 75000, 200000, 250, 475, 360, 318)
# # print(f"Battery 1 Index: {battery_1_index} {battery_1_series}S {battery_1_parallel}P, Battery 2 Index: {battery_2_index} {battery_2_series}S {battery_2_parallel}P")

# while multi_bat_success== 0:
#     if battery_2_index == 388:
#         battery_1_index += 1
#         battery_2_index = battery_1_index
#     else:
#         battery_2_index += 1
    
#     success, battery_1_series, battery_1_parallel, battery_2_series, battery_2_parallel = \
#     Two_Chemistries(battery_1_index, battery_2_index, 75000, 200000, 250, 475, 360, 318)

#     print(f"Battery 1 Index: {battery_1_index} Battery 2 Index: {battery_2_index}")
    
#     if multi_bat_success== 1:
#         print(f"Battery 1 Index: {battery_1_index} {battery_1_series}S {battery_1_parallel}P, Battery 2 Index: {battery_2_index} {battery_2_series}S {battery_2_parallel}P")
#         break

# Two_Chemistries(required_cap, battery_1, battery_2, peak_power_required, min_pack_voltage, max_pack_voltage, pack_voltage, max_mass(kg))
# print(min_battery_1_only, min_battery_2_only)