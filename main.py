import modul


status = modul.random_state()
print(status)
status_str = modul.status_to_str(status)
modul.print_matrix(status_str)
print()
status_str2=modul.status_to_str2(status)
print(status_str2)