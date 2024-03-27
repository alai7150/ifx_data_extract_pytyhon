import statistics

# This class will extract csv file and save data into dictionary{"tname1": [data_list], "tname2": [data_list2]}


class Extractor:
    # properties
    data_file_name = ""
    start_col = 0
    end_col = 0
    # Dict {idx: "col_name", idx2: "col_name2" ...}
    header_idx_dict = {}
    # Dict{'Test1':[Data list], 'Test2':[data list2]z, ...}
    all_data_dict = {}
    total_rows = 0

    def __init__(self):
        pass

    def extract_file(self, file_name):
        # Save data file to property
        self.data_file_name = file_name
        print(f'>>Reading file {self.data_file_name}<<')

        # reset all variables
        self.header_idx_dict = {}
        self.all_data_dict = {}
        self.total_rows = 0

        # start to read file
        with open(self.data_file_name, 'r') as file:
            line = file.readline()
            while line:
                # Create dictionary of list to store data when reading a header (1st row)
                if self.total_rows == 0:
                    lst = line.split(',')
                    for i in range(self.start_col, self.end_col + 1, 1):
                        test_name = lst[i].strip()
                        self.all_data_dict[test_name] = []
                        self.header_idx_dict[i] = test_name
                else:
                    # Process a data row
                    dlist = line.split(',')
                    for i in range(self.start_col, self.end_col, 1):
                        sdata = dlist[i].strip()  # string data
                        if len(sdata) != 0:  # string data is not null
                            # convert string data to float and save into data list of current test
                            self.all_data_dict[self.header_idx_dict[i]].append(float(sdata))

                # read next line if still remains
                line = file.readline()
                self.total_rows += 1
        self.total_rows -= 1  # minus one for total row # due to header row
        print(f'<<File reading completed>>')

    def compute_statistics(self, test_name):
        if test_name in self.all_data_dict:
            data_list = self.all_data_dict[test_name]
            # Proceed only when has data
            if len(data_list) > 0:
                print(f'Test Statistics of {test_name}, data count = {len(data_list)}:')
                # Sort list in order to get median
                data_list.sort()
                # Get mean and median
                mean = statistics.mean(data_list)
                median = data_list[int(len(data_list) / 2)]
                # Get Stdev
                stdev = 0.0
                # Stdev is valid only when we have at least 2 data points
                if len(data_list) > 1:
                    stdev = statistics.stdev(data_list, mean)
                print(f'Mean = {mean}')
                print(f'Median = {median}')
                print(f'Stdev = {stdev}')
            else:
                # Give a warning if specified test has no data
                print(f'Warning, {test_name} has ZERO data.')
        else:
            # Give a warning if test name does not exist in data dict
            print(f'Warning {test_name} does not exist in the data.')
