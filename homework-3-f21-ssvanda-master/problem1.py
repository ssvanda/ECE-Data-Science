import numpy as np
import matplotlib.pyplot as plt


def norm_histogram(hist):
    """
    takes a histogram of counts and creates a histogram of probabilities

    :param hist: a numpy ndarray object
    :return: list
    """

    normhist = {}
    hist_norm = {}
    norm_h = []
    #collect all points in hist
       
    for i in hist:
        norm_h.append(float(i) / (sum(hist)))
    #norm_h = list(norm_h.values())
    
    '''
    for k in hist:
        norm_h[k] = (float(k)) / (sum(hist))
  #      del norm_h[k]
    '''
    return(norm_h)


def compute_j(histo, width):
    """
    takes histogram of counts, uses norm_histogram to convert
    to probabilties, it then calculates compute_j for one bin
    width

    :param histo: list 
    :param width: float
    :return: float
    """
    norm_h = norm_histogram(histo)
    m = sum(histo)
    
    psquared = 0
    #print(norm_h)
    for x in norm_h:
        psquared = (x**2) + psquared
        #pquared is correct
    
    J1 = 2 / ((m-1)*width)
    J2 = (m+1)/((m-1)*width)
    Jval = J1 - J2 * psquared
    
    return(Jval)
    #computing the cross validation for 1 bin width




def sweep_n(data, minimum, maximum, min_bins, max_bins):
    """
    find the optimal bin
    calculate compute_j for a full sweep [min_bins to max_bins]
    please make sure max_bins is included in your sweep

    iterate across min number of bins to max mins
    for each iteration call compute j
    pass in histogram
    calls hist to make histogream
    calls compute j for hist

    sweeping thru 
    loop from min to max
        each it 
    :param data: list
    :param minimum: int
    :param maximum: int
    :param min_bins: int
    :param max_bins: int
    :return: list
    """
    Jval = []
    count = min_bins
    while count <= max_bins:
        histo = plt.hist(data, count, (minimum, maximum))[0]
        Jval.append(compute_j(histo, (maximum - minimum)/count))
        count = count + 1
    
    return Jval


def find_min(l):
    """
    Generic function that takes a list of numbers and returns the smallest number in that list and its index in the list.
    It will return the optimal value and the index of the optimal value as a tuple.

    :param l: list
    :return: tuple
    """
    minimum = min(l)
    stuff = ()
    count = 0
    for x in l:
        if minimum == x:
            final = count
        else:
            count = count + 1
    stuff = (minimum, final)
    return(stuff)


if __name__ == '__main__':
    data = np.loadtxt('input.txt')  # reads data from input.txt
    lo = min(data)
    hi = max(data)
    bin_l = 1
    bin_h = 100
    js = sweep_n(data, lo, hi, bin_l, bin_h)
    """
    the values bin_l and bin_h represent the lower and higher bounds of the range of bins.
    They will change when we test your code and you should be mindful of that.
    """
    print(find_min(js))
