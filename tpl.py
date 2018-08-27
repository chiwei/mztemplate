from docxtpl import DocxTemplate
from sqliteconv import loadfromCSV
import sqlite3
tpl=DocxTemplate('./doc/1.docx')
loadfromCSV('outputjb18.csv')
curMth=6
conn=sqlite3.connect('cmd.db')
cursor=conn.execute('select csdbrs from jbdata where sq="06" and qhdm="000000000000"')
print(cursor.row[0])
'''#
context={
    'curMth':curMth,
    'csdbrs':csdbrs,
    'csdbhs':csdbhs,
    'ncdbrs':ncdbrs,
    'ncdbhs':ncdbhs,

}

tpl.render(context)
tpl.save("./doc/db.docx")
#'''