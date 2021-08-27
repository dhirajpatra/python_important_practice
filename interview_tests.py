# remove adjacent duplicate chars
def reduce_string(string):
    try:

        # make the string lower case
        string = string.lower()
        l = len(string)
        # no need to process if the string len is 0 or 1
        if l == 0 or l == 1:
            return string

        # make it a list
        ls = list(string)
        matched_pairs = []
        previous = None
        # loop thorugh all chars of string as list
        for i in range(0, l):
            if ls[i] == previous:
                # adjacent duplicate or pair
                matched_pairs.append(ls[(i-1)] + ls[i])
            else:
                previous = ls[i]

        # now need to remove duplicate pair chars from string
        for i in matched_pairs:
            string = string.replace(i, '')

        # if still
        if len(matched_pairs) > 0:
            string = reduce_string(string)

    except:
        return -1

    return string


# swap left right of middle number and sum all digits of number
def swap_sum(num):
    try:
        l = len(str(num))
        # check length and odd or not
        if l < 3 or l % 2 == 0:
            return -1

        # middle number index in list
        middle_index = l // 2
        num_as_list = [int(i) for i in str(num)]

        # swapping
        temp = num_as_list[(middle_index - 1)]
        num_as_list[(middle_index - 1)] = num_as_list[(middle_index + 1)]
        num_as_list[(middle_index + 1)] = temp

        # sum of the all digits of num
        sum_num = sum(num_as_list)
    except:
        return -1

    return sum_num


# how many chocolates can get against total money, price of each chocolate
# discount number of wrappers need for each chocolate
def get_chocolates(money, price, discount):
    if type(money) != int or type(price) != int or type(discount) != int:
        return -1
    elif money < 0 or price < 0 or discount < 0:
        return -1
    elif price > money:
        return 0

    chocolate_first = money // price
    wrappers_discount = chocolate_first // discount
    total_chocolates = chocolate_first + wrappers_discount

    print(chocolate_first)
    print(wrappers_discount)
    print(total_chocolates)
