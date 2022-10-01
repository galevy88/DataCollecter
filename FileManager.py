import pandas as pd
from datetime import datetime
import csv


def __init__(self):
    self.df_list = []

def convert_indicators_to_CSV(path, asset_list ,indicator_Data, time_type):
    Time = datetime.now()
    for i in indicator_Data:
        i["Time"] = Time
    print(f'Saving Data For {time_type}. Current TIme is: {datetime.now()}')
    df = create_dataframe(asset_list, indicator_Data)
    df.to_csv(path, mode='a', index=True, header=True, float_format="%.4f")

def create_dataframe(asset_list ,Data):
    header_list = create_header_for_dataFrame(Data)
    ls = []
    for asset in Data:
        ls.append(asset.values())
    df = pd.DataFrame(ls, columns=header_list, index=asset_list)
    return df


def create_header_for_dataFrame(Data):  
    header_list = Data[0].keys()
    return header_list

