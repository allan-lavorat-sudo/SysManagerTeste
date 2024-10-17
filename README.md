# Projeto SysManager

Este projeto utiliza várias tecnologias e ferramentas para criar um pipeline de dados robusto e eficiente. Aqui está uma visão geral do projeto, tecnologias utilizadas e o processo de configuração.

## Tecnologias Utilizadas

- **Python**: A linguagem principal usada para criar os scripts e pipeline de dados.
- **Jenkins**: Ferramenta de integração contínua utilizada para automatizar o pipeline de build, teste e deploy.
- **Docker**: Utilizado para criar containers que garantem um ambiente consistente para a aplicação.
- **Apache Airflow**: Usado para orquestrar os DAGs e gerenciar o fluxo de trabalho de dados.
- **Git**: Sistema de controle de versão usado para gerenciar o código fonte e colaborar com outros desenvolvedores.

## Estrutura do Projeto

- **dags/**: Contém os DAGs do Airflow que definem as tarefas do pipeline.
  - `data_pipeline.py`: Script que define o pipeline de dados no Airflow.
- **data/**: Contém arquivos de dados usados pelo pipeline.
  - `sales_data_example 1.csv`: Exemplo de arquivo de dados que é processado pelo pipeline.
- **logs/**: Diretório para armazenar logs gerados pelo Airflow.
- **plugins/**: Diretório para plugins personalizados do Airflow.
- **docker-compose.yml**: Arquivo de configuração do Docker Compose para iniciar os containers necessários.
- **airflow.cfg**: Arquivo de configuração do Airflow.
- **webserver_config.py**: Configurações do servidor web do Airflow.
- **sql_queries.sql**: Arquivo contendo as queries SQL utilizadas no pipeline.

## Processo de Configuração

1. **Instalação do Git**:
   - Instalamos o Git para controle de versão e colaboração.

2. **Instalação do Jenkins**:
   - Baixamos e instalamos o Jenkins para gerenciar o pipeline de CI/CD.
   - Configuramos o Jenkins com os plugins recomendados e criamos um usuário administrador.

3. **Configuração do Pipeline no Jenkins**:
   - Criamos um novo projeto no Jenkins com um script de pipeline para orquestrar as tarefas de build, teste e deploy.

4. **Configuração do Apache Airflow**:
   - Configuramos o Airflow para gerenciar os DAGs e o fluxo de trabalho de dados.
   - Criamos e configuramos os scripts do DAG.

5. **Versionamento de Código no GitHub**:
   - Inicializamos um repositório Git e adicionamos todos os arquivos do projeto.
   - Subimos o projeto para um repositório no GitHub para compartilhamento e colaboração.

## Como Rodar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/allan-lavorat-sudo/SysManagerTeste.git
   cd SysManagerTeste
