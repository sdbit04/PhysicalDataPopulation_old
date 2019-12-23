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
            {"sd_path" :"D:\\Input_data_deep\\Antennas_sd.txt",
            "planning_file" :"D:\\Input_data_deep\\Planning_input.txt",
             "input_type":"csv",
             "input_delimiter" :"\\t",
             "out_put_data_dict_dir" :"D:\\out_dir",
             "profile_root_path": "D:\\Input_data_deep\\Ant Model"
            }""")
            time.sleep(1)
            raise json.decoder.JSONDecodeError
        else:
            try:
                sd_path = config_json_ob["sd_path"]
                planning_file = config_json_ob["planning_file"]
                out_put_data_dict_dir = config_json_ob["out_put_data_dict_dir"]
                profile_root_path = config_json_ob["profile_root_path"]
                print(sd_path)
                print(planning_file)
                print(out_put_data_dict_dir)
                print(profile_root_path)
            except KeyError:
                # raise KeyError("""Please make sure you have "sd_path","planning_file", "out_put_data_dict_dir","profile_root_path" with their value at config_phy.ini file, each key and value should be in " " """)
                print("""Please check config_phy.ini file, make sure you have "sd_path","planning_file", "out_put_data_dict_dir","profile_root_path" with their value, each key and value should be in " ",
                           Example: 
                           {"sd_path" :"D:\\Input_data_deep\\Antennas_sd.txt",
                            "planning_file" :"D:\\Input_data_deep\\Planning_input.txt",
                            "input_type":"csv",
                            "input_delimiter" :"\\t",
                            "out_put_data_dict_dir" :"D:\\out_dir",
                            "profile_root_path": "D:\\Input_data_deep\\Ant Model"
                        }""")
                time.sleep(1)
                raise KeyError
            else:
                return config_json_ob


if __name__ == "__main__":
    config_path = '..\\configuration\\config_phy.ini'
    config_json_ob = read_configuration(config_path)

