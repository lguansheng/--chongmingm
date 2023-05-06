# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this-is-a-secret-key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rename', methods=['POST'])
def rename():
    if request.method == 'POST':
        path = request.form['path']
        name = request.form['name']
        start_number = request.form['start_number']
        file_type = request.form['file_type']

        count = 0
        file_list = os.listdir(path)
        for file in file_list:
            old_name = os.path.join(path, file)
            if os.path.isdir(old_name):
                continue
            new_name = os.path.join(path, name + str(count + int(start_number)) + file_type)
            os.rename(old_name, new_name)
            count += 1

        flash(f"一共重命名了{count}个文件！", 'success')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

