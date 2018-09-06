from docxtpl import DocxTemplate
from utils.sqlutils import valueCoupleList
from utils.sqlutils import calcChain
from utils.sqlutils import calcYOY
TPLPATH='../docTpl/jbTPL1.docx'
RSTPATH='../docTpl/dbresult.docx'

def renderDocx(tplPath,curPeriod,prePeriod,preYear):
    tpl=DocxTemplate(tplPath)
    chain=calcChain(curPeriod,prePeriod)
    yoy=calcYOY(curPeriod,preYear)
    context=valueCoupleList(curPeriod)
    for key in chain:
        context[key]=chain[key]
    for key in yoy:
        context[key]=yoy[key]
    if curPeriod[4]=='0':
        context['curMth']=curPeriod[5]
    else:
        context['curMth']=curPeriod[4:6]
    tpl.render(context)
    tpl.save(RSTPATH)
    print('Template rendered.')

renderDocx(TPLPATH,'201806','201803','201706')
