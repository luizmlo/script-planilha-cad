# Trabalho de CAD
### Scripts e linguagem de programação
#### Objetivos:
* Implementar um **script em Python 3** que automatiza o processo de criação de planilhas de notas de avaliações.
* Instalação de Python 3 necessária no momento, mas o programa pode ser compilado posteriormente para uso independente da linguagem.
* _Cross Platform_, ou seja, pode ser utilizado tanto em sistemas Windows, como em sistemas Unix (MacOS, Linux).
#### Usagem:  
   Dentro de uma pasta vazia, devem estar os arquivos enviados pelos alunos e o script;  
   Os desenhos devem estar usando o padrão _**ARQ_CAD_IFG_NOME_DO_ALUNO**_;  
   O programa pode ser executado da seguinte forma:  
   ```
   $> python script.py
   ```

   ##### O script tem dois modos:
   ### **Modo 1 - Modo Real**
   ```
   Digite o Modo:
   1 - Real, usando os arquivos e notas reais
   2 - Teste, notas aleatórias para demonstração
   >>> 1
   ```
   **Planilha de saída:**

   ID|Nome do Arquivo|Nome do Aluno|Nota do Trabalho
   --- | --- | --- | ---
   0 | ARQ_CAD_IFG_ANA_LAURA_MARQUES.dwg | ANA LAURA MARQUES | 0.0
   1 | ARQ_CAD_IFG_ARTHUR_MEDEIROS.dwg | ARTHUR MEDEIROS | 0.0
   2 | ARQ_CAD_IFG_LUIZ_FELIPE_BRANCO.dwg | LUIZ FELIPE BRANCO | 10.0

   ### **Modo 2 - Modo de Testes, Notas aleatórias**
   ```
   Digite o Modo:
   1 - Real, usando os arquivos e notas reais
   2 - Teste, notas aleatórias para demonstração
   >>> 2
   ```
   **Planilha de saída:**

   ID|Nome do Arquivo|Nome do Aluno|Nota do Trabalho
   --- | --- | --- | ---
   0 | ARQ_CAD_IFG_ANA_LAURA_MARQUES.dwg | ANA LAURA MARQUES | 7.4
   1 | ARQ_CAD_IFG_ARTHUR_MEDEIROS.dwg | ARTHUR MEDEIROS | 8.2
   2 | ARQ_CAD_IFG_NOME_ALUNO.dwg | NOME ALUNO | 9.7


