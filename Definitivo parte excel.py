import datetime
import csv
import wx
import plotly.plotly as py
import plotly.figure_factory as ff
import plotly

def readtsv():
    lista = []
    labels = []
    with open('output.tsv') as csvfile:
        reader = csv.reader(csvfile, delimiter="\t")
        fields = ["Task", "Start", "Finish", "Resource"]
        for row in reader:
                lista.append({key: value for key, value in zip(fields, row)})
        fig = ff.create_gantt(lista, index_col='Resource', show_colorbar=True, group_tasks=True)
        csvfile.close
    with open('labels.tsv') as csvfile: 
        reader1 = csv.reader(csvfile, delimiter="\t")
        fields = ["text"]
        for row in reader1:
            labels.append({key: value for key, value in zip(fields, row)})




#    fig.layout.xaxis.tickformat = '%Y'
    plotly.offline.plot(fig, filename='dildo.html')



def convertion(da):
    delta = datetime.timedelta(days=(365*da))
    dd = datetime.date(1, 1, 1)
    dd = dd+(delta)
    return (dd)

def writetsv(task, start, finish, maquina, text):
    with open('./output.tsv', 'a') as out:
        write = csv.writer(out, delimiter='\t', lineterminator = '\n')
        write.writerow([task, start, finish, maquina])
        out.close
    with open('labels.tsv', 'a') as out1:
        write = csv.writer(out1, delimiter='\t', lineterminator = '\n')
        write.writerow([text])
        out1.close
#     ''', "tag"'''

#def nummaquinascolores(maquinas, inputo):
#    for x in range (n):
#        writetsv(usertask, dehtos, dehtof, usermaquina, tag) 
#        
#        for x in range (n):
#            yaesta=0
#            for y in range (len(maquinas)):
#                if (maquinas [y] == inputo[x][3]):
#                    yaesta=+1
#            if (yaesta==0):
#                maquinas.append(inputo[x][3])
            

if __name__ == "__main__":
    n = 3
    starto = 4
    finisho = 6
    dehtos = convertion(starto)
    dehtof = convertion(finisho)
    usertask = "2"
    usermaquina = "maquina 4"
    tag = "mondaaaa"
    writetsv(usertask, dehtos, dehtof, usermaquina, tag)
    maquinas = ['''esta monda se llena con las maquinas inputeadas en inputo cuando este marica termine la interfaz grafica''']
    inputo = ['''aqui se meten los diccionarios de los inputos con la monda grafica de este man''']


    print (dehtos, "\n",dehtof)
