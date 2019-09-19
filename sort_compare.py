import random
import time


def insertion_sort(a_list):
    """
    Function that takes in a list and sorts it using insertion sorting.
    :param a_list: A list containing shuffled values.
    :return: total: The time it took for the function to sort the list.
    """
    # var that stores the time of when function starts
    start = time.time()

    # loop to process through the list by index
    for index in range(1, len(a_list)):
        # set current value to the value at position index
        current_value = a_list[index]
        position = index

        # loop to process the sort
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
            a_list[position] = current_value

    # var to store time of when function ends
    end = time.time()

    # calculate total time function took to sort
    total = end - start

    return total


def shell_sort(a_list):
    """
    Function that takes in a list and sorts it using shell sorting.
    :param a_list: A list containing shuffled values.
    :return: total: The time it took for the function to sort the list.
    """
    # var that stores the time of when function starts
    start = time.time()

    # var to store the sublist
    sublist_count = len(a_list) // 2

    # loop to process the sort
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        sublist_count = sublist_count // 2

    # var to store time of when function ends
    end = time.time()

    # calculate total time function took to sort
    total = end - start

    return total


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value


def python_sort(a_list):
    """
    Function that takes in a list and sorts it using python's built in list sorting.
    :param a_list: A list containing shuffled values.
    :return: total: The time it took for the function to sort the list.
    """
    # var to store time of when function starts
    start = time.time()

    # sort list
    a_list.sort()

    # var to store time of when function ends
    end = time.time()

    # calculate total time function took to sort
    total = end - start

    return total


def generate_random_list(size):
    """Generates a list of integers in random order, based on the size passed in.
    :params: size: Number of elements in the list
    :returns: randlist: A list with size elements in random order
    """

    # create variable and store with list in range of size passed in
    randlist = list(range(0, size))

    # shuffle the list to randomize it
    random.shuffle(randlist)

    return randlist


def main():
    # list of the different sizes we need to test
    list_sizes = [500, 1000, 10000]

    # create loop to run for each test size
    for size_value in list_sizes:

        # create variable to start and stop the checks when 100 lists have been checked
        run = True

        # start loop when run is True
        while run:

            # set counter and running sums total to zero
            loop_counter = running_sum1 = running_sum2 = running_sum3 = 0

            while loop_counter < 100:
                # call function to generate random list for size value
                randlist = generate_random_list(size_value)

                # call function for insert sort, pass in random list and value to search by
                sort_insert = insertion_sort(randlist)

                # increment running sum for insert sort after each pass
                running_sum1 += sort_insert

                # call function to generate random list for size value
                randlist = generate_random_list(size_value)

                # call function for shell sort, pass in random list and value to search by
                sort_shell = shell_sort(randlist)

                # increment running sum for shell sort after each pass
                running_sum2 += sort_shell

                # call function to generate random list for size value
                randlist = generate_random_list(size_value)

                # call function for python sort, pass in random list and value to search by
                sort_python = python_sort(randlist)

                # increment running sum for python sort after each pass
                running_sum3 += sort_python

                # increment counter
                loop_counter += 1

            # stop loop when processing of 100 lists is done
            run = False

            # print message with average time to run the 100 lists
            print('\nStats Running with List of {} Items:'.format(size_value))
            print('Insertion Sort took {:10.7f} seconds to run, on average.'.format(running_sum1 / 100))
            print('\nStats Running with List of {} Items:'.format(size_value))
            print('Shell Sort took {:10.7f} seconds to run, on average.'.format(running_sum2 / 100))
            print('\nStats Running with List of {} Items:'.format(size_value))
            print('Python Sort took {:10.7f} seconds to run, on average.'.format(running_sum3 / 100))


if __name__ == '__main__':
    main()


