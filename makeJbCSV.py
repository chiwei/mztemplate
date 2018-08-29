from dbfread import DBF
import time

dbfpath='./data/jb18.dbf'
csvpath='./output/jb18.csv'
curYear=2018
headerpath='./output/headder.csv'
header=open(headerpath,'w')
indexName="qhdm,year,sq,F_2,F_3,F_7,F_8,F_10,F_13,F_14,F_16,F_19,F_24,F_25,F_28,F_33,F_34,F_46,F_49,F_52,F_62,F_70,F_73,F_76,F_101,F_106,F_111,F_112,F_113,F_114,F_115,F_116,F_117,F_118,F_121,F_122,F_123,F_124,F_137,F_139,F_140,F_142,F_143,F_144,F_157,F_158,F_170,F_181,F_191,F_193,F_204,F_210,F_227,F_230,F_231,F_232,F_234,F_235,F_237,F_238,F_242,F_243,F_244,F_245"

indexDict={'1.镇':'F_2','2.乡小计':'F_3','3.街道':'F_7','4.区公所':'F_8','（三）社会服务事业费累计支出':'F_10','3.社会福利':'F_13','4.社会救助':'F_14','A城市低保累计支出':'F_16','B农村低保累计支出':'F_19','B农村特困人员救助供养支出':'F_24','（3）直接医疗救助支出':'F_25','（4）临时救助支出':'F_28','1.机构数':'F_33','A、老年人与残疾人服务机构':'F_34','B、智障与精神病人服务机构':'F_46','C、儿童收养救助服务机构':'F_49','D、其他提供住宿的社会服务机构':'F_52','（1）老年人与残疾人服务床位数':'F_62','（2）智障与精神病人服务床位数':'F_70','（3）儿童收养救助服务床位数':'F_73','（4）其他提供住宿的社会服务床位数':'F_76','不提供住宿的社会服务机构和设施总数':'F_101','（1）社区服务机构和设施总数':'F_106','a社区服务指导中心':'F_111','社区服务指导中心：农村':'F_112','b社区服务中心':'F_113','社区服务中心：农村':'F_114','c社区服务站':'F_115','社区服务站：农村':'F_116','d社区养老机构和设施':'F_117','社区养老机构和设施：农村':'F_118','e社区互助型养老设施':'F_121','社区互助型养老设施：农村':'F_122','f其他社区服务机构和设施':'F_123','其他社区服务机构和设施：农村':'F_124','（1）孤儿':'F_137','（a）集中供养孤儿':'F_139','（b）社会散居孤儿':'F_140','（2）成立收养关系登记':'F_142','其中：涉外及港澳台收养登记':'F_143','（a）城市低保人数':'F_144','（d）城市低保户数':'F_157','（a）农村低保人数':'F_158','（d）农村低保户数':'F_170','供养人数':'F_181','（a）民政部门资助参加基本医疗保险':'F_191','（b）民政部门直接救助人次数':'F_193','（4）临时救助':'F_204','救助总人次数':'F_210','（4）社会捐赠接收站、点和慈善超市数':'F_227','1.社会团体':'F_230','2.民办非企业':'F_231','3.基金会':'F_232','1.村委会':'F_234','2.居委会':'F_235','（1）婚姻登记机构':'F_237','（2）殡葬机构':'F_238','（1）结婚登记':'F_242','其中：涉外及港澳台登记':'F_243','（2）离婚登记':'F_244','火化遗体数':'F_245'}
'''
print('区划代码,年度,时期,',end='',file=header)
for k,v in indexDict.items():
    print(k+',',end='',file=header)
    print(k+',',end='')
header.close()
header=open(headerpath,'a')
print(file=header)
print('qhdm,year,sq,',end='',file=header)
for k,v in indexDict.items():
    print(v+',',end='',file=header)
print(file=header)
header.close()
'''


def makeDataFromDBF():
    jbraw=open(headerpath,"a")
    print(indexName,sep=",",file=jbraw)
    try:
        tableDBF=DBF(dbfpath,ignore_missing_memofile=True)
    except:
        print("no file")
        return
    print('Start to create CSV file.')
    begin_time=time.time()
    for record in tableDBF:
        print(str(record['SYS_ZDM'])[0:12],curYear,str(record['SYS_ZDM'])[12:14],record['F_2'],record['F_3'],record['F_7'],
          record['F_8'],record['F_10'],record['F_13'],record['F_14'],record['F_16'],record['F_19'],record['F_24'],
          record['F_25'],record['F_28'],record['F_33'],record['F_34'],record['F_46'],record['F_49'],record['F_52'],
          record['F_62'],record['F_70'],record['F_73'],record['F_76'],record['F_101'],record['F_106'],record['F_111'],
          record['F_112'],record['F_113'],record['F_114'],record['F_115'],record['F_116'],record['F_117'],record['F_118'],
          record['F_121'],record['F_122'],record['F_123'],record['F_124'],record['F_137'],record['F_139'],record['F_140'],
          record['F_142'],record['F_143'],record['F_144'],record['F_157'],record['F_158'],record['F_170'],record['F_181'],
          record['F_191'],record['F_193'],record['F_204'],record['F_210'],record['F_227'],record['F_230'],record['F_231'],
          record['F_232'],record['F_234'],record['F_235'],record['F_237'],record['F_238'],record['F_242'],record['F_243'],
          record['F_244'],record['F_245'],sep=",",file=jbraw)
    print("csv created!", len(tableDBF), "items wrote down.", round(time.time() - begin_time, 2), "seconds elapsed.")
    jbraw.close()
    return

makeDataFromDBF()