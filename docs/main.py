# main.py
from mark2doc import Mark2doc

converter = Mark2doc()
markdown_file = "Начало работы/Подключение к системе.md"
word_file = "output.docx"
converter.markdown_to_docx(markdown_file, word_file)
