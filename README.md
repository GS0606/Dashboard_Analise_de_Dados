# 📊 Dashboard de Análise de Salários na Área de Dados

Dashboard interativo desenvolvido em Streamlit para análise exploratória de dados salariais na área de tecnologia e ciência de dados. O projeto permite visualizar e analisar informações sobre salários, cargos, níveis de experiência e outros fatores relevantes do mercado de trabalho em tecnologia.

## 🚀 Características

- **Interface Interativa**: Filtros dinâmicos para refinar análises
- **Visualizações Interativas**: Gráficos interativos usando Plotly
- **Métricas em Tempo Real**: KPIs atualizados conforme os filtros aplicados
- **Interface Completamente em Português**: Todos os textos, legendas, eixos e cargos traduzidos
- **Tradução Inteligente de Cargos**: Os cargos mais comuns são automaticamente traduzidos
- **Responsivo**: Layout adaptável para diferentes tamanhos de tela

## 📋 Funcionalidades

### Métricas Principais
- **Salário Médio e Mediano**: Estatísticas centrais dos salários
- **Faixa Salarial**: Mínimo, máximo e percentis (P25-P75)
- **Variação Ano a Ano**: Comparação com o ano anterior
- **Total de Registros**: Quantidade de dados analisados
- **Cargo Mais Frequente**: Cargo com maior ocorrência
- **Desvio Padrão**: Medida de dispersão dos salários
- **Número de Cargos Únicos**: Diversidade de cargos no dataset

### Visualizações

#### Visão Geral
1. **Top 10 Cargos por Salário Médio**: Gráfico de barras horizontal com cargos traduzidos
2. **Distribuição de Salários**: Histograma da distribuição salarial com eixos em português
3. **Proporção de Tipos de Trabalho**: Gráfico de pizza (Presencial, Híbrido, Remoto)
4. **Salário por País**: Mapa coroplético para Cientistas de Dados com legendas em português

#### Análises Comparativas
5. **Evolução Temporal**: Gráfico de linha mostrando tendência de salários ao longo dos anos
6. **Distribuição por Senioridade**: Box plot comparando salários por nível de experiência
7. **Salário por Tipo de Trabalho**: Comparação de salários médios (Remoto vs Presencial vs Híbrido)

### Insights Automáticos
O dashboard gera automaticamente insights baseados nos dados:
- Análise de crescimento/redução salarial
- Detecção de alta variabilidade
- Comparação entre trabalho remoto e presencial
- Análise de gap salarial por senioridade

### Filtros Disponíveis
- **Ano**: Filtro por ano de trabalho (múltipla seleção)
- **Senioridade**: Junior, Pleno, Senior, Executivo (múltipla seleção)
- **Tipo de Contrato**: Tempo Integral, Meio Período, Contrato, Freelancer (múltipla seleção)
- **Tamanho da Empresa**: Pequena, Média, Grande (múltipla seleção)
- **Cargo**: Filtro opcional por cargo específico (múltipla seleção)

## 🛠️ Tecnologias Utilizadas

- **Streamlit**: Framework para criação de aplicações web interativas
- **Pandas**: Manipulação e análise de dados
- **Plotly**: Criação de gráficos interativos
- **NumPy**: Operações numéricas

## 📦 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos para Instalação

1. **Clone o repositório** (ou baixe os arquivos):
   ```bash
   git clone <url-do-repositorio>
   cd Dashboard_Analise_de_Dados
   ```

2. **Crie um ambiente virtual** (recomendado):
   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual**:
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **Linux/Mac:**
   ```bash
   source venv/bin/activate
   ```

4. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Como Executar

Após instalar as dependências, execute o seguinte comando:

```bash
streamlit run app.py
```

O dashboard será aberto automaticamente no seu navegador padrão, geralmente em `http://localhost:8501`.

## 📁 Estrutura do Projeto

```
Dashboard_Analise_de_Dados/
│
├── app.py                 # Ponto de entrada do dashboard Streamlit
├── common.py              # Módulo com funções auxiliares (constantes, processamento, visualizações)
├── test.py                # Script de testes e análise exploratória
├── requirements.txt       # Dependências do projeto
└── README.md             # Este arquivo
```

### Descrição dos Arquivos

- **`app.py`**: Arquivo principal que inicia o dashboard. Contém apenas a função `main()` que orquestra a aplicação e importa todas as funções necessárias do módulo `common.py`.

- **`common.py`**: Módulo central contendo:
  - Constantes (URLs, traduções, configurações)
  - Funções de processamento de dados
  - Funções de cálculo de métricas
  - Funções de criação de visualizações
  - Funções de interface (filtros, exibição)
  - Função de geração de insights

- **`test.py`**: Script para testes e análises exploratórias. Contém código de exemplo para análise dos dados usando matplotlib, seaborn e plotly.

## 🔧 Arquitetura do Código

O código foi desenvolvido seguindo princípios de **Clean Code** e **Separação de Responsabilidades**:

- **Modularidade**: Código organizado em módulos separados (`app.py` e `common.py`)
- **Documentação**: Docstrings em todas as funções
- **Constantes**: Valores mágicos extraídos para constantes nomeadas
- **Type Hints**: Tipagem para melhor legibilidade e manutenção
- **Cache de Dados**: Uso de `@st.cache_data` para otimização de performance

### Estrutura Modular

O projeto está organizado em dois arquivos principais:

#### `app.py` (Ponto de Entrada)
- Configuração da página Streamlit
- Orquestração do dashboard
- Importa todas as funções do módulo `common.py`

#### `common.py` (Módulo de Funções)
Contém todas as funções organizadas por categoria:

