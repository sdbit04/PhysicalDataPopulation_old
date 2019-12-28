
"""
Sometime we use use a .py file as module.
However sometime we use a .py file as script.

While running the file as a script, there is no meaning of calculating root of the module path.
While calling the file as module, then need to identify the root of the module.

Argument:
    There are two types of arguments:
        Positional parameter 
        Optional parameter

parser.add_argument("square", type=int, help="display a square of a given number")
parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
args = parser.parse_args()
         
"""
import argparse
from Physical_data_population.read_configuration import *
from Physical_data_population.physical_data_population_sd import *


def run_physical_data_population(config_path_p):
    __config_path = config_path_p
    configuration_ob = read_configuration(__config_path)

    technology = configuration_ob["technology"]
    sd_path = configuration_ob["sd_path_csv"]
    planning_file = configuration_ob["planning_file_csv"]
    lte_carrier_file = configuration_ob["lte_carrier_file_csv"]
    CGI_file = configuration_ob["GSI_file_xlsb"]
    profile_root_path = configuration_ob["profile_root_path"]
    out_put_data_dict_dir = configuration_ob["out_put_data_dict_dir"]


    #
    # sd_path = configuration_ob["sd_path"]
    # planning_file = configuration_ob["planning_file"]
    # out_put_data_dict_dir = configuration_ob["out_put_data_dict_dir"]
    # profile_root_path = configuration_ob["profile_root_path"]
    # input_type = configuration_ob["input_type"]
    # input_delimiter = configuration_ob["input_delimiter"]

    data_processor = DataProcessor(technology=technology)
    out_put_data_dict = data_processor.update_sd_by_planner_step1(planning_file, sd_path, profile_root_path_p=profile_root_path)
    # print(type(out_put_data_dict))
    # print(out_put_data_dict)

    data_writer(out_put_data_dict, out_put_data_dict_dir)


def main_method():
    parser = argparse.ArgumentParser()
    parser.add_argument("config_path", help="Please provide the path of the configuration file")
    args = parser.parse_args()
    config_path_r = args.config_path
    run_physical_data_population(config_path_r)


if __name__ == "__main__":

    main_method()
