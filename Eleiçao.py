import re


def contar_palavras_chave(texto):
    texto = texto.lower()
    palavras_chave = [
        "idh",
        "economia",
        "desenvolvimento",
        "infraestrutura",
        "saude",
        "educacao",
        "seguranca",
        "sustentabilidade",
        "justica",
        "crescimento",
    ]

    total = 0
    for palavra in palavras_chave:
        total += len(re.findall(rf"\b{re.escape(palavra)}\b", texto))
    return total


def calcular_pontuacao(discurso):
    discurso = discurso.strip()
    if not discurso:
        return 0

    frase_banida = "ajudar os pobres"
    if frase_banida in discurso.lower():
        return 0

    pontuacao = len(discurso)
    pontuacao += contar_palavras_chave(discurso) * 5
    return pontuacao


print("=== Modelo de Político ===")

nome = input("Digite o nome do político: ").strip() or "Político sem nome"
partido = input("Digite o partido: ").strip() or "Sem partido"
ideologia = input("Digite a ideologia: ").strip() or "Sem ideologia"
discurso = input("Digite o discurso político: ").strip()

pontuacao = calcular_pontuacao(discurso)

print("\n=== Perfil do Político ===")
print(f"Nome: {nome}")
print(f"Partido: {partido}")
print(f"Ideologia: {ideologia}")
print(f"Discurso: {discurso}")
print(f"Pontuação: {pontuacao}")

if "ajudar os pobres" in discurso.lower():
    print("Resultado: pontuação zerada por mencionar 'ajudar os pobres'.")
elif pontuacao >= 500:
    print("Resultado: discurso muito forte e persuasivo!")
elif pontuacao >= 200:
    print("Resultado: discurso forte, mas ainda pode melhorar.")
else:
    print("Resultado: discurso curto e menos impactante.")