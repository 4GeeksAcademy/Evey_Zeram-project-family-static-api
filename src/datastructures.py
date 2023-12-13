
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure: # es constructor qué va a hacer la clase
    # __ es algo particular. 
    #esta clase tiene 5 métodos
    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = [
           {"id": self._generate_id(),
            "first_name": "John",
            "last_name": last_name,
            "age": 33,
            "lucky_number":[10,14,15]},
           {"id": self._generate_id(),
            "first_name": "Jane",
            "last_name": last_name,
            "age": 35,
            "lucky_number": [1,4,3]},
           {"id": self._generate_id(),
            "first_name": "Jimmy",
            "last_name": last_name,
            "age": 5,
            "lucky_number": [1]}]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generate_id(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member['id'] = self._generate_id()
        member['last_name'] = self.last_name
        self._members.append(member)

# pass evita que de error aunque esté vacío
    def delete_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member ['id'] == id:
                self._members.remove(member)
                return True
        return False

    # def update_member(self,id):
    #     for member in self._members:
    #         if member ['id'] == id:



    def get_member(self, id):
        for item in self._members:
            if item['id'] == id:
                return item
        return False

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
