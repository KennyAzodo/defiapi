import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask app and extensions
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'postgresql://postgres_db_xog9_user:MpW7ziWG1uqIpn9dHsp8jdeRmftDgjSN'
    '@dpg-d1r5cq2dbo4c73e7740g-a.oregon-postgres.render.com:5432/postgres_db_xog9'
)
db = SQLAlchemy(app)
api = Api(app)


# Models
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    reason = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)


class StartupApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    x_username = db.Column(db.String(120), nullable=False)
    telegram = db.Column(db.String(120))
    discord = db.Column(db.String(120))
    linkedin = db.Column(db.String(120))
    description = db.Column(db.Text)
    service = db.Column(db.String(50), nullable=False)
    coingecko = db.Column(db.String(255))
    pitchdeck = db.Column(db.String(255))
    listed = db.Column(db.String(10))
    stage = db.Column(db.String(50))
    funds = db.Column(db.String(10))
    howmuch = db.Column(db.String(50))
    extra = db.Column(db.Text)
    hear = db.Column(db.String(50))


class TeamApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    portfolio = db.Column(db.String(300))
    location = db.Column(db.String(100), nullable=False)
    x_username = db.Column(db.String(100), nullable=False)
    telegram = db.Column(db.String(100))
    discord = db.Column(db.String(100))
    linkedin = db.Column(db.String(300))
    role = db.Column(db.String(100), nullable=False)
    skills = db.Column(db.String(300), nullable=False)
    years = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.String(50), nullable=False)
    why_us = db.Column(db.Text, nullable=False)
    what_excites = db.Column(db.Text)
    what_unique = db.Column(db.Text, nullable=False)


# Create DB
with app.app_context():
    db.create_all()


# Resources
class ContactResource(Resource):
    def post(self):
        data = request.get_json()
        try:
            contact = Contact(
                name=data.get('name'),
                company=data.get('company'),
                email=data.get('email'),
                reason=data.get('reason'),
                message=data.get('message')
            )
            db.session.add(contact)
            db.session.commit()
            return {"message": "Contact form submitted successfully."}, 201
        except SQLAlchemyError as e:
            return {"error": str(e)}, 500


class StartupResource(Resource):
    def post(self):
        data = request.get_json()
        try:
            application = StartupApplication(
                project_name=data.get('project_name'),
                email=data.get('email'),
                x_username=data.get('x_username'),
                telegram=data.get('telegram'),
                discord=data.get('discord'),
                linkedin=data.get('linkedin'),
                description=data.get('description'),
                service=data.get('service'),
                coingecko=data.get('coingecko'),
                pitchdeck=data.get('pitchdeck'),
                listed=data.get('listed'),
                stage=data.get('stage'),
                funds=data.get('funds'),
                howmuch=data.get('howmuch'),
                extra=data.get('extra'),
                hear=data.get('hear')
            )
            db.session.add(application)
            db.session.commit()
            return {"message": "Startup application submitted successfully."}, 201
        except SQLAlchemyError as e:
            return {"error": str(e)}, 500


class TeamResource(Resource):
    def post(self):
        data = request.get_json()
        try:
            team_app = TeamApplication(
                name=data.get('name'),
                email=data.get('email'),
                portfolio=data.get('portfolio'),
                location=data.get('location'),
                x_username=data.get('x_username'),
                telegram=data.get('telegram'),
                discord=data.get('discord'),
                linkedin=data.get('linkedin'),
                role=data.get('role'),
                skills=data.get('skills'),
                years=data.get('years'),
                duration=data.get('duration'),
                why_us=data.get('why_us'),
                what_excites=data.get('what_excites'),
                what_unique=data.get('what_unique')
            )
            db.session.add(team_app)
            db.session.commit()
            return {"message": "Team application submitted successfully."}, 201
        except SQLAlchemyError as e:
            return {"error": str(e)}, 500


# Routing the APIs
api.add_resource(ContactResource, '/api/contact')
api.add_resource(StartupResource, '/api/startup')
api.add_resource(TeamResource, '/api/team')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
