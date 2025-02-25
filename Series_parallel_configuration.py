import numpy as np
import math

from Get_Data_From_Cell import Get_Data_EVs # row -2, colum -1

def Series_Parallel_Config_EV(EV_number): #, no_cells_series, no_cells_parallel, max_cells_parallel, peak_cell_current, min_cell_voltage, \
                           #peak_discharge_power, max_cells_series, min_cells_series, series_values, parallel_values):


    # Data retrieved from the excel sheet containing EV database
    EV_required_capacity = Get_Data_EVs(7, EV_number)
    cell_energy_capacity = Get_Data_EVs(33, EV_number)

    min_pack_voltage = Get_Data_EVs(21, EV_number)
    max_pack_voltage = Get_Data_EVs(20, EV_number)

    min_cell_voltage = Get_Data_EVs(31, EV_number)
    max_cell_voltage = Get_Data_EVs(29, EV_number)

    peak_discharge_power = 190512#Get_Data_EVs(12, EV_number)

    peak_cell_current = Get_Data_EVs(34, EV_number)
    nominal_pack_capacity = Get_Data_EVs(19, EV_number)
    cell_capacity = Get_Data_EVs(32, EV_number)

    # Calculate the minimum number of cells required for the EV capacity requirement
    min_cells = EV_required_capacity/cell_energy_capacity

    # Calculate the min and max number of cells in series for EV voltage requirements
    min_cells_series = math.ceil(min_pack_voltage/min_cell_voltage)
    max_cells_series = math.ceil(max_pack_voltage/max_cell_voltage)

    # Calculate the min and max number of cells in parallel for EV requirements
    min_cells_parallel = math.ceil(min_cells/max_cells_series)
    max_cells_parallel = math.ceil(nominal_pack_capacity/cell_capacity)
    # print(max_cells_parallel, min_cells_parallel)

    no_cells_series = min_cells_series
    no_cells_parallel = min_cells_parallel

    series_values = []
    parallel_values = []

    while no_cells_parallel <= max_cells_parallel:
        if (peak_cell_current * no_cells_parallel * min_cell_voltage * no_cells_series) < peak_discharge_power:
            
            result = peak_cell_current * no_cells_parallel * min_cell_voltage * no_cells_series
            # print(peak_discharge_power, result, no_cells_parallel, no_cells_series)

            if peak_discharge_power - (peak_cell_current * no_cells_parallel * min_cell_voltage * no_cells_series) < \
            peak_cell_current * no_cells_parallel * ((min_cell_voltage * max_cells_series) - (min_cell_voltage * min_cells_series)):

                if no_cells_series < max_cells_series:
                    no_cells_series += 1

            else:
                if no_cells_parallel < max_cells_parallel:
                    no_cells_parallel += 1

                else:
                    print("No combination found")
                    break
            
        else:
            
            series_values.append(no_cells_series)
            parallel_values.append(no_cells_parallel)
            
            no_cells_series = min_cells_series
            no_cells_parallel += 1
    
    return series_values, parallel_values, max_cells_series