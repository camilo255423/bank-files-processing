from utils.processing import FileProcessor
from os import listdir
from os.path import isfile, join
from datetime import date
import xlsxwriter

def add_to_workbook(file_processor, workbook):
    year = file_processor.get_year()
    month = file_processor.get_month()
    transactions = file_processor.get_transactions()
    document_date = '{}-{}'.format(month, year)
    worksheet = workbook.add_worksheet(document_date)

    row = 1
    col = 0
    headers = ['Fecha', 'Valor', 'Doc', 'Clase de Movimiento', 'Oficina']
    bold = workbook.add_format({'bold': True})
    money = workbook.add_format({'num_format': '$#,##0'})

    for header in headers:
        worksheet.write(row, col, header, bold)
        col += 1

    col = 0

    row = 2
    for transaction in transactions:
        worksheet.write(row, col, transaction['date'])
        worksheet.write(row, col + 1, transaction['value'], money)
        worksheet.write(row, col + 2, transaction['document_number'])
        worksheet.write(row, col + 3, transaction['transaction_type'])
        worksheet.write(row, col + 4, transaction['office'])
        row += 1

    worksheet.set_column('A:A', 10)
    worksheet.set_column('B:B', 15)
    worksheet.set_column('C:C', 5)
    worksheet.set_column('D:D', 45)
    worksheet.set_column('E:E', 15)


path = '/home/camilo/Documents/davivienda/'
workbook = xlsxwriter.Workbook('transactions.xlsx')

for element in listdir(path):
    if isfile(join(path, element)):
        file_name = join(path, element)
        file_processor = FileProcessor(file_name)
        add_to_workbook(file_processor, workbook)

workbook.close()

