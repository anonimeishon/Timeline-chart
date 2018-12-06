import datetime
import csv


def convertion(da):
    print(da)
    type(da)
    d = 365*da
    delta = datetime.timedelta(days=(d))
    dd = datetime.date(1, 1, 1)
    dd = dd+(delta)
    return (dd)

def writetsv(start, finish):
    with open('./output.tsv', 'wt') as out:
        write = csv.writer(out, delimiter='\t')
        write.writerow(["task", start, finish, "maquina", "tag"] )

if __name__ == "__main__":
    starto = 2
    finisho = 4
    dehtos = convertion(starto)
    dehtof = convertion(finisho)
    writetsv(dehtos, dehtof) 
    print (dehtos, "\n",dehtof)

"""df = [dict(Task="Job A", Start='convertion(userinputstart)', Finish='convertion(userinputfinish)'),
      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
      dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')]
"""

    #dd =dd(day=dayzz)
    #print (d)
    #remember to use %Y or %j