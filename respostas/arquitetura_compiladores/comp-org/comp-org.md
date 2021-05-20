
# Q1

 1. Análise léxica
É a primeira fase do processo de compilação, também é conhecida como leitura ou scanning. O objetivo nessa fase é identificar unidades léxicas ou lexemas que compõem o programa. O analisador léxico lê todos os caracteres do programa fonte e verifica se eles pertencem ao alfabeto da linguagem. Caso um caractere não pertença ao alfabeto da linguagem deve ser gerado um erro léxico. De uma forma resumida a análise léxica deve quebrar o texto do programa fonte em lexemas, verificar a categoria ao qual eles pertencem e produzir uma sequencia de símbolos léxicos chamados como tokens.
 
 2. Análise sintática
A análise sintática tem como objeto validar a gramática do programa, nessa etapa o objetivo é reconhecer se a estrutura gramatical do código fonte esta de acordo com as regras sintáticas da linguagem. Nessa etapa é feita uma varredura na sequência de tokens recebidas do analisador léxico e produzida uma estrutura de dados em formato de árvore (árvore sintática). 

 3. Análise semântica
 O objetivo dessa etapa é verificar se a semântica do programa fonte tem consistência. Para isso é utiliza a árvore sintática e as informações contidas na tabela de símbolos. A tabela de símbolos é muito importante nessa etapa pois é através dela que é possível recuperar informações sobre os identificadores que são utilizadas para avaliar as regras semânticas.
 
 4. Otimização
 Nessa fase o objetivo é otimizar o código em termos de velocidade de execução e consumo de memória. Essa etapa não depende da arquitetura de máquina e tem como objetivo fazer transformações no código intermediário afim obter um código objeto mais otimizado.
 
 5. Emissão de código
 A geração de código objeto é a última etapa do processo de compilação e recebe como entrada uma representação intermediaria que mapeia a linguagem objeto.