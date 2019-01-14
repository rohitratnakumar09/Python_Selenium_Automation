import csv
import xlrd


def getCSVData(fileName):
    # create an empty list to store rows
    rows = []
    # open the CSV file
    dataFile = open(fileName, "r")
    # create a CSV Reader from CSV file
    reader = csv.reader(dataFile)
    # skip the headers
    next(reader)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows


def get_data(file_name):
    # create an empty list to store rows
    rows = []
    # open the specified Excel spreadsheet as workbook
    book = xlrd.open_workbook(file_name)
    # get the first sheet
    sheet = book.sheet_by_index(0)
    # iterate through the sheet and get data from rows in list
    for row_idx in range(1, sheet.nrows):
        rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
    return rows