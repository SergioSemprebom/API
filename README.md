# Projeto Coletor de Dados Pokémon

Este projeto consiste em um script Python que interage com a [PokeAPI](https://pokeapi.co/) para buscar informações sobre Pokémons e armazená-las em um banco de dados local SQLite. A cada execução, um Pokémon aleatório (entre os IDs 1 e 350) é selecionado, seus dados (nome e tipo) são extraídos e salvos.

## Funcionalidades

* Busca dados de Pokémons (nome e tipo) da PokeAPI.
* Armazena os dados coletados em um banco de dados SQLite.
* Cria um arquivo JSON individual para cada Pokémon consultado com os dados brutos da API.
* Executa um loop contínuo, buscando um novo Pokémon a cada 5 segundos.
* Utiliza SQLAlchemy para ORM e Pydantic para validação de dados.

## Tecnologias Utilizadas

* **Python 3**
* **Requests:** Para realizar requisições HTTP à PokeAPI.
* **SQLAlchemy:** Para o mapeamento objeto-relacional (ORM) e interação com o banco de dados SQLite.
* **Pydantic:** Para validação de dados e definição de schemas.
* **SQLite:** Banco de dados SQL embarcado.

## Estrutura do Projeto

A estrutura principal do projeto está organizada da seguinte forma:

├── exemplo_01.py         
├── exemploLista.py      
├── hello.py             
├── README.md           
├── src/
│   ├── init.py
│   ├── controller.py     
│   ├── db.py             
│   ├── main.py           
│   ├── models.py        
│   └── schema.py         
└── pokemon.db            

O projeto está organizado da seguinte maneira:

* **`./` (Pasta Raiz do Projeto)**
    * `README.md`: Este arquivo com a descrição do projeto.
    * `exemplo_01.py`: Script de exemplo para buscar e exibir dados de um Pokémon específico.
    * `exemploLista.py`: Script de exemplo (não diretamente relacionado ao núcleo do projeto).
    * `hello.py`: Script de exemplo "Hello World" (não diretamente relacionado ao núcleo do projeto).
    * `pokemon.db`: (Gerado) Banco de dados SQLite onde os dados dos Pokémons são armazenados.
    * `[nome_do_pokemon].json`: (Gerado) Arquivos JSON contendo os dados brutos de cada Pokémon consultado (ex: `pikachu.json`).

* **`./src/` (Pasta com o Código Fonte Principal)**
    * `__init__.py`: Torna o diretório `src` um pacote Python.
    * `main.py`: Ponto de entrada da aplicação. Executa o loop de coleta de dados dos Pokémons.
    * `controller.py`: Contém a lógica para buscar dados da PokeAPI (`Workspace_pokemon_data`) e para adicionar os Pokémons ao banco de dados (`add_pokemon_to_db`).
    * `db.py`: Configura a conexão com o banco de dados SQLite usando SQLAlchemy.
    * `models.py`: Define o modelo de dados `Pokemon` (tabela do banco de dados) usando SQLAlchemy.
    * `schema.py`: Define o schema `PokemonSchema` usando Pydantic para validação dos dados do Pokémon.

### Descrição dos Componentes Principais:

* **`src/main.py`**: Orquestra a coleta de dados, chamando funções do `controller.py` em um loop.
* **`src/controller.py`**: Responsável por:
    * Buscar dados na PokeAPI.
    * Salvar os dados brutos da API em arquivos `.json` individuais para cada Pokémon na pasta raiz.
    * Processar os dados e prepará-los para o banco.
    * Adicionar os dados processados ao banco de dados SQLite.
* **`src/db.py`**: Estabelece a conexão com o banco `pokemon.db`.
* **`src/models.py`**: Define a estrutura da tabela `pokemons` (id, nome, tipo, data de criação).
* **`src/schema.py`**: Garante que os dados do Pokémon estejam no formato correto antes de serem processados.

## Como Executar

1.  **Clone o repositório (ou certifique-se de que todos os arquivos estejam na mesma estrutura descrita acima).**
2.  **Instale as dependências:**
    Certifique-se de ter o Python 3 instalado. Você precisará instalar as bibliotecas `requests`, `SQLAlchemy` e `Pydantic`.
    ```bash
    pip install requests sqlalchemy pydantic
    ```
3.  **Execute o script principal:**
    Navegue até a pasta raiz do projeto e execute:
    ```bash
    python src/main.py
    ```
    O script começará a buscar dados de Pokémons aleatórios e a salvá-los no arquivo `pokemon.db` (na pasta raiz). Ele também criará arquivos JSON com o nome de cada Pokémon consultado (ex: `pikachu.json`) na pasta raiz do projeto.

## Detalhes da Operação

O script `src/main.py` executa um loop infinito (`while True`):
1.  Gera um ID de Pokémon aleatório entre 1 e 350.
2.  Chama `Workspace_pokemon_data(pokemon_id)` do `controller.py`.
    * Esta função faz uma requisição GET para `https://pokeapi.co/api/v2/pokemon/{id}`.
    * Se a requisição for bem-sucedida (status code 200):
        * Os dados JSON da resposta são salvos em um arquivo `{nome_do_pokemon}.json` na pasta raiz.
        * Os tipos do Pokémon são extraídos e formatados.
        * Retorna um objeto `PokemonSchema` com o nome e os tipos do Pokémon.
    * Caso contrário, retorna `None`.
3.  Se `Workspace_pokemon_data` retornar dados válidos:
    * Exibe uma mensagem informando que o Pokémon está sendo adicionado ao banco.
    * Chama `add_pokemon_to_db(pokemon_schema)` do `controller.py`.
        * Esta função cria uma sessão com o banco de dados.
        * Cria um objeto `Pokemon` (modelo SQLAlchemy) com os dados do `PokemonSchema`.
        * Adiciona o objeto à sessão e commita as alterações no banco de dados.
4.  Se não for possível obter dados para o Pokémon, uma mensagem de aviso é exibida.
5.  O script aguarda 5 segundos (`time.sleep(5)`) antes de repetir o processo.

O banco de dados `pokemon.db` conterá uma tabela chamada `pokemons` com as seguintes colunas:
* `id` (Integer, Chave Primária)
* `name` (String)
* `type` (String) - Tipos do Pokémon, separados por vírgula se houver mais de um.
* `created_at` (DateTime) - Data e hora em que o registro foi criado.

Este projeto serve como um exemplo prático de consumo de uma API externa, processamento de dados e persistência em um banco de dados relacional utilizando Python e bibliotecas comuns no ecossistema de desenvolvimento.
