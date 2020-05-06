from flask import Flask, flash,request, jsonify, render_template, redirect
import json
import os
import sys
import urllib.request
from werkzeug.utils import secure_filename
from flask_dropzone import Dropzone

#Modulos Internos
from modules.lotes_site.lotesite import getlotesite
from modules.detail_lote_site.detaillotesite import getdetaillotesite
from app import UPLOAD_FOLDER
from config import ConfigSectionMap


#Configuraciones Iiciales
extension = ConfigSectionMap('Extension')
separator = ConfigSectionMap('Separator')
fileencode = ConfigSectionMap('FileEncode')

EXTENSION = extension['extensionallow']
EXTENSION = (json.loads(EXTENSION.replace("'",'"')))
SEPARATOR = separator['type']
SEPARATOR = (json.loads(SEPARATOR.replace("'",'"')))
FILEENCODE = fileencode['typefile']
FILEENCODE = (json.loads(FILEENCODE.replace("'",'"')))



app = Flask(__name__)
dropzone = Dropzone(app)
UPLOAD_FOLDER = '/home/quintanada/Pictures/upload/'
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 3000 * 1024 * 1024

#Extensiones peritidas CSV TXT JSONLINE
ALLOWED_EXTENSIONS = set(EXTENSION)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def Index():
    #return 'Aplicacion conecta a Base de Datos'
    return render_template('index.html')


@app.route('/lotesite/', methods=['GET'])
def getLoteSite():
    id= request.args.get('id_lote')
    l_lote = getlotesite(id)
    return render_template('lotesite.html', lotesite = l_lote)


@app.route('/detaillote/', methods=['GET'])
def getDetailLoteSite():
    id_dt = request.args.get('id_dtlote')
    l_detaillote = getdetaillotesite(id_dt)
    return render_template('detaillote.html', detaillote = l_detaillote)

@app.route('/upload/')
def upload_form():
    l_encode = FILEENCODE
    l_tiparch = ALLOWED_EXTENSIONS
    l_sepcol = SEPARATOR
    l_sepfil = l_sepcol
    return render_template('upload.html', list_encode= l_encode,
                        tiparch= l_tiparch,sepcol=l_sepcol,sepfil=l_sepfil)

@app.route('/upload/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the files part
		if 'files[]' not in request.files:
			flash('No file part')
			return redirect(request.url)
		files = request.files.getlist('files[]')
		for file in files:
			if file and allowed_file(file.filename):
				filename = secure_filename(file.filename)
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		flash('File(s) successfully uploaded')
		return redirect('/')



@app.errorhandler(500)
def handle_500(error):
    return str(error), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)