from flask import Flask, send_file, request, render_template, after_this_request, jsonify
from converter.converter import PdfConverter
import os
import uuid

app = Flask(__name__)

generatedFile = ""

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/convert', methods=['POST'])
def convert_pdf_to_word():
    file = request.files['file']

    if not PdfConverter.isExtensionValid(file.filename):
        return jsonify({"erreur": "Le type de fichier n'est pas pris en charge. Veuillez importer un fichier pdf"})

    pdf_path = f"{uuid.uuid4()}.pdf"
    docx_path = f"{uuid.uuid4()}.docx"
    generatedFile = os.path.abspath(docx_path)

    file.save(pdf_path)

    PdfConverter.convert(pdf_path, docx_path)

    response = send_file(
        docx_path,
        as_attachment=True,
        download_name="converted.docx"
    )

    # nettoyage après des fichiers temporaires après envoie
    @after_this_request
    def cleanup(response):
        try:
            os.remove(pdf_path)
        except Exception as e:
            print(e)
        return response

    return response

@app.route("/clear", methods=["POST"])
def clear():
    try:
        os.remove(generatedFile)
    except Exception as e:
        print(e)
    return jsonify({"message": "File converted successfuly"})

if __name__ == '__main__':
    app.run(debug=True)