from docx2pdf import convert


def Converter():
    try:
        file_to_be_converted = input(
            "Give the name of docx file that needs to be converted :\n")
        pdf_file = file_to_be_converted + ".pdf"
        file_to_be = file_to_be_converted + ".docx"
        convert(file_to_be)
        convert(file_to_be, pdf_file)
        convert("python/")
    except AssertionError as e:
        pass
