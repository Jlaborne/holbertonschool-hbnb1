#!/usr/bin/python3
# Persistence for amenities

from model.amenity import Amenity
from persistence.IPersistenceManager import IPersistenceManager


class AmenityRepository(IPersistenceManager):
    """Class for managing the persistence of amenities."""
    def __init__(self):
        self.amenities = {}
        self.next_id = 1

    def save(self, amenity):
        """Saves an amenity."""
        if not isinstance(amenity, Amenity):
            raise ValueError("Object is not an instance of Amenity")

        if amenity.amenity_id is None:
            amenity.amenity_id = self.next_id
            self.next_id += 1

        self.amenities[amenity.amenity_id] = amenity

    def get(self, amenity_id):
        """Fetches an amenity."""
        return self.amenities.get(amenity_id)

    def get_all(self):
        """Fetches all amenities."""
        return list(self.amenities.values())

    def update(self, amenity_id, new_amenity_data):
        """Updates an existing amenity."""
        amenity = self.amenities.get(amenity_id)
        if amenity:
            amenity.update_from_dict(new_amenity_data)
            return True
        return False

    def delete(self, amenity_id):
        """Deletes an existing amenity."""
        if amenity_id in self.amenities:
            del self.amenities[amenity_id]
            return True
        return False