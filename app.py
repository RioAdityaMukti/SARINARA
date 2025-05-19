from flask import Flask, render_template, jsonify
import csv

app = Flask(__name__)


def load_qa_data(filename):
    qa_pairs = {}
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            qa_pairs[row['pertanyaan'].lower()] = row['jawaban']
    return qa_pairs
qa_data = load_qa_data('static/assets/cleaned_data_qna.csv')

@app.route('/')
def home():
    return render_template('index.html')  

@app.route('/deteksi')
def deteksi():
    return render_template('deteksi.html')  

@app.route('/statistik')
def statistik():
    return render_template('statistik.html')  

@app.route('/tentang')
def tentang():
    return render_template('tentang.html')  # Your about page

@app.route('/detail_zat/<int:zat_id>')
def detail_zat(zat_id):
    details = {
        0: {"name": "Nikotin", "description": "Nikotin is a highly addictive substance found in cigarettes."},
        1: {"name": "Tar", "description": "Tar is a carcinogen found in cigarette smoke."},
        2: {"name": "Carbon Monoxide", "description": "A poisonous gas that can affect the lungs and heart."},
        3: {"name": "Formaldehyde", "description": "Formaldehyde is a toxic chemical used in preservatives."},
    }
    zat = details.get(zat_id, {"name": "Unknown", "description": "No details available."})
    return render_template('detail_zat.html', zat=zat)

@app.route('/get_response/<message>', methods=['GET'])
def get_response(message):
    message = message.lower()
    response = qa_data.get(message, "Maaf, saya tidak mengerti pertanyaan itu. Silakan coba tanyakan yang lain!")
    return jsonify(response=response)

if __name__ == '__main__':
    app.run(debug=True)