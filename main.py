import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Configure database URI (example: SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///defifoundry.db'

# Initialize Flask-SQLAlchemy
db = SQLAlchemy(app)


# Define a sample model
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
    __tablename__ = 'team_applications'

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





# Create database tables (run this once, typically in a setup script or shell)
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template('About.html')  # Replace with `render_template("about.html")` if you create one

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        company = request.form.get('company')
        email = request.form.get('email')
        reason = request.form.get('reason')
        message = request.form.get('message')

        # Create a new Contact instance
        contact_message = Contact(
            name=name,
            company=company,
            email=email,
            reason=reason,
            message=message
        )

        # Save to the database
        db.session.add(contact_message)
        db.session.commit()

        # Redirect to homepage after successful submission
        return redirect(url_for('index'))

    return render_template('Contact.html')



@app.route("/startup", methods=['GET', 'POST'])
def startup():
    if request.method == 'POST':
        data = request.form
        application = StartupApplication(
            project_name=data.get('name'),
            email=data.get('email'),
            x_username=data.get('x'),
            telegram=data.get('telegram'),
            discord=data.get('discord'),
            linkedin=data.get('linkedin'),
            description=data.get('description'),
            service=data.get('service'),
            coingecko=data.get('coingecko'),
            pitchdeck=data.get('pitchdeck'),
            listed=request.form.get('listed'),
            stage=data.get('stage'),
            funds=data.get('funds'),
            howmuch=data.get('howmuch'),
            extra=data.get('Anything'),
            hear=data.get('hear')
        )
        db.session.add(application)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('Startup.html')


@app.route("/team", methods=['GET', 'POST'])
def team():
    if request.method == 'POST':
        data = request.form

        # Create a new team application instance
        team_application = TeamApplication(
            name=data.get('name'),
            email=data.get('email'),
            portfolio=data.get('portfolio'),
            location=data.get('location'),
            x_username=data.get('x'),
            telegram=data.get('telegram'),
            discord=data.get('discord'),
            linkedin=data.get('linkedin'),
            role=data.get('role'),
            skills=data.get('skills'),
            years=data.get('Years'),
            duration=data.get('duration'),
            why_us=data.get('whyus'),
            what_excites=data.get('what'),
            what_unique=data.getlist('what')[-1]  # Last textarea value
        )

        db.session.add(team_application)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('Team.html')



@app.route('/whitepaper')
def whitepaper():
    return render_template('Whitepaper.html')


@app.route('/terms')
def terms_of_service():
    return render_template('TermsOfService.html')


@app.route('/privacy')
def privacy_policy():
    return render_template('PrivacyPolicy.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # fallback to 5000 locally
    app.run(host="0.0.0.0", port=port, debug=True)
