-- Insert organizers (must be inserted first)
INSERT INTO organizer (name, contact_info) VALUES
('John Smith', 'john@example.com'),
('Emily Lee', 'emily.lee@example.com'),
('Karen Blake', 'karen.blake@example.com'),
('David Yang', 'david.yang@example.com'),
('Michael Brown', 'michael.b@example.com'),
('Sophia Turner', 'sophia.t@example.com'),
('James Wilson', 'james.w@example.com'),
('Olivia White', 'olivia.w@example.com'),
('Ethan Clark', 'ethan.c@example.com'),
('Lily Johnson', 'lily.j@example.com'),
('Brian Adams', 'brian.a@example.com'),
('Rachel Green', 'rachel.g@example.com'),
('Steve Parker', 'steve.p@example.com'),
('Grace Kim', 'grace.k@example.com'),
('Jason Lee', 'jason.l@example.com');

-- Insert venues (can be inserted right after organizer)
INSERT INTO venue (name, location, capacity) VALUES
('Grand Hall', '123 Main St', 300),
('Conference Center', '456 Elm St', 200),
('Skyline Ballroom', '789 Pine St', 150),
('Innovation Hub', '321 Maple Ave', 100),
('Metro Pavilion', '654 Cedar Rd', 250),
('Tech Tower', '987 Silicon Blvd', 180),
('Ocean View Center', '111 Beach Dr', 350),
('Downtown Arena', '222 Capital Way', 400),
('Mountain Retreat', '333 Hilltop Ln', 120),
('Civic Auditorium', '444 City Plz', 275),
('Harmony Hall', '555 Unity Blvd', 160),
('Metro Tech Space', '888 Code Rd', 210),
('Summit Center', '777 Peak Ln', 290),
('Lakeview Lodge', '999 Lakefront Dr', 180),
('Creative Commons', '101 Art St', 140);


-- Insert events (depends on venue and organizer IDs existing)
INSERT INTO event (name, date, venue_id, organizer_id) VALUES
('Tech Conference 2025', '2025-05-15', 1, 1),
('Startup Pitch Night', '2025-06-10', 2, 2),
('Women in Tech Summit', '2025-08-20', 3, 3),
('Green Future Forum', '2025-09-12', 4, 4),
('Cybersecurity Meetup', '2025-10-05', 5, 5),
('AI Expo', '2025-11-01', 6, 6),
('HealthTech Roundtable', '2025-11-15', 7, 7),
('UX Design Jam', '2025-12-02', 8, 8),
('Climate Action Panel', '2025-12-15', 9, 9),
('FinTech Workshop', '2026-01-05', 10, 10),
('DevOps Day', '2026-01-15', 11, 11),
('Design Sprint Weekend', '2026-02-01', 12, 12),
('SaaS Summit', '2026-02-20', 13, 13),
('Innovation Awards', '2026-03-10', 14, 14),
('Global Tech Meetup', '2026-03-25', 15, 15);

-- Insert attendees (depends on event IDs existing)
INSERT INTO attendee (name, email, event_id) VALUES
('Alice Johnson', 'alice.j@example.com', 1),
('Bob Martinez', 'bob.m@example.com', 1),
('Clara Davis', 'clara.d@example.com', 2),
('Samantha Lee', 'samantha.lee@example.com', 3),
('Tom Alvarez', 'tom.a@example.com', 4),
('Nina Kapoor', 'nina.k@example.com', 5),
('Daniel Cruz', 'daniel.cruz@example.com', 6),
('Ravi Patel', 'ravi.patel@example.com', 7),
('Angela Brooks', 'angela.b@example.com', 8),
('Marcus Hall', 'marcus.h@example.com', 9),
('Priya Singh', 'priya.s@example.com', 10),
('Lucas Gray', 'lucas.g@example.com', 11),
('Elena Torres', 'elena.t@example.com', 12),
('Mohamed Idris', 'mohamed.i@example.com', 13),
('Chloe Bennett', 'chloe.b@example.com', 14);

