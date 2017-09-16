from utils.processing import FileProcessor
from os import listdir
from os.path import isfile, join
from datetime import date
import xlsxwriter

path = '/home/camilo/Documents/davivienda/'
file_name = '/home/camilo/Documents/davivienda/extracto_201608.txt'
# for element in listdir(path):
#     if isfile(join(path, element)):
#         file_name = join(path, element)
#         file_processor = FileProcessor(file_name)
#         year = file_processor.get_year()
#         month = file_processor.get_month()
#         transactions = file_processor.get_transactions()
#         print('{}/{}'.format(month, year))
#         print(transactions)


file_processor = FileProcessor(file_name)
year = file_processor.get_year()
month = file_processor.get_month()
transactions = file_processor.get_transactions()
print('{}/{}'.format(month, year))
print(transactions)

# workbook = xlsxwriter.Workbook('transactions.xlsx')
# worksheet = workbook.add_worksheet('month')
#
# row = 1
# fields = ['Fecha', 'Valor', 'Doc', 'Clase de Movimiento', 'Oficina']
#
# for transaction in transactions:
#     col = 0
#     print("{}-{}-{}".format(year, month, transaction[0]))
#     worksheet.write(row, col, "{}-{}-{}".format(transaction[0], month, year))
#     # for value in values:
#     #     value = value.replace("'", '')
#     #     worksheet.write(row, col, value)
#     #     col += 1
#     row += 1

workbook.close()