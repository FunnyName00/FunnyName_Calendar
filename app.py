from flask import *
from python.ListFunctions import *
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = 'secret_key'

# Create a db file in project folder
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Model (Your Class)
class GeneralItem(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Unique ID for every item
    item_type = db.Column(db.String(50), default="general")
    user = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)

    date = db.Column(db.String(100), nullable=True)
    place = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'{self.item_type.upper()} | {self.content} | {self.user}'
    
# Initialize the Database
with app.app_context():
    db.create_all()



@app.route('/')
def index():
    # Query all items from the database instead of a list
    items = GeneralItem.query.all()
    
    return render_template('index.html', items=items)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/add', methods=['POST'])
def add_item():
    item_type = request.form.get('type')
    user = session['username'] 
    content = request.form.get('content')

    new_item = GeneralItem(user=user, content=content, item_type=item_type)

    if item_type == 'activity':
        new_item.date=request.form.get('date')
        new_item.place=request.form.get('place')

    db.session.add(new_item) 
    db.session.commit()      
        
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_item(id):
    item_to_delete = GeneralItem.query.get_or_404(id)
    db.session.delete(item_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)