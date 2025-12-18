"""
QUESTION:
Implement a function or class method named `rental_management` to manage the rental process for a vehicle rental company. The function should take the following parameters: 
- `vehicle_type` (string, either 'car' or 'motorcycle') 
- `rental_date` (date or integer representing days from now) 
- `advance_days` (integer representing days in advance the booking is made) 
- `deposit_amount` (integer representing percentage of the total rental cost) 
- `payment_method` (string, one of 'email', 'SMS', 'phone', 'Zalo', 'Viber') 
- `days_before_rental` (integer representing days before the rental date the booking is cancelled) 
- `deposit_received` (boolean indicating whether the deposit has been received) 
- `proof_of_residence` (boolean indicating whether the customer has provided proof of residence) 
- `driver_license` (boolean indicating whether the customer has provided a valid driver's license) 
- `id_card_or_passport` (boolean indicating whether the customer has provided an ID card or passport)

The function should return a string response based on the rental company's policies for booking confirmation, deposit payment, cancellation, and rental requirements.
"""

def rental_management(vehicle_type, rental_date, advance_days, deposit_amount, payment_method, days_before_rental, deposit_received, proof_of_residence, driver_license, id_card_or_passport):
    """
    This function manages the rental process for a vehicle rental company.
    
    Parameters:
    vehicle_type (str): Type of vehicle, either 'car' or 'motorcycle'.
    rental_date (date or int): Date of rental or days from now.
    advance_days (int): Days in advance the booking is made.
    deposit_amount (int): Percentage of the total rental cost.
    payment_method (str): Method of payment, one of 'email', 'SMS', 'phone', 'Zalo', 'Viber'.
    days_before_rental (int): Days before the rental date the booking is cancelled.
    deposit_received (bool): Whether the deposit has been received.
    proof_of_residence (bool): Whether the customer has provided proof of residence.
    driver_license (bool): Whether the customer has provided a valid driver's license.
    id_card_or_passport (bool): Whether the customer has provided an ID card or passport.
    
    Returns:
    str: A string response based on the rental company's policies.
    """

    # Booking confirmation
    if advance_days >= 2 and vehicle_type == 'car':
        booking_response = "Booking confirmed. Please pay the deposit within 24 hours."
    elif advance_days >= 3 and vehicle_type == 'motorcycle':
        booking_response = "Booking confirmed. Please pay the deposit within 24 hours."
    else:
        booking_response = "Booking cannot be confirmed due to insufficient advance notice."

    # Deposit payment
    if 30 <= deposit_amount <= 50 and payment_method in ['email', 'SMS', 'phone', 'Zalo', 'Viber']:
        payment_response = "Deposit payment confirmed. Your booking is secured."
    else:
        payment_response = "Invalid deposit amount or payment method. Please contact customer support."

    # Cancellation policy
    if days_before_rental > 5:
        if deposit_received and payment_method in ['email', 'SMS', 'phone', 'Zalo', 'Viber']:
            cancellation_response = "Full refund processed for the cancelled booking."
        else:
            cancellation_response = "No refund can be processed for the cancelled booking."
    else:
        cancellation_response = "No refund can be processed for the cancelled booking."

    # Rental requirements
    if proof_of_residence and driver_license and id_card_or_passport:
        requirement_response = "Rental requirements are met. Enjoy your trip!"
    else:
        requirement_response = "Please provide all necessary documents to fulfill the rental requirements."

    # Return a combined response
    return f"{booking_response}\n{payment_response}\n{cancellation_response}\n{requirement_response}"