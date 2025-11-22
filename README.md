# Song Manager App

**Aplicação CLI para gerenciar um recurso simples (música) utilizando SQLite, com propriedades obrigatórias e opcionais, implementando operações CRUD completas, scripts SQL, validação de dados, logging e containerização Docker.**


---

## 📋 Recurso: Song (Música)

### Propriedades

| Propriedade | Tipo | Obrigatório | Descrição |
|------------|------|-------------|-----------|
| `id` | Integer | ✅ (auto) | Identificador único (gerado automaticamente) |
| `title` | String | ✅ | Título da música |
| `artist` | String | ✅ | Nome do artista |
| `album` | String | ❌ | Nome do álbum |
| `genre` | String | ❌ | Gênero musical |
| `release_date` | Date | ❌ | Data de lançamento (formato: YYYY-MM-DD) |
| `duration` | Float | ❌ | Duração em segundos |
| `created_at` | DateTime | ✅ (auto) | Data/hora de criação (gerado automaticamente) |
| `updated_at` | DateTime | ✅ (auto) | Data/hora da última atualização (atualizado automaticamente) |

### Validações

- **title** e **artist**: Não podem ser vazios ou conter apenas espaços
- **Campos de texto**: Espaços no início e fim são removidos automaticamente
- **Campos opcionais**: Strings vazias são convertidas para `None`
- **duration**: Validação para garantir valores positivos

---

## 🛠️ Tecnologias Utilizadas

### Linguagem
- **Python 3.11**: Linguagem de programação principal

### Frameworks e Bibliotecas

| Biblioteca | Versão | Finalidade |
|-----------|--------|------------|
| **SQLAlchemy** | 2.0.23 | ORM (Object-Relational Mapping) para manipulação do banco de dados SQLite |
| **Pydantic** | 2.5.0 | Validação de dados e schemas com tipos Python |
| **python-dotenv** | 1.0.0 | Gerenciamento de variáveis de ambiente |
| **pytest** | 7.4.3 | Framework de testes unitários |

### Banco de Dados
- **SQLite**: Banco de dados leve, baseado em arquivo, sem necessidade de servidor

### Containerização
- **Docker**: Containerização da aplicação para execução isolada

---

## 📦 Instalação

### Pré-requisitos
- Python 3.11+
- Docker (opcional, para execução em container)

### 1. Clonar o Repositório
```bash
git clone https://github.com/GabrielcMiranda/song-manager-app.git
cd song-manager-app
```

### 2. Criar Ambiente Virtual
```bash
python -m venv venv
```

### 3. Ativar Ambiente Virtual

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 5. Configurar Variáveis de Ambiente (Opcional)

Crie um arquivo `.env` na raiz do projeto:
```env
DATABASE_URL=sqlite:///app/database/songs.db
```

> **Nota**: Se não configurado, a aplicação usará o caminho padrão automaticamente.

### 6. Criar o Banco de Dados
```bash
python app/database/run_create_schema.py
```

---

## 🚀 Como Executar

### Opção 1: Execução Local (Python)

```bash
python -m app.main
```

### Opção 2: Execução com Docker

**Build da imagem:**
```bash
docker build -t song-manager-app .
```

**Executar container:**
```bash
docker run -it --rm -v ${PWD}/app/database:/app/app/database -v ${PWD}/logs:/app/logs song-manager-app
```

> **Nota**: Os volumes `-v` mapeiam as pastas do container para o seu computador:
> - `app/database` → Persiste o banco de dados SQLite
> - `logs` → Persiste os arquivos de log (`app.log` e `errors.log`)

### Opção 3: Script Automatizado (Testes + Docker)

```powershell
.\run.ps1
```

Este script:
1. ✅ Executa todos os testes unitários
2. ✅ Faz build da imagem Docker (somente se os testes passarem)
3. ✅ Inicia a aplicação no container

---

## 📖 Funcionalidades

### Menu Principal

Ao iniciar a aplicação, você verá o menu interativo:

```
================================ SONG MANAGER ================================

Choose an option:
1. List songs
2. Store a new song
3. Search song by ID
4. Update song by ID
5. Delete song by ID
6. Exit
```

