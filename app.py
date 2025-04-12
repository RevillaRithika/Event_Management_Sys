from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Organizer, Venue, Event, Attendee
from config import Config
from datetime import datetime
import re  # For email validation

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
    return render_template('events_list.html', events=events)

@app.route('/events/create', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        name = request.form['name']
        date_str = request.form['date']
        venue_id = request.form['venue_id']
        organizer_id = request.form['organizer_id']

        if not name or not date_str or not venue_id or not organizer_id:
            flash('All fields are required!', 'error')
            return redirect(request.url)

        date = datetime.strptime(date_str, '%Y-%m-%d').date()

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
        name = request.form['name']
        date_str = request.form['date']
        venue_id = request.form['venue_id']
        organizer_id = request.form['organizer_id']

        if not name or not date_str or not venue_id or not organizer_id:
            flash('All fields are required!', 'error')
            return redirect(request.url)

        event.name = name
        event.date = datetime.strptime(date_str, '%Y-%m-%d').date()
        event.venue_id = venue_id
        event.organizer_id = organizer_id

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

    if not name or not email:
        flash('Name and email are required!', 'error')
        return redirect(request.url)

    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_pattern, email):
        flash('Invalid email format!', 'error')
        return redirect(request.url)

    attendee = Attendee(name=name, email=email, event_id=event_id)
    db.session.add(attendee)
    db.session.commit()
    flash('Attendee added successfully!')
    return redirect(url_for('event_attendees', event_id=event_id))

@app.route('/venues')
def venues():
    venues = Venue.query.all()
    return render_template('venues.html', venues=venues)

@app.route('/venues/add', methods=['GET', 'POST'])
def add_venue():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        capacity = request.form['capacity']

        venue = Venue(name=name, location=location, capacity=capacity)
        db.session.add(venue)
        db.session.commit()
        flash('Venue added successfully!', 'success')
        return redirect(url_for('venues'))

    return render_template('add_venue.html')

@app.route('/venues/<int:venue_id>/edit', methods=['GET', 'POST'])
def edit_venue(venue_id):
    venue = Venue.query.get_or_404(venue_id)
    if request.method == 'POST':
        venue.name = request.form['name']
        venue.location = request.form['location']
        venue.capacity = int(request.form['capacity'])

        db.session.commit()
        flash('Venue updated successfully!')
        return redirect(url_for('venues'))

    return render_template('edit_venue.html', venue=venue)

@app.route('/venues/<int:venue_id>/delete', methods=['POST'])
def delete_venue(venue_id):
    venue = Venue.query.get_or_404(venue_id)
    db.session.delete(venue)
    db.session.commit()
    flash('Venue deleted successfully!')
    return redirect(url_for('venues'))

# --------------------------
# Organizers CRUD
# --------------------------

@app.route('/organizers')
def organizers():
    organizers = Organizer.query.all()
    return render_template('organizers.html', organizers=organizers)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)