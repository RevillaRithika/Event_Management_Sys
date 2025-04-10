-- Table: organizer
-- Functional Dependency: organizer_id → name, contact_info

CREATE TABLE organizer (
    organizer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    contact_info VARCHAR(150)
);

-- Table: venue
-- Functional Dependency: venue_id → name, location, capacity

CREATE TABLE venue (
    venue_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(150),
    capacity INT
);

-- Table: event
-- Functional Dependency: event_id → name, date, venue_id, organizer_id

CREATE TABLE event (
    event_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    date DATE,
    venue_id INT,
    organizer_id INT,
    FOREIGN KEY (venue_id) REFERENCES venue(venue_id) ON DELETE SET NULL,
    FOREIGN KEY (organizer_id) REFERENCES organizer(organizer_id) ON DELETE SET NULL
);

-- Table: attendee
-- Functional Dependency: attendee_id → name, email, event_id

CREATE TABLE attendee (
    attendee_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150),
    event_id INT,
    FOREIGN KEY (event_id) REFERENCES event(event_id) ON DELETE CASCADE
);
