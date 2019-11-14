import csv, os,random

arquivos = os.listdir('.')

def abrir_planilha():
    try:
        planilha = open('Planilha_Notas.csv', 'w', newline='')
        modo = int(input('Já foi encontrada uma planilha na pasta, os dados serão sobrescrevidos\nDigite o Modo:\n1 - Real, usando os arquivos e notas reais\n2 - Teste, notas aleatórias para demonstração\n>>> '))

    except FileNotFoundError:
        modo = int(input('Planilha Não encontrada, criando arquivo\nDigite o Modo:\n1 - Real, usando os arquivos e notas reais\n2 - Teste, notas aleatórias para demonstração\n>>> '))
        planilha = open('Planilha_Notas.csv', 'w+', newline='')
    
    return planilha, modo


def parsar_nomes():
    nomes = []
    nomes_arquivos = []
    for i in range(len(arquivos)):
        if(arquivos[i][-3:] == 'dwg'):
            nome_arquivo = arquivos[i]
            nomes_arquivos.append(nome_arquivo)
            nome_parsed = nome_arquivo.split('_')
            nome_parsed = nome_parsed[3:]
            nome = ''
            n_nomes = 0
            for x in nome_parsed:
                n_nomes += 1
                if(n_nomes <= 1):
                    nome += x
                else:
                    nome += ' ' + x

            nome = nome[:-4]
            print(nome)
            nomes.append(nome)

    return nomes_arquivos, nomes

def escrever_planilha(handler_planilha, matriz_arquivos, matriz_nomes, modo):
    nomes_arquivos = matriz_arquivos
    nomes = matriz_nomes
    planilha = handler_planilha
    colunas = ['Nº','Nome do Arquivo', 'Nome do Aluno', 'Nota do Trabalho']
    writer = csv.writer(planilha, delimiter=',')
    writer.writerow(colunas)

    for i in range(len(nomes)):
        if(modo == 1):
            nota = 0.00
        else:
            nota = random.randint(4,9)
            nota_decimal = 0.1 * random.randint(1,9)
            nota += nota_decimal
        linha = [i,nomes_arquivos[i],nomes[i],nota]
        writer.writerow(linha)

def main():
    planilha, modo = abrir_planilha()
    nomes_arquivos, nomes = parsar_nomes()
    escrever_planilha(planilha, nomes_arquivos, nomes, modo)
    #print(nomes_arquivos)

if __name__ == "__main__":
    main()

