import json
import time


def read_configuration(config_path_p):
    config_path = config_path_p
    with open(config_path, 'r') as config_ob:
        try:
            config_json_ob = json.load(config_ob)
        except json.decoder.JSONDecodeError:
            # raise json.decoder.JSONDecodeError("""Please make sure you have "sd_path","planning_file", "out_put_data_dict_dir","profile_root_path" with their value at config_phy.ini file, each key and value should be in " " """)
            print("""Please check config_phy.ini file, make sure you have "sd_path","planning_file", "out_put_data_dict_dir","profile_root_path" with their value, each key and value should be in " ",
            Example: 
            {"technology":"UMTS"
            "sd_path_csv" :"D:\\Input_data_deep\\Antennas_sd.txt",
            "planning_file_csv" :"D:\\Input_data_deep\\Planning_input.txt",
            "lte_carrier_file_csv":"D:\\Input_data_deep\\lte_carrier.txt",
            "GSI_file_xlsb" :"D:\\Input_data_deep\\SGI_input.xlsb",
            "out_put_data_dict_dir" :"D:\\out_dir",
            "profile_root_path": "D:\\Input_data_deep\\Ant Model"
            }""")
            time.sleep(1)
            raise json.decoder.JSONDecodeError
        else:
            try:
                technology = config_json_ob["technology"]
                sd_path = config_json_ob["sd_path_csv"]
                planning_file = config_json_ob["planning_file_csv"]
                lte_carrier_file = config_json_ob["lte_carrier_file_csv"]
                CGI_file = config_json_ob["GSI_file_xlsb"]
                profile_root_path = config_json_ob["profile_root_path"]
                out_put_data_dict_dir = config_json_ob["out_put_data_dict_dir"]

                print(technology)
                print(sd_path)
                print(planning_file)
                print(lte_carrier_file)
                print(CGI_file)
                print(out_put_data_dict_dir)
                print(profile_root_path)
            except KeyError:
                # raise KeyError("""Please make sure you have "sd_path","planning_file", "out_put_data_dict_dir","profile_root_path" with their value at config_phy.ini file, each key and value should be in " " """)
                print("""Please check config_phy.ini file, make sure you have "sd_path","planning_file", "out_put_data_dict_dir","profile_root_path" with their value, each key and value should be in " ",
                           Example: 
                           {"technology":"UMTS"
                            "sd_path_csv" :"D:\\Input_data_deep\\Antennas_sd.txt",
                            "planning_file_csv" :"D:\\Input_data_deep\\Planning_input.txt",
                            "lte_carrier_file_csv":"D:\\Input_data_deep\\lte_carrier.txt",
                            "GSI_file_xlsb" :"D:\\Input_data_deep\\SGI_input.xlsb",
                            "out_put_data_dict_dir" :"D:\\out_dir",
                            "profile_root_path": "D:\\Input_data_deep\\Ant Model"
                        }""")
                time.sleep(1)
                raise KeyError
            else:
                return config_json_ob


if __name__ == "__main__":
    config_path = 'config\\config_phy.ini'
    config_json_ob = read_configuration(config_path)

