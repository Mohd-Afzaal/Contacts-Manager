from flask import Flask, request, render_template, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_scss import Scss
from datetime import datetime
import uuid

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'alakazam'
Scss(app, static_dir='static', asset_dir='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    notes = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.name}>"

with app.app_context():
        db.create_all()

@app.before_request
def make_session_permanent():
    session.permanent = True
    if "user_id" not in session:
        session["user_id"] = str(uuid.uuid4())

# Route Setups
@app.route('/')
def index():
    search_query = request.args.get('search')
    if search_query:
        contacts = contact.query.filter(
            contact.user_id == session["user_id"],
            contact.name.ilike(f'%{search_query}%') |
            contact.email.ilike(f'%{search_query}%') |
            contact.phone.ilike(f'%{search_query}%')
        ).order_by(contact.created_at.desc()).all()
    else:
        contacts = contact.query.filter_by(user_id=session["user_id"]).order_by(contact.created_at.desc()).all()
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['GET', 'POST'])
def add_contacts():
    # add contacts
    if request.method == "POST":
        current_name = request.form["name"]
        current_email = request.form["email"]
        current_phone = request.form["phone"]
        current_notes = request.form["notes"]

         # Check if phone or email already exists
        existing_phone = contact.query.filter_by(phone=current_phone, user_id=session["user_id"]).first()
        existing_email = contact.query.filter_by(email=current_email, user_id=session["user_id"]).first()
        if existing_phone and existing_email:
            flash("Phone number and email already exist!", "error")
            return redirect('/add')
        elif existing_phone:
            flash("Phone number already exists!", "error")
            return redirect('/add')
        elif existing_email:
            flash("Email already exists!", "error")
            return redirect('/add')
        else:
            new_contact = contact(name=current_name, email=current_email, phone=current_phone, notes=current_notes, user_id=session["user_id"])
        try:
            db.session.add(new_contact)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            db.session.rollback()
            return f"An error occurred: {e}"
            return redirect('/add')

    # see all contacts
    else:
        contacts = contact.query.order_by(contact.created_at.desc()).filter_by(user_id=session["user_id"]).all()
        return render_template('add.html')

# Delete contact
@app.route('/delete/<int:id>')
def delete_contact(id):
    contact_to_delete = contact.query.filter_by(id=id, user_id=session["user_id"]).first_or_404()
    try:
        db.session.delete(contact_to_delete)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        db.session.rollback()
        return f"An error occurred: {e}"

# update contact
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_contact(id):
    contact_to_update = contact.query.filter_by(id=id, user_id=session["user_id"]).first_or_404()
    if request.method == "POST":
        contact_to_update.name = request.form["name"]
        contact_to_update.email = request.form["email"]
        contact_to_update.phone = request.form["phone"]
        contact_to_update.notes = request.form["notes"]
        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            db.session.rollback()
            return f"An error occurred: {e}"
    else:
        return render_template('update.html', contact=contact_to_update)

if __name__ == '__main__':
    app.run()  