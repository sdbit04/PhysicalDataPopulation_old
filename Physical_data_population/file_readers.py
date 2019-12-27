import csv

lte_carrier = \
    "D:\\D_drive_BACKUP\\Study\\PycharmProjects\\PhysicalDataPopulation\\Input_data_deep\\New\\lte-carriers.txt"


class AntennaDataReader(object):

    def __init__(self, technology):
        self.technology = technology
        if self.technology.upper() == 'UMTS':
            self.SD_fields_used_to_create_key = ['RNC Id', 'Sector Name']
            self.SD_fields_need_to_update = ['RNC Id', 'Sector Name','NodeB Longitude', 'NodeB Latitude', 'Antenna Longitude', 'Antenna Latitude',
                                    'Height', 'Mechanical DownTilt', 'Azimuth']
            self.planner_fields_required = ['RNC Id', 'Sector Name']
            self.lte_carrier_fields_required = ['RNC', 'Sector Name']

        elif self.technology.upper() == 'LTE':
            self.SD_fields_used_to_create_key = ['RNC Id', 'Sector Name']
            self.SD_fields_need_to_update = ['RNC Id', 'Sector Name','NodeB Longitude', 'NodeB Latitude', 'Antenna Longitude', 'Antenna Latitude',
                                    'Height', 'Mechanical DownTilt', 'Azimuth']
            self.planner_fields_required = []
            self.lte_carrier_fields_required = []
        else:
            raise ("{} technology is not supported ".format(self.technology))

    def __validate_fields(self, csv_sd_planner_path):
        csv_sd_planner_path = csv_sd_planner_path
        if self.technology.upper() == 'UMTS':
            # check if all the fields at SD_fields_need_to_update are into the file
            return True
        elif self.technology.upper() == 'LTE':
            # check if all the fields at SD_fields_need_to_update are into the file
            return True
    #     if self.technology.upper() == 'UMTS':
    #         SD_fields_used_to_create_key = ['RNC Id', 'Sector Name']
    #         SD_fields_need_to_update = ['NodeB Longitude', 'NodeB Latitude', 'Antenna Longitude', 'Antenna Latitude',
    #                                 'Height', 'Mechanical DownTilt', 'Azimuth']
    #         SD_fields_need_to_update.extend(SD_fields_used_to_create_key)
    #     elif self.technology.upper() == 'LTE':
    #         SD_fields_used_to_create_key = ['RNC Id', 'Sector Name']
    #         SD_fields_need_to_update = ['NodeB Longitude', 'NodeB Latitude', 'Antenna Longitude', 'Antenna Latitude',
    #                                     'Height', 'Mechanical DownTilt', 'Azimuth']
    #         SD_fields_need_to_update.extend(SD_fields_used_to_create_key)
    #     else:
    #         raise ("{} is not supported, use LTE, or UMTS ".format(self.technology))
    #
    #     # planner_fields_to_get_profile = ['Antenna Model', 'Antenna Tilt-Electrical']
    #     # TODO : Need validate planner fields -> planner_fields_to_get_profile
    #
    #     if self.input_file_type == 'csv':
    #         with open(csv_sd_planner_path, 'r') as sd_object:
    #             top_row = sd_object.readline().split(self.input_file_dilimiter)
    #             # we cant use sd_object.readline() to read the top line again, as it has iterate over already
    #             print("Fields name of {} are {}".format(csv_sd_planner_path, top_row))
    #             for field in SD_fields_need_to_update:
    #                 if field in top_row:
    #                     pass
    #                 else:
    #                     print("Following fields should be into the input SD, and planner .csv files = {}".format(
    #                         SD_fields_need_to_update))
    #                     raise ValueError("Field name {} not present into {}".format(field, csv_sd_planner_path))
    #     else:
    #         raise NotImplementedError("Only csv format supported")

    def __read_csv_sd(self, csv_sd_path):
        """
        read planner file and return a dictionary having RNC-ID and Sector-name as key for each row of the input csv
        :param csv_sd_path:
        :param separator:
        :return:
        """
        # TODO at present I have only UMTS data
        sd_dict_out = {}
        with open(csv_sd_path, mode='r', encoding='utf-8') as sd_ob:
            # As we know the delimiter for parsed SD antennas.txt is tab, So I made it hard coded
            sd_dict = csv.DictReader(sd_ob, delimiter='\t')
            for row in sd_dict:
                rnc_id_sector_key = "{}-{}".format(row[self.SD_fields_used_to_create_key[0]],
                                                   row[self.SD_fields_used_to_create_key[1]])
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
                # , encoding='utf-8'
                # As we convert the planner.xlsx file into a tab delimited file, So I made it hard coded in next line
                sd_dict = csv.DictReader(sd_ob, delimiter='\t')
                for row in sd_dict:
                    rnc_id_sector_key = "{}-{}".format(row[self.planner_fields_required[0]],
                                                       row[self.planner_fields_required[1]])
                    # Insert data into dict, having rnc_id_sector_key as key for each top level dict item
                    planner_dict_out[rnc_id_sector_key] = row
                return planner_dict_out
        except UnicodeDecodeError:
            with open(csv_planner_path, mode='r', encoding='utf-8') as sd_ob:
                sd_dict = csv.DictReader(sd_ob, delimiter='\t')
                for row in sd_dict:
                    rnc_id_sector_key = "{}-{}".format(row[self.planner_fields_required[0]],
                                                       row[self.planner_fields_required[1]])
                    # Insert data into dict, having rnc_id_sector_key as key for each top level dict item
                    planner_dict_out[rnc_id_sector_key] = row
                return planner_dict_out

    def read_sd_antennas_file(self, sd_file_path):
        if self.__validate_fields(sd_file_path):
            sd_dict_out = self.__read_csv_sd(sd_file_path)
            return sd_dict_out
        else:
            raise NotImplementedError("Input file was not validated")

    def read_planner_file(self, planner_file_path):
        if self.__validate_fields(planner_file_path):
            planner_dict_out = self.__read_csv_planner(planner_file_path)
            return planner_dict_out
        else:
            raise NotImplementedError("Input file was not validated")

    def read_lte_carrier(self, lte_carrier_path):
        lte_carrier_dict_out = {}
        try:
            with open(lte_carrier_path, 'r') as lte_carrier_ob:
                lte_carrier_dict = csv.DictReader(lte_carrier_ob, delimiter='\t')
                # print(lte_carrier_dict.__next__())
                for row in lte_carrier_dict:
                    lte_carrier_rncid_sector_key = "{}-{}".format(row[self.lte_carrier_fields_required[0]],
                                                                  row[self.lte_carrier_fields_required[1]])
                    # TODO In the line below, I have assigned whole row to the key, I can only assign required fields
                    lte_carrier_dict_out[lte_carrier_rncid_sector_key] = row
            return lte_carrier_dict_out
        except:
            raise Exception("Lte_carrier file was not readable")


if __name__ == "__main__":
    reader = AntennaDataReader(technology='UMTS')
    lte_carrier_dict_out_r = reader.read_lte_carrier(lte_carrier_path=lte_carrier)
    print(lte_carrier_dict_out_r)
