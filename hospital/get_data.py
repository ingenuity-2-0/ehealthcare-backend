from .models import Hospital, Works


def all_hospital_information():
    hospital_objects = Hospital.objects.all()
    hospital_list = extract_information(hospital_objects)
    return hospital_list


def extract_information(objects):
    hospital_list = []
    for h in objects:
        name = h.name
        h_id = h.hospital_id
        city = h.city
        address = h.address
        phone = h.phone
        temp = {
            'hospital_name': name,
            'hospital_id': h_id,
            'city': city,
            'address': address,
            'phone': phone
        }
        hospital_list.append(temp)
    return hospital_list


def hospital_details_information(hospital_id):
    hospital_object = Hospital.objects.get(hospital_id=hospital_id)
    image = hospital_object.image
    name = hospital_object.name
    city = hospital_object.city
    address = hospital_object.address
    phone = hospital_object.phone
    related_hospital = Hospital.objects.filter(city__iregex=city)[0:3]
    related_hospital_list = []
    for x in related_hospital:
        r_name = x.name
        r_city = x.city
        r_image = x.image
        r_id = x.hospital_id
        temp = {
            'r_id': r_id,
            'r_name': r_name,
            'r_city': r_city,
            'r_image': r_image
        }
        related_hospital_list.append(temp)
    hospital_info = {
        'hospital_name': name,
        'hospital_image': image,
        'hospital_city': city,
        'hospital_address': address,
        'hospital_phone': phone,
        'related_hospital': related_hospital_list
    }
    return hospital_info
