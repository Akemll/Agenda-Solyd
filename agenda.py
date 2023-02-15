import pandas, time, random, os
contatos = {}
rodar = True
direc = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
def pontos():
    for e in range(1, 4):
        time.sleep(0.5)
        if e == 3:
            print(".")
        else:
            print(".", end="")
    time.sleep(1)
try:
    print("Verificando se há backup", end="")
    pontos()
    reload = pandas.read_csv(f"{direc}\\contatos.csv")
    print("Carregando", end="")
    pontos()
    for e in reload.values:
        contatos[(len(contatos) + 1)] = {"nome": e[0], "numero": e[1], "email": e[2], "endereço": e[3]}
except Exception:
    pass
print("Carregado com sucesso!")

def imprimir_menu():
    tupla = ("Mostrar todos os contatos da agenda", "Buscar contato", "Incluir contato", "Editar contato", "Excluir contato", "Exportar contatos para CSV", "Importar contatos CSV", "Fechar agenda")
    print("-"*20)
    for e in range(0, 8):
        print(f"{e} - {tupla[e]}")
    print("-"*20)

def tudo(num):
    global rodar, direc
    print("-"*20)
    if not num.isnumeric() or int(num) < 0 or int(num) > 7:
        print("Opção inválida!")
    else:
        if num == "0":
            for e, v in contatos.items():
                print("-"*20)
                print(f"Contato: {e}")
                print("-"*20)
                for t, q in v.items():
                    print(f"{t}:{q}")
                print("-"*20)
        elif num == "1":
            print("Carregando")
            pontos()
            nome = str(input("Insira o nome do contato:"))
            print("Procurando", end="")
            pontos()
            encontrado = False
            for e, v in contatos.items():
                if v["nome"] == nome:
                    encontrado = True
                    print("\n")
                    print("Contato encontrado!")
                    print("Carregando contato", end="")
                    pontos()
                    print("-"*20)
                    for t, q in v.items():
                        print(f"{t}:{q}")
                    print("-"*20)
            if not encontrado:
                print(">>>>>> Contato não encontrado!")
        elif num == "2":
            print("Carregando", end="")
            pontos()
            nome = str(input("Nome do contato:"))
            while True:
                numero = str(input("Número do contato:"))
                if not numero.isnumeric():
                    print("Número inválido!")
                else:
                    break
            while True:
                email = str(input("Email do contato:"))
                if "@" not in email or ".com" not in email:
                    print("Email inválido!")
                else:
                    break
            endereco = str(input("Endereço do contato:"))
            for e, v in contatos.items():
                if v["nome"] == nome and v["numero"] == numero and v["email"] == email and v["endereço"] == endereco:
                    print("Já há um contanto igual! Saindo", end="")
                    pontos()
            print("Incluindo contato", end="")
            pontos()
            contatos[(len(contatos) + 1)] = {"nome": nome, "numero": numero, "email": email, "endereço": endereco}   
            print("Incluido!")
        elif num == "3":
            permitido = ["numero", "nome", "email","endereço"]
            print("Carregando", end="")
            pontos()
            nome = str(input("Insira o nome do contato:"))
            lista = {}
            for e, v in contatos.items():
                if v["nome"] == nome:
                    lista[e] = v
            if len(lista) > 1:
                print("Multiplos usuários encontrados, carregando", end="")
                pontos()
                for e, v in lista.items():
                    print("-"*20)
                    print(f"Contato número {e}")
                    print("-"*20)
                    for t, q in v.items():
                        print(f"{t}:{q}")
                    print("-"*20)
                print(lista)
                while True:
                    escolher = str(input("Escolha algum dos usuários(0 para sair):"))
                    if not lista[int(escolher)]:
                        print("Escolha inválida!")
                    elif escolher == 0:
                        print("Saindo", end="")
                        pontos()
                        break
                    else:
                        break
                if escolher == 0:
                    return
                print("Selecionando contato", end="")
                pontos()
                print("Usuário encontrado, carregando usuário.", end="")
                pontos()
                print("-"*20)
                for t, q in contatos[int(escolher)].items():
                    print(f"{t}:{q}")
                print("-"*20)
                for e, v in contatos.items():
                    if int(e) == int(escolher):
                        while True:
                            alvo = str(input("Oque deseja editar?(Exit:0)"))
                            if alvo == "0":
                                print("Saindo", end="")
                                pontos()
                                break
                            elif alvo not in permitido:
                                print("Opção não encontrada!")
                            else:
                                print(f"Selecionando {alvo}", end="")
                                pontos()
                                while True:
                                    valor = str(input("Informe o valor que deseja inserir:"))
                                    if "@" not in valor and alvo == "email" or ".com" not in valor and alvo == "email":
                                        print("Email inválido!")
                                    elif alvo == "numero" and not valor.isnumeric():
                                        print("Número inválido!")
                                    else:
                                        break
                                print("Inserindo dados", end="")
                                pontos()
                                v[alvo] = valor
                                print("Dados inseridos com sucesso!")
            elif len(lista) == 1:
                print("Usuário encontrado, carregando usuário.", end="")
                pontos()
                print("-"*20)
                for e, v in contatos.items():
                    if v["nome"] == nome:
                        for t, q in v.items():
                            print(f"{t}:{q}")
                print("-"*20)
                for e, v in contatos.items():
                    if v["nome"] == nome:
                        while True:
                            alvo = str(input("Oque deseja editar?(Exit:0)"))
                            if alvo == "0":
                                print("Saindo", end="")
                                pontos()
                                break
                            elif alvo not in permitido:
                                print("Opção não encontrada!")
                            else:
                                print(f"Selecionando {alvo}", end="")
                                pontos()
                                while True:
                                    valor = str(input("Informe o valor que deseja inserir:"))
                                    if "@" not in valor and alvo == "email" or ".com" not in valor and alvo == "email":
                                        print("Email inválido!")
                                    else:
                                        break
                                print("Inserindo dados", end="")
                                pontos()
                                v[alvo] = valor
                                print("Dados inseridos com sucesso!")
            else:
                print("Usuário não encontrado, saindo", end="")
                pontos()
        elif num == "4":
            print("Carregando", end="")
            pontos()
            alvo = str(input("Informe o nome do contato:"))
            print("Procurando", end="")
            pontos()
            destino = None
            lista = {}
            for e, v in contatos.items():
                if v["nome"] == alvo:
                    lista[e] = v
            if len(lista) > 1:
                print("Multiplos usuários encontrados, carregando", end="")
                pontos()
                for e, v in lista.items():
                    print("-"*20)
                    print(f"Contato número {e}")
                    print("-"*20)
                    for t, q in v.items():
                        print(f"{t}:{q}")
                    print("-"*20)
                while True:
                    escolher = str(input("Escolha algum dos usuários(0 para sair):"))
                    if not lista[int(escolher)]:
                        print("Escolha inválida!")
                    elif escolher == 0:
                        print("Saindo", end="")
                        pontos()
                        break
                    else:
                        break
                if escolher == 0:
                    return
                print("Selecionando contato", end="")
                pontos()
                print("Usuário encontrado, deletando usuário.", end="")
                pontos()
                contatos.pop(int(escolher))
            elif len(lista) == 1:
                for e, v in lista.items():
                    contatos.pop(e)
                print("Selecionando contato", end="")
                pontos()
                print("Usuário encontrado, deletando usuário.", end="")
                pontos()
            
            if destino:
                contatos.pop(destino)
                print("Deletado com sucesso!")
            
        elif num == "5":
            print("Carregando", end="")
            pontos()
            print("Exportando", end="")
            pontos()
            nome = random.randint(0, 10000000)
            arquivo = open(f"{direc}\{nome}.csv", "w")
            total = "nome,email,numero,endereco\n"
            for e, v in contatos.items():
                for q, t in v.items():
                    if q != "endereço":
                        total += f"{t},"
                    else:
                        total += f"{t}\n"
            arquivo.write(total)
            arquivo.close()
            print(f"Exportado com sucesso! Nome do arquivo:{nome}.csv")
        elif num == "6":
            print("Carregando", end="")
            pontos()
            diretorio = str(input("Informe o diretório exato:"))
            try:
                arquivo = pandas.read_csv(diretorio).values
                contar = 0
                for e in arquivo:
                    liberado = True
                    for q,v in contatos.items():
                        if v["nome"] == e[0] and v["numero"] == e[1] and v["email"] == e[2] and v["endereço"] == e[3]:
                            print("-"*20)
                            print("Contato já existente, ignorado.")
                            print("-"*20)
                            print(f"Nome:{e[0]}")
                            print(f"Número:{e[1]}")
                            print(f"Email:{e[2]}")
                            print(f"Endereço:{e[3]}")
                            print("-"*20)
                            liberado = False
                    if liberado:
                        contar +=1
                        contatos[(len(contatos) + 1)] = {"nome": e[0], "numero": e[1], "email": e[2], "endereço": e[3]}
                print(f"Contatos novos adicionados:{contar}")
                print("Saindo", end="")
                pontos()
                        
            except Exception:
                print("Não foi possível encontrar o diretório, retornando ao menu", end="")
                pontos()
                return
        elif num == "7":
            print("Salvando contatos atuais", end="")
            pontos()
            arquivo = open(f"{direc}}contatos.csv", "w")
            total = "nome,email,numero,endereco\n"
            for e, v in contatos.items():
                for q, t in v.items():
                    if q != "endereço":
                        total += f"{t},"
                    else:
                        total += f"{t}\n"
            arquivo.write(total)
            print("Saindo", end="")
            pontos()
            arquivo.close()
            rodar = False
            
if __name__ == "__main__":
    while rodar:
        imprimir_menu()
        tudo(str(input("Escolha uma opção: ")))
