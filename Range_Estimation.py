from Get_Data_From_Cell import Get_Data_EVs # row -2, colum -1


def Range_Estimation_for_EVs(battery_cap, EV_number):
    # m1 = EV mass without battery, m2 = battery mass, Cd = drag coefficient, 
    # A = frontal area, Rr = rolling resistance

    m1 = Get_Data_EVs(3, EV_number) # EV mass without battery
    m2 = Get_Data_EVs(18, EV_number) # Battery mass
    m3 = Get_Data_EVs(17, EV_number) - m2 # Pack mass
    Cd = Get_Data_EVs(6, EV_number)
    A = Get_Data_EVs(4, EV_number)
    Rr = Get_Data_EVs(5, EV_number)
    # print(m1, m2, Cd)

    d = 1 # distance (meters)
    p = 1.225 # air density (kg/m^3)
    v1 = 13.888889 # speed (m/s = 50kph)
    v2 = 27.7778 # (100kph)
    

    Drag = (0.5 * Cd * A * p * v1 * v1 * d)
    Road_resistance = ((m1+m2+m3) * 9.81 * Rr * d)
    Joules_per_m = Drag + Road_resistance
    # print(Drag, Road_resistance)
    
    Wh_per_km = (Joules_per_m/3600000) * 1000000
    # print(f"Wh/km: {Wh_per_km}, Battery Capacity: {battery_cap}")
    range_est_50kph = battery_cap/(Wh_per_km)

    Joules_per_m = (0.5 * Cd * A * p * v2 * v2 * d) + ((m1+m2+m3) * 9.81 * Rr * d)
    Wh_per_km = (Joules_per_m/3600000) * 1000000
    range_est_100kph = battery_cap/(Wh_per_km)
    
    return range_est_50kph, range_est_100kph
          
