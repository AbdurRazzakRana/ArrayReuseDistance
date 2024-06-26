import sys

number_of_list = 3

list_1_start = -1
list_1_updated = []

list_2_start = -1
list_2_updated = []

list_3_start = -1
list_3_updated = []

list_n = []
list_n_count = 0
list_n_start = -1

# Intialize and reset to begin at the time of each prediction call
def init():
    global number_of_list, list_1_start, list_1_updated, list_2_start, list_2_updated, list_3_start, list_3_updated
    global list_n, list_n_count, list_n_start

    list_1_start = -1
    list_1_updated = []

    list_2_start = -1
    list_2_updated = []

    list_3_start = -1
    list_3_updated = []

    list_n = []
    list_n_count = 0
    list_n_start = -1


# This method will initialize intermil lists with deducting the initial value from all values in the list
def init_updated_lists(list1, list2, list3):
	
    global list_1_updated, list_2_updated, list_3_updated
    global list_1_start, list_2_start, list_3_start
    list_1_start = list1[0]
    for index, rd in enumerate(list1):
        list_1_updated.append(list1[index]-list_1_start)
    
    list_2_start = list2[0]
    for index, rd in enumerate(list2):
        list_2_updated.append(list2[index]-list_2_start)
        
    list_3_start = list3[0]
    for index, rd in enumerate(list3):
        list_3_updated.append(list3[index]-list_3_start)

# At this point, before calling this function
# we know that we have to expend the list with maintaing incremental order with previous values
# this function will fill out those numbers
def fillout_rest_incremental(list_n_count, list_n):
    sz = len(list_n)
    diff = list_n[sz -1] - list_n[sz-1-1]
    while sz < list_n_count:
        list_n.append(list_n[sz-1] + diff)
        sz += 1
    return 

# This function will fillout with linear connected numbers
# Before calling this function, we have to know that the relationship between the numbers are linear
def fillout_rest_linear(list_n_count, list_n):
    sz = len(list_n)
    diff = list_n[sz -1] - list_n[sz-1-1]
    i = 1
    while sz < list_n_count:
        list_n.appand(list_n[sz-1] + diff * i)
        sz += 1
        i+=1
    return 

# This method will check if the same indexed numbers of all the lists are linearly connected or not
# For example, in the below case, we can say index 1 of all lists are linearly connected with index 0
# list1[1] - list1[0] = 10
# list2[1] - list2[0] = 12
# list3[1] - list3[0] = 14
def is_linear(same_indexed_nums, list_n_diff, n):
    diff = same_indexed_nums[1] - same_indexed_nums[0]
    for i in range(1, len(same_indexed_nums)):
        if (same_indexed_nums[i] - same_indexed_nums[i-1]) != diff:
            return False
    if same_indexed_nums[0] + diff * (n-1) != list_n_diff:
        return False
    
    # print("Numbers are linearly connected")
    return True

# This method will check if the same indexed numbers of all the lists are incrementally connected or not
# For example, in the below case, we can say index 1 of all lists are linearly connected with index 0
# list1[1] - list1[0] = 10
# list2[1] - list2[0] = 10
# list3[1] - list3[0] = 10    
def is_constant(same_indexed_nums, list_n_diff, n):
    const = True
    val_0 = same_indexed_nums[0]
    for index, value in enumerate(same_indexed_nums):
        const = const and same_indexed_nums[index] == val_0
    if not const:
        return False
    
    if not list_n_diff == val_0:
        return False
    
    # print ("Numbers are incremental")
    return True

# Finalizing list with adding the starting value
def finalize_list(list_n, list_n_start):
    for index, value in enumerate(list_n):
        list_n[index] = list_n[index] + list_n_start

# Rule 3: The Predicted list size will be somehow connected with the given small list sizes
# this method will identify what will be the size of the list
def predict_n_list_size(n):
	
    global list_n_count, number_of_list
    incremental_from_base = len(list_2_updated) - len(list_1_updated)
    prev_list = list_2_updated
    for i in range(3,number_of_list+1):
        list_name = "list_"+str(i)+"_updated"
        working_list = globals()[list_name]
        if (len(working_list) - len(prev_list)) != incremental_from_base:
            print("Barf: incremental is not the same")
            sys.exit(1)
        prev_list = working_list
    # End of For loop
    list_n_count =  len(list_1_updated) + incremental_from_base * (n-1)
    return

# Rule 2: Lists connected with their neighbours. Same index of different lists are connected eigher in linearly or incrementally
# This method will predict the list based on neighbour list
def predict_list_from_neighbour(list_n_count, list_n_start, interim_lists, n):
    global list_n
    out_list_interim = []
    # find the lowest size of the list
    min_length = sys.maxsize
    for index, sublist in enumerate(interim_lists):
        list_size = len(sublist)
        if list_size < min_length:
            min_length = list_size
    
    # At this point all the lists has the minimum items of min_length starting from 0
    # We are gonna produce rules up until that size for the final array

    for i in range (0, min_length):
        # observe each ith element of the lists and come up with the rule for ith index of target list
        
        index_base = interim_lists[0][i]
        index_incremental = interim_lists[1][i] - index_base
        # index_base = interim_lists[1][i]
        # j = 2
        # while j<len(interim_lists) : 
        #     if(interim_lists[j][i] - index_base) != index_incremental:
        #         print("Barf: Neighbour list is not sequaltial")
        #         sys.exit(1)
        #     index_base = interim_lists[j][i]
        #     j+=1
        
        # index_base = interim_lists[0][i]
        out_list_interim.append(index_base + (n-1) * index_incremental)

        # print(out_list_interim[i] )
    list_n = out_list_interim

