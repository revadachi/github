def kenaRazia(date, data):
    # Initialize an empty dictionary to store the violators
    violators = {}

    # Define the locations where odd-even plate number rule is enforced
    ganjilGenapLocations = ["Gajah Mada", "Hayam Wuruk", "Sisingamangaraja", "Panglima Polim", "Fatmawati", "Tomang Raya"]

    # Check if the date is within the valid range (1 to 31)
    if date < 1 or date > 31:
        return "Invalid date. Please provide a date between 1 and 31."

    # Iterate over the data list to check for violations
    for vehicle in data:
        # Check if the vehicle is a car and is passing through a ganjilGenapLocation
        if vehicle['type'] == "Mobil" and any(route in ganjilGenapLocations for route in vehicle['rute']):
            # Extract the last digit from the plate number
            last_digit = int(vehicle['plat'].split(" ")[1][-1])

            # Check if the last digit is odd for even date or even for odd date
            is_violation = (date % 2 == 0 and last_digit % 2 != 0) or (date % 2 != 0 and last_digit % 2 == 0)

            if is_violation:
                # Update the violators dictionary
                if vehicle['name'] in violators:
                    violators[vehicle['name']] += 1
                else:
                    violators[vehicle['name']] = 1

    # Convert the violators dictionary to the required output format
    result = [{'name': name, 'tilang': count} for name, count in violators.items()]
    return result

print(
    kenaRazia(27, [
        {'name': "Denver", 'plat': "B 2791 KDS", 'type': "Mobil", 'rute': ["TB Simatupang", "Panglima Polim", "Depok", "Senen Raya"]},
        {'name': "Toni", 'plat': "B 1212 JBB", 'type': "Mobil", 'rute': ["Pintu Besar Selatan", "Panglima Polim", "Depok", "Senen Raya", "Kemang"]},
        {'name': "Stark", 'plat': "B 444 XSX", 'type': "Motor", 'rute': ["Pondok Indah", "Depok", "Senen Raya", "Kemang"]},
        {'name': "Anna", 'plat': "B 678 DD", 'type': "Mobil", 'rute': ["Fatmawati", "Panglima Polim", "Depok", "Senen Raya", "Kemang", "Gajah Mada"]}
    ])
)