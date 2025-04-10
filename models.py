from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Organizer(db.Model):
    __tablename__ = 'organizer'
    organizer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(150))
    events = db.relationship('Event', backref='organizer', lazy=True)

class Venue(db.Model):
    __tablename__ = 'venue'
    venue_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(150))
    capacity = db.Column(db.Integer)
    events = db.relationship('Event', backref='venue', lazy=True)

class Event(db.Model):
    __tablename__ = 'event'
    event_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.venue_id', ondelete='SET NULL'))
    organizer_id = db.Column(db.Integer, db.ForeignKey('organizer.organizer_id', ondelete='SET NULL'))
    attendees = db.relationship('Attendee', backref='event', lazy=True)

class Attendee(db.Model):
    __tablename__ = 'attendee'
    attendee_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150))
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id', ondelete='CASCADE')) 