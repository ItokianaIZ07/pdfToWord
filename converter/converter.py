from pdf2docx import Converter

class PdfConverter:
    @staticmethod
    def convert(fileInput, fileOutput):
        cv = Converter(fileInput)
        cv.convert(fileOutput)
        cv.close()

    @staticmethod
    def isExtensionValid(file):
        return file.find(".pdf") != -1
