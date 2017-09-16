def get_year(lines):
    tag = "INFORME DEL MES: "
    start = lines.find(tag) + len(tag)
    end = lines.find("\n",start)
    year = lines[start:end].split('/')[1]
    return year


def get_transaction_row(row):
    columns = row.split('  ')
    columns = [column.strip() for column in columns]
    columns = filter(lambda value: value != '', columns)
    columns[2] = columns[2].replace('$', '').\
        replace('-', '').replace(',', '').replace('+', '')
    columns[2] = columns[2].strip()
    return columns


def get_pages(document, header, footer):
    pages = []
    pages.append(document.split(footer)[0])
    if len(document.split(footer)) >1:
        pages += get_pages(document.split(footer)[1], header, footer)

    return pages


def get_transactions_from_page(page):
    transactions = []
    tag = "Fecha"
    start = page.find(tag)
    lines = page[start:].split('\n')
    for i, line in enumerate(lines):
        if '$' in line:
            transactions.append(get_transaction_row(line))
    return transactions

with open('/home/camilo/Documents/davivienda/extracto_201608.txt') as extracto_file:
    document = extracto_file.read()
    header = 'CUENTA DE AHORROS'
    footer = 'Banco Davivienda S.A NIT.860.034.313-7'
    pages = get_pages(document, header, footer)
    transactions = []
    for i, page in enumerate(pages):
        transactions += get_transactions_from_page(page)

    print len(transactions)


