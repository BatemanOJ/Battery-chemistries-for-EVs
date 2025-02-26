from Get_Data_From_Cell import Get_Data_EVs # row -2, colum -1


def Range_Estimation_for_EVs(battery_cap, EV_number):
    # m1 = EV mass without battery, m2 = battery mass, Cd = drag coefficient, 
    # A = frontal area, Rr = rolling resistance

    m1 = Get_Data_EVs(3, EV_number)
    m2 = Get_Data_EVs(19, EV_number)
    Cd = Get_Data_EVs(6, EV_number)
    A = Get_Data_EVs(4, EV_number)
    Rr = Get_Data_EVs(5, EV_number)
    # print(m1, m2, Cd)

    d = 1000 # distance (meters)
    p = 1.225 # air density (kg/m^3)
    v1 = 13.888889 # speed (m/s = 50kph)
    v2 = 27.7778 # (100kph)
    
    Joules_per_km = (0.5 * Cd * A * p * v1 * v1 * d) + ((m1+m2) * 9.81 * Rr * d)
    print(Joules_per_km)
    kWh_per_km = Joules_per_km/3600000
    range_est_50kph = kWh_per_km/battery_cap

    Joules_per_km = (0.5 * Cd * A * p * v2 * v2 * d) + ((m1+m2) * 9.81 * Rr * d)
    kWh_per_km = Joules_per_km/3600000
    range_est_100kph = kWh_per_km/battery_cap
    
    return range_est_50kph, range_est_100kph