import pprint
import random
import sys
from docx import Document

def anzahl(thema):
    anzahl = 0

    if thema == 0:
        anzahl = 2
    elif thema == 1:
        anzahl = 2
    elif thema == 2:
        anzahl = 2
    elif thema == 3:
        anzahl = 1
    elif thema == 4:
        anzahl = 1
    elif thema == 5:
        anzahl = 5
    elif thema == 6:
        anzahl = 5
    elif thema == 7:
        anzahl = 5
    elif thema == 8:
        anzahl = 5
    elif thema == 9:
        anzahl = 5
    elif thema == 10:
        anzahl = 5
    elif thema == 11:
        anzahl = 2
    elif thema == 12:
        anzahl = 5
    elif thema == 13:
        anzahl = 5
    else:
        anzahl = 0
    return anzahl


def create_fragebogen():

    fragen = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    feld = 0

    id = random.randint(1,1000000)
    print (id)


    with open("fragen.txt", "r") as file:
        for line in file:
            line.strip()
            if line != "###\n":
                fragen[feld].append(line)
            else:
                feld +=1

    res = []

    for thema in range(0, len(fragen)):
        if len(fragen[thema]) > 0:
            output = random.sample(fragen[thema], anzahl(thema))
            for item in output:
                res.append(item)       

    pprint.pprint(res)

    with open("fragebogen_"+str(id)+".txt", "a") as out:
        with open ("fragebogen_antwort_"+str(id)+".txt", "w") as control:
            q = random.sample(res, len(res))
            for item in q:
                f = item.split("?")[0]
                out.write(f+"?\n")
                antworten = item.split("?")[1].split("#")[0].split(",")
                for a in antworten:
                    out.write("O "+a+"\n")
                
                out.write("\n")
                control.write(f+": "+(str)(item.split("?")[1].split("#")[1]))


    with open("fragebogen_"+str(id)+".txt", "r") as input:
        contents =input.read()

        document = Document()

        document.add_heading('Fragebogen: '+str(id), 0)
        document.add_paragraph(contents)


        document.save('fragebogen'+str(id)+'.docx')

if __name__ == "__main__":
     for x in range(0,int(sys.argv[1])):
         create_fragebogen()