import tabula

tables = tabula.read_pdf("../Binder05.pdf", pages='all', multiple_tables=True)
table_text = ""

for table in tables:
    table_text += table.to_string(index=False, header=False) + "\n"

with open("tabulaOutput.txt", 'w', encoding='utf-8') as file:
    file.write(table_text)
