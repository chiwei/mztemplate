from docxtpl import DocxTemplate
from sqliteconv import loadfromCSV
from sqliteconv import wrapperSelector
import sqlite3
tpl=DocxTemplate('./doc/db.docx')
#loadfromCSV('outputjb18.csv')
curMth=6
SQ="06"
preSQ="03"
csdbrs=round(wrapperSelector("csdbrs",SQ)/10000,1)
csdbrsTB=round((wrapperSelector("csdbrs",SQ)-wrapperSelector("csdbrs",preSQ))/wrapperSelector("csdbrs",preSQ)*100,1)
csdbhs=round(wrapperSelector("csdbhs",SQ)/10000,1)
csdbhsTB=round((wrapperSelector("csdbhs",SQ)-wrapperSelector("csdbhs",preSQ))/wrapperSelector("csdbhs",preSQ)*100,1)
ncdbrs=round(wrapperSelector("ncdbrs",SQ)/10000,1)
ncdbrsTB=round((wrapperSelector("ncdbrs",SQ)-wrapperSelector("ncdbrs",preSQ))/wrapperSelector("ncdbrs",preSQ)*100,1)
ncdbhs=round(wrapperSelector("ncdbhs",SQ)/10000,1)
ncdbhsTB=round((wrapperSelector("ncdbhs",SQ)-wrapperSelector("ncdbhs",preSQ))/wrapperSelector("ncdbhs",preSQ)*100,1)
context={
    'curMth':curMth,
    'csdbrs':csdbrs,
    'csdbrsTB':csdbrsTB,
    'csdbhs':csdbhs,
    'csdbhsTB':csdbhsTB,
    'ncdbrs':ncdbrs,
    'ncdbrsTB':ncdbrsTB,
    'ncdbhs':ncdbhs,
    'ncdbhsTB':ncdbhsTB,

}

tpl.render(context)
tpl.save("./doc/dbresult.docx")
