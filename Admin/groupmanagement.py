import datetime
from dateutil.relativedelta import relativedelta
from file_manager import group_manager


class Group:
    def __init__(self, name, subject, start, end, duration, weekdays, time, room, description):
        self.name = name
        self.subject = subject
        self.start = start
        self.end = end
        self.duration = duration
        self.weekdays = weekdays
        self.time = time
        self.room = room
        self.description = description
        self.teachers = []
        self.status = False

    def to_dict(self):
        return {
            "name": self.name,
            "subject": self.subject,
            "start": self.start.strftime("%d.%m.%Y"),
            "end": self.end.strftime("%d.%m.%Y"),
            "duration": self.duration,
            "weekdays": self.weekdays,
            "time": self.time,
            "room": self.room,
            "description": self.description,
            "teachers": self.teachers,
            "status": self.status
        }


def create_group():
    group_name = input("Enter a group name: ").title().strip()
    subject = input("Enter a subject name for the group: ").title().strip()
    start_date_str = input("Enter start date (ex: 18.03.2024): ")
    duration_months = int(input("Enter duration in months: "))
    weekdays_str = input("Enter weekdays (ex: Monday, Wednesday, Friday): ").title().strip()
    time_str = input("Enter time (ex: 13:00-15:00): ").strip()
    room = input("Enter room number or room name (ex: Yandex room): ").strip()
    group_description = input("Enter a description of the group: ").capitalize().strip()

    # Parse the start date
    start_date = datetime.datetime.strptime(start_date_str, "%d.%m.%Y")

    # Calculate the end date by adding the duration in months
    end_date = start_date + relativedelta(months=duration_months)

    # Create the Group object with the calculated end date
    group = Group(group_name, subject, start_date,
                  end_date, duration_months, weekdays_str,
                  time_str, room, group_description)

    # Store the group data
    group_manager.add_data(group.to_dict())


def show_all_groups():
    groups = group_manager.read_data()  # Fetch the group data from storage

    if not groups:  # If no groups are created yet
        print("{:<20} {:<20}".format("No groups created yet", ''))
        return False

    print("All groups:\n")
    print("{:<20} {:<20} {:<15} {:<10} {:<10} {:<30}".format("Group name", "Subject", "Start time", "Duration", "Room", "Teachers"))
    print("-" * 100)

    try:
        for group in groups:
            if group:  # Checking if group is not empty
                teachers_list = ', '.join(teacher['full_name'] for teacher in group['teachers'])
                print("{:<20} {:<20} {:<15} {:<10} {:<10} {:<30}".format(
                    group['name'], group['subject'], group['start'], group['duration'],
                    group['room'], teachers_list))
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def delete_group():
    group_name = input("Enter a group name: ").title().strip()
    group_data = group_manager.read_data()
    if group_name not in group_data:
        print("Group not found, try again later")
        return False

    for data in group_data:
        if data['name'] == group_name:
            group_manager.delete_group(data)
            print("Group deleted successfully")
            return True
