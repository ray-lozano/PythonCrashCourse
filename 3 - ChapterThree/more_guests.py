guest_list = ['Sydney', 'Justin', 'yaeris', 'erik']
print(f"Invite {guest_list[0]} to dinner.")
print(f"Invite {guest_list[1]} to dinner.")
print(f"Invite {guest_list[2]} to dinner.")
print(f"Invite {guest_list[3]} to dinner.")
print(f"{guest_list[3]} can't make it to dinner.")

removed_guest = guest_list.remove('erik')
print(guest_list)

print("Found a bigger table.")
guest_list.insert(0, 'lady')
guest_list.insert(3, 'thrall')
guest_list.append('zhu yuan')

print(guest_list)