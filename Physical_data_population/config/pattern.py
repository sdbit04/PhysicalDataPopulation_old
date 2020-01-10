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

with open('D:\\D_drive_BACKUP\\Study\\PycharmProjects\\PhysicalDataPopulation\\Input_data_deep\\Networks\\N1\\COMPLETE_CONFIGURATION-31102019-063948007 [+0200]6858253598689744_69\\lte-carriers.txt', 'r') as  file_ob:
    all_lines = file_ob.readlines()
    all_lines_iter = iter(all_lines)
    next(all_lines_iter)
    for line in all_lines_iter:
        pass


