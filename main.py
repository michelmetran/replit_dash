from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

# we are using the restaurant tips dataset from Plotly Express
df = px.data.tips()

# create the app
app = Dash(__name__)

# specify the choices in the dropdown list, with default value
dropdown = dcc.Dropdown(["Fri", "Sat", "Sun"], "Fri", clearable=False)

# create the chart component
graph = dcc.Graph()

# layout of the app -- Heading 4 text followed by the dropdown list, followed by the chart
app.layout = html.Div(
    [html.H4("Restaurant tips by day of week"), dropdown, graph])

# what output to get when you select an input
@callback(Output(graph, "figure"), Input(dropdown, "value"))
def update_bar_chart(day):
    mask = df["day"] == day
    fig = px.bar(df[mask],
                 x="sex",
                 y="total_bill",
                 color="smoker",
                 barmode="group")
    return fig


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
