from flask import Flask, redirect, render_template, request

from database import *
from models import User

app = Flask(__name__)

@app.route('/')
def select():
    users = db_session.query(User).all()
    # users = db_session.query(User).first()
    return render_template('index.html', users=users)

# データ挿入
@app.route('/insert', methods=['POST'])
def insert():
    name = request.form.get('name')
    age = request.form.get('age')
    
    user = User(name, age)
    db_session.add(user)
    db_session.commit()
    return redirect('/')

# データ削除
@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    user = db_session.query(User).get(id)
    db_session.delete(user)
    db_session.commit()
    return redirect('/')
    
# データ編集
@app.route('/edit/<id>', methods=['POST'])
def edit(id):
    user = db_session.query(User).get(id)
    return render_template('edit.html', user=user)
# データ更新
@app.route('/update/<id>', methods={'POST'})
def update(id):
    user = db_session.query(User).get(id)
    user.name = request.form.get('name')
    user.age = request.form.get('age')
    
    db_session.commit()
    return redirect('/')
    
if __name__ == '__main__':
    app.run(debug=True, port=8000)