---

### 1️⃣ Listar Músicas (List songs)

**Descrição**: Exibe todas as músicas cadastradas no banco de dados.

**Como usar**:
1. Digite `1` no menu principal
2. A aplicação lista todas as músicas no formato: `Song #ID: Title by Artist`

**Exemplo de saída**:
```
Song #1: Bohemian Rhapsody by Queen
Song #2: Hotel California by Eagles
Song #3: Imagine by John Lennon
```

**Comportamento**:
- ✅ Lista todas as músicas ordenadas por ID
- ❌ Exibe erro se o banco estiver vazio

---

### 2️⃣ Cadastrar Nova Música (Store a new song)

**Descrição**: Adiciona uma nova música ao banco de dados.

**Como usar**:
1. Digite `2` no menu principal
2. Preencha os campos solicitados

**Campos solicitados**:
```
Enter song title: Bohemian Rhapsody
Enter artist name: Queen
Enter album name (optional): A Night at the Opera
Enter genre (optional): Rock
Enter release date (YYYY-MM-DD, optional): 1975-10-31
Enter duration in seconds (optional): 354
```

**Exemplo de sucesso**:
```
Song Bohemian Rhapsody created with ID: 1
```

**Validações**:
- ✅ **title** e **artist** são obrigatórios
- ✅ Campos vazios para opcionais são aceitos (salvos como `None`)
- ✅ Espaços extras são removidos automaticamente
- ❌ Strings vazias ou apenas espaços em campos obrigatórios geram erro
- ❌ Formato de data inválido gera erro
- ❌ Duration zero ou negativa gera erro

---

### 3️⃣ Buscar Música por ID (Search song by ID)

**Descrição**: Exibe os detalhes completos de uma música específica.

**Como usar**:
1. Digite `3` no menu principal
2. Informe o ID da música

**Exemplo de entrada**:
```
Enter song ID: 1
```

**Exemplo de saída**:
```
Song #1: Bohemian Rhapsody by Queen
 release date: 1975-10-31
 album: A Night at the Opera
 genre: Rock
 duration: 5:54 min
 song created at: 2025-11-22 14:30:00
 last update at: 2025-11-22 14:30:00
```

**Comportamento**:
- ✅ Duração é exibida no formato `MM:SS`
- ✅ Campos opcionais não preenchidos aparecem como `None`
- ❌ ID inexistente exibe mensagem de erro

---

### 4️⃣ Atualizar Música (Update song by ID)

**Descrição**: Atualiza os dados de uma música existente.

**Como usar**:
1. Digite `4` no menu principal
2. Informe o ID da música a ser atualizada
3. Preencha os novos valores (todos os campos são solicitados)

**Exemplo de entrada**:
```
Enter song ID to update: 1

Enter song title: Bohemian Rhapsody (Remastered)
Enter artist name: Queen
Enter album name (optional): A Night at the Opera
Enter genre (optional): Progressive Rock
Enter release date (YYYY-MM-DD, optional): 1975-10-31
Enter duration in seconds (optional): 354
```

**Exemplo de sucesso**:
```
Song ID 1 updated successfully.
```

**Comportamento**:
- ✅ Atualiza **todos** os campos
- ✅ Para remover valores opcionais, deixe o campo vazio
- ✅ `updated_at` é atualizado automaticamente
- ❌ ID inexistente exibe mensagem de erro

---

### 5️⃣ Deletar Música (Delete song by ID)

**Descrição**: Remove uma música do banco de dados permanentemente.

**Como usar**:
1. Digite `5` no menu principal
2. Informe o ID da música a ser deletada

**Exemplo de entrada**:
```
Enter song ID to delete: 1
```

**Exemplo de sucesso**:
```
Song ID 1 deleted successfully.
```

**Comportamento**:
- ✅ Remove a música permanentemente
- ❌ ID inexistente exibe mensagem de erro
- ⚠️ **Ação irreversível!**

---

### 6️⃣ Sair (Exit)

**Descrição**: Encerra a aplicação.

**Como usar**:
1. Digite `6` no menu principal
2. A aplicação é encerrada

---

## 📂 Estrutura do Projeto

