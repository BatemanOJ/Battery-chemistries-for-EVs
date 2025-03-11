

def Charging_times(battery_data_series_parallel, battery_1, battery_2, successful_combinations):

    # print(f"Charging times: {successful_combinations[0]}")
    battery_1_capacity = battery_1[14]
    battery_2_capacity = battery_2[14]

    battery_1_max_charging = battery_1[23]
    battery_2_max_charging = battery_2[23]

    battery_1_std_charging = battery_1[24]
    battery_2_std_charging = battery_2[24]

    battery_1_min_time = 60 * (battery_1_capacity/battery_1_max_charging)
    battery_2_min_time = 60 * (battery_2_capacity/battery_2_max_charging)
    min_total_time = battery_1_min_time + battery_2_min_time

    battery_1_std_time = battery_1_capacity/battery_1_std_charging
    battery_2_std_time = battery_2_capacity/battery_2_std_charging
    std_total_time = battery_1_std_time + battery_2_std_time

    print(f"Min charging times (mins): {battery_1_min_time, battery_2_min_time, min_total_time}")
    print(f"Standard charging times (hours): {battery_1_std_time, battery_2_std_time}")
    


    return battery_1_min_time, battery_2_min_time, battery_1_std_time, battery_2_std_time#time_battery_1, time_battery_2, time_total