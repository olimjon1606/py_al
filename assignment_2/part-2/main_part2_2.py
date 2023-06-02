def dfs(guest, dislike, table_assignment, table):
    table_assignment[guest] = table

    for disliked_guest in dislike[guest]:
        if table_assignment[disliked_guest] == table:
            return False

        if table_assignment[disliked_guest] == 0 and not dfs(disliked_guest, dislike, table_assignment, 3 - table):
            return False

    return True


def set_up_sitting_scheme(invited_guests, dislikes):
    table_assignment = {}  # Stores the table assignment for each guest
    dislike = {}  # Stores the dislikes for each guest

    for guest in invited_guests:
        table_assignment[guest] = 0
        dislike[guest] = []

    for pair in dislikes:
        guest1, guest2 = pair
        dislike[guest1].append(guest2)
        dislike[guest2].append(guest1)

    for guest in invited_guests:
        if table_assignment[guest] == 0 and not dfs(guest, dislike, table_assignment, 1):
            return "No sitting scheme possible."

    table1 = [guest for guest in invited_guests if table_assignment[guest] == 1]
    table2 = [guest for guest in invited_guests if table_assignment[guest] == 2]

    return table1, table2


# Example usage
invited_guests = ['Alice', 'Bob', 'Charlie', 'Dave']
dislikes = [('Alice', 'Bob'), ('Charlie', 'Dave')]

sitting_scheme = set_up_sitting_scheme(invited_guests, dislikes)

if sitting_scheme == "No sitting scheme possible.":
    print("No sitting scheme is possible due to dislikes.")
else:
    table1, table2 = sitting_scheme
    print("Table 1:", table1)
    print("Table 2:", table2)
