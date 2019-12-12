import os


class ProfileReader(object):

    def __init__(self, antenna_profile_directory):
        self.profile_root_path = antenna_profile_directory

    def create_antenna_model_vs_profile_map(self):
        antenna_model_vs_profile_map = {}
        antenna_models_list = os.listdir(self.profile_root_path)
        os.chdir(self.profile_root_path)
        # print(os.getcwd())
        for model_dir in antenna_models_list:
            model_dir_abs = os.path.join(self.profile_root_path, model_dir)
            # print(model_dir_abs)
            for profile in os.listdir(model_dir_abs):
                # print(profile)
                profile_path_abs = os.path.join(model_dir_abs, profile)
                antenna_model_profile_combination = "{}/{}".format(model_dir, profile.rstrip(".txt"))
                # print(antenna_model_profile_combination)
                ELECTRICAL_TILT =self.read_profile(profile_path_abs)['ELECTRICAL_TILT']
                antenna_model_eTilt_combination = "{}/{}".format(model_dir, ELECTRICAL_TILT)
                try:
                    value1 = antenna_model_vs_profile_map[antenna_model_eTilt_combination]
                except KeyError:
                    antenna_model_vs_profile_map[antenna_model_eTilt_combination] = antenna_model_profile_combination
                else:
                    print("Key {} is already exist, overwriting by new value".format(antenna_model_eTilt_combination))
                    antenna_model_vs_profile_map[antenna_model_eTilt_combination] = antenna_model_profile_combination

        return antenna_model_vs_profile_map

    def read_profile(self, profile_path_p):
        profile_dict = {}
        profile_path = profile_path_p
        with open(profile_path, 'r', newline='') as profile_ob:
            for line in profile_ob.readlines():
                line_item = line.split(' ')
                # print("{}".format(line_item[0]))
                if line_item[0] == 'ELECTRICAL_TILT':
                    profile_dict[line_item[0]] = line_item[1]
                    return profile_dict


if __name__ == "__main__":
    profile_root_path = r'D:\D_drive_BACKUP\Study\PycharmProjects\PhysicalDataPopulation\Input_data_deep\Ant Model'
    profile_reader = ProfileReader(profile_root_path)
    # profile_reader.create_antenna_model_vs_profile_map()
    antenna_model_vs_profile_map = profile_reader.create_antenna_model_vs_profile_map()

    print(antenna_model_vs_profile_map)







