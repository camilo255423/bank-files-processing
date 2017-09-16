from utils.processing import FileProcessor

file_name = '/home/camilo/Documents/davivienda/extracto_201608.txt'
file_processor = FileProcessor(file_name)
print file_processor.get_transactions()
