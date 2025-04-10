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

-- 1. List All Events with Venue and Organizer Info
SELECT 
    e.EventID,
    e.Name AS EventName,
    e.Date,
    v.Name AS VenueName,
    o.Name AS OrganizerName,
    v.Location
FROM Event e
JOIN Venue v ON e.VenueID = v.VenueID
JOIN Organizer o ON e.OrganizerID = o.OrganizerID
ORDER BY e.Date DESC;


-- 2. List Attendees and the Events They’re Attending
SELECT 
    a.AttendeeID,
    a.Name AS AttendeeName,
    e.Name AS EventName,
    e.Date
FROM Attendee a
JOIN `Order` o ON a.AttendeeID = o.AttendeeID
JOIN Event e ON o.EventID = e.EventID
ORDER BY e.Date;


-- 3. Get Events That Have More Than 50 Attendees
SELECT 
    e.EventID,
    e.Name AS EventName,
    COUNT(o.OrderID) AS AttendeeCount
FROM Event e
JOIN `Order` o ON e.EventID = o.EventID
GROUP BY e.EventID, e.Name
HAVING COUNT(o.OrderID) > 50;


-- 4. List Products and Their Suppliers with Current Inventory
SELECT 
    p.ProductID,
    p.Name AS ProductName,
    s.Name AS SupplierName,
    COALESCE(SUM(it.Quantity), 0) AS CurrentInventory
FROM Product p
LEFT JOIN Supplier s ON p.SupplierID = s.SupplierID
LEFT JOIN InventoryTransaction it ON p.ProductID = it.ProductID
GROUP BY p.ProductID, p.Name, s.Name;


-- 5. Find Events at the Largest Capacity Venues
SELECT 
    e.Name AS EventName,
    v.Name AS VenueName,
    v.Capacity
FROM Event e
JOIN Venue v ON e.VenueID = v.VenueID
WHERE v.Capacity = (
    SELECT MAX(Capacity)
    FROM Venue
);


-- 6. Events That Haven’t Had Any Orders Yet
SELECT 
    e.EventID,
    e.Name AS EventName,
    e.Date
FROM Event e
WHERE NOT EXISTS (
    SELECT 1
    FROM `Order` o
    WHERE o.EventID = e.EventID
);

