import random
import time


def sequential_search(a_list, item):
    """
    Function that takes in a shuffled list and item, and checks sequentially if item is in list.
    :param a_list: A list containing randomly shuffled numbers.
    :param item: The value that we are looking for in the list.
    :return: total: The total time it took for the search to run.
    """
    # variables to keep track of when function started processing, the position in the list, and current status
    start = time.time()
    position = 0
    found = False

    # loop through list when position is less than the number of items in list and the status of found is false
    while position < len(a_list) and not found:
        # if the value in the list at index position equals the item, found is True
        if a_list[position] == item:
            found = True
        # increment the position value if item is not found
        else:
            position = position + 1

    # variable to store when function stops processing the list, and total time
    end = time.time()
    total = end - start

    return total


def ordered_sequential_search(a_list, item):
    """
    Function that takes in a ordered list and item and checks sequentially if item is in list.
    :param a_list: A list containing ordered numbers.
    :param item: The value that we are looking for in the list.
    :return: total: The total time it took for the search to run.
    """
    # variables to keep track of when function started processing, the position in the list, current status,
    start = time.time()
    position = 0
    found = False
    stop = False

    # loop through list when position is less than the number of items in list and the status of found and stop is false
    while position < len(a_list) and not found and not stop:
        # if the value in the list at the index position equals the item, found is True
        if a_list[position] == item:
            found = True
        else:
            # if the value in the list at the index position is greater than item, stop equals True
            if a_list[position] > item:
                stop = True
            # increment the position value if item is not found and not stopped
            else:
                position = position + 1

    # variable to store when function stops processing the list and total time
    end = time.time()
    total = end - start

    return total


def binary_search_iterative(a_list, item):
    """
    Function that takes in a list and item, and checks using binary iterative search to see if item is in the list.
    :param a_list: A list containing ordered numbers.
    :param item: The value that we are looking for in the list.
    :return: total: The total time it took for the search to run.
    """
    # variables to keep track of when function started processing, first index, last index, and current status
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False

    # start loop when first index is less than or equal to last index and status is not found
    while first <= last and not found:
        # create a midpoint index value
        midpoint = (first + last) // 2

        # if value at midpoint equals the item, found is set to True
        if a_list[midpoint] == item:
            found = True
        else:
            # if item is less than value at index midpoint, set new last position to 1 less than midpoint
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                # if item is greater than midpoint, set first position to 1 more than midpoint
                first = midpoint + 1

    # variable to store when function stops processing the list and total time
    end = time.time()
    total = end - start

    return total


def binary_search_recursive(a_list, item):
    """
    Function that takes in a list and item, and checks using binary recursive search to see if the item is in the list.
    :param a_list: A list containing ordered numbers.
    :param item: The value that we are looking for in the list.
    :return: time: The total time it took for the search to run.
    """
    # variables to keep track of when function started processing
    start = time.time()

    # if the number of items in list is equal to 0, set end time and return it
    if len(a_list) == 0:
        end = time.time()
        total = end - start
        return total
    else:
        # if number of items in list is greater than 0, set a midpoint index value
        midpoint = len(a_list) // 2

        # if value at midpoint equals item, set end time and return time
        if a_list[midpoint] == item:
            end = time.time()
            total = end - start
            return total
        else:
            # if item is smaller than value at index midpoint,
            # recursively call itself with new parameters, list ending at index midpoint
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                # else call search function with new parameters, list starting at midpoint + 1
                return binary_search_recursive(a_list[midpoint + 1:], item)


def generate_random_list(size):
    """Generates a list of integers in random order, based on the size passed in.
    :params: size: Number of elements in the list
    :returns: randlist: A list with size elements in random order
    """
    # create variable to store a list with range of size passed in
    randlist = list(range(0, size))

    # shuffle the list to randomize it
    random.shuffle(randlist)

    return randlist


def main():
    # variable to store item that we will search for
    valsearch = -1

    # list with the different sizes we need to create
    list_sizes = [500, 1000, 10000]

    # create loop to run each test size
    for size in list_sizes:

        # create variable to start and stop the search after 100 attempts
        run = True

        # start loop when run is True
        while run:

            # set counter and running sums totals for each search method to zero
            counter = 0
            running_sum1 = running_sum2 = running_sum3 = running_sum4 = 0

            # loop the calling of the search functions when counter is less than 100
            while counter < 100:

                # call function to generate random list for size values
                randlist = generate_random_list(size)

                # call function for seq search, pass in random list and value to search by
                seq_search = sequential_search(randlist, valsearch)

                # increment running sum for seq search after each pass
                running_sum1 += seq_search

                # sort list for ordered and binary search functions
                randlist.sort()

                # call function for ord search, pass in sorted list and value to search by
                ord_search = ordered_sequential_search(randlist, valsearch)

                # increment running sum for ordered search after each pass
                running_sum2 += ord_search

                # call function for binary search iterative, pass in sorted list and value to search by
                b_iterative = binary_search_iterative(randlist, valsearch)

                # increment running sum for binary search iterative after each pass
                running_sum3 += b_iterative

                # call function for binary search recursive, pass in sorted list and value to search by
                b_recursive = binary_search_iterative(randlist, valsearch)

                # increment running sum for binary search recursive after each pass
                running_sum4 += b_recursive

                # increment counter
                counter += 1

            # stop loop when processing of 100 lists is done
            run = False

            # print message with average time to run the 100 lists
            print('\nStats Running with List of {} Items:'.format(size))
            print('Sequential Search took {:10.7f} seconds to run, on average.'.format(running_sum1/100))
            print('Ordered Sequential Search took {:10.7f} seconds to run, on average.'.format(running_sum2/100))
            print('Binary Iterative Search took {:10.7f} seconds to run, on average.'.format(running_sum3/100))
            print('Binary Recursive Search took {:10.7f} seconds to run, on average.'.format(running_sum4/100))


if __name__ == '__main__':
    main()
