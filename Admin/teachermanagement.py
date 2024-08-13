from Teacher.teacher import Teacher
from file_manager import teacher_manager, group_manager, student_manager


def create_teacher():
    teacher_login = input("Create teacher's login: ").strip()
    teacher_password = input("Create teacher's password: ").strip()
    teacher_name = input("Enter teacher's full name: ").title().strip()
    teacher_email = input("Enter teacher's email: ").strip()
    teacher_gender = input("Enter teacher's gender: ").title().strip()

    teacher = Teacher(login=teacher_login, password=teacher_password, full_name=teacher_name, email=teacher_email, gender=teacher_gender)
    teacher_manager.add_data(teacher.__dict__)
    return True


def show_all_teachers():
    teacher_data = teacher_manager.read_data()

    if not teacher_data:  # If teacher_data is empty
        print("{:<30} {:<30}".format("No Teachers found", ''))
        return False

    print("Teachers:\n")
    print("{:<30} {:<30}".format("Full name", "Email"))
    print("-" * 50)

    for data in teacher_data:
        if data:  # Checking if data is not empty
            print("{:<30} {:<30}".format(data['full_name'], data['email']))

    return True


def add_entity_to_groups(entity_type):
    # Determine the correct file managers based on the entity type
    if entity_type == 'teacher':
        entity_manager = teacher_manager
    elif entity_type == 'student':
        entity_manager = student_manager
    else:
        print(f"Unknown entity type: {entity_type}")
        return False

    # Load the data for the entities and groups
    entities = entity_manager.read_data()
    groups = group_manager.read_data()

    if not groups:  # If no group is created yet
        print("{:<30} {:<30}".format("No groups created yet, please, first create groups", ''))
        return False

    if not entities:  # If no entities are found
        print(f"No {entity_type}s found")
        return False

    print(f"\nAvailable {entity_type}s:\n")
    print("{:<30} {:<30}".format("Full name", "Email"))
    print("-" * 50)
    for entity in entities:
        print("{:<30} {:<30}".format(entity['full_name'], entity['email']))

    print("\n\nAvailable groups:\n")
    print("{:<30} {:<30} {:<15} {:<10}".format("Group name", "Subject", "Start date", "Duration"))
    print("-" * 50)
    for group in groups:
        print("{:<30} {:<30} {:<15} {:<10}".format(group['name'], group['subject'], group['start'], group['duration']))

    entity_name = input(f"\nEnter {entity_type}'s full name: ").title().strip()
    group_name = input("Enter group name to add to entity: ").title().strip()

    # Find the entity and group in the respective lists
    selected_entity = next((entity for entity in entities if entity['full_name'] == entity_name), None)
    selected_group = next((group for group in groups if group['name'] == group_name), None)

    if not selected_entity:
        print(f"No such {entity_type} found:", entity_name)
        return False

    if not selected_group:
        print("No such group found:", group_name)
        return False

    # Add the selected group to the entity's 'groups' list
    selected_entity.setdefault('groups', []).append(selected_group)
    selected_group.setdefault(f'{entity_type}s', []).append({"full_name": entity_name})

    # Update the data
    entity_manager.write_data(entities)
    group_manager.write_data(groups)

    print(f"Group {group_name} added to {entity_type} {entity_name}'s groups list successfully.")
    return True


def remove_entity_from_groups(entity_type, entity_name_key, group_key, entity_manager):
    entity_name = input(f"Enter the full name of the {entity_type} to remove from groups: ").title().strip()
    groups = group_manager.read_data()
    entity_data = entity_manager.read_data()

    # Flag to check if any removal occurred
    removed = False

    # Remove the entity from the `group_key` list in each group
    for group in groups:
        if group_key in group:
            group[group_key] = [entity for entity in group[group_key] if entity[entity_name_key] != entity_name]

    # Find the entity in the list
    selected_entity = next((entity for entity in entity_data if entity[entity_name_key] == entity_name), None)

    if selected_entity and 'groups' in selected_entity:
        # Remove the group data from the entity's `groups` list
        selected_entity['groups'] = [g for g in selected_entity['groups'] if g['name'] not in [group['name'] for group in groups]]
        removed = True

    if removed:
        # Write updated data back to the files
        group_manager.write_data(groups)
        entity_manager.write_data(entity_data)
        print(f"{entity_type.capitalize()} '{entity_name}' has been removed from all associated groups.")
    else:
        print(f"No {entity_type} named '{entity_name}' found in any group.")

    return removed


def delete_teacher():
    teacher_login = input("Enter teacher's login to delete account: ").strip()
    teacher_data = teacher_manager.read_data()

    for teacher in teacher_data:
        if teacher['login'] == teacher_login:
            teacher_manager.delete_data(teacher_login, 'login')
            print(f"Teacher with login '{teacher_login}' has been deleted.")
            return True

    print(f"No teacher found with login '{teacher_login}'.")
    return False
