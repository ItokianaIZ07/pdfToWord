from pdf2docx import Converter

class Converter:
    @staticmethod
    def convert(file):
        cv = Converter(file)
        cv.convert(file)
        cv.close()

    @staticmethod
    def isExtensionValid(file):
        return str.find(".pdf") != -1
