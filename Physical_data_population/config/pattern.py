''' Read input from STDIN. Print your output to STDOUT '''


# Use input() to read input from STDIN and use print to write your output to STDOUT

def main(input_nbr_p):
    # Write code here
    input_nbr = input_nbr_p
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    if 1 <= input_nbr <= 26:
        alpha_comb = None
        for index in range(1, input_nbr+1):
            if index == 1:
                alpha_comb = alphabet[0]
                print(' '*(input_nbr-1), end='')
                print(alpha_comb)
            else:
                alpha_comb = "{0} {1} {0}".format(alphabet[index-1], alpha_comb)
                print(" "*(input_nbr - index), end='')
                print(alpha_comb)


# main(5)

l1 = [1,2,3]
print("{}".format(l1))
print(len(l1))

