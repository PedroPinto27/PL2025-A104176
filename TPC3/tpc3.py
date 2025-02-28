import re

def main(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            texto = f.read()
    except Exception as e:
        print("Ficheiro Inválido ou erro ao ler o arquivo:", e)
        return 0
    
    # Headers
    texto = re.sub(r"^(#+)\s(.+)$", lambda m: f"<h{len(m.group(1))}>{m.group(2)}</h{len(m.group(1))}>\n", texto, flags=re.MULTILINE)
    
    # Bold
    texto = re.sub(r"\*\*([^\*]+)\*\*", r"<b>\1</b>", texto)

    # Italic
    texto = re.sub(r"\*([^\*]+)\*", r"<i>\1</i>", texto)

    # Lists
    texto = re.sub(r"^\d+\.\s(.+)$", r"\t<li>\1</li>", texto, flags=re.MULTILINE)
    texto = re.sub(r"(\t<li>.+?</li>\n)+", lambda m: f"<ol>\n{m.group(0)}</ol>\n", texto, flags=re.DOTALL)

    # Img
    texto = re.sub(r"!\[([^\]]+)\]\(([^)]+)\)", r'<img src="\2" alt="\1"/>', texto)

    # Links
    texto = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', texto)

    output = 'output.html'
    try:
        with open(output, 'w', encoding='utf-8') as f:
            f.write(texto)
    except Exception as e:
        print("Erro ao escrever no arquivo de saída:", e)
        return 0

main('input.md')
