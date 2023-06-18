from pdfminer.high_level import extract_text

# pdfminer
text = extract_text('../Binder05.pdf')

# Вывести извлеченный текст
with open('minerParseOutput.txt', 'w', encoding='utf-8') as file:
    file.write(text.replace("ё", "æ").replace("Ё", "Æ"))