```
song-manager-app/
├── app/
│   ├── controllers/
│   │   └── song_controller.py      # Lógica de interação com usuário
│   ├── database/
│   │   ├── config.py                # Configuração SQLAlchemy
│   │   ├── create_schema.sql       # Script SQL de criação
│   │   ├── run_create_schema.py    # Executor do script SQL
│   │   └── songs.db                 # Banco de dados SQLite (gerado)
│   ├── models/
│   │   └── song.py                  # Model SQLAlchemy (Song)
│   ├── schemas/
│   │   └── song_schema.py           # Schema Pydantic (validação)
│   ├── services/
│   │   └── song_service.py          # Lógica de negócio (CRUD)
│   ├── utils/
│   │   └── logger.py                # Configuração de logs
│   └── main.py                      # Ponto de entrada da aplicação
├── logs/
│   ├── app.log                      # Logs de INFO e WARNING
│   └── errors.log                   # Logs de ERROR e CRITICAL
├── tests/
│   ├── conftest.py                  # Fixtures do pytest
│   ├── test_input_validation.py    # Testes de validação Pydantic
│   ├── test_song_service_create.py # Testes do método create()
│   ├── test_song_service_get_by_id.py # Testes do método get_by_id()
│   ├── test_song_service_update.py # Testes do método update()
│   ├── test_song_service_delete.py # Testes do método delete()
│   └── test_song_service_list.py # Testes do método list()
├── .dockerignore                    # Arquivos ignorados no build Docker
├── .env                             # Variáveis de ambiente
├── .gitignore                       # Arquivos ignorados no Git
├── Dockerfile                       # Configuração do container
├── README.md                        # Documentação
├── requirements.txt                 # Dependências Python
└── run.ps1                          # Script de execução (testes + Docker)
```

---

## 🧪 Testes

O projeto possui **31 testes unitários** cobrindo:
- ✅ Validação de entrada (Pydantic)
- ✅ Operações CRUD (create, read, update, delete, list)
- ✅ Tratamento de erros
- ✅ Persistência de dados

### Executar Testes

**Todos os testes:**
```bash
pytest tests/ -v
```

**Testes específicos:**
```bash
pytest tests/test_song_service_create.py -v
```

---

## 📝 Logs

A aplicação gera logs em dois arquivos separados:

- **`logs/app.log`**: Logs de operações normais (INFO, WARNING)
- **`logs/errors.log`**: Apenas erros (ERROR, CRITICAL)

**Exemplo de log**:
```
2025-11-22 14:30:00 - song_manager - INFO - Song created: ID=1, Title='Bohemian Rhapsody', Artist='Queen'
2025-11-22 14:31:15 - song_manager - WARNING - Song not found: ID=999
2025-11-22 14:32:00 - song_manager - ERROR - Error in create_song: Validation error
```

---

## 🐛 Tratamento de Erros

A aplicação trata os seguintes tipos de erros:

| Erro | Descrição | Mensagem |
|------|-----------|----------|
| **ValidationError** | Dados inválidos (Pydantic) | Detalha campo e tipo do erro |
| **ValueError/TypeError** | Tipo de dado incorreto | "Invalid input format" |
| **Exception (Not Found)** | Recurso não encontrado | "Song with ID X not found!" |
| **Exception (Empty DB)** | Banco vazio | "No songs found!" |

---

## 🐳 Docker

### Build da Imagem
```bash
docker build -t song-manager-app .
```

### Executar Container (com persistência)
```bash
docker run -it --rm -v ${PWD}/app/database:/app/app/database -v ${PWD}/logs:/app/logs song-manager-app
```

### Por que usar `-v`?
- ✅ Dados persistem entre execuções (banco e logs)
- ✅ Banco fica no seu computador (`app/database`)
- ✅ Logs ficam no seu computador (`logs/`)
- ❌ Sem `-v`, os dados são perdidos ao sair

---

## 👨‍💻 Autor

**Gabriel Miranda**
- GitHub: [@GabrielcMiranda](https://github.com/GabrielcMiranda)
- LinkedIn: [@gabrielcmiranda](https://www.linkedin.com/in/gabrielcmiranda)

---

## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.
