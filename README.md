# web-motors
Desafio WebMotors - Criação de um BSBI (Blocked sort-based indexing)

Para mais referências, foi utilizado o seguinte link:
 - https://www.youtube.com/watch?v=7VzUvnZraSI

Popular a pasta dataset com arquivos de texto no formato numerico (apenas arquivos com formatação de valores inteiros são processados no BSBI).

Os dados são salvos em uma pasta temporária em formato .csv para necessidade de consulta mas fica recomendado outro tipo de fornecimento como um banco de dados chave-valor.

Para rodar o programa, executar o arquivo main.py. Por exemplo:
```console
python3 main.py
```

O programa se constitui de dois principais jobs:

1 - Jobs.word_dict_job - Criação de uma lookup table contendo a palavra e um id;

2 - Jobs.block_sort_based_index_job - Match das palavras via word_id, ordenação e agrupamento para criação do índice.

# Classes auxiliares

Foram criadas classes auxiliares para manipulação de strings, lists e criação de strings a partir de um diretório contendo arquivos de texto. Essas classes estão na pasta utils.

# Classes principais

As classes principais estão contidas no arquivo main.py. Se consistem em uma classe responsável pela criação de um word dictionary (constituído pela composição de word e word_id como chave e valor) e os jobs citados acima. Um para criar o word_dict e outro para rodar o BSBI.

# Observações realizadas
Foram aplicadas remoções de pontuação e cleanup de dados, porém ainda assim algumas palavras apareceram de forma mal formatadas devido a características observadas dentro dos próprios textos e da língua inglesa como a presença de asteriscos para definições, aspas, etc. O processo resultou em aproximadamente 140k palavras únicas seguindo a regra que uma palavra é definida pela sua separação de um espaço. Compreende-se que para um match de palavras presentes em um dicionário de língua inglesa seria necessária uma melhoria na criação da lookup table word + word_id.

# Melhorias possíveis de processamento e considerações finais
Compreende-se que o job 1 pode ser melhorado caso exista a necessidade de novos documentos serem adicionados posteriormente. Atualmente ele captura todo um diretório com arquivos para levantamento das palavras com word_id e word e roda tudo de uma vez. Caso um arquivo novo seja adicionado, ele precisa carregar todos os arquivos novamente. Isto pode ser um problema para futuras operações.

Também nota-se que o job 2 atualmente roda de forma serializada, foram feitos testes com aumento do número de arquivos para serem processados até 1Gb de arquivos sem crash de memória do Python. Porém, entende-se que caso exista a necessidade de paralelização, a solução atual pode gastar mais memória do que se deseja. Como solução para as agregações, recomenda-se testar o uso de PySpark que pode realizar gravações em disco de forma mais eficiente para transformações. Apesar da possibilidade do uso de PySpark, compreende-se que o BSBI é um processo 'caro' para a criação de uma tabela que vai permitir processamentos mais rápidos a partir dela. Nota-se uma relação bastante semelhante de resultado com o Elastic Search, que realiza um processo de custo maior para indexação dos dados e posterior maior velocidade na suas buscas.

# Agradecimentos

Obrigado ao time da WebMotors pelo desafio, acredito que outras soluções mais otimizadas são possíveis e seria um prazer conversar mais sobre!