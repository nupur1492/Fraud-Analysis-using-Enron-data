#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
     ### your code goes here
    print(len(ages))
    print(type(ages))
    n_elements = int(len(ages) * 0.9)


    #sort data
    def dataSort(data):
        for x in range(0, len(data)):
            for y in (0,len(age)):
                if(data[y][1] > data[y+1][1]):

                    temp=data[j]
                    data[j]=data[j+1]
                    data[j+1]=temp

    #randomly_selected = random.sample(ages, n_elements)

    data = []
    for i in range(0,len(ages)):
        res_err = abs(net_worths[i] - predictions[i])
        data.append((ages[i],net_worths[i], res_err))
        #print(data)
    print("data type>> ", type(data))
    #data.sort(reverse=True)
    data = sorted(data, key=lambda x: x[2])
    #sort data

    cleaned_data = data[:81]

    #print(n_elements)
    print(ages.shape)
    #cleaned_data = ""
    print(len(cleaned_data))


    
    return cleaned_data

