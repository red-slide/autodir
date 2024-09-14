import sys

async def get_range():
    try:
        # Solicita os comprimentos mínimo e máximo do usuário
        min_length = int(input("\033[36m[+]\033[0m Enter the minimum length: "))
        max_length = int(input("\033[36m[+]\033[0m Enter the maximum length: "))

        # Verifica se os comprimentos são positivos e se o máximo não é menor que o mínimo
        if min_length <= 0 or max_length <= 0:
            raise ValueError("Os valores devem ser maiores que zero.")
            sys.exit()
        if min_length > max_length:
            raise ValueError("O comprimento máximo não pode ser menor que o comprimento mínimo.")
            sys.exit()
            
        # Se tudo estiver correto, retorna a lista com os valores
        return [min_length, max_length]
        
    except ValueError as e:
        # Exibe uma mensagem de erro e solicita a entrada novamente
        print("\n\033[41mPor favor, insira valores válidos.\033[0m")
        sys.exit()
