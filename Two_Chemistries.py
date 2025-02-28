import math 
import numpy as np

from Get_Data_From_Cell import Get_Data_EVs # row -2, colum -1
from Get_Data_From_Cell import Get_Data_Battery_Cell # row -3, column -2
from Get_Data_From_Cell import Get_Battery_Data_Row # gets the row of data and puts it into an array
from Find_Power_Dense_Battery import Find_Power_Dense_Battery


def Two_Chemistries(required_cap, battery_1, battery_2, peak_power_required, min_pack_voltage, max_pack_voltage, pack_voltage, max_mass):

    # Battery 1 is the energy dense one and battery 2 is the power dense one
    battery_1, battery_2, battery_1_Wh, battery_2_Wh = Find_Power_Dense_Battery(battery_1, battery_2)

    min_battery_1_only = math.ceil(required_cap/(battery_1_Wh))
    min_battery_2_only = math.ceil(required_cap/(battery_2_Wh))

    no_battery_1 = math.ceil(min_battery_1_only/2)
    no_battery_2 = math.ceil(min_battery_2_only/2)

    capacity = no_battery_1 * battery_1_Wh + no_battery_2 * battery_2_Wh
    mass = no_battery_1 * (battery_1[20]/1000) + no_battery_2 * (battery_2[20]/1000)
    print(f"Capacity: {capacity} Batteries: {no_battery_1, no_battery_2}, Mass: {mass}")

    while required_cap > capacity and mass <= max_mass:

        if required_cap - (no_battery_1 * battery_1_Wh + no_battery_2 * battery_2_Wh) > 100 * battery_1_Wh:
            no_battery_1 += 100

        elif required_cap - (no_battery_1 * battery_1_Wh + no_battery_2 * battery_2_Wh) > 10 * battery_1_Wh:
            no_battery_1 += 10

        elif required_cap - (no_battery_1 * battery_1_Wh + no_battery_2 * battery_2_Wh) > battery_1_Wh:
            no_battery_1 += 1
        
        elif required_cap - (no_battery_1 * battery_1_Wh + no_battery_2 * battery_2_Wh) > battery_2_Wh:
            no_battery_2 += 1
        
        capacity = no_battery_1 * battery_1_Wh + no_battery_2 * battery_2_Wh
        mass = no_battery_1 * (battery_1[20]/1000) + no_battery_2 * (battery_2[20]/1000)
        print(f"Capacity: {capacity} Batteries: {no_battery_1, no_battery_2}, Mass: {mass}")
    

    battery_1_peak_power = battery_1[15] * battery_1[18]
    battery_2_peak_power = battery_2[15] * battery_2[18]

    peak_power_generated = no_battery_1 * battery_1_peak_power + no_battery_2 * battery_2_peak_power

    while peak_power_required > peak_power_generated and mass <= max_mass:
        
        if peak_power_required - peak_power_generated > 100 * battery_2_peak_power:
            no_battery_2 += 100

        elif required_cap - (no_battery_1 * battery_1_Wh + no_battery_2 * battery_2_Wh) > 10 * battery_2_peak_power:
            no_battery_2 += 10

        elif required_cap - (no_battery_1 * battery_1_Wh + no_battery_2 * battery_2_Wh) > battery_2_peak_power:
            no_battery_2 += 1
        
        else:
            no_battery_1 += 1
        
        peak_power_generated = no_battery_1 * battery_1_peak_power + no_battery_2 * battery_2_peak_power
        mass = no_battery_1 * (battery_1[20]/1000) + no_battery_2 * (battery_2[20]/1000)

        print(f"Power: {peak_power_generated}, Batteries: {no_battery_1, no_battery_2}, Mass: {mass}")


    # Calculate the min and max number of cells in series for EV voltage requirements
    min_cells_series_battery_1 = math.ceil(min_pack_voltage/battery_1[16])
    max_cells_series_battery_1 = math.ceil(max_pack_voltage/battery_1[14])

    # Calculate the min and max number of cells in parallel for EV requirements
    min_cells_parallel_battery_1 = math.ceil(min_battery_1_only/max_cells_series_battery_1)
    max_cells_parallel_battery_1 = math.ceil((required_cap/pack_voltage)/battery_1[13])
    # print(max_cells_parallel, min_cells_parallel)

    # no_cells_series = min_cells_series
    # no_cells_parallel = min_cells_parallel

   




    return no_battery_1, no_battery_2 #series_values, parallel_values, max_cells_series, calculated_pack_capacity