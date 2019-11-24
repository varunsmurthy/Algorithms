import random
import math

def binary_search(input_list, required_element):
    idx = -1
    input_length = len(input_list)
    low_idx = 0
    high_idx = input_length - 1

    while (low_idx <= high_idx):
        mid_idx = math.floor((low_idx+high_idx)/2.0)

        if(input_list[mid_idx] == required_element):
            return (mid_idx)
        elif (input_list[mid_idx] > required_element):
            high_idx = mid_idx - 1
        else:
            low_idx = mid_idx + 1

    return(idx)


def main():
    #create a list of sorted integers
    n = 100
    input_list = [2*i for i in range(n)]
    req_value = random.randrange(0,200)

    bin_search_index = binary_search(input_list, req_value)
    if (bin_search_index != -1):
        print("Required value: ",str(req_value)," Index: ", str(bin_search_index))
    else:
        print("Required value: ",str(req_value),", not found")

if __name__ == "__main__":
    main()

# Required value:  162  Index:  81
# Required value:  95 , not found