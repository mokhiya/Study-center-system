import datetime
from dateutil.relativedelta import relativedelta
from file_manager import group_manager

class Group:
    def __init__(self, name, subject, start, end, duration, description):
        self.name = name
        self.subject = subject
        self.start = start
        self.end = end
        self.duration = duration
        self.description = description
        self.status = False

    def to_dict(self):
        # Convert the group object to a dictionary for storage
        return {
            "name": self.name,
            "subject": self.subject,
            "start": self.start.strftime("%d.%m.%Y"),
            "end": self.end.strftime("%d.%m.%Y"),
            "duration": self.duration,
            "description": self.description
        }


def create_group():
    group_name = input("Enter a group name: ")
    subject = input("Enter a subject name for the group: ")
    start_date_str = input("Enter start date (ex: 18.03.2024): ")
    duration_months = int(input("Enter duration in months: "))
    group_description = input("Enter a description of the group: ")

    # Parse the start date
    start_date = datetime.datetime.strptime(start_date_str, "%d.%m.%Y")

    # Calculate the end date by adding the duration in months
    end_date = start_date + relativedelta(months=duration_months)

    # Create the Group object with the calculated end date
    group = Group(group_name, subject, start_date, end_date, duration_months, group_description)

    # Store the group data
    group_manager.add_data(group.to_dict())