- **Constantes**: Configurações e mapeamentos de tradução (colunas, valores, cargos)
- **Processamento de Dados**: 
  - `carregar_dados()`: Carrega dados do CSV
  - `traduzir_colunas()`: Traduz nomes das colunas
  - `traduzir_valores()`: Traduz valores categóricos
  - `traduzir_cargos_comuns()`: Traduz cargos para português
  - `processar_dados()`: Pipeline completo de processamento
  - `filtrar_dataframe()`: Filtragem de dados
- **Cálculo de Métricas**: 
  - `calcular_metricas()`: Calcula KPIs e estatísticas
  - `gerar_insights()`: Gera insights automáticos
- **Visualizações**: 
  - `criar_grafico_top_cargos()`: Gráfico de barras horizontal
  - `criar_grafico_distribuicao_salarios()`: Histograma
  - `criar_grafico_tipos_trabalho()`: Gráfico de pizza
  - `criar_grafico_salario_por_pais()`: Mapa coroplético
  - `criar_grafico_boxplot_senioridade()`: Box plot
  - `criar_grafico_tendencia_temporal()`: Gráfico de linha
  - `criar_grafico_salario_por_tipo_trabalho()`: Gráfico de barras
- **Interface**: 
  - `criar_barra_lateral_filtros()`: Cria filtros interativos
  - `exibir_metricas()`: Exibe métricas principais
  - `exibir_insights()`: Exibe insights automáticos
  - `exibir_graficos()`: Exibe gráficos organizados por abas
  - `exibir_tabela_dados()`: Exibe tabela de dados detalhados

## 📊 Fonte de Dados

Os dados são carregados diretamente do repositório GitHub:
```
https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv
```

## 🎨 Personalização

### Traduções Implementadas

O dashboard possui tradução completa para português brasileiro:

#### Tradução de Colunas
- Todas as colunas do dataset são traduzidas automaticamente
- Exemplo: `work_year` → `ano`, `job_title` → `cargo`

#### Tradução de Valores Categóricos
- **Senioridade**: EN → junior, MI → Pleno, SE → Senior, EX → executivo
- **Tipo de Contrato**: FT → Tempo Integral, PT → Meio Período, CT → Contrato, FL → Freelancer
- **Tamanho da Empresa**: S → Pequena, M → Média, L → Grande
- **Modalidade de Trabalho**: 0 → Presencial, 50 → Híbrido, 100 → Remoto

#### Tradução de Cargos
Os cargos mais comuns são automaticamente traduzidos, incluindo:
- Data Scientist → Cientista de Dados
- Data Engineer → Engenheiro de Dados
- Data Analyst → Analista de Dados
- Machine Learning Engineer → Engenheiro de Machine Learning
- Research Team Lead → Líder de Equipe de Pesquisa
- Analytics Engineering Manager → Gerente de Engenharia de Analytics
- E muitos outros...

#### Tradução de Legendas dos Gráficos
- Todos os eixos dos gráficos estão em português
- Títulos e labels traduzidos
- Exemplo: "count" → "Frequência", "salary_in_usd" → "Salário (USD)"

### Modificar Traduções

As traduções podem ser ajustadas nas constantes no arquivo `common.py`:

```python
# Tradução de senioridade
TRADUCAO_SENIORIDADE = {
    'EN': 'junior',
    'MI': 'Pleno',
    'SE': 'Senior',
    'EX': 'executivo'
}

# Tradução de cargos (função traduzir_cargos_comuns)
traducao_cargos = {
    'Data Scientist': 'Cientista de Dados',
    'Data Engineer': 'Engenheiro de Dados',
    # Adicione mais traduções aqui
}
```

### Adicionar Novos Gráficos

Para adicionar novos gráficos:

1. Crie uma função no arquivo `common.py` seguindo o padrão:

```python
def criar_grafico_novo(dataframe: pd.DataFrame) -> Optional[px.Chart]:
    """
    Cria um novo gráfico.
    
    Args:
        dataframe: DataFrame filtrado
        
    Returns:
        Gráfico Plotly ou None se o DataFrame estiver vazio
    """
    if dataframe.empty:
        return None
    
    # Sua lógica aqui
    grafico = px.bar(...)
    return grafico
```

2. Adicione a chamada na função `exibir_graficos()` no arquivo `common.py`

3. O gráfico será automaticamente exibido no dashboard através do `app.py`

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

## 📝 Licença

Este projeto é de código aberto e está disponível para uso educacional e pessoal.

## 👤 Autor

Desenvolvido como projeto de análise de dados e visualização.

## 🙏 Agradecimentos

- Dados fornecidos pelo repositório [data-jobs](https://github.com/guilhermeonrails/data-jobs)
- Comunidade Streamlit pelo excelente framework
- Comunidade Plotly pelas ferramentas de visualização

---

## 🧪 Testes e Análise Exploratória

O arquivo `test.py` contém código para testes e análises exploratórias dos dados. Você pode usar este arquivo para:

- Testar transformações de dados
- Criar visualizações experimentais
- Explorar o dataset antes de adicionar ao dashboard principal

Para executar:

```bash
python test.py
```

**Nota**: Alguns códigos estão comentados. Descomente conforme necessário para suas análises.

## 🌐 Internacionalização

O dashboard foi desenvolvido com foco na experiência do usuário brasileiro, oferecendo:

- ✅ **100% em Português**: Interface, filtros, métricas e gráficos
- ✅ **Cargos Traduzidos**: Os principais cargos do mercado são exibidos em português
- ✅ **Legendas Claras**: Todos os eixos e labels dos gráficos estão traduzidos
- ✅ **Fácil Extensão**: Sistema modular permite adicionar novas traduções facilmente

**Nota**: Este dashboard é uma ferramenta de análise exploratória. Os dados são atualizados conforme a fonte original. Cargos que não possuem tradução específica são mantidos em inglês para preservar a precisão dos dados.
