import pandas as pd
import numpy as np

def load_and_process_data(path):
    rawData = pd.read_csv(path, sep=";")
    rawData = rawData[rawData.columns[:-2]].dropna().rename(columns={"RH": "Relative Humidity", "AH": "Absolute Humdity", "T": "Temp"})
    
    for col in rawData.columns:
        #covert strings into floats
        if rawData[col].dtypes == object:
            try:
                rawData[col] = rawData[col].str.replace(",", ".")
                rawData[col] = rawData[col].astype(float)
            except ValueError:
                pass
        #remove row with values of less than 0
        if rawData[col].dtypes==np.float64:
            rawData = rawData[rawData[col]>=0]
    return rawData
def getAverageConcentration(df, column):
    '''
    takes in dataFrame and a string column name
    returns an array of 24 integers representing the average values of the column for every hour of the day
    '''
    average=0
    averages = np.zeros(24)
    print(type(df[column][0]))
    for hour in range(24):
        time = "%s.00.00"%hour
        validColumns = df[df["Time"]==time]
        average = float(validColumns.sum()[column]) / int(df.shape[0])
        averages[hour]= average
    return averages
    pass