veggie = input("¿Quiere la pizza vegetariana?(S/N): ")

print("Solo puede escoger un ingrediente.")
print("Escoga el número del ingrediente:")

if veggie.lower() == "s":
    ingrediente = input("1-Pimiento / 2-Tofu: ")
    print("La pizza elegida es vegetariana y tiene los sigueintes ingredientes: \nMozzarella")
    if ingrediente == "1":
        print("Pimiento")
    else:
        print("Tofu")
else:
    ingrediente = input("1-Peperoni / 2-Jamón / 3-Salmón: ")
    print("La pizza elegida no es vegetariana y tiene los siguientes ingredientes: \nMozzarella")
    if ingrediente == "1":
        print("Peperoni")
    elif ingrediente == "2":
        print("Jamón")
    else:
        print("Salmón")