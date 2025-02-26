import pandas
import math
import numpy as np


from Get_Data_From_Cell import Get_Data_Battery # row -3, column -2
# from Get_Data_From_Cell import Get_Data_EVs # row -2, colum -1
from Series_parallel_configuration import Series_Parallel_Config_EV 
from Range_Estimation import Range_Estimation_for_EVs

# Load the Excel file
# battery_database = pd.read_excel("Battery database from open source_CellDatabase_v6.xlsx", sheet_name="RAW DATA")

# # Convert each row into a list
# batteries_as_arrays = battery_database.values.tolist()

battery_index = 11  # row -3
stat_index = 17  # column -2

cell_data = Get_Data_Battery(battery_index, stat_index)


EV_number = 3 # column number of the selected EV

# Gets the series and parallel cell configuration that meets the capacity and power requirements of the EV
series_values, parallel_values, max_cells_series, pack_capacity = Series_Parallel_Config_EV(EV_number)

# Prints the possible min series number for each parallel number that is possible 
# i.e. 20s 1p could have more than 20s up to the max number of series 
print(f"Combinations found: {len(series_values)}")
for i in range(len(series_values)):  # Loop through all available combinations
    print(f"Combination {i+1}, Series: {series_values[i]} Parallel: {parallel_values[i]}, Max series: {max_cells_series}")


range_est_50kph, range_est_100kph = Range_Estimation_for_EVs(pack_capacity, EV_number)

print(range_est_50kph, range_est_100kph)