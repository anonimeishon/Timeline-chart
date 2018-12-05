import plotly.plotly as py
import plotly.figure_factory as ff
import plotly

df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
      dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')]

fig = ff.create_gantt(df)
fig.layout.xaxis.tickformat = '%j'

fig['layout']['annotations'] = [dict(x='2009-02-01',y=0,text="This is a label", showarrow=False, font=dict(color='white'))]

plotly.offline.plot(fig, filename='dildo.html')