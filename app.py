from flask import Flask
from models import db
from flask_migrate import Migrate

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1001Jitesh36$@localhost:3306/hospital_managementdb'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/api/")
def home():
    return "Flask App Running!"

if __name__ == "__main__":
    app.run(debug=True)
