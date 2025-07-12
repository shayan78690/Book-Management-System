from flask import Flask, render_template, request, redirect, jsonify
import os
import json
import csv
import xml.etree.ElementTree as ET # for reading xml format
import pandas as pd
from werkzeug.utils import secure_filename 

# bootup the flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads' # whenever you upload a file, i want to store the file in vendor version and also to my custom version, i want to keep all files, i will keep original files in uploads folder
ALLOWED_EXTENSIONS = {'csv', 'xml', 'json', 'xlsx'}

BOOKS_FILE = 'books.json' # this is our central storage file which we will use to store all the books from different vendors


# initialize books storage(central storage)
def load_books():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, 'r') as f: # if file exist we will read that json file
            return json.load(f)
    return [] # if not exist we will return empty list

# saving books to the central storage file which is books.json
def save_books(books):
    with open(BOOKS_FILE, 'w') as f:
        json.dump(books, f, indent=2)
        
# checks if a file format is allowed or not
# filename.csv, filename.xml, filename.json, filename.xlsx , CSV > csv, XML > xml, JSON > json, XLSX > xlsx >> True else False
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# API routes/endpoints
# submit book through UI
# READ/CREATE
@app.route('/', methods = ['GET', 'POST'])
def home():
    # 2 responsibility >> 1. sllow user to add new books >> 2.  display all books in the central file storgage
    books = load_books() # it is returning us as array of books from the central storage file
    if request.method == 'POST':
        # new books are being added
        # save the books in the books.jsonJSONProvJSON
        new_book = {
            'title': request.form.get('title'),
            'author': request.form.get('author', ''),
            'isbn': request.form.get('isbn', '')
        }
        books.append(new_book)
        save_books(books)
    return render_template('home.html', books=books) # home.html gets the updated array of books

# add books via a file upload
# submit book through api
# single entry
# CREATE
@app.route('/api/books', methods=['POST'])
def add_books_json():
    if not request.is_json():
        return jsonify({"error": "Content type must be application/json"}), 400
    # book data we are getting
    data = request.get_json()
    
    # validate the json data
    if 'title' not in data:
        return jsonify({"error": "Title is required"}), 400
    
    # load all the old books
    books = load_books()
    books.append(
        {
            'title': data['title'],
            'author': data.get('author', ''),
            'isbn': data.get('isbn', '')
        }
    )
    
    save_books(books)
    return jsonify(data), 201
    


# upload a file
# submit book through file
# multiple entries
# CREATE
@app.route('/upload', methods = ["POST"])
def upload_file():
    # submit a file from the user and checks the differeent file ormat if it is matching or not
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    # process files based on file formats
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename) # it makes sure that the filename is secure and does not contain any malicious content
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        file.save(file_path)
        
        # process different file formats the file
        # read one by one book and store it in json
        try:
            if filename.endswith('.csv'):
                process_csv(file_path)
            elif filename.endswith('.xml'):
                process_xml(file_path)
            elif filename.endswith('.xlsx'):
                process_xlsx(file_path)
            elif filename.endswith('json'):
                process_json(file_path)
                
            return jsonify({"message": "File processed successfully"}), 200
        except Exception as e:
            if os.path.exists(file_path):
                os.remove(file_path)
            return jsonify({"error": str(e)}), 400
    return jsonify({"error": "Filetype not supported"}), 400

def process_csv(file_path):
    # load the books in books.json
    books = load_books()
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # only process book which have a title else ignore
            if 'title' in row:
                books.append(
                    {
                        'title': row['title'],
                        'author': row.get('author', ''),
                        'isbn': row.get('isbn', '')
                    }
                )
    # last steps
    # Save it
    save_books(books)
    
def process_xml(file_path):
    books = load_books()
    tree = ET.parse(file_path)
    root = tree.getroot() # root element of the XML file >> books
    for book_elem in root.findall('book'):
        title_elem = book_elem.findall('title')
        
        if title_elem is not None:
            books.append(
                {
                    'title': title_elem.text,
                    'author': book_elem.find('author').text if book_elem.find('author') is not None else '', # it is a pythonic way of writing a code
                    'isbn': book_elem.find('isbn').text if book_elem.find('isbn') is not None else ''
                }
            )
    save_books(books)
    
def process_xlsx(file_path):
    books = load_books()
    df = pd.read_excel(file_path)
    for _, row in df.iterrows():
        if 'title' in row:
            books.append(
                {
                    'title' : row['title'],
                    'author': row.get('author', ''),
                    'isbn': row.get('isbn', '')
                }
            )
    
    save_books(books)
    
def process_json(file_path):
    books = load_books()
    with open(file_path, 'r') as file:
        data = json.load(file)
        
        for book_data in data:
            if 'title' in book_data:
                books.append(
                    {
                        'title': book_data['title'],
                        'author': book_data.get('author', ''),
                        'isbn': book_data.get('isbn', '')
                    }
                )
    save_books(books)
            
            
# this is how request object is looking like
# request = {
#     files: {
#         'file': [file in json format]
#     }
#     method : GET/POST
# }



# UPDATA AND DELETE ONLY LEFT
# CRUD OPERATIONS
# WE HAVE COMPLETED CREATE AND READ

@app.route('/update', methods = ['POST'])
def update():
    books = load_books()
    
    old_title = request.form.get('old_title')
    new_title = request.form.get('new_title')
    
    for book in books:
        if book['title'] == old_title:
            book['title'] = new_title
            break
    save_books(books)
    return redirect('/')

@app.route('/delete', methods = ['POST'])
def delete():
    books = load_books()
    
    title_to_delete = request.form.get('title')
    
    # books = [book for book in books if book['title'] != title_to_delete]
    for book in books:
        if book['title'] == title_to_delete:
            books.remove(book)
            break
    
    save_books(books)
    return redirect('/')

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    if not os.path.exists(BOOKS_FILE):
        save_books([])        
    
    
    app.run(debug=True, host="0.0.0.0", port=8080)
    
# vendor jisbhi format me book add karega we don't care we will only store that only in json format