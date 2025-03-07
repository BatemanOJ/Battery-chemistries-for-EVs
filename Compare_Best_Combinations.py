from Meets_Conditions import Meets_Conditions


def Compare_Best_Combination(successful_combinations):
    
    average_range = sum(x[10] for x in successful_combinations)/len(successful_combinations)
    average_mass = sum(x[8] for x in successful_combinations)/len(successful_combinations)
    # average_capacity = sum(x[6] for x in successful_combinations)/len(successful_combinations)
    average_discharging_power = sum(x[7] for x in successful_combinations)/len(successful_combinations)
    average_charging_power = sum(x[9] for x in successful_combinations)/len(successful_combinations)

    list_weighted_total = []

    for i in range(0, len(successful_combinations)):
        range_difference = (successful_combinations[i][10] / average_range) - 1
        charging_power_difference = (successful_combinations[i][9] / average_charging_power) - 1
        discharging_power_difference = (successful_combinations[i][7] / average_discharging_power) - 1
        mass_difference = 1 - (successful_combinations[i][8] / average_mass)

        weighted_range_difference = range_difference * 4
        weighted_charging_power_difference = charging_power_difference * 3
        weighted_discharging_power_difference = discharging_power_difference * 2
        weighted_mass_difference = mass_difference

        weighted_total = weighted_range_difference + weighted_charging_power_difference + weighted_discharging_power_difference + weighted_mass_difference

        list_weighted_total.append([i, weighted_total])
    
    max_weighted_total = max(list_weighted_total, key=lambda x: x[1])
    print(f"Max Weighted Total: {max_weighted_total}")

    print(f"successful_combinations: {successful_combinations[max_weighted_total[0]]}")
    # print(f"Range Difference: {range_difference}, Charging Power Difference: {charging_power_difference}, Discharging Power Difference: {discharging_power_difference}, Mass Difference: {mass_difference}")
    print(f"Average Discharging Power: {average_discharging_power}, Average Mass: {average_mass}, Average Charging Power: {average_charging_power}, Average Range: {average_range}")
        
        





    
    # perfect_counter = 0

    # Three_out_of_4_counter_mass = 0
    # Three_out_of_4_mass_list = []

    # Three_out_of_4_counter = 0
    # Three_out_of_4_list = []

    # Two_out_of_4_counter = 0
    # Two_out_of_4_list = []

    # for i in range(0, len(successful_combinations)):
    #     conditions_met = Meets_Conditions(successful_combinations[i], average_range, average_mass, average_discharging_power, average_charging_power)
    #     if conditions_met[0] == 4:
    #         perfect_counter += 1

    #     elif conditions_met[0] == 3:
    #         if conditions_met[1] == 2: # means mass is the one thats below average
    #             Three_out_of_4_counter_mass += 1
    #             Three_out_of_4_mass_list.append(successful_combinations[i])
    #         Three_out_of_4_counter += 1
    #         Three_out_of_4_list.append(successful_combinations[i])
        
    #     elif conditions_met[0] == 2: 
    #         Two_out_of_4_counter += 1
    #         Two_out_of_4_list.append(successful_combinations[i])
        

        

    
    
    # # if better_than_average_combo:
    # #     print(len(better_than_average_combo))

    # print(f"Counter: {perfect_counter}, 3/4 mass: {Three_out_of_4_counter_mass}, 3/4: {Three_out_of_4_counter}, 2/4: {Two_out_of_4_counter}")

    # print(Three_out_of_4_mass_list)

    # max_range_row = max(Three_out_of_4_mass_list, key=lambda x: x[10])
    # print(f"Max Range: {max_range_row}")

    return range_difference 