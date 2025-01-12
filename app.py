from flask import Flask, render_template
from flask_migrate import Migrate, upgrade

from models import db,  seedData, Category, Product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost/FunShop'
db.app = app
db.init_app(app)
migrate = Migrate(app,db)



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')




if __name__ == "__main__":
    with app.app_context():
        upgrade()
        seedData(db)

    app.run(debug=True)
