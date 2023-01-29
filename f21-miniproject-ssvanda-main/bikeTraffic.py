import re
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
def get_formatted_text(filename) :

#fill in

    lines = []

    stuff = list()

    dataLine = list()

    date = list()

    day = list()

    highTemp = list()

    lowTemp = list()

    precipitation = list()

    b = list()

    m = list()

    w = list()

    q = list()

    total = list()

    allData = list()

    with open(filename,'r') as f:

        lines = f.readlines()

    #lines = [line.strip()for line in lines]

    del lines[0]

    for line in lines:
        data=[]
        line=line.strip()
        if line:
            part1,*part2 = line.split(',\"')
            data.extend(part1.split(','))
            data.extend([ele.strip('"') for ele in part2])
            dataLine.append(data)
    
    for data in dataLine:

        date.append(data[0])

        day.append(data[1])

        highTemp.append(float(data[2].strip('"')))

        lowTemp.append(float(data[3].strip('"')))

        precipitation.append((data[4].strip('"').strip('T').strip('(S)').strip(' ')))

        b.append(int(data[5].replace(',','')))

        m.append(int(data[6].replace(',','')))

        w.append(int(data[7].replace(',','')))

        q.append(int(data[8].replace(',','')))

        total.append(int(data[9].replace(',','')))

    for x in range(len(precipitation)):

        if precipitation[x] == '':

            precipitation[x] = 0

        precipitation[x] = float(precipitation[x])

    return date, day, highTemp, lowTemp, precipitation, b, m, w, q, total


if __name__ == '__main__':
    #text = get_formatted_text('behavior-performance.txt')
    data = list()
    date, day, highTemp, lowTemp, precipitation, brooklyn, manhattan, williamsburg, queensboro, total = get_formatted_text('NYC_Bicycle_Counts_2016_Corrected.csv')
    data.append(date)
    data.append(day)
    data.append(highTemp)
    data.append(lowTemp)
    data.append(precipitation)
    data.append(brooklyn)
    data.append(manhattan)
    data.append(williamsburg)
    data.append(queensboro)
    data.append(total)
    
    # for first, run to see spread, the smallest deviation doesnt need sensors
    
        #brooklyn
    brooklynSize = len(brooklyn)
    brooklynMean = np.mean(brooklyn)
    brooklynSD = np.std(brooklyn, ddof = 1)
    brooklynSE = brooklynSD / np.sqrt(brooklynSize)
    
    print(f'Mean of the Brooklyn Bridge data is {brooklynMean}\nStandard Deviation of the Brooklyn Bridge data is {brooklynSD}\nStandard Error of the Brooklyn Bridge data is {brooklynSE}\n')
        #manhattan
    manhattanSize = len(manhattan)
    manhattanMean = np.mean(manhattan)
    manhattanSD = np.std(manhattan, ddof = 1)
    manhattanSE = manhattanSD / np.sqrt(manhattanSize)
    print(f'Mean of the Manhattan Bridge data is {manhattanMean}\nStandard Deviation of the Manhattan Bridge data is {manhattanSD}\nStandard Error of the Manhattan Bridge data is {manhattanSE}\n')

        #williamsburg
    williamsburgSize = len(williamsburg)
    williamsburgMean = np.mean(williamsburg)
    williamsburgSD = np.std(williamsburg, ddof = 1)
    williamsburgSE = williamsburgSD / np.sqrt(williamsburgSize)   
    print(f'Mean of the Williamsburg Bridge data is {williamsburgMean}\nStandard Deviation of the Williamsburg Bridge data is {williamsburgSD}\nStandard Error of the Williamsburg Bridge data is {williamsburgSE}\n')

        #Queens  
    queensboroSize = len(queensboro)
    queensboroMean = np.mean(queensboro)
    queensboroSD = np.std(queensboro, ddof = 1)
    queensboroSE = queensboroSD / np.sqrt(queensboroSize) 
    print(f'Mean of the Queensboro Bridge data is {queensboroMean}\nStandard Deviation of the Queensboro Bridge data is {queensboroSD}\nStandard Error of the Queensboro Bridge data is {queensboroSE}\n')


    

    #for second, run weather on traffic for temperature and precipitation
    
    tempMean = np.mean([lowTemp, highTemp])
    highTempMean = np.mean(highTemp)
    index = 0
    highIndex = list()
    highTotal = list()
    for i in highTemp:
        if i > tempMean:
            highIndex.append(index)
        index+=1

    for i in highIndex:
        highTotal.append(total[i])
    highTotalAvg = np.mean(highTotal)
    highTempSD = np.std(highTotal, ddof = 1)
    highTempSE = highTempSD / np.sqrt(len(highTotal))
    

    lowTempMean = np.mean(lowTemp)
    
    index = 0
    lowIndex = list()
    lowTotal = list()
    for i in lowTemp:
        if i < tempMean:
            lowIndex.append(index)
        index+=1

    for i in lowIndex:
        lowTotal.append(total[i])
    lowTotalAvg = np.mean(lowTotal)
    lowTempSD = np.std(lowTotal, ddof = 1)
    lowTempSE = lowTempSD / np.sqrt(len(lowTotal))
    
    

    diffMean = highTotalAvg - lowTotalAvg
    diffSD = np.sqrt(lowTempSE**2 + highTempSE**2)
    zScore = diffMean / diffSD
    

    p = 2 * norm.cdf(-abs(zScore))


    print(f'The difference between the low temperature mean and the high temperature mean is {diffMean}')
    print(f'The standard deviation of the difference between the two means is {diffSD}')
    print(f'The Z score of the difference in the total number of people during high and low temperatures is {zScore}')
    print(f'The P value associated with the z score is {p}\n')
    

    #finding the rain
    
    # whether it will rain or not
    # x= total traffic
    # y = precipitation
    # convert precipitation values to 0s and 1s
    index = 0
    rainIndex = list()
    rainTotal = list()
    for i in precipitation:
        if i > 0:
            rainIndex.append(index)
        index+=1

    for i in rainIndex:
        rainTotal.append(total[i])
    rainTotalAvg = np.mean(rainTotal)
    rainTotalSD = np.std(rainTotal)
    rainTotalSE = rainTotalSD / np.sqrt(len(rainTotal))


    totalAvg = np.mean(total)
    totalSD = np.std(total, ddof = 1)
    totalSE = totalSD / np.sqrt(len(total))

    SD = np.sqrt(totalSE**2 + rainTotalSE**2)

    rainZscore = (rainTotalAvg - totalAvg) / SD
    pRain = 2 * norm.cdf(-abs(rainZscore))
    
    print(f'The difference between the non rainy day mean and the rainy day mean is {totalAvg - rainTotalAvg}')
    print(f'The standard deviation of the difference between the two means is {SD}')
    print(f'The Z score of the rainy day population is {rainZscore}')
    print(f'The P value associated with the z score is {pRain}\n')