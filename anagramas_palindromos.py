def remove_espacos(texto):
    nova_str = ""
    for c in texto:
        if c != " ":
            nova_str = nova_str + c.lower()
    return nova_str

def sao_anagramas(str1, str2):
    s1 = remove_espacos(str1)
    s2 = remove_espacos(str2)
    
    if len(s1) != len(s2):
        return False
        
    # Verifica se cada caractere de s1 está presente na mesma quantidade em s2
    for letra in s1:
        # Conta ocorrências manuais sem usar .count() nativo avançado
        cont1 = 0
        cont2 = 0
        for c in s1:
            if c == letra:
                cont1 = cont1 + 1
        for c in s2:
            if c == letra:
                cont2 = cont2 + 1
        if cont1 != cont2:
            return False
            
    return True

print("=== Verificador de Anagramas ===")
palavra_a = input("Digite a primeira palavra ou frase: ")
palavra_b = input("Digite a segunda palavra ou frase: ")

if sao_anagramas(palavra_a, palavra_b):
    print("São anagramas!")
else:
    print("Não são anagramas")
