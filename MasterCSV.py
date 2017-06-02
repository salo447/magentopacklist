###Merge all test data CSVs into one and export
import pandas as pd

ampCutoff = -15


###Merge
CSVList = ['Test2 - Discharge.csv', 'Test3 - Discharge.csv',
                'Sample2 - Discharge.csv']
colIndices = ['Test2', 'Test3', 'Sample2']

masterlist = pd.DataFrame()

for row, dataset in enumerate(CSVList):
    temp = pd.read_csv(dataset, delimiter = ',', encoding="utf-8-sig")

    temp = temp.loc[temp['Amps'] < ampCutoff] #Eliminate data under ampCutoff discharge

    for column in list(temp.columns.values):
        masterlist[colIndices[row]+column] = temp[column]






###Export
masterlist.to_csv('BatteryTest.csv', encoding='utf-8')






