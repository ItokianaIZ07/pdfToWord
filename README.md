# PDF to Word Converter

## Description

PDF to Word Converter est une application web permettant de convertir facilement des fichiers PDF en documents Microsoft Word (`.docx`).

L'application est développée en **Python** avec le framework **Flask** et utilise la bibliothèque **pdf2docx** pour effectuer la conversion des documents. L'interface utilisateur permet de sélectionner un fichier PDF, de l'envoyer au serveur, puis de télécharger automatiquement le document Word généré.

---

## Fonctionnalités

* Conversion de fichiers PDF en format Word (`.docx`)
* Interface web simple et intuitive
* Vérification du type de fichier avant conversion
* Téléchargement automatique du document converti
* Gestion des fichiers temporaires pour éviter l'encombrement du serveur
* API REST simple basée sur Flask

---

## Technologies utilisées

### Backend

* Python 3
* Flask
* pdf2docx

### Frontend

* HTML5
* CSS3
* JavaScript (Fetch API)

---

## Installation

### 1. Cloner le projet

```bash
git clone https://github.com/votre-utilisateur/pdf-to-word-converter.git

cd pdf-to-word-converter
```

### 2. Créer un environnement virtuel

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

Ou manuellement :

```bash
pip install flask pdf2docx
```

---

## Lancement de l'application

```bash
python app.py
```

Par défaut, Flask démarre sur :

```text
http://127.0.0.1:5000
```

Ouvrez ensuite cette adresse dans votre navigateur.

---

## Utilisation

1. Ouvrir l'application dans un navigateur.
2. Sélectionner un fichier PDF.
3. Cliquer sur le bouton de conversion.
4. Attendre la fin du traitement.
5. Télécharger automatiquement le document Word généré.

---

## Structure du projet

```text
pdf-to-word-converter/
│
├── app.py
├── converter/
│   └── PdfConverter.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   └── index.html
│
├── requirements.txt
└── README.md
```

---

## Exemple de route Flask

```python
@app.route('/convert', methods=['POST'])
def convert_pdf_to_word():
    file = request.files['file']

    pdf_path = f"{uuid.uuid4()}.pdf"
    docx_path = f"{uuid.uuid4()}.docx"

    file.save(pdf_path)

    PdfConverter.convert(pdf_path, docx_path)

    return send_file(
        docx_path,
        as_attachment=True,
        download_name="converted.docx"
    )
```

---

## Bibliothèque pdf2docx

La conversion est réalisée grâce à la bibliothèque **pdf2docx**, qui analyse le contenu du document PDF (texte, paragraphes, tableaux, images simples) afin de recréer une structure équivalente dans un document Word.

Exemple d'utilisation :

```python
from pdf2docx import Converter

cv = Converter("document.pdf")
cv.convert("document.docx")
cv.close()
```

---

## Limitations

La qualité de conversion dépend fortement de la structure du PDF :

* Les documents textuels simples sont généralement bien convertis.
* Les mises en page complexes peuvent être partiellement modifiées.
* Les formulaires interactifs ne sont pas toujours conservés.
* Certains éléments graphiques avancés peuvent être altérés.
