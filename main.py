# Import
from flask import Flask, render_template,request, redirect
# Importowanie biblioteki bazy danych
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Podłączanie SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creating a DB
db = SQLAlchemy(app )

#Zadanie nr 1. Utwórz tabelę DB











# Uruchamianie strony z treścią
@app.route('/')
def index():
    # Wyświetlanie obiektów Bazy
    # Assignment #2. Display the objects from the DB in index.html
    

    return render_template('index.html',
                           #karty = cards

                           )

# Uruchomienie strony z kartą
@app.route('/card/<int:id>')
def card(id):
    #Zadanie #2. Wyświetl właściwą kartę według jej identyfikatora
    

    return render_template('card.html', card=card)

# Uruchomienie strony i utworzenie karty
@app.route('/create')
def create():
    return render_template('create_card.html')

# Formularz karty
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        #Zadanie #2. Stwórz sposób przechowywania danych w bazie danych
        




        return redirect('/')
    else:
        return render_template('create_card.html')


if __name__ == "__main__":
    app.run(debug=True)