from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Organizer, Venue, Event, Attendee
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    events = Event.query.all()
    return render_template('index.html', events=events)

@app.route('/events')
def events():
    events = Event.query.all()
    return render_template('events.html', events=events)

@app.route('/events/create', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        name = request.form['name']
        date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
        venue_id = request.form['venue_id']
        organizer_id = request.form['organizer_id']
        
        event = Event(name=name, date=date, venue_id=venue_id, organizer_id=organizer_id)
        db.session.add(event)
        db.session.commit()
        flash('Event created successfully!')
        return redirect(url_for('events'))
    
    venues = Venue.query.all()
    organizers = Organizer.query.all()
    return render_template('create_event.html', venues=venues, organizers=organizers)

@app.route('/events/<int:event_id>/edit', methods=['GET', 'POST'])
def edit_event(event_id):
    event = Event.query.get_or_404(event_id)
    if request.method == 'POST':
        event.name = request.form['name']
        event.date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
        event.venue_id = request.form['venue_id']
        event.organizer_id = request.form['organizer_id']
        
        db.session.commit()
        flash('Event updated successfully!')
        return redirect(url_for('events'))
    
    venues = Venue.query.all()
    organizers = Organizer.query.all()
    return render_template('edit_event.html', event=event, venues=venues, organizers=organizers)

@app.route('/events/<int:event_id>/delete', methods=['POST'])
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    flash('Event deleted successfully!')
    return redirect(url_for('events'))

@app.route('/events/<int:event_id>/attendees')
def event_attendees(event_id):
    event = Event.query.get_or_404(event_id)
    return render_template('attendees.html', event=event)

@app.route('/events/<int:event_id>/attendees/add', methods=['POST'])
def add_attendee(event_id):
    name = request.form['name']
    email = request.form['email']
    
    attendee = Attendee(name=name, email=email, event_id=event_id)
    db.session.add(attendee)
    db.session.commit()
    flash('Attendee added successfully!')
    return redirect(url_for('event_attendees', event_id=event_id))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 