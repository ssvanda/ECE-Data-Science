import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
#Return fitted model parameters to the dataset at datapath for each choice in degrees.
#Input: datapath as a string specifying a .txt file, degrees as a list of positive integers.
#Output: paramFits, a list with the same length as degrees, where paramFits[i] is the list of
#coefficients when fitting a polynomial of d = degrees[i].
def main(datapath, degrees):
    paramFits = []
    #fill in
    #read the input file, assuming it has two columns, where each row is of the form [x y] as
    #in poly.txt.
    #iterate through each n in degrees, calling the feature_matrix and least_squares functions to solve
    #for the model parameters in each case. Append the result to paramFits each time.
    fullData = []
    xData = []
    yData = []
    myFile = open(datapath,'r')
    data = myFile.readlines()
    myFile.close()
    
    
    for eachline in data:
        [x,y] = eachline.split()
        #fullData.append([float(x),float(y)])
        xData.append(float(x))
        yData.append(float(y))
        #xData[count] = float(x)
        # x is feature
        # y is target
    copyData = []
    copyData = xData
    #variables now has all the data in two columns
    plt.scatter(xData, yData, color = 'blue', label = 'data')
    #xData.sort()
    pred_y = []
    for a in degrees:
        featureResult = feature_matrix(copyData, a)
        # multiply the feature result by the element in the 
        # get a feature matrix in each loop and np.dot that with the parameters
        
        variable = least_squares(featureResult,yData)
        paramFits.append(variable)
        #print(variable)
        # get row from matrix
        # create feature matrix
        # for degrees, take care of itself
        # degrees changes based on length of paramfits
        
        #loop thru paramfits
        
        pred_y.append(np.multiply(featureResult,variable))
        #print(f"pred_y value is {pred_y}")
        #print(xData.size())
        #print(pred_y.size())
        #print(f"featureResult value is {featureResult}")
    #for var in paramFits:  

    #for var in paramFits:
    #    pred_y = np.multiply(featureResult,var)
    
    xData.sort()
    paramFits1 = []
    paramFits2 = []
    paramFits3 = []
    paramFits4 = []
    paramFits5 = []
    #print(len(paramFits[4]))
    thing1Split = []
    thing2Split = []
    thing3Split = []
    thing4Split = []
    thing5Split = [] 
    
    thing1 = (np.multiply(paramFits[0],feature_matrix(xData,degrees[0]))) + paramFits[0][1]
    thing2 = (np.multiply(paramFits[1],feature_matrix(xData,degrees[1]))) + paramFits[1][2]
    thing3 = (np.multiply(paramFits[2],feature_matrix(xData,degrees[2]))) + paramFits[2][3]
    thing4 = (np.multiply(paramFits[3],feature_matrix(xData,degrees[3]))) + paramFits[3][4]
    thing5 = (np.multiply(paramFits[4],feature_matrix(xData,degrees[4]))) + paramFits[4][5]
    '''
    thing1 = (np.multiply(paramFits[0],feature_matrix(xData,degrees[0])))
    thing2 = (np.multiply(paramFits[1],feature_matrix(xData,degrees[1])))
    thing3 = (np.multiply(paramFits[2],feature_matrix(xData,degrees[2])))
    thing4 = (np.multiply(paramFits[3],feature_matrix(xData,degrees[3])))
    thing5 = (np.multiply(paramFits[4],feature_matrix(xData,degrees[4])))
    '''
    for eachline in thing1:
        thing = eachline[0]
        #thing1Split = sum(thing)
        thing1Split.append(thing)
    for eachline in thing2:
        thing = eachline[1]
        #thing2Split = sum(thing)
        thing2Split.append(thing)
    for eachline in thing3:
        thing = eachline[0]
        #thing3Split = sum(thing)
        thing3Split.append(thing)
    for eachline in thing4:
        thing = eachline[1]
        #thing4Split = sum(thing)
        thing4Split.append(thing)
    for eachline in thing5:
        thing = eachline[2]
        #thing5Split = sum(thing) 
        thing5Split.append(thing)
    
    plt.plot(xData, thing1Split, color = 'red', label = 'd = 1')
    plt.plot(xData, thing2Split, color = 'pink', label = 'd = 2')
    plt.plot(xData, thing3Split, color = 'black', label = 'd = 3')
    plt.plot(xData, thing4Split, color = 'green', label = 'd = 4')
    plt.plot(xData, thing5Split, color = 'purple', label = 'd = 5')
    plt.legend()
    plt.show()
    
    return paramFits


#Return the feature matrix for fitting a polynomial of degree d based on the explanatory variable
#samples in x.
#Input: x as a list of the independent variable samples, and d as an integer.
#Output: X, a list of features for each sample, where X[i][j] corresponds to the jth coefficient
#for the ith sample. Viewed as a matrix, X should have dimension #samples by d+1.
def feature_matrix(x, d):
    # takes one colum x and produces a matrix
    # takes in the original x and then the degree that x should be expanded to
    # if d = 2, the number of col should be 3, based on the power thingy

    # 4 columns, each corresponds to a degree
    #fill in
    #There are several ways to write this function. The most efficient would be a nested list comprehension
    #which for each sample in x calculates x^d, x^(d-1), ..., x^0.
    #X = np.zeros(len(x),d)
    #print(x)
    #print(d)
    X = []
    newList = []
    for a in range(len(x)):
        for b in range(d,-1,-1):
            newList.append(x[a]**b)
        X.append(newList)
        newList = []
    '''
    for a in x:
        for b in range(d):
            X[a][b] = (a**b)
    '''
    return X


#Return the least squares solution based on the feature matrix X and corresponding target variable samples in y.
#Input: X as a list of features for each sample, and y as a list of target variable samples.
#Output: B, a list of the fitted model parameters based on the least squares solution.
def least_squares(X, y):
    X = np.array(X)
    y = np.array(y)
    # X produced by calling feature
    #fill in
    #Use the matrix algebra functions in numpy to solve the least squares equations. This can be done in just one line.
    '''
    a = np.transpose(X)
    b = np.linalg.inv((np.transpose(X),X))
    c = np.dot(b, np.transpose(X)) 
    B = np.dot(c,y)
    #c = np.dot(np.transpose(X),y)
    '''
    first = X.T @ X
    second = np.linalg.inv(first)
    third = second @ X.T
    fourth = third @ y
    B = fourth
    #B = np.dot(b,c)
    return B

if __name__ == '__main__':
    datapath = 'poly.txt'
    # degrees = [2, 4]
    degrees = [1,2,3,4,5]
    paramFits = main(datapath, degrees)
    #for i in degrees:
    #    featureResult = feature_matrix(xData, i)
    #    pred_y = np.multiply(featureResult,least_squares(featureResult,yData))
    
    print(paramFits)

    # plt.plot(xData, paramFits*feature_matrix(xData,degree))
#make degrees as 1 2 3 4 5 and then plot it 