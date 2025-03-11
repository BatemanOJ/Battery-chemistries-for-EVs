import math
import numpy as np


from Check_Constraints import Check_Mass_One_Bat, Check_Max_V, Check_Min_V, Check_energy_one_battery
from Calculate_Pack_Mass import Calculate_Mass_One_Batteries 




def One_Chem_Comparison(battery_1, req_energy, peak_power_req, max_pack_V_allowed, min_pack_V_allowed, max_pack_mass, peak_charge_power_req):

    # Battery 1 is the energy dense one and battery 2 is the power dense one
    # battery_1, battery_2, battery_1_Wh, battery_2_Wh = Find_Power_Dense_Battery_Efficient(battery_1, battery_2)

    battery_1_Wh = battery_1[14] * battery_1[16]

    min_battery_1_only = math.ceil(req_energy/(battery_1_Wh))
    # min_battery_2_only = math.ceil(req_energy/(battery_2_Wh))

    no_battery_1 = math.ceil(min_battery_1_only/3)
    # no_battery_2 = math.ceil(min_battery_2_only/3)

    energy = no_battery_1 * battery_1_Wh
    pack_mass = ((no_battery_1 * (battery_1[21]/1000))/battery_1[40]) * 100

    # print(f"Pre-tests, energy: {energy} Batteries: {no_battery_1}, Mass: {pack_mass}")

    
    while req_energy > energy and pack_mass <= max_pack_mass:

        if req_energy - (no_battery_1 * battery_1_Wh) > 100 * battery_1_Wh:
            no_battery_1 += 100

        elif req_energy - (no_battery_1 * battery_1_Wh) > 10 * battery_1_Wh:
            no_battery_1 += 10
        
        else:
            no_battery_1 += 1
        
        energy = math.floor(no_battery_1 * battery_1_Wh)
        pack_mass = Calculate_Mass_One_Batteries(battery_1, no_battery_1)

        if pack_mass > max_pack_mass:
            # print(f"Maximum mass exceeded: {pack_mass}, Maximum: {max_pack_mass}")
            success = 0
            # print(f"Fail, energy: {energy} Batteries: {no_battery_1}, Mass: {pack_mass}")
            return success, no_battery_1, 0, energy, 0, pack_mass, 0
        # else:
            
    # print(f"energy: {energy} Batteries: {no_battery_1}, Mass: {pack_mass}")

    max_pack_V = battery_1[15] * no_battery_1
    pack_mass = ((no_battery_1 * (battery_1[21]/1000))/battery_1[40]) * 100

    counter_max_voltage = 0
    check_mass = 1 
    check_max_V = 0
    no_battery_1_parallel = 1
    no_battery_1_series = no_battery_1

    check_max_V, max_pack_V = Check_Max_V(battery_1[15], 0, no_battery_1_series, 0, max_pack_V_allowed)
    check_min_V, min_pack_V = Check_Min_V(battery_1[17], 0, no_battery_1_series, 0, min_pack_V_allowed)
    check_mass, pack_mass = Check_Mass_One_Bat(battery_1, no_battery_1_series, no_battery_1_parallel, max_pack_mass)
    check_energy, energy = Check_energy_one_battery(battery_1_Wh, no_battery_1_series, no_battery_1_parallel, req_energy)


    while check_max_V == 0 and check_mass == 1 and check_min_V == 1 and check_energy == 1:

        no_battery_1_series = no_battery_1_series - math.floor(no_battery_1_series/(1+no_battery_1_parallel))
        no_battery_1_parallel += 1

        check_mass, pack_mass = Check_Mass_One_Bat(battery_1, no_battery_1_series, no_battery_1_parallel, max_pack_mass)
        while check_mass == 0:
            if  no_battery_1_parallel > 0 and no_battery_1_series > 1:

                no_battery_1_series -= 1
            
            else: 
                success = 0
                # print(f"Fail Mass. energy: {energy} Batteries: {no_battery_1}, Mass: {pack_mass}")
                return success, no_battery_1_series, no_battery_1_parallel, energy, 0, pack_mass, 0
            
            check_mass, pack_mass = Check_Mass_One_Bat(battery_1, no_battery_1_series, no_battery_1_parallel, max_pack_mass)
            
        check_max_V, max_pack_V = Check_Max_V(battery_1[15], 0, no_battery_1_series, 0, max_pack_V_allowed)
        check_min_V, min_pack_V = Check_Min_V(battery_1[17], 0, no_battery_1_series, 0, min_pack_V_allowed)
        check_mass, pack_mass = Check_Mass_One_Bat(battery_1, no_battery_1_series, no_battery_1_parallel, max_pack_mass)
        check_energy, energy = Check_energy_one_battery(battery_1_Wh, no_battery_1_series, no_battery_1_parallel, req_energy)


        if check_min_V == 0 or check_energy == 0 or check_mass == 0:
            success = 0
            # print(f"Fail Min-V. energy: {energy} Batteries: {no_battery_1}, Mass: {pack_mass}")
            return success, no_battery_1_series, no_battery_1_parallel, energy, 0, pack_mass, 0
    
    # print(f"Voltage Check Batteries: {no_battery_1_series, no_battery_1_parallel}")

    battery_1_peak_power = battery_1[16] * battery_1[19]

    peak_power_generated = no_battery_1_series * no_battery_1_parallel * battery_1_peak_power

    # print(f"Power: {peak_power_generated}, Batteries: {no_battery_1}, Mass: {pack_mass}")

    while peak_power_req > peak_power_generated and check_mass == 1 and check_max_V == 1:
        
        if peak_power_req - peak_power_generated > (no_battery_1_series * battery_1_peak_power):
            no_battery_1_parallel += 1
        
        else:
            no_battery_1_series += 1
            
        
        peak_power_generated = no_battery_1_series * no_battery_1_parallel * battery_1_peak_power
        # mass = no_battery_1 * (battery_1[21]/1000) + no_battery_2 * (battery_2[21]/1000)

        check_mass, pack_mass = Check_Mass_One_Bat(battery_1, no_battery_1_series, no_battery_1_parallel, max_pack_mass)
        check_max_V, max_pack_V = Check_Max_V(battery_1[15], 0, no_battery_1_series, 0, max_pack_V_allowed)
        check_min_V, min_pack_V = Check_Min_V(battery_1[17], 0, no_battery_1_series, 0, min_pack_V_allowed)
        check_energy, energy = Check_energy_one_battery(battery_1_Wh, no_battery_1_series, no_battery_1_parallel, req_energy)


        if check_mass == 0 or check_max_V == 0 or check_min_V == 0 or check_energy == 0:
            # print(f"Mass or voltage over limit{pack_mass, max_pack_V, min_pack_V}")
            success = 0
            # print(f"Fail Mass or V max/min. energy: {energy} Batteries: {no_battery_1}, Mass: {pack_mass}")
            return success, no_battery_1_series, no_battery_1_parallel, energy, 0, pack_mass, 0

        # print(f"Power: {peak_power_req, peak_power_generated}, Batteries: {no_battery_1_series, no_battery_1_parallel, no_battery_2_series, no_battery_2_parallel}, Mass: {mass}")

    # print(f"Power: {peak_power_req, peak_power_generated}, Batteries: {no_battery_1_series, no_battery_1_parallel}, Mass: {pack_mass}")
    
    battery_1_peak_charge_power = battery_1[16] * battery_1[23]

    peak_charge_power_generated = no_battery_1_series * no_battery_1_parallel * battery_1_peak_charge_power
    
    # print(f"Discharging Power: {peak_power_req, peak_power_generated}")

    while peak_charge_power_req > peak_charge_power_generated and check_mass == 1 and check_max_V == 1:
        
        if peak_charge_power_req - peak_charge_power_generated > (no_battery_1_series * battery_1_peak_charge_power):
            no_battery_1_parallel += 1

        else:
            no_battery_1_series += 1
        
        peak_charge_power_generated = no_battery_1_series * no_battery_1_parallel * battery_1_peak_charge_power
        # mass = no_battery_1 * (battery_1[21]/1000) + no_battery_2 * (battery_2[21]/1000)

        # print(f"Charging Power 2{peak_charge_power_req, peak_charge_power_generated}")

        check_mass, pack_mass = Check_Mass_One_Bat(battery_1, no_battery_1_series, no_battery_1_parallel, max_pack_mass)
        check_max_V, max_pack_V = Check_Max_V(battery_1[15], 0, no_battery_1_series, 0, max_pack_V_allowed)
        check_min_V, min_pack_V = Check_Min_V(battery_1[17], 0, no_battery_1_series, 0, min_pack_V_allowed)
        check_energy, energy = Check_energy_one_battery(battery_1_Wh, no_battery_1_series, no_battery_1_parallel, req_energy)


        if check_mass == 0 or check_max_V == 0 or check_min_V == 0 or check_energy == 0:
            # print(f"Mass or voltage over limit{pack_mass, max_pack_V, min_pack_V}")
            success = 0
            # print(f"Fail Mass. energy: {energy} Batteries: {no_battery_1}, Mass: {pack_mass}")
            return success, no_battery_1_series, no_battery_1_parallel, energy, 0, pack_mass, 0

        # print(f"Charging Power 3{peak_charge_power_req, peak_charge_power_generated}")

        # print(f"Power: {peak_power_req, peak_power_generated}, Batteries: {no_battery_1_series, no_battery_1_parallel, no_battery_2_series, no_battery_2_parallel}, Mass: {mass}")

    # print(f"Charging Power: {peak_charge_power_req, peak_charge_power_generated}")
    success = 1

    return success, no_battery_1_series, no_battery_1_parallel, energy, peak_power_generated, pack_mass, peak_charge_power_generated