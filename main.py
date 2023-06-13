from pullenti.unitext import UnitextService
from pullenti.util import TextHelper

import PyPDF2

# doc = UnitextService.UnitextService.create_document("Binder05.pdf")

# print(TextHelper.TextHelper.correct_whitespaces("Binder05. \n \t \r asd  daws dpdf"))


print(TextHelper.TextHelper.extract_text("Binder05.pdf"))

# Открываем PDF-файл в режиме чтения бинарных данных
with open('Binder05.pdf', 'rb') as pdf_file:
    # Создаем объект PdfFileReader, который представляет PDF-файл
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Получаем количество страниц в PDF-файле
    num_pages = len(pdf_reader.pages)

    with open('output.txt', 'w', encoding="utf-8") as output_file:
        # Итерируемся по страницам и получаем текст
        for page_num in range(num_pages):
            # Получаем объект страницы
            page = pdf_reader.pages[page_num]

            # Получаем текст на странице
            text = page.extract_text()

            output_file.write(TextHelper.TextHelper.correct_newlines_for_paragraphs(text, 100))
            # Печатаем текст

output_file.close()
pdf_file.close()
