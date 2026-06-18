import openpyxl

def get_test_data(file_path,sheet_no):
    wb=openpyxl.load_workbook(file_path)
    sheet=wb[sheet_no]
    data=[]
    for row in sheet.iter_rows(min_row=2,values_only=True):
        data.append(row)
    return data