import random


def selection_sort(input_list):
    n = len(input_list)

    for i in range(n-1):
        smallest_idx = 0
        for j in range(1,n-i):
            if(input_list[j]<input_list[smallest_idx]):
                smallest_idx = j

        if(smallest_idx != j):
            input_list[smallest_idx] = input_list[smallest_idx] + input_list[j]
            input_list[j] = input_list[smallest_idx] - input_list[j]
            input_list[smallest_idx] = input_list[smallest_idx] - input_list[j]
    return(input_list)


def main():
    n = 10
    input_list = []

    for i in range(n):
        input_list.append(random.randrange(-100,100))
    print("input array: ", str(input_list))
    sorted_list = selection_sort(input_list)
    print("sorted array: ",str(sorted_list))

if __name__ == "__main__":
    main()