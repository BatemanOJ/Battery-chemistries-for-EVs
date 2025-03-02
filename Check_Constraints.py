from Get_Data_From_Cell import Get_Battery_Data_Row # gets the row of data and puts it into an array


def Check_Mass(battery_1_mass, battery_2_mass, series_1, series_2, parallel_1, parallel_2, max_mass):
    
    mass = (series_1 * parallel_1) * (battery_1_mass/1000) + (series_2 * parallel_2) * (battery_2_mass/1000)
    # print(mass, max_mass)

    if mass > max_mass:
        check = 0
    else:
        check = 1

    return check, mass

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

# req_capacity, peak_power_req, min_pack_V_req, max_pack_V_allowed, pack_voltage, 