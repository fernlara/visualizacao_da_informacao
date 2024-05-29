import plotly.express as px
import pandas as pd
from matplotlib import pyplot as plt
from plotly import graph_objects as go

# Importando arquivo CSV que será usado
dataset = pd.read_csv('https://github.com/fernlara/visualizacao_da_informacao/raw/master/src/dataset.csv')
dataset = pd.DataFrame(dataset)
# Selecionando e tratando apenas os dados que serão usados no gráfico 1
deaths_df = dataset.loc[dataset['Year'] == 2017]
world_deaths = deaths_df.loc[deaths_df['Entity'] == 'World']
world_deaths = world_deaths.drop(['Entity', 'Code', 'Year'], axis=1)
world_deaths = world_deaths.sort_values(by = 6573, axis=1, ascending=False)
# Criando novo dataset com dados tratados
x_data = list(world_deaths.loc[6573])
y_data = list(world_deaths.columns)
# Criando gráfico
fig = px.bar(x=x_data, y=y_data, orientation='h', labels={'y': 'Causa', 'x': 'Mortes (em milhões)', 'text':'Float'},
            title='Principais causas de morte no mundo em 2017 (Fonte: OMS)', text=x_data, range_y=[0, 10])
# Renderizando gráfico
fig.show()

# Importando dataset base
file_url = 'https://github.com/fernlara/visualizacao_da_informacao/raw/master/src/dataset.csv'
dataset = pd.read_csv(file_url)
dataset = pd.DataFrame(dataset)
# Tratando dataset e selecionando os dados que serão usados
topic = 'Deaths - Road injuries - Sex: Both - Age: All Ages (Number)'
deaths_df = dataset.loc[dataset['Year'] == 2017, ['Entity','Year', topic]]
numbers = list(pd.Series(deaths_df[topic]))
entities = list(pd.Series(deaths_df.Entity))
# Removendo a entidade Mundo da lista
entities.pop(-4)
numbers.pop(-4)
# Criando imagem
fig = go.Figure(data=go.Choropleth(
    locations=entities,
    z = numbers,
    locationmode = 'country names',
    colorscale = ('yellow','orange','red'),
    colorbar_title = "Mortes",
    )
)
fig.update_layout(title_text='Mortes em acidentes de transito no mundo em 2017, segundo OMS ((Organização Mundial da Saúde)')
# Renderizando
fig.show()

#Importando dataset base
file_url = 'https://github.com/fernlara/visualizacao_da_informacao/raw/master/src/dataset.csv'
dataset = pd.read_csv(file_url)
dataset = pd.DataFrame(dataset)
#Tratando dataset e selecionando os dados que serão usados
topic = 'Deaths - Road injuries - Sex: Both - Age: All Ages (Number)'
deaths_df = dataset.loc[dataset['Entity'] == 'World', ['Entity','Year', topic]]
numbers = list(pd.Series(deaths_df[topic]))
years = list(pd.Series(deaths_df.Year))
#Criando uma list para tornar mais simples e visualmente amigável o plot
deaths_df = [years, numbers]
# Criando o gráfico
plt.plot(years, numbers)
plt.title('Mortes no trânsito de 1990 a 2017, segundo a OMS (Organização Mundial da Saúde)')
plt.ylabel('Mortes (em milhões)')
# Renderizando
plt.show()
