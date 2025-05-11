from flask import Flask, send_from_directory, redirect, url_for, render_template

app = Flask(__name__)
@app.route('/')
@app.route('/23_1')
def serve_cipher_page():
    return render_template('23_1.html')

@app.route('/ilymargiecao')
def serve_spectrogram_page():
    return render_template('nqdrfwlnjhft.html')

@app.route('/12_4')
def serve_final_page():
    return render_template('12_4.html')

# Serve static files like audio
@app.route('/<path:filename>')
def serve_static_files(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(debug=True)
