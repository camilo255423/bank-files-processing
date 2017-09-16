from utils.processing import FileProcessor
from os import listdir
from os.path import isfile, join

path = '/home/camilo/Documents/davivienda/'
for element in listdir(path):
    if isfile(join(path, element)):
        file_name = join(path, element)
        file_processor = FileProcessor(file_name)
        year = file_processor.get_year()
        month = file_processor.get_month()
        transactions = file_processor.get_transactions()
        print('{}/{}'.format(month, year))
        print(transactions)

