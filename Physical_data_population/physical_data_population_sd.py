import csv
from Physical_data_population.profile_reader import *
from Physical_data_population.file_readers import *







class DataProcessor(object):

    def __init__(self, input_type, input_delimiter='\t'):
        # I am creating only one type  of DataReader object considering we support only csv now,
        # also we have only one type param input_type
        self.data_reader_ob = AntennaDataReader(input_type, input_delimiter)
        # We can have another data reader object if planner and SD are of different type
        # self.data_planner_object = self.data_reader_ob.read_planner_file()

    def update_sd_by_planner_step1(self, input_planner_file_path, input_sd_file_path, profile_root_path_p):
        sd_ob_out = {}
        n = 0
        # travers through planner file

        planner_object = self.data_reader_ob.read_planner_file(input_planner_file_path)
        sd_object = self.data_reader_ob.read_sd_antennas_file(input_sd_file_path)
        # print(sd_object)
        #Here the planner_object and sd_object are dictonary
        profile_root_path = profile_root_path_p
        profile_reader = ProfileReader(profile_root_path)
        antenna_model_vs_profile_map = profile_reader.create_antenna_model_vs_profile_map()
        print("antenna_model_vs_profile_map from profile directory")
        # print(antenna_model_vs_profile_map)
        for sd_rnc_sector_key, sd_input_row in sd_object.items():
            # take a key from SD-ob
            try:
                # search for the key at planner-ob
                planner_input = planner_object[sd_rnc_sector_key]
            except KeyError:
                print("Key {} not found into Planner ".format(sd_rnc_sector_key))
                sd_ob_out[n] = sd_input_row
                n += 1
            else:
                # Now I have corresponding records from planner and SD, they are OrderDict object
                planner_input_row = planner_input
                # print(type(planner_input_row))
                # print("planner_input_row = {}".format(planner_input_row))
                # print(type(sd_input_row))
                # print("sd_input_row = {}".format(sd_input_row))
                # print("*********************")
                SD_fields_need_to_update = ['NodeB Longitude', 'NodeB Latitude', 'Antenna Longitude',
                                            'Antenna Latitude',
                                            'Height', 'Mechanical DownTilt', 'Azimuth']
                sd_input_row['NodeB Longitude'] = planner_input_row['NodeB Longitude']
                sd_input_row['NodeB Latitude'] = planner_input_row['NodeB Latitude']
                sd_input_row['Antenna Longitude'] = planner_input_row['Antenna Longitude']
                sd_input_row['Antenna Latitude'] = planner_input_row['Antenna Latitude']
                sd_input_row['Height'] = planner_input_row['Height']
                sd_input_row['Mechanical DownTilt'] = planner_input_row['Mechanical DownTilt']
                sd_input_row['Azimuth'] = planner_input_row['Azimuth']
                # print("sd_input_row_updated = {}".format(sd_input_row))
                # We populate antenna/profile at antenna-Model field
                antenna_model = planner_input_row['Antenna Model']
                antenna_e_tilt = planner_input_row['Antenna Tilt-Electrical']
                antenna_model_antenna_e_tilt_key = "{}/{}".format(antenna_model, antenna_e_tilt)
                try:
                    antenna_model_profile = antenna_model_vs_profile_map[antenna_model_antenna_e_tilt_key]
                except KeyError:
                    print("Profile {} was not found into source of profiles files".format(antenna_model_antenna_e_tilt_key))
                else:
                    sd_input_row['Antenna Model'] = antenna_model_profile
                    sd_ob_out[n] = sd_input_row
                    n += 1
        return sd_ob_out


def data_writer(temp_out_dict, out_put_file_p):
    # temp_out_dict = update_sd_by_planner_step1(planner_ob, sd_ob)
    import time
    import datetime
    try:
        sample_out = temp_out_dict[0]
    except KeyError:
        print("No match between Planner and antentnnas.txt parsed from SD")
        return
    else:
        out_csv_fields = list(sample_out.keys())
        print("The list of fields into the output antennas.txt file{}".format(out_csv_fields))
        output_file = "antennas{}.txt".format(str(datetime.datetime.utcnow()).split(' ')[0])
        out_put_file = os.path.join(out_put_file_p, output_file)
        with open(out_put_file, 'w') as out_a:
            pass

        with open(out_put_file, 'a',
                  newline='') as out:
            # Create an writer object for the file
            dict_writers = csv.DictWriter(f=out, fieldnames=out_csv_fields, delimiter='\t')
            dict_writers.writeheader()
            for row in temp_out_dict.values():
                dict_writers.writerow(row)

