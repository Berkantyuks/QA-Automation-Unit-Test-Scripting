import csv

class read_in_data_test_timing_data:

    timing_data = []

    def start(self):

        with open("./tests/test_docs/TestTimingData.csv") as test_csv_file:
            file_read = csv.reader(test_csv_file)

            for row in file_read:
                self.timing_data.append(row)

        column_chart_data = [["Test Name", "Diff from Avg"]]
        table_data = [["Test Name", "Run Time (s)"]]

        for row in self.timing_data[1:]:
            test_name = row[0]

            # if each rows have a null test result, skip that test
            if not row[1] or not row[2]:
                continue
            try:
                current_run_time = float(row[1])
                avg_run_time = float(row[2])
            except:
                print(row[1], row[2])

            diff_from_avg = avg_run_time - current_run_time

            column_chart_data.append([test_name, diff_from_avg])
            table_data.append([test_name, current_run_time])

        print(column_chart_data)
        print(table_data)

        return (column_chart_data)
    pass

class read_in_data_test_analysis_data:

    analysis_data = []

    def start(self):

        with open("./tests/test_docs/TestAnalysisData.csv") as test_csv_file:
            file_read = csv.reader(test_csv_file)

            for row in file_read:
                self.analysis_data.append(row)

        chart_data = [self.analysis_data[0]]
        for row in self.analysis_data[1:]:

            try:
                num_asserts = int(row[1])
                num_failed_asserts = int(row[2])
            except:
                print("Expected Errors "+str(num_asserts), str(num_failed_asserts))

            chart_data.append([row[0], num_asserts, num_failed_asserts])

        print(chart_data)
        return (chart_data)

    pass
