from extractor import Extractor

# This is a python script to extract IFX CSV data and compute statistics for specified test

# Configuration, need to specify before running this script
data_file_path = 'C:/IFX_SAMPLE_DATA.csv'
specified_test_name = "VTH@IG=3.000000E-005A"
data_col_start_index = 11
data_col_end_index = 24

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('**** Start of Python script to extract CSV data file ****')
    # Setup extractor
    extr = Extractor()
    extr.start_col = data_col_start_index
    extr.end_col = data_col_end_index

    # extract file
    extr.extract_file(data_file_path)

    # print total rows
    print(f'Total rows: {extr.total_rows}')

    # compute statistics of specified test and print it
    extr.compute_statistics(specified_test_name)
    print('**** End of execution ****')
