# 1. crea un tuple
empty_tuple = ()
print('Tuple: ', empty_tuple)

# 2. crea un tuple con nombres
brothers = ('Noe',"Tiago","Ragnar")
print("Mis hermanos:", brothers)
sister = ("Odette","Veronica","Gabriela")
print("Mis hermanas:", sister)

# 3. crea un tuple uniendo los tuples pasados
siblings = brothers + sister
print("Mis hermanos son:",siblings)

# 4. Cuantos hermanos tienes
print("En total son:",len(siblings))

# 5. modifica la lista y agraga a tu papa y mama y asigna una nueva tuple
lst_brother = list(brothers)
lst_brother.append("Papa Abel")
brother = tuple(lst_brother)
print(brother)
lst_sister = list(sister)
lst_sister.append(" Mama Irma")
sister = tuple(lst_sister)
print(sister)
family_members = brother + sister
print("los miembros de mi familia son:",family_members)

# Segundo bloque de ejercicios

# 1. Divide ambas listas de hermanos y crea una nueva tuple para papa y mama
papa = family_members[3]
mama = family_members[7]
parents = papa + mama
print(parents)

# 2. crea tres tuples, unelas y asigna a una nueva variable
frutas = ("manzana","fresas","kiwi")
verduras = ("tomate","chile","cebolla")
animales = ("tiburon","tigre", "rinoceronte")
food_stuff_tp = frutas + verduras + animales
print(food_stuff_tp)

# 3. cambia la variable a lista 
print(len(food_stuff_tp))
food_stuff_lt = list(food_stuff_tp)

# 4. corta el elemento de enmedio de la lista
food_stuff_lt.pop(4)
print(food_stuff_lt)

# 5.borra los tres primeros elementos y los ultimos 3 elmentos
del food_stuff_lt[0:3]
del food_stuff_lt[-1:-4:-1]
print(food_stuff_lt)

# 6. cambia la lista a tplu y elimina
food_stuff_tp = tuple(food_stuff_lt)
del food_stuff_tp

# 7. compruebe si existe un elemento en la tuple
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)





