async def get_word(charset, length_range, last_word=None):
    # Converte o charset para uma lista e cria um dicionário para acesso rápido
    charset = sorted(set(charset))  # Garante que charset esteja ordenado e único
    charset_dict = {char: index for index, char in enumerate(charset)}
    
    min_len, max_len = length_range

    if last_word is None:
        # Gera a primeira palavra para o comprimento mínimo
        return charset[0] * min_len
    
    # Converte a última palavra em uma lista de índices
    indices = [charset_dict[char] for char in last_word]
    
    # Incrementa a última palavra
    for i in reversed(range(len(indices))):
        if indices[i] < len(charset) - 1:
            indices[i] += 1
            break
        indices[i] = 0
    else:
        # Se estivermos aqui, precisamos adicionar um novo caractere no início
        indices = [0] * (len(indices) + 1)
    
    # Converte os índices de volta para caracteres
    next_word = ''.join(charset[i] for i in indices)
    
    # Se a palavra gerada é maior que o comprimento máximo, retorna None
    if len(next_word) > max_len:
        return None
    
    return next_word
