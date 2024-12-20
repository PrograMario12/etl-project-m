''' This is the main file that will be executed when the program is 
run. '''

from process.payroll import ProcessPayroll

if __name__ == '__main__':
    file_path = input("Please enter the path to your CSV file: ")
    file_name = input("Please enter the name of your CSV file: ")

    payroll = ProcessPayroll(file_path, file_name)
    payroll.process()
