import tempfile
from flask import Blueprint, request, send_file
from main.services import EncrypterService
from main import metrics

encrypter = Blueprint('encrypter', __name__)

by_path_counter = metrics.counter(
    'by_path_counter', 'Request count by request paths',
    labels={'path': lambda: request.path}
)


@by_path_counter
@encrypter.route('/upload/', methods=['POST'])
def upload():
    file = request.files["file"]
    username = request.form["username"]
    email = request.form["email"]
    if file:
        enc = EncrypterService()
        data_encrypted = enc.encrypt_data(username, file.read(), email)
        with tempfile.NamedTemporaryFile() as f:
            f.write(data_encrypted)
            f.flush()
            filename_enc = file.filename + '.enc'
            return send_file(f.name, as_attachment=True, attachment_filename=filename_enc)

@by_path_counter
@encrypter.route('/download/', methods=['POST'])
def download():
    file = request.files["file"]
    username = request.form['username']
    email = request.form['email']
    if file:
        dec = EncrypterService()
        data_decrypted = dec.decrypt_data(username, file.read(), email)

        with tempfile.NamedTemporaryFile() as f:
            f.write(data_decrypted)
            f.flush()
            filename_enc = file.filename[:-4]
            return send_file(f.name, as_attachment=True, attachment_filename=filename_enc)
