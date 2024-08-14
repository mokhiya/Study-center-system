import os
import json


class JsonManager:
    """
    This class provides an interface for managing JSON data files.

    Attributes:
    - file_name (str): The name of the JSON file to manage.

    Methods:
    - _file_exists_and_not_empty(): Checks if the file exists and is not empty.
    - read_data(): Reads and returns the data from the JSON file.
    - write_data(data): Writes the provided data to the JSON file.
    - add_data(data): Adds a new record to the JSON file.
    - update_data(identifier, key, new_data): Updates an existing record in the JSON file.
    - delete_data(identifier, key): Deletes a record from the JSON file based on a specified key.
    """

    def __init__(self, file_name):
        """
        This function initializes the JsonManager class with a file name.

        Parameters:
        - file_name (str): The name of the JSON file to manage.
        """
        self.file_name = file_name

    def _file_exists_and_not_empty(self):
        """
        This function checks if the file exists and is not empty.

        Returns:
        - bool: True if the file exists and is not empty, False otherwise.
        """
        return os.path.exists(self.file_name) and os.path.getsize(self.file_name) > 0

    def read_data(self):
        """
        This function reads and returns the data from the JSON file.

        Returns:
        - list: The data from the JSON file or an empty list if the file is empty or doesn't exist.
        """
        if self._file_exists_and_not_empty():
            with open(self.file_name, 'r') as file:
                return json.load(file)
        return []

    def write_data(self, data):
        """
        This function writes the provided data to the JSON file, replacing any existing content.

        Parameters:
        - data (list): The data to write to the JSON file.
        """
        with open(self.file_name, 'w') as file:
            json.dump(data, file, indent=4)

    def add_data(self, data: dict):
        """
        This function adds a new record (dictionary) to the JSON file.

        Parameters:
        - data (dict): The new record to add to the JSON file.

        Returns:
        - str: A success message indicating the data was added successfully.
        """
        all_data = self.read_data()
        all_data.append(data)
        self.write_data(all_data)
        return "Data added successfully"

    def update_data(self, identifier, key, new_data):
        """
        This function updates an existing record in the JSON file based on the specified key and identifier.

        Parameters:
        - identifier (str): The value to search for within the specified key.
        - key (str): The key to identify the record to update.
        - new_data (dict): The new data to update the record with.

        Returns:
        - bool: True if the record was updated successfully, False otherwise.
        """
        all_data = self.read_data()
        updated = False

        for item in all_data:
            if key in item and item[key] == identifier:
                item.update(new_data)
                updated = True
                break

        if updated:
            self.write_data(all_data)
            return True
        return False

    def delete_data(self, identifier, key):
        """
        This function deletes a record from the JSON file based on the specified key and identifier.

        Parameters:
        - identifier (str): The value to search for within the specified key.
        - key (str): The key to identify the record to delete.

        Returns:
        - bool: True if any records were deleted, False otherwise.
        """
        all_data = self.read_data()
        updated_data = [item for item in all_data if item[key] != identifier]

        self.write_data(updated_data)
        return len(updated_data) < len(all_data)


student_manager = JsonManager("Student/students.json")
teacher_manager = JsonManager("Teacher/teachers.json")
admin_manager = JsonManager("Admin/admins.json")
group_manager = JsonManager("Admin/groups.json")
