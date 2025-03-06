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
from Range_Estimation import Range_Estimation_for_Batteries
from Check_battery_index_order import Check_Battery_Order



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
battery_data = {f"battery_{i}_index": battery_database.iloc[i].tolist() for i in range(388)}  # Adjusted for 388 rows

print("Battery Data Imported")

WLTP_data = {}

WLTP_database = pd.read_excel("Battery database from open source_CellDatabase_v6.xlsx", sheet_name="WLTP Acc")
i = 1 

WLTP_data = {f"WLTP_{i}_index": WLTP_database.iloc[i].tolist() for i in range(1493)}  # Adjusted for 1211 rows
# print(len(WLTP_data))
# print(WLTP_data[f"WLTP_{1490}_index"][4], WLTP_data[f"WLTP_{1491}_index"][4], WLTP_data[f"WLTP_{1492}_index"][4])

print("WLTP Data Imported")

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

req_capacity = 135000
req_discharging_power = 511000
req_max_V = 550
req_min_V = 210
req_max_mass_battery = 540
req_charging_power = 210000

while multi_bat_success == 0:

    # print(f"Battery 1 Index: {battery_1_index} Battery 2 Index: {battery_2_index}")
    multi_bat_success, battery_1_series, battery_1_parallel, battery_2_series, battery_2_parallel, capacity, discharging_power, mass, charging_power = \
    Two_Chem_Efficient_Battery_Mass_Not_Pack(battery_data[f"battery_{battery_1_index}_index"], battery_data[f"battery_{battery_2_index}_index"],\
                                             req_capacity, req_discharging_power, req_max_V, req_min_V, req_max_mass_battery, req_charging_power)

    if multi_bat_success == 1:
        
        # Check the battery indexes are the right way round
        check_battery_order = Check_Battery_Order (battery_data, battery_1_index, battery_2_index, battery_1_series, battery_1_parallel, \
                                                   battery_2_series, battery_2_parallel, capacity)

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
                                # capacity(7), discharging_power(8), mass(9), charging_power(10), range(11)]

end_time = time.time()  # End timer

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")
        
print(count_successful_combinations)

if successful_combinations:
    max_capacity_row = max(successful_combinations, key=lambda x: x[7])
    min_mass_row = min(successful_combinations, key=lambda x: x[9])
    print(min_mass_row)
    print(max_capacity_row)

car_data = [3100, 0.3, 3.38, 0.015, 0] # Rivian R1T             Actual: 505, Calculated: 508
# car_data = [1748, 0.29, 2.37, 0.015, 0] # Kia Niro EV         Actual: 384, Calculated: 405
# car_data = [1486, 0.28, 2.33, 0.015, 0] # Nissan Leaf         Actual: 169(excel)/135, Calculated: 179 Using 2 chems: 310
# car_data = [1830, 0.23, 2.268, 0.015, 0] # Tesla model 3      Actual: 576, Calculated: 572
# car_data = [2584, 0.29, 2.3, 0.015, 0] # Polestar 3              Actual: 482, Calculated: 532

# battery_data_series_parallel_1 = [max_capacity_row[1], max_capacity_row[2], max_capacity_row[4], max_capacity_row[5]]
# battery_1 = battery_data[f"battery_{max_capacity_row[0]}_index"]
# battery_2 = battery_data[f"battery_{max_capacity_row[3]}_index"]

# print(f"series/parallel: {battery_data_series_parallel_1}, battery 1: {max_capacity_row[0]}, battery 2: {max_capacity_row[3]}")


# Range_1 = Range_Estimation_for_Batteries(WLTP_data, car_data, battery_data_series_parallel_1, battery_1, battery_2)

# battery_data_series_parallel_2 = [min_mass_row[1], min_mass_row[2], min_mass_row[4], min_mass_row[5]]
# battery_3 = battery_data[f"battery_{min_mass_row[0]}_index"]
# battery_4 = battery_data[f"battery_{min_mass_row[3]}_index"]

# print(f"series/parallel: {battery_data_series_parallel_2}, battery 1: {min_mass_row[0]}, battery 2: {min_mass_row[3]}")


# Range_2 = Range_Estimation_for_Batteries(WLTP_data, car_data, battery_data_series_parallel_2, battery_3, battery_4)

# print(f"Range 1 max capacity: {Range_1} km, Range 2 min mass: {Range_2} km")
if successful_combinations:
    for i in range(0, len(successful_combinations)):
        battery_data_series_parallel = [successful_combinations[i][1], successful_combinations[i][2], successful_combinations[i][4], successful_combinations[i][5]]
        battery_1 = battery_data[f"battery_{successful_combinations[i][0]}_index"]
        battery_2 = battery_data[f"battery_{successful_combinations[i][3]}_index"]

        print(f"Battery number series parallel {successful_combinations[i][0], successful_combinations[i][1], successful_combinations[i][2], successful_combinations[i][3], successful_combinations[i][4], successful_combinations[i][5]}")

        Range = Range_Estimation_for_Batteries(WLTP_data, car_data, battery_data_series_parallel, battery_1, battery_2)

        successful_combinations[i].append(Range)

        # print(f"Range {i}: {Range} km")

if successful_combinations:
    max_range_row = max(successful_combinations, key=lambda x: x[10])
    min_range_row = min(successful_combinations, key=lambda x: x[10])
    max_capacity_row = max(successful_combinations, key=lambda x: x[7])
    min_mass_row = min(successful_combinations, key=lambda x: x[9])

    print(f"Min mass: {min_mass_row}")
    print(f"Max capacity: {max_capacity_row}")
    print(f"Max range: {max_range_row}")
    print(f"Min range: {min_range_row}")

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