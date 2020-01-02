from Physical_data_population.profile_reader import *
from Physical_data_population.file_readers import *


class DataProcessor(object):

    def __init__(self, technology):
        # I am creating only one type  of DataReader object considering we support only csv now,
        # also we have only one type param input_type
        self.data_reader_ob = AntennaDataReader(technology=technology)
        # We can have another data reader object if planner and SD are of different type
        # self.data_planner_object = self.data_reader_ob.read_planner_file()

    def update_sd_by_planner_step1(self, input_planner_file_path, input_sd_file_path, input_lte_carrier_path,
                                   input_sgi_file_path, profile_root_path_p):
        sd_ob_out = {}
        n = 0
        # travers through planner file
        planner_object = self.data_reader_ob.read_planner_file(input_planner_file_path)
        sd_object = self.data_reader_ob.read_sd_antennas_file(input_sd_file_path)
        lte_carrier_ob = self.data_reader_ob.read_lte_carrier(input_lte_carrier_path)
        sgi_file_ob = self.data_reader_ob.read_gsi_file(input_sgi_file_path)
        # print(sd_object)
        # Here the planner_object and sd_object are dictionary
        profile_root_path = profile_root_path_p
        profile_reader = ProfileReader(profile_root_path)
        antenna_model_vs_profile_map = profile_reader.create_antenna_model_vs_profile_map()
        print("antenna_model_vs_profile_map from profile directory")
        # print(antenna_model_vs_profile_map)
        for sd_rnc_sector_key, sd_input_row in sd_object.items():
            # take a key from SD-ob
            try:
                # search for the key at planner-ob
                matching_planner_input = planner_object[sd_rnc_sector_key]
            except KeyError:
                print("Key {} not found into Planner ".format(sd_rnc_sector_key))
                # TODO need to add lookup with lte_carrier and SGI-file
                try:
                    lte_carrier_input = lte_carrier_ob[sd_rnc_sector_key]
                    temp_l = str(lte_carrier_input['Sector Carrier Name']).split('-')
                    mcc_mnc_sector_carrier_key = '{0}-{1}-{2}-{3}'.format(lte_carrier_input['MCC'], lte_carrier_input['MNC'], temp_l[1], temp_l[2])
                except KeyError:
                    print("Key {} not even found into lte_carrier, so not updating physical data for this sector".format(sd_rnc_sector_key))
                    sd_ob_out[n] = sd_input_row
                    n += 1
                else:
                    print("Key {} was FOUND into lte_carrier".format(sd_rnc_sector_key))
                    print("Key for next level CGI file lookup is {}".format(mcc_mnc_sector_carrier_key))
                    try:
                        matching_cgi_data_input = sgi_file_ob[mcc_mnc_sector_carrier_key]
                    except KeyError:
                        print("Key {} was not found into CGI file".format(mcc_mnc_sector_carrier_key))
                    else:
                        print("Key {} was FOUND into CGI file".format(mcc_mnc_sector_carrier_key))
                        print("matching_cgi_data_input is {}".format(matching_cgi_data_input))
                        sd_input_row[self.data_reader_ob.SD_fields_need_to_update[2]] = matching_cgi_data_input[self.data_reader_ob.cgi_file_fields_required[2]]
                        sd_input_row[self.data_reader_ob.SD_fields_need_to_update[3]] = matching_cgi_data_input[self.data_reader_ob.cgi_file_fields_required[3]]
                        sd_input_row[self.data_reader_ob.SD_fields_need_to_update[4]] = matching_cgi_data_input[self.data_reader_ob.cgi_file_fields_required[4]]
                        sd_input_row[self.data_reader_ob.SD_fields_need_to_update[5]] = matching_cgi_data_input[self.data_reader_ob.cgi_file_fields_required[5]]
                        sd_input_row[self.data_reader_ob.SD_fields_need_to_update[6]] = matching_cgi_data_input[self.data_reader_ob.cgi_file_fields_required[6]]
                        sd_input_row[self.data_reader_ob.SD_fields_need_to_update[7]] = matching_cgi_data_input[self.data_reader_ob.cgi_file_fields_required[7]]
                        sd_input_row[self.data_reader_ob.SD_fields_need_to_update[8]] = matching_cgi_data_input[self.data_reader_ob.cgi_file_fields_required[8]]
                        print("matching_cgi_row = {}".format(matching_cgi_data_input))
                        print("antenna-model field name from cgi_reqired_fields = {}".format(self.data_reader_ob.cgi_file_fields_required[9]))
                        antenna_model = matching_cgi_data_input[self.data_reader_ob.cgi_file_fields_required[9]]
                        antenna_e_tilt = matching_cgi_data_input[self.data_reader_ob.cgi_file_fields_required[10]]
                        band = matching_cgi_data_input[self.data_reader_ob.cgi_file_fields_required[11]]
                        antenna_model_antenna_e_tilt_key = "{}/{}/{}".format(antenna_model, antenna_e_tilt, band)
                        try:
                            antenna_model_profile = antenna_model_vs_profile_map[antenna_model_antenna_e_tilt_key]
                        except KeyError:
                            print("Profile {} was not found into source of profiles files".format(antenna_model_antenna_e_tilt_key))
                        else:
                            sd_input_row[self.data_reader_ob.SD_fields_need_to_update[9]] = antenna_model_profile
                            sd_ob_out[n] = sd_input_row
                            n += 1
            else:
                # Now I have corresponding records from planner and SD, they are OrderDict object
                planner_input_row = matching_planner_input
                # print(type(planner_input_row))
                # print("planner_input_row = {}".format(planner_input_row))
                # print(type(sd_input_row))
                # print("sd_input_row = {}".format(sd_input_row))
                # print("*********************")
                sd_input_row[self.data_reader_ob.SD_fields_need_to_update[2]] = planner_input_row[self.data_reader_ob.planner_fields_required[2]]
                sd_input_row[self.data_reader_ob.SD_fields_need_to_update[3]] = planner_input_row[self.data_reader_ob.planner_fields_required[3]]
                sd_input_row[self.data_reader_ob.SD_fields_need_to_update[4]] = planner_input_row[self.data_reader_ob.planner_fields_required[4]]
                sd_input_row[self.data_reader_ob.SD_fields_need_to_update[5]] = planner_input_row[self.data_reader_ob.planner_fields_required[5]]
                sd_input_row[self.data_reader_ob.SD_fields_need_to_update[6]] = planner_input_row[self.data_reader_ob.planner_fields_required[6]]
                sd_input_row[self.data_reader_ob.SD_fields_need_to_update[7]] = planner_input_row[self.data_reader_ob.planner_fields_required[7]]
                sd_input_row[self.data_reader_ob.SD_fields_need_to_update[8]] = planner_input_row[self.data_reader_ob.planner_fields_required[8]]
                # print("sd_input_row_updated = {}".format(sd_input_row))
                # We populate antenna/profile at antenna-Model field
                antenna_model = planner_input_row[self.data_reader_ob.planner_fields_required[9]]
                antenna_e_tilt = planner_input_row[self.data_reader_ob.planner_fields_required[10]]
                band = planner_input_row[self.data_reader_ob.planner_fields_required[11]]
                antenna_model_antenna_e_tilt_key = "{}/{}/{}".format(antenna_model, antenna_e_tilt, band)
                try:
                    antenna_model_profile = antenna_model_vs_profile_map[antenna_model_antenna_e_tilt_key]
                except KeyError:
                    print("Profile {} was not found into source of profiles files".format(antenna_model_antenna_e_tilt_key))
                else:
                    sd_input_row[self.data_reader_ob.SD_fields_need_to_update[9]] = antenna_model_profile
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
        print("output file name is {}".format(out_put_file))
        with open(out_put_file, 'w') as out_a:
            pass

        with open(out_put_file, 'a',
                  newline='') as out:
            # Create an writer object for the file
            dict_writers = csv.DictWriter(f=out, fieldnames=out_csv_fields, delimiter='\t')
            dict_writers.writeheader()
            for row in temp_out_dict.values():
                dict_writers.writerow(row)

