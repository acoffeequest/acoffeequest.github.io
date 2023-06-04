import altair as alt
import datapane as dp
import pandas as pd


df = pd.DataFrame({'price': [1.89, 4.60, 3.20], 'rating': [6, 4, 5]})

fig = (
    alt.Chart(df)
    .mark_point()
    .encode(
        x=alt.X("price", scale=alt.Scale(zero=False)),
        y=alt.X("rating", scale=alt.Scale(zero=False)),
        color="price",
        tooltip=list(df.columns),
    )
)

dp.save_report(fig, "../_includes/scatter.html")
