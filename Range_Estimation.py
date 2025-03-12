import math
import numpy as np  
import scipy.integrate as spi

from Get_Data_From_Cell import Get_Data_EVs # row -2, colum -1


def Range_Estimation_for_EVs(battery_cap, EV_number):
    # m1 = EV mass without battery, m2 = battery mass, Cd = drag coefficient, 
    # A = frontal area, Rr = rolling resistance

    m1 = Get_Data_EVs(3, EV_number) # EV mass without battery
    m2 = Get_Data_EVs(18, EV_number) # Battery mass
    m3 = Get_Data_EVs(17, EV_number) - m2 # Pack mass
    Cd = Get_Data_EVs(6, EV_number) # drag coefficient
    A = Get_Data_EVs(4, EV_number) # frontal area
    Rr = Get_Data_EVs(5, EV_number) # rolling resistance
    # print(m1, m2, Cd)

    d = 1 # distance (meters)
    p = 1.225 # air density (kg/m^3)
    v1 = 13.888889 # speed (m/s = 50kph)
    v2 = 27.7778 # (100kph)
    

    Drag = (0.5 * Cd * A * p * v1 * v1 * d)
    Road_resistance = ((m1+m2+m3) * 9.81 * Rr * d)
    Joules_per_m = Drag + Road_resistance   # Speed = 50kph
    # print(Drag, Road_resistance)
    
    Wh_per_km = (Joules_per_m/3600000) * 1000000
    # print(f"Wh/km: {Wh_per_km}, Battery Capacity: {battery_cap}")
    range_est_50kph = battery_cap/(Wh_per_km)

    Joules_per_m = (0.5 * Cd * A * p * v2 * v2 * d) + ((m1+m2+m3) * 9.81 * Rr * d)   # Speed = 100kph
    Wh_per_km = (Joules_per_m/3600000) * 1000000
    range_est_100kph = battery_cap/(Wh_per_km)
    
    return range_est_50kph, range_est_100kph



def Range_Estimation_for_Batteries(WLTP_data, car_data, battery_data_series_parallel, battery_1, battery_2):

    # battery_data = [no_series_1, no_series_2, no_parallel_1, no_parallel_2]

    WLTP_Acceleration = 4   # acceleration (m/s^2)
    WLTP_Velocity = 3       # velocity (m/s)
    WLTP_Time = 1           # time (s)
    WLTP_Distance = 5       # distance (m)

    EV_mass = car_data[0]           # EV mass without battery
    Cd = car_data[1]                # drag coefficient
    Af = car_data[2]                # frontal area
    Rr = car_data[3]                # rolling resistance
    Angle_of_Car = car_data[4]     # angle of road

    p = 1.225 # air density (kg/m^3)
 
    Power_values = []
    Time_values = []

    if battery_data_series_parallel[2] == 0:
        Battery_mass = battery_data_series_parallel[0] * battery_data_series_parallel[1] * (battery_1[21]/1000)
        
        Pack_mass = ((battery_data_series_parallel[0] * battery_data_series_parallel[1] * (battery_1[21]/1000))/battery_1[40])*100
        
        battery_energy = (battery_data_series_parallel[0] * battery_data_series_parallel[1] * battery_1[14] * battery_1[16])/1000
    
    else:
    
        Battery_mass = battery_data_series_parallel[0] * battery_data_series_parallel[1] * (battery_1[21]/1000) + \
                    battery_data_series_parallel[2] * battery_data_series_parallel[3] * (battery_2[21]/1000)
        
        Pack_mass = ((battery_data_series_parallel[0] * battery_data_series_parallel[1] * (battery_1[21]/1000))/battery_1[40])*100 + \
                    ((battery_data_series_parallel[2] * battery_data_series_parallel[3] * (battery_2[21]/1000))/battery_2[40])*100
        
        battery_energy = (battery_data_series_parallel[0] * battery_data_series_parallel[1] * battery_1[14] * battery_1[16] + \
                        battery_data_series_parallel[2] * battery_data_series_parallel[3] * battery_2[14] * battery_2[16])/1000
    

    # print(f"battery mass: {battery_1[21]}, {battery_2[21]}")
    # print(f"Series - parallel {battery_data_series_parallel[0], battery_data_series_parallel[1], battery_data_series_parallel[2], battery_data_series_parallel[3]}")
    
    # Pack_mass_test = 795.92 # Rivian R1T
    # Pack_mass_test = 443 # Kia Niro
    # Pack_mass_test = 273 # Nissan leaf
    # Pack_mass_test = 315.7 # Tesla model 3
    # Pack_mass_test = 664.7 # polesar 3


    # Power = m*a + (p/2)*Cd*Af*v^2 + Rr*m*g + m*g*sin(theta)

    for i in range(1, len(WLTP_data)):
        WLTP_row_index = i # 1 = row 3
        #     print(f"Row 1 acc: {WLTP_data[f"WLTP_{0}_index"][4], WLTP_data[f"WLTP_{1}_index"][4], WLTP_data[f"WLTP_{2}_index"][4]}")
        
        
        Power = (EV_mass + Pack_mass) * WLTP_data[f"WLTP_{WLTP_row_index}_index"][4] + (p) * Cd * Af * (WLTP_data[f"WLTP_{WLTP_row_index}_index"][3]**2) + \
                Rr * (EV_mass + Pack_mass) * 9.81 + (EV_mass + Pack_mass) * 9.81 * math.sin(Angle_of_Car)
        
        
        time = WLTP_data[f"WLTP_{WLTP_row_index}_index"][1]

        Power_values.append(Power)
        Time_values.append(time)
        

    Energy_1 = np.trapz(Power_values, Time_values)
    # print(f"Power: {Power_values[0:10]}, Time: {Time_values[0:10]}")
    # print(f"Energy: {Energy_1}")

    Energy_1_per_km = Energy_1/ (23.29023374 * 360000)
    # print(f"Energy 1 per km: {Energy_1_per_km}")
    
    Range_1 = ((battery_energy)/Energy_1_per_km) * 0.97

    # print(f"Pack mass: {Pack_mass}, Battery mass {Battery_mass}, Battery capacity(kWh): {battery_energy}, Range: {Range_1}")

    # battery_energy_test = 135 # Rivian R1T
    # battery_energy_test = 64 # Kia Niro
    # battery_energy_test = 24 # Nissan Leaf
    # battery_energy_test = 82.1 # Tesla model 3
    # battery_energy_test = 111 # Polestar 3 

    # Range_1 = ((battery_energy_test)/Energy_1_per_km) * 0.97

    # Power_1 = (EV_mass + Pack_mass_test) * WLTP_data[f"WLTP_{1}_index"][4] 
    # Power_2 = (p/2) * Cd * Af * (WLTP_data[f"WLTP_{1}_index"][3]**2) 
    # Power_3 = Rr * (EV_mass + Pack_mass_test) * 9.81 
    # Power_4 = (EV_mass + Pack_mass_test) * 9.81 * math.sin(Angle_of_Car)
    # print(f"Power 1: {Power_1}, Power 2: {Power_2}, Power 3: {Power_3}, Power 4: {Power_4}")
    # print(EV_mass)

    return Range_1
          
