meu_set = {"Maçã", "Banana", "Cereja"}
set_duplicado = {"Maçã", "Banana", "Maçã"}
print(set_duplicado) # Resultará em {'Maçã', 'Banana'}

if "Banana" in meu_set:
    print("A banana está no conjunto!")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))         # {1, 2, 3, 4, 5, 6}
print(A.intersection(B))  # {3, 4}
print(A.difference(B))    # {1, 2}
