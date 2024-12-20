""" This module contains the ProcessPayroll class. """

from extraction import extract_from_csv as extraction

class ProcessPayroll:
    """
    A class used to process payroll data.
    Attributes
    ----------
    data : any
        The data to be processed.
    Methods
    -------
    process():
        Processes the payroll data by validating and extracting it
        from a CSV file.
    """
    def __init__(self, file_path, file_name):
        self.file_path = file_path
        self.file_name = file_name

    def process(self):
        """
        Processes the payroll data by validating and extracting
        information from a CSV file.
        This method constructs the full file path by combining the
        base file path and file name, then uses the CSVExtractor to
        validate and extract data from the CSV file. If the validation
        is successful, the extracted data is printed. Otherwise, an
        error message is printed.
        Returns:
            None
        """

        file_path = self.file_path + '\\' + self.file_name
        csv_extractor = extraction.CSVExtractor(file_path)

        is_valid = csv_extractor.validate()

        if is_valid is True:
            data = csv_extractor.extract()
            print(data)
        else:
            print("Validation failed...", is_valid)

    def __str__(self):
        return f""" ProcessPayroll(file_path={self.file_path},
        file_name={self.file_name}) """
