import math
# mean is proone to outliers
def mean(*args):
    total = sum(args)
    return total/len(args)

print(f"Mean:{mean(1,2,3,4,5)}")

#Median

def median(*args):
    if len(args)%2 == 0:
        i = round(len(args)/2)
        j = i -1 
        k = (args[i] + args[j])/2
        return k
    else:
        i = round(len(args)/2)
        return args[i]


print(f"Median:{median(1,2,3,4,5,6)}")

#mode

def mode(*args):
    dict = {i : args.count(i) for i in args}
    max_list = [k for k,v in dict.items() if v == max(dict.values())]
    return max_list

print(f"Mode:{mode(1,2,3,4,5,3,4,5,6)}")


#variance gives extra weight to variance since we squareing it
# SD square root of variance gives idea about how spread out data is


# coeff of variation = compare multiple data sets SD/ mean that they're ratio of disperion is same , eg miles and km 

# covariance =  to check whether the two groups of data are moving in the same direction +ve means its moving together -ve means its going in the oppposite directions
# apple earning and market cap


def variance(*args):
    mean_val = mean(*args)
    numerator = 0
    for i in args:
        numerator += (i - mean_val) ** 2
    denominator = len(args) - 1
    return numerator / denominator
 
 
def standard_deviation(*args):
    return math.sqrt(variance(*args))
 
 
def coefficient_variation(*args):
    return standard_deviation(*args) / mean(*args)
 
 
def covariance(*args):
    # Use a list comprehension to get all values
    # stored in the 1st & 2nd list
    list_1 = [i[0] for i in args]
    list_2 = [i[1] for i in args]
    # Pass those lists to get their means
    list_1_mean = mean(*list_1[0])
    list_2_mean = mean(*list_2[0])
    numerator = 0
 
    # We must have the same number of elements
    # in both lists
    if len(list_1[0]) == len(list_2[0]):
        for i in range(len(list_1[0])):
            # FInd xi - x mean * yi - y mean
            numerator += (list_1[0][i] - list_1_mean) * (list_2[0][i] - list_2_mean)
        denominator = len(list_1[0]) - 1
        return numerator / denominator
    else:
        print("Error : You must have the same number of values in both lists")
 
 
def correlation_coefficient(*args):
    list_1 = [i[0] for i in args]
    list_2 = [i[1] for i in args]
    # Pass those lists to get their standard deviations
    list_1_sd = standard_deviation(*list_1[0])
    list_2_sd = standard_deviation(*list_2[0])
    print(f"L1 SD : {list_1_sd}")
    print(f"L2 SD : {list_2_sd}")
    denominator = list_1_sd * list_2_sd
    # Get the covariance
    numerator = covariance(*args)
    return numerator / denominator
 
 
print(f"Mean : {mean(1, 2, 3, 4, 5)}")
print(f"Median : {median(1, 2, 3, 4, 5)}")
print(f"Median : {median(1, 2, 3, 4, 5, 6)}")
print(f"Mode : {mode(1, 2, 3, 4, 5, 4, 5)}")
print(f"Variance : {variance(4, 6, 3, 5, 2)}")
print(f"Standard Deviation : {standard_deviation(4, 6, 3, 5, 2)}")
print(f"Coefficient Variation (miles): {coefficient_variation(3, 4, 4.5, 3.5)}")
print(f"Coefficient Variation (kms): {coefficient_variation(4.828, 6.437, 7.242, 5.632)}")
 
# List that contains market cap in 1st list
# and earnings in the 2nd list
m_d_list = [[1532, 1488, 1343, 928, 615], [58, 35, 75, 41, 17]]
print(f"Stock Covariance : {covariance(m_d_list)}")
 
# Get the Correlation Coefficient
print(f"Correlation Coefficient : {correlation_coefficient(m_d_list)}")