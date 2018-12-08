import plotly.plotly as py
import plotly.figure_factory as ff
import plotly.graph_objs as go
import plotly
import csv
import pandas as pd


#funcion que lee el archivo y lo escribe en una lista de diccionarios
def readtsv():
      lista = []
      labels = []
      with open('output.tsv') as csvfile:
            reader = csv.reader(csvfile, delimiter="\t")
            fields = ["Task", "Start", "Finish", "Resource"]
            for row in reader:
                  lista.append({key: value for key, value in zip(fields, row)})
      with open('labels.tsv') as csvfile: 
            reader1 = list(list(rec)for rec in csv.reader(csvfile, delimiter='\t'))
      labels = reader1
      return (lista, labels)



def anotar(basura,fig, labels):
      trash = []
      identificador = []
      #check how many tasks there are
      for i in basura:
            if i.get("Task") not in identificador:
                  identificador.append(i.get("Task"))
      
      #assign each id to each task
      ids = []
      for i in range(len(identificador)-1,-1,-1):
            ids.append(i)
            v=0                        

      #assign annotations to each resource according to the
      #task they are assigned to
      for i in basura:  

            for j in range(len(identificador)):
                  valor = str(labels[v])
                  if i.get("Task") == identificador[j]:
                        trash.append(dict(x=i.get("Start"),y=ids[j],text=valor, showarrow=True, font=dict(color='black')))
                        quit
            v = v+1
      fig['layout']['annotations'] = tuple(trash)
'''      for i in basura:  
            v=0                        
            for j in range(len(identificador)):
                  valor = str(labels[v])
                  if i.get("Task") == identificador[j]:
                        trash.append(dict(x=i.get("Start"),y=ids[j],text=valor, showarrow=True, font=dict(color='black')))
                  v= v+1
'''
      #layout = go.Layout(showlegend=False,annotations=tuple(trash))


if __name__ == "__main__":
      
#Creando lista de datos y llamando funciones que crean grafica
      lista= []  
      labels = []
      lista, labels = readtsv()


      fig = ff.create_gantt(lista, index_col='Resource', show_colorbar=True, group_tasks=True)
      #Configuraciones de fig
      fig['layout']['xaxis']['tickformat'] = '%Y'
      #fig['layout']['xaxis']['tickvals'] = pd.date_range('2000-01-01', '2100-03-01', freq='d')
      #fig['layout']['xaxis']['ticktext'] = list(range(len(fig['layout']['xaxis']['tickvals'])))
      
      anotar(lista, fig, labels)

      plotly.offline.plot(fig, filename='dildo.html')
