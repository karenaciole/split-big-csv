import os
import shutil
import pandas as pd

''' 
Simple script using pandas to split a big csv file into smaller csv files.

Parameters
    file: str
        path to the big csv file ("file.csv" or if not in the same dir "path/to/file.csv")
    
    number_of_csv_files: int 
        number of csv files to be created
    
    number_of_rows_in_each_csv_file: int 
        number of rows in each csv file

'''

def multiple_files(file, number_of_csv_files, number_of_rows_in_each_csv_file):
    big_file = pd.read_csv(file)
    file_name = os.path.splitext(os.path.basename(file))[0]
    dst = os.path.join(os.getcwd(), file_name) # destination path

    if not os.path.exists(dst):
        os.mkdir(dst)

    for i in range(number_of_csv_files):
        data = big_file[number_of_rows_in_each_csv_file * i:number_of_rows_in_each_csv_file * (i + 1)]

        if data.empty:
            break

        data.to_csv(file_name + f'{i + 1}.csv', index=False)

        src_file = os.path.join(os.getcwd(), file_name + f'{i + 1}.csv')
        destination_file = os.path.join(dst, file_name + f'{i + 1}.csv')

        shutil.move(src_file, destination_file)

    return "Done! Files created in directory: " + dst


if __name__ == "__main__":
    print(multiple_files('file.csv', 0, 0))
