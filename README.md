# web-motors
Desafio WebMotors - Criação de um BSBI (Blocked sort-based indexing)

Para mais referências, foi utilizado o seguinte link:
 - https://www.youtube.com/watch?v=7VzUvnZraSI

Popular a pasta dataset com arquivos de texto no formato numerico (apenas arquivos com formatação de valores inteiros são processados no BSBI).

Os dados são salvos em uma pasta temporária em formato .csv para necessidade de consulta mas fica recomendado outro tipo de fornecimento.

Para rodar o programa, executar o arquivo main.py. Por exemplo:
```console
python3 main.py
```

O programa se constitui de dois principais jobs:

1 - Jobs.word_dict_job - Criação de uma lookup table contendo a palavra e um id;

2 - Jobs.block_sort_based_index_job - Match das palavras via word_id, ordenação e agrupamento para montagem do índice.

# Observações realizadas
Foram aplicadas remoções de pontuação e cleanup de dados, porém ainda assim algumas palavras apareceram de forma mal formatadas devido a cracterísticas realizadas dentro dos próprios textos e da língua inglesa como a presença de asteriscos para definições, aspas, etc. O processo resultou em aproximadamente 140k palavras únicas seguindo a regra que uma palavra é definida pela sua separação de um espaço. Compreende-se que para um match de palavras apenas reais seria necessária uma melhoria na criação da lookup table word + word_id

# Melhorias possíveis de processamento
Compreende-se que o job 1 pode ser melhorado caso novos documentos sejam adicionados. Atualmente ele captura todo um folder com arquivos para levantamento das palavras com word_id e word.

Também nota-se que o job 2 atualmente roda de forma serializada, foram feitos testes com aumento do número de arquivos para serem processados em até 1Gb de arquivos sem crash de memória do Python. Porém, entende-se que caso exista a necessidade de paralelização, a solução atual pode gastar mais memória do que se deseja. Como solução para as agregações, recomenda-se testar o uso de PySpark que pode realizar gravações em disco de forma mais eficiente para transformações. Apesar disso, compreende-se que é um processo 'caro' para a criação de uma tabela que vai permitir processamentos mais rápidos a partir dela.