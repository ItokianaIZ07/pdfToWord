from flask import Flask, send_file, request
from converter.converter import Converter
import os
import uuid

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_pdf_to_word():
    file = request.files['file']

    if not Converter.isExtensionValid(file):
        return {"erreur": "Le type de fichier n'est pas pris en charge. Veuillez importer un fichier pdf"}

    pdf_path = f"{uuid.uuid4()}.pdf"
    docx_path = f"{uuid.uuid4()}.docx"

    file.save(pdf_path)

    Converter.convert(pdf_path)

    response = send_file(
        docx_path,
        as_attachment=True,
        download_name="converted.docx"
    )

    # Nettoyage des fichiers temporaire après réponse
    os.remove(pdf_path)
    os.remove(docx_path)

    return response


if __name__ == '__main__':
    app.run(debug=True)