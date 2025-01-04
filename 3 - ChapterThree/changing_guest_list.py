guest_list = ['Sydney', 'Justin', 'yaeris', 'erik']
print(f"Invite {guest_list[0]} to dinner.")
print(f"Invite {guest_list[1]} to dinner.")
print(f"Invite {guest_list[2]} to dinner.")
print(f"Invite {guest_list[3]} to dinner.")
print(f"{guest_list[3]} can't make it to dinner.")

removed_guest = guest_list.remove('erik')
print(guest_list)