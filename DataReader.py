import pandas as pd
import xlrd


class DataReader:
    def __init__(self):
        fileName = 'main_data.xlsx'
        xlrd_workbook = xlrd.open_workbook(fileName)
        self.data = pd.read_excel(xlrd_workbook, engine='xlrd')

    def GetDataAmongPeriod(self, UPC, startDate, endDate):
        specificData = self.data.query('UPC =='+UPC)
        pdStartDate = pd.to_datetime(startDate)
        pdEndDate = pd.to_datetime(endDate)
        specificData = specificData.loc[(specificData['Week_and_date'] >= pdStartDate) & (specificData['Week_and_date'] <= pdEndDate)]
        return specificData

    def GetDataAmongPeriodWithGrouping(self, UPC, startDate, endDate):
        specificData = self.GetDataAmongPeriod(UPC, startDate, endDate)
        specificData = specificData.groupby(['PRICE'], as_index=False)
        specificData = specificData['Units'].sum()
        return specificData
