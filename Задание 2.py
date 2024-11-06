# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separator=","):
    set_first_group = set(first_group.split(separator))
    set_second_group = set(second_group.split(separator))

    common_participants = set_first_group.intersection(set_second_group)
    common_participants = list(common_participants)

    return sorted(common_participants)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, separator = '|'))
