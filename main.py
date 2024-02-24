def main():

    original_str = 'Python Programming'
    ##################################################
    # Comlete your code here
    ##################################################
    
     # Extract "Python" from original string with index slicing
    sub1 = original_str[:6]

    # Extract "Programming" from original string with index slicing
    sub2 = original_str[7:]

    # Using string concatenation('+'), merge two substrings sub1 and sub2
    merged_str = sub2 + " " + sub1

    print(sub2)
    print(sub1)
    print(merged_str)

    #########################################
    # Do not delete the return statement
    return sub1, sub2, merged_str


if __name__ == '__main__':
    main()
