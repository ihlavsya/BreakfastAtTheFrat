import PlotGenerator as pltGenerator
import Calculations as calc
import DataReader as dataReader


def DisplayProfitAmongPeriod(reader, UPC, startDate, endDate, label):
    data = reader.GetDataAmongPeriod(UPC, startDate, endDate)
    profit = calc.MultiplyLists(data['Units'], data['PRICE'])
    plt = pltGenerator.PlotGenerator()
    plt.GetPlot(data['Week_and_date'].tolist(), profit, 'dates', 'profit', label)


def DisplayUnitsVsPrices(reader, UPC, date):
    data = reader.GetDataAmongPeriod(UPC, date, date)
    plt = pltGenerator.PlotGenerator()
    plt.GetScatter(data['PRICE'], data['Units'], 'prices', 'units', date)


def GetBestPriceWithinOneYear(reader, UPC, startDate, endDate):
    data = reader.GetDataAmongPeriodWithGrouping(UPC, startDate, endDate)
    return calc.GetBestPrice(data['Units'], data['PRICE'])


def GetBestPriceForNextTwoWeeks(reader, UPC):
    # Today is 2018-12-02, so:
    startDate2011 = '2011-12-07'
    endDate2011 = '2011-12-14'

    startDate2010 = '2010-12-08'
    endDate2010 = '2010-12-15'

    startDate2009 = '2009-12-09'
    endDate2009 = '2009-12-16'

    bestPrice2011 = GetBestPriceWithinOneYear(reader, UPC, startDate2011, endDate2011)
    bestPrice2010 = GetBestPriceWithinOneYear(reader, UPC, startDate2010, endDate2010)
    bestPrice2009 = GetBestPriceWithinOneYear(reader, UPC, startDate2009, endDate2009)

    bestPrices = [bestPrice2011, bestPrice2010, bestPrice2009]

    return sum(bestPrices)/len(bestPrices)


def main():
    #let`s take a look how profit (units*prices) depends on datetime for one product
    UPC = input("enter UPC for your product: ")
    reader = dataReader.DataReader()
    DisplayProfitAmongPeriod(reader, UPC, '2009-01-14', '2011-12-28', '2009-2011')
    # let`s take a look how profit depends on dates within one year for three years (2011, 2010, 2009)
    DisplayProfitAmongPeriod(reader, UPC, '2011-01-05', '2011-12-28', '2011')
    DisplayProfitAmongPeriod(reader, UPC, '2010-01-06', '2010-12-29', '2010')
    DisplayProfitAmongPeriod(reader, UPC, '2009-01-14', '2009-12-30', '2009')
    # let`s take a look how units depends on prices for one week (2011-12-07)
    DisplayUnitsVsPrices(reader, UPC, '2011-12-07')
    # as i can see there is no obvious dependencies within these features.
    # That`s why I decided to calculate best price this way.
    price = GetBestPriceForNextTwoWeeks(reader, UPC)
    print(price)


if __name__ == "__main__":
    main()