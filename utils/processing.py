
class FileProcessor(object):
    def __init__(self, file_name):
        with open(file_name) as file_:
            self.document = file_.read()

    def get_year(self, tag="INFORME DEL MES: "):
        start = self.document.find(tag) + len(tag)
        end = self.document.find("\n", start)
        year = self.document[start:end].split('/')[1]
        return year

    def get_transaction_row(self, row):
        columns = row.split('  ')
        columns = [column.strip() for column in columns]
        columns = filter(lambda value: value != '', columns)
        columns[2] = columns[2].replace('$', '').\
            replace('-', '').replace(',', '').replace('+', '')
        columns[2] = columns[2].strip()
        return columns

    def get_pages(self, header, footer):
        pages = []
        document = self.document
        pages.append(document.split(footer)[0])
        if len(document.split(footer)) > 1:
            pages += self.get_pages(document.split(footer)[1], header, footer)

        return pages

    def get_transactions_from_page(self, page):
        transactions = []
        tag = "Fecha"
        start = page.find(tag)
        lines = page[start:].split('\n')
        for i, line in enumerate(lines):
            if '$' in line:
                transactions.append(self.get_transaction_row(line))
        return transactions

    def get_transactions(self,
                         footer='Banco Davivienda S.A NIT.860.034.313-7'):
        pages = self.get_pages(footer)
        transactions = []
        for i, page in enumerate(pages):
            transactions += self.get_transactions_from_page(page)

        return transactions
