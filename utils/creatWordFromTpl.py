from docxtpl import DocxTemplate
from utils.sqliteconv import valueCoupleList
from utils.sqliteconv import calcChain
TPLPATH='../docTpl/1.docx'
RSTPATH='../docTpl/dbresult.docx'

def renderDocx(tplPath,curPeriod,prePeriod,divTimes):
    tpl=DocxTemplate(tplPath)
    chain=calcChain(curPeriod,prePeriod)
    context=valueCoupleList(curPeriod,divTimes)
    for key in chain:
        context[key]=chain[key]
    if curPeriod[4]=='0':
        context['curMth']=curPeriod[5]
    else:
        context['curMth']=curPeriod[4:6]
    tpl.render(context)
    tpl.save(RSTPATH)
    print('Template rendered.')

renderDocx(TPLPATH,'201806','201803',10000)
