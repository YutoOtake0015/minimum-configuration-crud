from flask import Flask, redirect, render_template, request

from database import *
from model import *

app = Flask(__name__)

@app.route('/')
def select():
    users = session.query(User).all()
    return render_template('index.html', users=users)

# データ挿入
@app.route('/insert', methods=['POST'])
def insert():
    name = request.form.get('name')
    age = request.form.get('age')
    
    user = User(name, age)
    session.add(user)
    session.commit()
    return redirect('/')

# データ削除
@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    user = session.query(User).get(id)
    session.delete(user)
    session.commit()
    return redirect('/')
    
# データ編集
@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    user = session.query(User).get(id)
    if request.method == 'POST':
        user.name = request.form.get('name')
        user.age = request.form.get('age')
        session.commit()
        return redirect('/')
    return render_template('edit.html', user=user)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
