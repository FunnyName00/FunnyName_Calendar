from flask import *
from python.ListFunctions import *

app = Flask(__name__)

globalList = GeneralList()

@app.route('/')
def index():
    return render_template('index.html', items = globalList.items)

@app.route('/add', methods=['POST'])
def add_item():
    user = request.form.get('user')
    content = request.form.get('content')

    if user and content:
        newItem = GeneralItem(user, content)
        globalList.addItem(newItem)
    
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_item(index):
    if 0 <= index < len(globalList.items):
        globalList.deleteItem(index)
    return(redirect(url_for('index')))

if __name__ == '__main__':
    app.run(debug=True)