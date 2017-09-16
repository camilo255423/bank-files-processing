class FileProcessor(object):
    def __init__(self, file_name):
        with open(file_name) as file_:
            self.document = file_.read()

    def get_year(self, tag="INFORME DEL MES: "):
        start = self.document.find(tag) + len(tag)
        end = self.document.find("\n", start)
        year = self.document[start:end].split('/')[1].strip()
        return year

    def get_month(self, tag="INFORME DEL MES: "):
        start = self.document.find(tag) + len(tag)
        end = self.document.find("\n", start)
        month_name = self.document[start:end].split('/')[0].strip()
        months = {'ENERO': '01',
                  'FEBRERO': '02',
                  'MARZO': '03',
                  'ABRIL': '04',
                  'MAYO': '05',
                  'JUNIO': '06',
                  'JULIO': '07',
                  'AGOSTO': '08',
                  'SEPTIEMBRE': '09',
                  'OCTUBRE': '10',
                  'NOVIEMBRE': '11',
                  'DICIEMBRE': '12'
                  }
        return months[month_name]

    def get_transaction_row(self, row):
        columns = row.split('  ')
        columns = [column.strip() for column in columns]
        columns = filter(lambda value: value != '', columns)
        columns[2] = columns[2].replace('$', '').\
            replace('-', '').replace(',', '').replace('+', '')
        columns[2] = columns[2].strip()
        return columns

    def get_transaction_as_dict(self, transaction):
        year = self.get_year()
        if len(transaction) > 5:
            office = transaction[5]
        else:
            office = ''
        dict_transaction = {
            'date': '{}-{}-{}'.format(transaction[0],
                                      transaction[1],
                                      year),
            'value': float(transaction[2]),
            'document_number': transaction[3],
            'transaction_type': transaction[4],
            'office': office
        }
        return dict_transaction

    def get_pages(self, document, footer):
        pages = []
        pages.append(document.split(footer)[0])
        if len(document.split(footer)) > 1:
            pages += self.get_pages(document.split(footer)[1], footer)

        return pages

    def get_transactions_from_page(self, page):
        transactions = []
        tag = "Fecha"
        start = page.find(tag)
        lines = page[start:].split('\n')
        for i, line in enumerate(lines):
            if '$' in line:
                transaction = self.get_transaction_row(line)
                transaction_dict = self.get_transaction_as_dict(transaction)
                transactions.append(transaction_dict)
        return transactions

    def get_transactions(self,
                         footer='Banco Davivienda S.A NIT.860.034.313-7'):
        pages = self.get_pages(self.document, footer)
        transactions = []
        for i, page in enumerate(pages):
            transactions += self.get_transactions_from_page(page)

        return transactions