# Rule 1: As we predicted the list using rule 2 with neighbour, we have to verify the predicted
# list correctness using same list connection. Numbers inside a list are connected.
# this method will evaluate that relationship
def verify_list_from_own_list_conn(list_n_count, list_n_start, interim_lists, n):
    global list_n
    list_n_sz = len(list_n)
    same_indexed_nums = []
    incremental_coutner = 0
    linear_counter = 0
    is_last_one_incremental = False
    for i in range(1, list_n_sz):
        for j in range (0, len(interim_lists)):
            same_indexed_nums.append (interim_lists[j][i] - interim_lists[j][i-1])
        
        list_n_diff = list_n[i] - list_n[i-1]
        #print(same_indexed_nums)
        
        if is_constant(same_indexed_nums, list_n_diff, n):
            incremental_coutner += 1
            is_last_one_incremental = True
        elif is_linear(same_indexed_nums, list_n_diff, n):
            linear_counter += 1
            is_last_one_incremental = False
        
        # if not is_constant(same_indexed_nums, list_n_diff, n) and not is_linear(same_indexed_nums, list_n_diff, n): 
        #     print("Barf: Verification Failed: neither incremental nor linear")
        #     sys.exit(1)
        same_indexed_nums = []
    return incremental_coutner, linear_counter, is_last_one_incremental

# This function will calculated the starting number of the predicted list
def func_predict_n_start(n, interim_firsts):
    global list_n_start

    num = interim_firsts[1]
    incremental = interim_firsts[1] - interim_firsts[0]
    for index, rd in enumerate(interim_firsts):
        if(index <= 1):
            continue
        if (interim_firsts[index] - num) != incremental:
            print("Barf: Incremental is not linear")
            sys.exit(1)
        num = interim_firsts[index]
    
    list_n_start = interim_firsts[0] + incremental*(n-1)

# This is the main funcition that is responsible to generate the predicted list
# Input: 3 lists in order of loop bound smaller to upper like 2 to 4 lists, and n to predict for n loop bounds
# output: Dialated reuse distance list prediction analyzing from other 3 lists
def generate_n_list(lists, n):
    global list_n, list_n_start, list_n_count
    # print("-->")
    # print(lists)
    init()
    list1 = lists[0]
    list2 = lists[1]
    list3 = lists[2]
    init_updated_lists(list1, list2, list3)
    predict_n_list_size(n)
    
    # print(f'Number of Items in {n}th List: {list_n_count}')

    interim_lists = []
    interim_lists.append(list_1_updated)
    interim_lists.append(list_2_updated)
    interim_lists.append(list_3_updated)

    interim_firsts = []
    interim_firsts.append(list_1_start)
    interim_firsts.append(list_2_start)
    interim_firsts.append(list_3_start)
        

    # print(interim_lists)

    func_predict_n_start(n, interim_firsts)


    # print(f'List starts with: {list_n_start}')

    predict_list_from_neighbour(list_n_count, list_n_start, interim_lists, n)
    # print(list_n)

    incremental_changes, linear_chnages, is_last_one_incremental = verify_list_from_own_list_conn(list_n_count, list_n_start, interim_lists, n)

    if incremental_changes > linear_chnages and is_last_one_incremental: 
        fillout_rest_incremental(list_n_count, list_n)
    elif linear_chnages > incremental_changes and not is_last_one_incremental:
        fillout_rest_linear(list_n_count, list_n)
    # else:
    #     print("Step yet undecided")

    # print(list_n)
    finalize_list(list_n, list_n_start)
    # print(list_n)

    return list_n

def set_common_numbers(list1, list2, list3, list_n, n):
    for i in range(0, len(list1)):
        diff = list2[i] - list1[i]
        base = list1[i]
        if (base + diff * 2) == list3[i]:
            list_n[i] =  base + diff * (n-1)
        diff = list2[len(list2) -1 - i] - list1[len(list1) -1 - i]
        base = list1[len(list1) -1 - i]

        if (base + diff * 2) == list3[len(list3) -1 - i]:
            list_n[len(list_n) -1 - i] =  base + diff * (n-1)
    
    # print(list_n)
    return list_n

def fill_up_rest_follow_list_3(list_n, list3, n):
    diff = -1
    base = -1
    starting_ind = -1
    for index, value in enumerate(list_n):
        if value == -1:
            base = list_n[index-1]
            diff = list3[index] - list3[index-1]
            starting_ind = index
            break
    multipy_fact = 1
    for i in range (starting_ind, len(list_n)):
        if list_n[i] == -1:
            list_n[i] = base + diff * multipy_fact
        multipy_fact += 1
    
    return list_n

def generate_dynamic_rd_count_list(unique_rds_count, n):
    list1 = unique_rds_count[0]
    list2 = unique_rds_count[1]
    list3 = unique_rds_count[2]
    list_n_size = -1

    diff = len(list2) - len(list1)
    if len(list3) == len(list1) + 2 * diff:
        list_n_size = len(list1) + (n-1) * diff
    if list_n_size == -1:
        print("Barf: List sizes has no relation")
        sys.exit(1)
    list_n= [-1 for _ in range(list_n_size)]

    list_n = set_common_numbers(list1, list2, list3, list_n, n)
    list_n = fill_up_rest_follow_list_3(list_n, list3, n)
    return list_n



