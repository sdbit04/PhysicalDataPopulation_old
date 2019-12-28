from pyxlsb import *

file_path = "D:\\D_drive_BACKUP\\Study\\PycharmProjects\\PhysicalDataPopulation\\Input_data_deep\\New\\4G GIS Data Kolkata.xlsb"


class GSIFileReader(object):

    @classmethod
    def read_GSI(cls, file_path):
        rows_list = []
        col_name_position = {}
        data_dict = {}
        with open_workbook(file_path) as GSI_file:
            sheet = GSI_file.get_sheet(1)  # Index of first row is 1
            rows_iter = iter(sheet.rows())
            head_row = next(rows_iter)  # Header record only
            for cell in head_row:  # Speed linearly depends on number of columns into the GSI file
                if cell.v == 'LTE CGI':
                    col_name_position[cell.v] = cell.c
                elif cell.v == 'Latitude':
                    col_name_position[cell.v] = cell.c
                elif cell.v == 'Longitude':
                    col_name_position[cell.v] = cell.c
                elif cell.v == 'Antenna Height (m)':
                    col_name_position[cell.v] = cell.c
                elif cell.v == 'Antenna Tilt-Mechanical':
                    col_name_position[cell.v] = cell.c
                elif cell.v == 'Antenna Tilt-Electrical':
                    col_name_position[cell.v] = cell.c
                elif cell.v == 'Status Active / Locked':
                    col_name_position[cell.v] = cell.c
                elif cell.v == 'Band':
                    col_name_position[cell.v] = cell.c
                elif cell.v == 'Antenna  Model':
                    col_name_position[cell.v] = cell.c
                elif cell.v == 'Azimuth':
                    col_name_position[cell.v] = cell.c
                elif str(cell.v).__contains__('Site Type'):
                    print(str(cell.v))
                    col_name_position['Site Type'] = cell.c
                else:
                    pass
            # F
            print(col_name_position)

            for row in rows_iter:  # accessing all data rows
                col_name_data = {}  # dict for each data row
                # print(row[3])  ==>  Cell(r=1, c=3, v='EKOL0000KONG')

                for col_name, position in col_name_position.items():  # Seems a quadratic, but this iteration is
                    # constant in count
                    cell = row[position]  # getting the cell using cell_position as an index of row, it is a constant
                    # time operation
                    col_name_data[col_name] = cell.v
                data_dict["{0}".format(col_name_data['LTE CGI'])] = col_name_data
        return data_dict








