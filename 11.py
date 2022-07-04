import plotly.express as px
  
# using the dataset
df = px.data.tips()
  
# plotting the histogram
fig = px.histogram(df, x="total_bill", color='sex',
                   nbins=50, histnorm='percent',
                   barmode='overlay')
  
# showing the plot
fig.show()