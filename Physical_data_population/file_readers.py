import csv


lte_carrier = \
    "D:\\D_drive_BACKUP\\Study\\PycharmProjects\\PhysicalDataPopulation\\Input_data_deep\\New\\lte-carriers.txt"


class AntennaDataReader(object):

    def __init__(self, input_type, input_delimiter='\t'):
        self.input_file_type = input_type
        self.input_file_dilimiter = input_delimiter

    def __validate_fields(self, csv_sd_planner_path):
        SD_fields_used_to_create_key = ['RNC Id', 'Sector Name']
        SD_fields_need_to_update = ['NodeB Longitude', 'NodeB Latitude', 'Antenna Longitude', 'Antenna Latitude',
                                    'Height', 'Mechanical DownTilt', 'Azimuth']
        planner_fields_to_get_profile = ['Antenna Model', 'Antenna Tilt-Electrical']
        #TODO : Need validate planner fields -> planner_fields_to_get_profile
        SD_fields_need_to_update.extend(SD_fields_used_to_create_key)
        if self.input_file_type == 'csv':
            with open(csv_sd_planner_path, 'r') as sd_object:
                top_row = sd_object.readline().split(self.input_file_dilimiter)
                # we cant use sd_object.readline() to read the top line again, as it has iterate over already
                print("Fields name of {} are {}".format(csv_sd_planner_path, top_row))
                for field in SD_fields_need_to_update:
                    if field in top_row:
                        pass
                    else:
                        print("Following fields should be into the input SD, and planner .csv files = {}".format(
                            SD_fields_need_to_update))
                        raise ValueError("Field name {} not present into {}".format(field, csv_sd_planner_path))
        else:
            raise NotImplementedError("Only csv format supported")

    def __read_csv_sd(self, csv_sd_path):
        """
        read planner file and return a dictionary having RNC-ID and Sector-name as key for each row of the input csv
        :param csv_sd_path:
        :param separator:
        :return:
        """
        sd_dict_out = {}
        with open(csv_sd_path, mode='r', encoding='utf-8') as sd_ob:
            # sd_dict = csv.DictReader(sd_ob, delimiter='\t')
            sd_dict = csv.DictReader(sd_ob, delimiter=self.input_file_dilimiter)
            for row in sd_dict:
                rnc_id_sector_key = "{}-{}".format(row['RNC Id'], row['Sector Name'])
                sd_dict_out[rnc_id_sector_key] = row
            return sd_dict_out

    def __read_csv_planner(self, csv_planner_path):
        """
        read planner file and return a dictionary having RNC-ID and Sector-name as key for each row of the input csv
        :param csv_planner_path:
        :param separator:
        :return:
        """
        planner_dict_out = {}
        try:
            with open(csv_planner_path, mode='r') as sd_ob:
                #, encoding='utf-8'
                # sd_dict = csv.DictReader(sd_ob, delimiter='\t')
                sd_dict = csv.DictReader(sd_ob, delimiter=self.input_file_dilimiter)
                for row in sd_dict:
                    rnc_id_sector_key = "{}-{}".format(row['RNC Id'], row['Sector Name'])
                    # Insert data into dict, having rnc_id_sector_key as key for each top level dict item
                    planner_dict_out[rnc_id_sector_key] = row
                return planner_dict_out
        except UnicodeDecodeError:
            with open(csv_planner_path, mode='r', encoding='utf-8') as sd_ob:
                sd_dict = csv.DictReader(sd_ob, delimiter=self.input_file_dilimiter)
                for row in sd_dict:
                    rnc_id_sector_key = "{}-{}".format(row['RNC Id'], row['Sector Name'])
                    # Insert data into dict, having rnc_id_sector_key as key for each top level dict item
                    planner_dict_out[rnc_id_sector_key] = row
                return planner_dict_out

    def read_sd_antennas_file(self, sd_file_path):
        if self.input_file_type == 'csv':
            self.__validate_fields(sd_file_path)
            sd_dict_out = self.__read_csv_sd(sd_file_path)
            return sd_dict_out
        else:
            raise NotImplementedError("Only csv format supported")

    def read_planner_file(self, planner_file_path):
        if self.input_file_type == 'csv':
            self.__validate_fields(planner_file_path)
            planner_dict_out = self.__read_csv_planner(planner_file_path)
            return planner_dict_out
        else:
            raise NotImplementedError("Only csv format supported")

    def __read_lte_carrier(self, lte_carrier_path):
        try:
            with open(lte_carrier_path, 'r') as lte_carrier_ob:
                lte_carrier_dict = csv.DictReader(lte_carrier_ob, delimiter=self.input_file_dilimiter)
                pass
        except:
            pass

