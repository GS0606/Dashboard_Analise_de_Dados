"""
Dashboard de Análise de Salários na Área de Dados

Este módulo implementa o ponto de entrada principal do dashboard interativo.
Todas as funções auxiliares estão organizadas no módulo common.py para
facilitar a manutenção e reutilização do código.
"""

import streamlit as st
from common import (
    URL_DADOS,
    processar_dados,
    filtrar_dataframe,
    criar_barra_lateral_filtros,
    calcular_metricas,
    exibir_metricas,
    exibir_insights,
    exibir_graficos,
    exibir_tabela_dados,
    gerar_insights,
    validar_dataframe,
    formatar_moeda
)


def main() -> None:
    """
    Função principal que orquestra a execução do dashboard.
    """
    # Configuração da página
    st.set_page_config(
        page_title="Análise de Dados de Salários em Tecnologia",
        layout="wide",
        page_icon="📊"
    )
    
    # Processamento dos dados
    df = processar_dados(URL_DADOS)
    
    # Criação dos filtros
    filtros = criar_barra_lateral_filtros(df)
    
    # Filtragem dos dados
    df_filtrado = filtrar_dataframe(
        df,
        filtros['anos'],
        filtros['senioridades'],
        filtros['contratos'],
        filtros['tamanhos_empresa'],
        filtros['cargos']
    )
    
    # Cabeçalho principal
    st.title("📊 Dashboard de Análise de Salários na Área de Dados")
    st.markdown(
        "Explore os dados salariais na área de dados nos últimos anos. "
        "Utilize os filtros à esquerda para refinar sua análise."
    )
    
    # Verificar se há dados filtrados
    if not validar_dataframe(df_filtrado):
        st.warning("⚠️ Nenhum dado encontrado com os filtros selecionados. Por favor, ajuste os filtros.")
        return
    
    # Exibição das métricas
    metricas = calcular_metricas(df_filtrado, df)
    exibir_metricas(metricas)
    
    st.markdown("---")
    
    # Exibir insights
    insights = gerar_insights(df_filtrado, metricas)
    exibir_insights(insights)
    
    # Organizar visualizações em tabs
    tab1, tab2, tab3 = st.tabs(["📈 Visão Geral", "🔍 Análises Comparativas", "📋 Dados Detalhados"])
    
    with tab1:
        st.header("Visão Geral dos Dados")
        exibir_graficos(df_filtrado, "Visão Geral")
    
    with tab2:
        st.header("Análises Comparativas e Tendências")
        exibir_graficos(df_filtrado, "Análises Comparativas")
    
    with tab3:
        st.header("Dados Detalhados")
        exibir_tabela_dados(df_filtrado)
        
        # Estatísticas descritivas
        st.subheader("📊 Estatísticas Descritivas")
        if validar_dataframe(df_filtrado):
            st.dataframe(
                df_filtrado['salario_usd'].describe().apply(
                    lambda x: formatar_moeda(x) if isinstance(x, (int, float)) else x
                ),
                use_container_width=True
            )


if __name__ == "__main__":
    main()
