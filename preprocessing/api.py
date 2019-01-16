import os
from flask import Flask, request, redirect, url_for
from preprocessing.AudioConverter import getext
from preprocessing.SyllabelCounter import syllables_in_text
from SyllablesFinder import syllablesForSentence
from ProportionCalulator import countAllSyllables

UPLOAD_FOLDER = '/home/dilshan/uploads/'
ALLOWED_EXTENSIONS = set(['txt','wav'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            print(filename)
            file_path=app.config['UPLOAD_FOLDER']+filename
            file.save(file_path)
            o_text="Our Voice Recorder is a convenient and simple online tool that can be used right in your browser"
            text=getext(file_path)
            print(syllablesForSentence(text))
            print(syllablesForSentence(o_text))
            syllables=syllables_in_text(text)
            o_syllables=syllables_in_text(o_text)
            print(syllables)
            print(o_syllables)
            prop=countAllSyllables(syllables)
            o_prop=countAllSyllables(o_syllables)
            result={}
            result["original text syllables"]=o_prop[0]
            result["uttered text syllables"] =prop[0]
            result["stuttered"]=prop[1]-o_prop[1]
            result["syllables"]=syllables
            return redirect(url_for('index'))
    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    <p>%s</p>
    """ % "<br>".join(os.listdir(app.config['UPLOAD_FOLDER'],))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001, debug=True)