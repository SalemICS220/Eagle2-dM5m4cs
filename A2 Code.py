class Guest:
    """Represents a hotel guest with booking history and feedback."""

    def __init__(self, name: str, contact_info: str, guest_id: int):
        """Initialize guest details."""
        self._name = name  # Private attribute for guest name
        self._contact_info = contact_info  # Private contact information
        self._guest_id = guest_id  # Unique ID for the guest
        self._reservations = []  # List of bookings made by the guest
        self._feedback = None  # One-to-one relation with Feedback
        self._service_requests = []  # Composition: Guest has service requests
        self._has_vip_status = False  # Indicates if the guest is a VIP

    def update_profile(self, new_name: str, new_contact: str):
        """Update the guest's profile information."""
        self._name = new_name  # Update name
        self._contact_info = new_contact  # Update contact details

    def request_service(self, service_type: str):
        """Request a hotel service."""
        request = ServiceRequest(len(self._service_requests) + 1, self, service_type)
        self._service_requests.append(request)  # Store service request

    def provide_feedback(self, rating: int, comments: str):
        """Submit feedback for the hotel."""
        self._feedback = Feedback(len(self._reservations), self, rating, comments)  # Store feedback

    def __str__(self):
        """Return string representation of the guest."""
        return f"Guest({self._name}, {self._contact_info}, ID: {self._guest_id})"


class VIPGuest(Guest):
    """Represents a VIP guest with additional privileges."""

    def __init__(self, name: str, contact_info: str, guest_id: int, vip_level: str, discount_rate: float):
        """Initialize a VIP guest with extra privileges."""
        super().__init__(name, contact_info, guest_id)  # Inherit Guest attributes
        self._vip_level = vip_level  # VIP level of the guest
        self._discount_rate = discount_rate  # Discount percentage for VIP

    def apply_discount(self, amount: float) -> float:
        """Apply VIP discount to a payment."""
        return amount - (amount * self._discount_rate / 100)  # Apply discount formula

    def upgrade_vip_level(self, new_level: str):
        """Upgrade the VIP level."""
        self._vip_level = new_level  # Set new VIP level

    def __str__(self):
        """Return string representation of a VIP guest."""
        return f"VIPGuest({self._name}, Level: {self._vip_level}, Discount: {self._discount_rate}%)"


class Room:
    """Represents a hotel room with its details."""

    def __init__(self, number: int, room_type: str, amenities: list, price: float):
        """Initialize room details."""
        self._room_number = number  # Room number
        self._type = room_type  # Type of the room
        self._amenities = amenities  # List of room amenities
        self._price_per_night = price  # Room cost per night
        self._availability_status = True  # Availability status of the room

    def update_availability(self, status: bool):
        """Update the availability of the room."""
        self._availability_status = status  # Change availability status

    def update_price(self, new_price: float):
        """Update the price per night."""
        self._price_per_night = new_price  # Set new price

    def __str__(self):
        """Return string representation of the room."""
        return f"Room({self._room_number}, {self._type}, Price: {self._price_per_night})"


class Booking:
    """Handles room bookings."""

    def __init__(self, booking_id: int, guest: Guest, room: Room, check_in: str, check_out: str):
        """Initialize booking details."""
        self._booking_id = booking_id  # Unique ID for the booking
        self._guest = guest  # Guest who made the booking
        self._room = room  # Room assigned to the booking
        self._check_in_date = check_in  # Check-in date
        self._check_out_date = check_out  # Check-out date

    def confirm_booking(self):
        """Confirm the room booking."""
        self._room.update_availability(False)  # Set room as occupied

    def cancel_booking(self):
        """Cancel the booking."""
        self._room.update_availability(True)  # Set room as available

    def __str__(self):
        """Return string representation of the booking."""
        return f"Booking({self._booking_id}, Guest: {self._guest._name}, Room: {self._room})"


class Hotel:
    """Represents a hotel with rooms and guests."""

    def __init__(self, hotel_id: int, name: str, location: str):
        """Initialize hotel details."""
        self._hotel_id = hotel_id  # Unique hotel ID
        self._name = name  # Hotel name
        self._location = location  # Hotel location
        self._rooms = []  # List of rooms in the hotel
        self._guests = []  # List of registered guests
        self._bookings = []  # List of bookings

    def add_room(self, room: Room):
        """Add a room to the hotel."""
        self._rooms.append(room)  # Append room to hotel

    def find_available_room(self, room_type: str):
        """Find an available room of a specific type."""
        for room in self._rooms:
            if room._type == room_type and room._availability_status:
                return room  # Return the first available room
        return None  # No available room found

    def register_guest(self, guest: Guest):
        """Register a new guest at the hotel."""
        self._guests.append(guest)  # Add guest to the guest list

    def process_booking(self, booking: Booking):
        """Process a new booking."""
        self._bookings.append(booking)  # Add booking to records

    def __str__(self):
        """Return string representation of the hotel."""
        return f"Hotel({self._name}, Location: {self._location}, Rooms: {len(self._rooms)}, Guests: {len(self._guests)})"


class Feedback:
    """Stores guest feedback on their stay."""

    def __init__(self, feedback_id: int, guest: Guest, rating: int, comment: str):
        """Initialize feedback details."""
        self._feedback_id = feedback_id  # Unique feedback ID
        self._guest = guest  # Guest providing feedback
        self._rating = rating  # Guest rating
        self._comment = comment  # Guest comments

    def update_feedback(self, new_comment: str, new_rating: int):
        """Update guest feedback."""
        self._comment = new_comment  # Modify comment
        self._rating = new_rating  # Modify rating

    def __str__(self):
        """Return string representation of the feedback."""
        return f"Feedback({self._guest._name}, Rating: {self._rating}, Comment: {self._comment})"


class ServiceRequest:
    """Handles service requests made by guests."""

    def __init__(self, request_id: int, guest: Guest, service_type: str):
        """Initialize service request details."""
        self._request_id = request_id  # Unique request ID
        self._guest = guest  # Guest who requested the service
        self._service_type = service_type  # Type of service requested

    def __str__(self):
        """Return string representation of the service request."""
        return f"ServiceRequest({self._request_id}, Guest: {self._guest._name}, Type: {self._service_type})"
