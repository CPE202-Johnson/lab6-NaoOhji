import random
import time

def selection_sort(list):
    comps = 0
    for index in range(len(list)):
        minIndex = index
        j = index+1
        while j<len(list):
            if list[j] < list[minIndex]:
                minIndex = j
            j += 1
            comps += 1
        swap(list[index],list[minIndex])
    return comps

def swap(x,y):
    temp = x
    x = y
    y = temp

def insertion_sort(list):
    comps = 0
    for index in range(len(list)):
        j = index
        value = index
        while value != -1 and list[j] <= list[value]:
            value -= 1
            comps += 1
        if value +1 != j:
            temp = list.pop(j)
            list.insert(value+1,temp)
    return comps
   

def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 32000)
    start_time = time.time() 
    #comps = selection_sort(randoms)
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()

