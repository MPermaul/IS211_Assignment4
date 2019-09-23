import random
import time


def insertion_sort(a_list):
    """
    Function that takes in a list and sorts it using insertion sorting.
    :type a_list: object
    :param a_list: A list containing shuffled values.
    :return: total: The time it took for the function to sort the list.
    """
    # variable that stores the time of when function starts processing
    start = time.time()

    # loop to process through the list by index
    for index in range(1, len(a_list)):
        # set current value to the value at index position
        current_value = a_list[index]
        position = index

        # loop to process the sort
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
            a_list[position] = current_value

    # variable to store time of when function ends and total time
    end = time.time()
    total = end - start

    return total


def shell_sort(a_list):
    """
    Function that takes in a list and sorts it using shell sorting.
    :param a_list: A list containing shuffled values.
    :return: total: The time it took for the function to sort the list.
    """
    # variable that stores the time of when function starts
    start = time.time()

    # variable to store midpoint value for a sublist
    midpoint = len(a_list) // 2

    # loop to process the sorting when sublist count is greater than zero
    while midpoint > 0:
        # loop through list up to the midpoint index
        for index in range(midpoint):
            for i in range(index + midpoint, len(a_list), midpoint):
                current_value = a_list[i]
                position = i
                while position >= midpoint and a_list[position - midpoint] > current_value:
                    a_list[position] = a_list[position - midpoint]
                    position = position - midpoint

                a_list[position] = current_value

        # set new midpoint
        midpoint = midpoint // 2

    # variable to store time of when function ends and total time
    end = time.time()
    total = end - start

    return total


def python_sort(a_list):
    """
    Function that takes in a list and sorts it using python's built in list sorting.
    :param a_list: A list containing shuffled values.
    :return: total: The time it took for the function to sort the list.
    """
    # variable to store time of when function starts
    start = time.time()

    # sort list using python's built in sort
    a_list.sort()

    # variable to store time of when function ends and total timee
    end = time.time()
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
    # list of the different sizes we need to test and how many times to run checks
    list_sizes = [500, 1000, 10000]
    times_to_check = 100

    # create loop to run for each test size
    for size_value in list_sizes:

        # create variable to start and stop the checks when 100 lists have been checked
        run = True

        # start loop when run is True
        while run:

            # set counter and running sums total to zero
            loop_counter = running_sum1 = running_sum2 = running_sum3 = 0

            while loop_counter < times_to_check:
                # call function to generate random list for size value for first sort
                randlist = generate_random_list(size_value)

                # call function for insert sort, pass in random list and value to search by
                sort_insert = insertion_sort(randlist)

                # increment running sum for insert sort after each pass
                running_sum1 += sort_insert

                # call function to generate random list for size value for second sort
                randlist = generate_random_list(size_value)

                # call function for shell sort, pass in random list and value to search by
                sort_shell = shell_sort(randlist)

                # increment running sum for shell sort after each pass
                running_sum2 += sort_shell

                # call function to generate random list for size value for third sort
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
            print('Insertion Sort took {:10.7f} seconds to run, on average.'.format(running_sum1 / times_to_check))
            print('Shell Sort took {:10.7f} seconds to run, on average.'.format(running_sum2 / times_to_check))
            print('Python Sort took {:10.7f} seconds to run, on average.'.format(running_sum3 / times_to_check))


if __name__ == '__main__':
    main()
