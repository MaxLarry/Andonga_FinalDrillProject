# Andonga_FinalDrillProject

Project Details
This project is a Flask-based API for a hotel management system. It provides endpoints for managing guests, bookings, and room types. The API interacts with a MySQL database to retrieve and store data.

Installation Instructions
To run this project, follow the steps below:

-Clone the project repository to your local machine then create a environment inside of clone repo.
-Install the required libraries needded in this project.
-Set up the MySQL database and update the database configuration in the api.py file.
-Start the Flask development server.

Basic authentication:
Username: larry
Password: 12345


Usage Examples

Welcome Page
-Endpoint: /
-Method: GET
-Authentication: Basic Auth
-Example Request: GET / with Basic Auth credentials
-Example Response: HTML response with a welcome message.

Get Guests
-Endpoint: /guests
-Method: GET
-Authentication: Basic Auth
-Example Request: GET /guests with Basic Auth credentials
-Example Response: JSON response with a list of guests.

Get Bookings
-Endpoint: /bookings
-Method: GET
-Authentication: Basic Auth
-Example Request: GET /bookings with Basic Auth credentials
-Example Response: JSON response with a list of bookings.

Get Room Types
-Endpoint: /Room_types
-Method: GET
-Authentication: Basic Auth
-Example Request: GET /Room_types with Basic Auth credentials
-Example Response: JSON response with a list of room types.

Get Guest by ID
-Endpoint: /guests/<id>
-Method: GET
-Authentication: Basic Auth
-Example Request: GET /guests/1 with Basic Auth credentials
-Example Response: JSON response with the guest details.

Search Guests
-Endpoint: /guests/search
-Method: GET
-Authentication: Basic Auth
-Query Parameters: firstname, lastname
-Example Request: GET /guests/search?firstname=John&lastname=Doe with Basic Auth credentials
-Example Response: JSON response with the search results.

Get Booking by Guest ID
-Endpoint: /guests/<id>/booking
-Method: GET
-Authentication: Basic Auth
-Example Request: GET /guests/<id>/booking with Basic Auth credentials
-Example Response: JSON response with the guest's booking details.

Add Guest
-Endpoint: /guests
-Method: POST
-Authentication: Basic Auth
-Example Request: POST /guests with Basic Auth credentials and guest data in the request body
-Example Response: JSON response confirming the successful addition of the guest.

Update Guest
-Endpoint: /guests/<id>
-Method: PUT
-Authentication: Basic Auth
-Example Request: PUT /guests/<id> with Basic Auth credentials and updated guest data in the request body
-Example Response: JSON response confirming the successful update of the guest.
-Please note that for the POST and PUT requests, the request body should contain the necessary guest information in JSON format.

Delete Guest
-Endpoint: /guests/<id>
-Method: DELETE
-Authentication: Basic Auth
-Example Request: DELETE /guests/<id> with Basic Auth credentials
-Example Response: JSON response confirming the successful deletion of the guest.

Please note that for all the POST, PUT, and DELETE requests, appropriate authentication and request bodies are required.