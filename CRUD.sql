-- CREATE: Add a new event
INSERT INTO event (name, date, venue_id, organizer_id)
VALUES ('AI Expo', '2025-07-01', 1, 1);

-- READ: List all events with organizer and venue details
SELECT e.name AS event_name, e.date, o.name AS organizer, v.name AS venue
FROM event e
JOIN organizer o ON e.organizer_id = o.organizer_id
JOIN venue v ON e.venue_id = v.venue_id;

-- UPDATE: Change venue of an event
UPDATE event
SET venue_id = 2
WHERE event_id = 1;

-- DELETE: Remove an attendee
DELETE FROM attendee
WHERE attendee_id = 3;
