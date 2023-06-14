# import aspose.words as aw
# from pdfminer.high_level import extract_text
# import PyPDF2
import tabula


# PyPDF2
# doc = UnitextService.UnitextService.create_document("Binder05.pdf")

# print(TextHelper.TextHelper.correct_whitespaces("Binder05. \n \t \r asd  daws dpdf"))


# print(TextHelper.TextHelper.extract_text("Binder05.pdf"))

# # Открываем PDF-файл в режиме чтения бинарных данных
# with open('Binder05.pdf', 'rb') as pdf_file:
#     # Создаем объект PdfFileReader, который представляет PDF-файл
#     pdf_reader = PyPDF2.PdfReader(pdf_file)
#
#     # Получаем количество страниц в PDF-файле
#     num_pages = len(pdf_reader.pages)
#
#     with open('output.txt', 'w', encoding="utf-8") as output_file:
#         # Итерируемся по страницам и получаем текст
#         for page_num in range(num_pages):
#             # Получаем объект страницы
#             page = pdf_reader.pages[page_num]
#
#             # Получаем текст на странице
#             text = page.extract_text()
#             # print(text)
#             t = text.split("\n")
#             print(t)
#             for i in t:
#                 # print(i)
#                 # print(i.replace("\n", " "))
#                 output_file.write(i)
#                 output_file.write("")
#
#             # tr = list(map(lambda x: str(x.split("\n", " ")), t))
#             # print(tr)
#             # # print(tr)
#             # output_file.write("\n".join(tr))
#             # Печатаем текст
# # TextHelper.TextHelper.correct_newlines_for_paragraphs(text, 100)
# output_file.close()
# pdf_file.close()

# Aspose-Words
# pdf = aw.Document("Binder05.pdf")
# print(pdf.get_text())
# print(pdf.sections)
#
# pdf.save("output.txt")


# pdfminer
# text = extract_text('Binder05.pdf')
#
# # Вывести извлеченный текст
# with open('output.txt', 'w', encoding='utf-8') as file:
#     file.write(text.replace("ё", "æ").replace("Ё", "Æ"))



# tables = tabula('Binder05.pdf', pages='all')
#
# # Вывести содержимое каждой таблицы
# for table in tables:
#     print(table)
