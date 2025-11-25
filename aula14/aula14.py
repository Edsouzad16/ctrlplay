# Aula 14 - Testes com python unittest

def SobrenomeNaOrdem(nome,s1,s2):
    if len(s1) > len(s2):
     return f"{nome} {s1} {s2}"
    else:
        return f"{nome} {s2} {s1}"
    
print(SobrenomeNaOrdem('Lucas','Mathias','Ferreira'))