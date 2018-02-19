import os
from app import app
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from app.utils import filter_resumes


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload-cv', methods=['POST'])
def upload_cv():
    file = request.files['file']
    if not os.path.exists(os.path.join(app.config['STATIC_PATH'], 'cv-uploads')):
        os.makedirs(os.path.join(app.config['STATIC_PATH'], 'cv-uploads'))
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['STATIC_PATH'], 'cv-uploads', filename))

    return redirect(url_for('index'))


@app.route('/filtered-cvs', methods=['GET'])
def filtered_cvs():
    all_cvs = os.listdir(os.path.join(app.config['STATIC_PATH'], 'cv-uploads'))
    matched_cvs = list(filter(filter_resumes, all_cvs))
    return render_template('filtered_resumes.html', paths=matched_cvs)


@app.route('/search-keywords', methods=['POST'])
def search_keywords():
    keywords = request.form['keywords']
    keywords = [x.strip() for x in keywords.split(',')]
    all_cvs = os.listdir(os.path.join(app.config['STATIC_PATH'], 'cv-uploads'))
    matched_cvs = list(filter(lambda seq: filter_resumes(seq, keywords), all_cvs))
    return render_template('filtered_resumes.html', paths=matched_cvs, keywords=', '.join(keywords ))