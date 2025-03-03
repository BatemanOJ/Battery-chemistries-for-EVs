

from Get_Data_From_Cell import Get_Battery_Data_Row # gets the row of data and puts it into an array
from Calculate_Pack_Mass import Calculate_Mass_One_Batteries, Calculate_Mass_Two_Batteries

def Check_Mass(battery_1, battery_2, series_1, series_2, parallel_1, parallel_2, max_mass):

    no_battery_1 = series_1 * parallel_1
    no_battery_2 = series_2 * parallel_2
    # print(no_battery_1, no_battery_2)
    
    pack_mass = Calculate_Mass_Two_Batteries(battery_1, battery_2, no_battery_1, no_battery_2)
    # print(pack_mass, max_mass)
    # print(mass, max_mass)

    if pack_mass > max_mass:
        check = 0
    else:
        check = 1

    return check, pack_mass

def Check_Mass_Battery_Only(battery_1_mass, battery_2_mass, series_1, series_2, parallel_1, parallel_2, max_mass):
    
    mass = (series_1 * parallel_1) * (battery_1_mass/1000) + (series_2 * parallel_2) * (battery_2_mass/1000)
    # print(mass, max_mass)

    if mass > max_mass:
        check = 0
    else:
        check = 1

    return check, mass

def Check_Mass_One_Bat(battery_1, series_1, parallel_1, max_mass):

    no_battery_1 = series_1 * parallel_1
    
    pack_mass = Calculate_Mass_One_Batteries(battery_1, no_battery_1)
    # print(mass, max_mass)

    if pack_mass > max_mass:
        check = 0
    else:
        check = 1

    return check, pack_mass


def Check_Max_V(battery_1_max_V, battery_2_max_V, series_1, series_2, max_pack_V_allowed):
    
    voltage = battery_1_max_V * series_1 + battery_2_max_V * series_2

    if voltage > max_pack_V_allowed:
        check = 0
    else:
        check = 1

    return check, voltage

def Check_Min_V(battery_1_min_V, battery_2_min_V, series_1, series_2, min_pack_V_allowed):
    
    voltage = battery_1_min_V * series_1 + battery_2_min_V * series_2

    if voltage < min_pack_V_allowed:
        check = 0
    else:
        check = 1

    return check, voltage

def Check_Capacity(battery_1_capacity, battery_2_capacity, series_1, series_2, parallel_1, parallel_2, req_capacity):
    
    capacity = (battery_1_capacity * series_1 * parallel_1) + (battery_2_capacity * series_2 * parallel_2)

    if capacity < req_capacity:
        check = 0
    else:
        check = 1

    return check, capacity

# req_capacity, peak_power_req, min_pack_V_req, max_pack_V_allowed, pack_voltage, 