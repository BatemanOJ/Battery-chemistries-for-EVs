import pandas as pd
import numpy as np

def Get_Data_From_Cell(row_index, column_index):

    battery_database = pd.read_excel("Battery database from open source_CellDatabase_v6.xlsx", sheet_name="RAW DATA")

    value = battery_database.iloc[row_index, column_index]

    return value

def Get_Data_EVs(row_index, column_index):

    battery_database = pd.read_excel("Battery database from open source_CellDatabase_v6.xlsx", sheet_name="EV Data")

    value = battery_database.iloc[row_index, column_index]

    return value
