import os
import shutil

# base_directory = "D:\\D_drive_BACKUP\\Study\\PycharmProjects\\PhysicalDataPopulation\\Input_data_deep\\Networks"
# input_directory_list = ['N1', 'N2', 'N3']

base_directory = "\\\\DEEPMLT01\\Mentor\System\\data\\networks"
input_directory_list = ['ZTE_LTE_KOL_01-4490265003385246_98', 'ZTE_LTE_KOL_06-5883175451772760_68']


def filter_dir(dir_name: str):
    if dir_name.split("-")[0] == 'COMPLETE_CONFIGURATION':
        return True
    else:
        return False


def find_recent_complete_conf_for_each_ne(network_base_directory, NE_directory_list):
    network_dir_compl_conf = {}  # We will populate this dict and return it.
    for directory in NE_directory_list:
        abs_network_directory = os.path.join(network_base_directory, directory)
        compl_conf_dirs_list = filter(filter_dir, os.listdir(abs_network_directory))
        # recent_compl_dir = compl_conf_dirs_list.__next__()
        recent_date_time: int = 1112017064015000
        recent_compl_dir_under_this_NE = None
        for compl_dir in compl_conf_dirs_list:  # this loop is running as nest of each network-NE directory.
            compl_dir_numeric_part = compl_dir.split("[")[0].strip(" ").split("-")
            date_n_time_part = int("{}{}".format(compl_dir_numeric_part[1].lstrip("0"), compl_dir_numeric_part[2]))
            if date_n_time_part > recent_date_time:
                recent_date_time = date_n_time_part
                recent_compl_dir_under_this_NE = compl_dir

        network_dir_compl_conf[abs_network_directory] = recent_compl_dir_under_this_NE
    return network_dir_compl_conf


def get_list_of_antennas_and_lte_carriers_txt_files_to_be_stitched(network_base_directory, NE_directory_list):
    network_dir_compl_conf = find_recent_complete_conf_for_each_ne(network_base_directory, NE_directory_list)
    antennas_txt_list = []
    lte_carriers_list = []
    for abs_ne, compl_dir in network_dir_compl_conf.items():
        abs_path_compl_dir = os.path.join(abs_ne, compl_dir)
        abs_path_antennas_txt = os.path.join(abs_path_compl_dir, 'antennas.txt')
        abs_path_lte_carrier_txt = os.path.join(abs_path_compl_dir, 'lte-carriers.txt')
        antennas_txt_list.append(abs_path_antennas_txt)
        lte_carriers_list.append(abs_path_lte_carrier_txt)
    return antennas_txt_list, lte_carriers_list


class FileStitcher(object):

    def __init__(self, network_base_directory, NE_directory_list):
        self.network_base_directory = network_base_directory
        self.NE_directory_list = NE_directory_list
        self.antennas_txt_files_list, self.lte_carriers_files_list = get_list_of_antennas_and_lte_carriers_txt_files_to_be_stitched(self.network_base_directory, self.NE_directory_list)
        self.current_dir = os.path.abspath(os.path.dirname(__file__))
        self.temp_dir = os.path.join(self.current_dir, "temp_files")

    def stitch_antennas_txt(self):
        # print(self.antennas_txt_files_list)
        print(self.temp_dir)
        consolidated_antennas_txt_temp = "{}\\{}".format(self.temp_dir, "antennas_temp.txt")
        consolidated_antennas_txt = "{}\\{}".format(self.temp_dir, "antennas.txt")
        # Directly copy the first file at temp_file directory
        shutil.copy(self.antennas_txt_files_list[0], consolidated_antennas_txt_temp)
        for antennas_txt_index in range(1, len(self.antennas_txt_files_list)):
            with open(consolidated_antennas_txt_temp, 'a') as temp_antennas_file_ob:
                with open(self.antennas_txt_files_list[antennas_txt_index], 'r') as one_of_antennas_txt_ob:
                    all_lines = one_of_antennas_txt_ob.readlines()
                    number_of_lines = len(all_lines)
                    for line_nbr in range(1, number_of_lines):
                        temp_antennas_file_ob.write(all_lines[line_nbr])
        shutil.move(consolidated_antennas_txt_temp, consolidated_antennas_txt)

    def stitch_lte_carriers_txt(self):
        # print(self.lte_carriers_files_list)
        print(self.temp_dir)
        consolidated_lte_carrier_txt_temp = "{}\\{}".format(self.temp_dir, "lte_carrier_temp.txt")
        consolidated_lte_carrier_txt = "{}\\{}".format(self.temp_dir, "lte_carriers.txt")
        # Directly copy the first file at temp_file directory
        shutil.copy(self.lte_carriers_files_list[0], consolidated_lte_carrier_txt_temp)
        for lte_carrier_txt_index in range(1, len(self.lte_carriers_files_list)):
            with open(consolidated_lte_carrier_txt_temp, 'a') as temp_antennas_file_ob:
                with open(self.lte_carriers_files_list[lte_carrier_txt_index], 'r') as one_of_lte_carrier_txt_ob:
                    all_lines = one_of_lte_carrier_txt_ob.readlines()
                    number_of_lines = len(all_lines)
                    for line_nbr in range(1, number_of_lines):
                        temp_antennas_file_ob.write(all_lines[line_nbr])
        shutil.move(consolidated_lte_carrier_txt_temp, consolidated_lte_carrier_txt)


# if __name__ == "__main__":
#     file_stitcher = FileStitcher(base_directory, input_directory_list)
#     file_stitcher.stitch_antennas_txt()
#     file_stitcher.stitch_lte_carriers_txt()

