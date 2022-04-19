import os
from flask import Flask, flash, request, redirect, url_for
from flask import render_template
from werkzeug.utils import secure_filename

import caption_generator as cg
FOLDER_PATH = "C:\\Users\\shlok\\Desktop\\Minor\\shlokenv\\app\\static"
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = FOLDER_PATH
@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/', methods =['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['image']
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(filename)
        file_upload_path = 'static\\'+ str(filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        description = cg.caption_generator(file_path)		
        result_dic = {'image' : file_upload_path, 'description' : description}

    return render_template('index.html', results = result_dic)
if __name__ == '__main__':
	app.run(debug = True)