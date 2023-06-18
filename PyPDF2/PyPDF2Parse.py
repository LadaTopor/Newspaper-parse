import PyPDF2



# Открываем PDF-файл в режиме чтения бинарных данных
with open('../Binder05.pdf', 'rb') as pdf_file:
    # Создаем объект PdfFileReader, который представляет PDF-файл
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Получаем количество страниц в PDF-файле
    num_pages = len(pdf_reader.pages)

    with open('PyPDF2output.txt', 'w', encoding="utf-8") as output_file:
        # Итерируемся по страницам и получаем текст
        for page_num in range(num_pages):
            # Получаем объект страницы
            page = pdf_reader.pages[page_num]

            # Получаем текст на странице
            text = page.extract_text()
            # print(text)
            t = text.split("\n")
            print(t)
            for i in t:
                # print(i)
                # print(i.replace("\n", " "))
                output_file.write(i)
                output_file.write("")

            # tr = list(map(lambda x: str(x.split("\n", " ")), t))
            # print(tr)
            # # print(tr)
            # output_file.write("\n".join(tr))
            # Печатаем текст
# TextHelper.TextHelper.correct_newlines_for_paragraphs(text, 100)
output_file.close()
pdf_file.close()
