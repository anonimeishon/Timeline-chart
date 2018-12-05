import plotly.plotly as py
import plotly.figure_factory as ff
import plotly
df = [
    dict(Task='1', Start='0635', Finish='0785', Resource='Maquina 4'),
    dict(Task='1', Start='0087', Finish='0334', Resource='Maquina 1'),
    dict(Task='1', Start='0334', Finish='0457', Resource='Maquina 7'),
    dict(Task='1', Start='0823', Finish='0968', Resource='Maquina 8'),

    dict(Task='2', Start='0462', Finish='0676', Resource='Maquina 1'),
    dict(Task='2', Start='0817', Finish='0883', Resource='Maquina 2'),
    dict(Task='2', Start='0894', Finish='0989', Resource='Maquina 6'),
    dict(Task='2', Start='1088', Finish='1208', Resource='Maquina 5'),

    dict(Task='3', Start='0000', Finish='0087', Resource='Maquina 1'),
    dict(Task='3', Start='0238', Finish='0338', Resource='Maquina 5'),
    dict(Task='3', Start='0338', Finish='0503', Resource='Maquina 8'),
    dict(Task='3', Start='087', Finish='0232', Resource='Maquina 7'),

    dict(Task='4', Start='0000', Finish='0065', Resource='Maquina 2'),
    dict(Task='4', Start='0490', Finish='0635', Resource='Maquina 4'),
    dict(Task='4', Start='0065', Finish='0238', Resource='Maquina 5'),
    dict(Task='4', Start='0647', Finish='0817', Resource='Maquina 7'),

    dict(Task='5', Start='0489', Finish='0536', Resource='Maquina 5'),
    dict(Task='5', Start='0714', Finish='0894', Resource='Maquina 6'),

    dict(Task='5', Start='0572', Finish='0672', Resource='Maquina 2'),

    dict(Task='5', Start='0334', Finish='0462', Resource='Maquina 1'),
    dict(Task='6', Start='0968', Finish='1088', Resource='Maquina 5'),

    dict(Task='6', Start='0823', Finish='0946', Resource='Maquina 4'),
    dict(Task='6', Start='1088', Finish='1208', Resource='Maquina 5'),

    dict(Task='6', Start='0672', Finish='0817', Resource='Maquina 2'),
    dict(Task='7', Start='0000', Finish='0145', Resource='Maquina 3'),
    dict(Task='7', Start='0145', Finish='0269', Resource='Maquina 3'),
    dict(Task='7', Start='0536', Finish='0681', Resource='Maquina 5'),
    dict(Task='7', Start='0681', Finish='0821', Resource='Maquina 5'),

    dict(Task='8', Start='0245', Finish='0490', Resource='Maquina 4'),
    dict(Task='8', Start='0817', Finish='0995', Resource='Maquina 7'),
    dict(Task='8', Start='0490', Finish='0714', Resource='Maquina 6'),
    dict(Task='8', Start='1055', Finish='1205', Resource='Maquina 7'),

    dict(Task='9', Start='0269', Finish='0449', Resource='Maquina 3'),
    dict(Task='9', Start='0449', Finish='0489', Resource='Maquina 5'),
    dict(Task='9', Start='0065', Finish='0215', Resource='Maquina 2'),
    dict(Task='9', Start='0503', Finish='0673', Resource='Maquina 8'),

    dict(Task='10', Start='0000', Finish='0245', Resource='Maquina 4'),
    dict(Task='10', Start='0245', Finish='0469', Resource='Maquina 6'),
    dict(Task='10', Start='0469', Finish='0647', Resource='Maquina 7'),
    dict(Task='10', Start='0673', Finish='0087', Resource='Maquina 8'),

    dict(Task='11', Start='0449', Finish='0599', Resource='Maquina 3'),
    dict(Task='11', Start='0785', Finish='1005', Resource='Maquina 4'),
    dict(Task='11', Start='1055', Finish='1205', Resource='Maquina 6'),
    dict(Task='11', Start='1005', Finish='1055', Resource='Maquina 7'),

    dict(Task='12', Start='0215', Finish='0087', Resource='Maquina 2'),
    dict(Task='12', Start='0599', Finish='0823', Resource='Maquina 3'),
    dict(Task='12', Start='0823', Finish='0968', Resource='Maquina 5'),
    dict(Task='12', Start='0968', Finish='1198', Resource='Maquina 8'),
]

colors = {'Maquina 1': 'rgb(220, 0, 0)',
          'Maquina 2': (1, 0.9, 0.16),
          'Maquina 3': 'rgb(0, 255, 100)',
          'Maquina 4': 'rgb(0, 40, 20)',
          'Maquina 5': 'rgb(59, 20, 200)',
          'Maquina 6': 'rgb(20, 140, 100)',
          'Maquina 7': 'rgb(80, 0, 100)',
          'Maquina 8': 'rgb(250, 0, 100)',
          }


fig = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True, group_tasks=True)
plotly.offline.plot(fig, filename='gantt.html')
