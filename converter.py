import sys
import os
import xml.etree.cElementTree as ET
import json
from collections import OrderedDict
from flashtext import KeywordProcessor
keyword_processor = KeywordProcessor()

dict = {
    'Uid': ['УИД_ЗН'],
    'EmTemp': ['АварТемпер'],
    'AdrInf' : ['АдрИнф'],
    'AdrComment' : ['АдрКоммент'],
    'LocAdr':['АдрМН'],
    'AdrPlcDelVeh': ['АдрМесПодТС'],
    'AdrRF':['АдрРФ'],
    'AdrTxt':['АдрТекст'],
    'VersProg' :['ВерсПрог'],
    'VersForm':['ВерсФорм'],
    'TypeDoc':['ВидДок'],
    'ContType':['ВидТар'],
    'Capacity' :['Вместим'],
    'PossDistr' :['ВозмРаспр'],
    'TInfChart' :['ВрИнфФт'],
    'TInfFrei' :['ВрИнфФщ'],
    'TFileInfChart' :['ВрФайлИнфФт'],
    'TFileInfFrei' :['ВрФайлИнфФщ'],
    'Altitude' :['ВысЗнач'],
    'GLN' :['ГЛН'],
    'Dimens' :['Габар'],
    'City' :['Город'],
    'PackGroup' :['ГрУп'],
    'LoadCap' :['Грузопод'],
    'DataFor' :['ДаннИно'],
    'DatTimFinUseVeh' :['ДатВрЗавПолТС'],
    'DatTMark' :['ДатВрОтмет'],
    'DatTDelVeh' :['ДатВрПодТС'],
    'DatInfChart' :['ДатИнфФт'],
    'DatInfFrei' :['ДатИнфФщ'],
    'DatExpRet' :['ДатИстВрУдер'],
    'DatFileInfChart' :['ДатФайлИнфФт'],
    'DatFileInfFrei' :['ДатФайлИнфФщ'],
    'DatExpDrLicense' :['ДатаВыдВУ'],
    'DatWaybillExtracts' :['ДатаВыпПЛ'],
    'DatePwrAtrn' :['ДатаДовер'],
    'DateDok' :['ДатаДок'],
    'DateOrd' :['ДатаЗН'],
    'DateFix' :['ДатаИспр'],
    'DateExRate' :['ДатаКурсВал'],
    'DatFinDrLicense' :['ДатаОконВУ'],
    'DatePrizOrd' :['ДатаПринЗН'],
    'DateSP' :['ДатаСР'],
    'Length' :['ДлЗнач'],
    'DocCar' :['ДокКГр'],
    'DocOrd' :['ДокКЗН'],
    'Document' :['Документ'],
    'Longitude' :['Долгота'],
    'PosPersOrd' :['ДолжПринЗН'],
    'Position' :['Должн'],
    'Home' :['Дом'],
    'AddInfDoc' :['ДопСведДок'],
    'DifInfCarg' :['ДрОГруз'],
    'DangSign' :['ЗнОп'],
    'Value' :['Значение'],
    'INNI' :['ИННФЛ'],
    'INNL' :['ИННЮЛ'],
    'IdDoc' :['ИдДок'],
    'IdDatInfChart' :['ИдИнфФт'],
    'IdDatInfFrei' :['ИдИнфФщ'],
    'IdCont' :['ИдКонтейн'],
    'IdDetlsDoc' :['ИдРекСост'],
    'IdSP' :['ИдСР'],
    'IdStorSyst' :['ИдСистХран'],
    'IdStatus' :['ИдСтат'],
    'IdFile' :['ИдФайл'],
    'IdInfField' :['ИдФайлИнфПол'],
    'IdDatFileInfChart' :['ИдФайлИнфФт'],
    'IdDatFileInfFrei' :['ИдФайлИнфФщ'],
    'IdentDov' :['ИдентДовер'],
    'Identif' :['Идентиф'],
    'ChDatTTrnsf' :['ИзмДатВрВыпПрвз'],
    'ChWayTrnsf' :['ИзмМршВыпПрвз'],
    'ChTTrnsf' :['ИзмСрокВыпПрвз'],
    'Name' :['Имя'],
    'ForgnCont' :['ИнКонт'],
    'DifRecsIdent' :['ИнРекИдентифЛиц'],
    'Index' :['Индекс'],
    'IndexWout' :['ИндексБез'],
    'InField' :['ИнфПол'],
    'DifParams' :['ИныеСвед'],
    'FixOrd' :['ИспрЗН'],
    'FinAmountFor' :['ИтогРазмШтрИн'],
    'FinAmountRub' :['ИтогРазмШтрРФ'],
    'KND' :['КНД'],
    'PackCat' :['КатУпак'],
    'Flat' :['Кварт'],
    'Class' :['Клас'],
    'ClassCode' :['КласКод'],
    'CodeGAR' :['КодГАР'],
    'CodeOKV' :['КодОКВ'],
    'CodeLimTonnel' :['КодОгрЧерТун'],
    'CodeDistr' :['КодРегион'],
    'CodeCount' :['КодСтр'],
    'CodeCargNew' :['КодТовНом'],
    'NumberCont' :['КолКонтейн'],
    'NumSeats' :['КолМест'],
    'NumPall' :['КолПалл'],
    'Number' :['Колво'],
    'Cont' :['Конт'],
    'ContTemper' :['КонтТемпер'],
    'Contact' :['Контакт'],
    'Coord' :['Коорд'],
    'Building' :['Корпус'],
    'ExRate' :['КурсВал'],
    'MaxActiv' :['МаксАкт'],
    'Marking' :['Марк'],
    'Mark' :['Марка'],
    'MassBrutVal' :['МасБрутЗнач'],
    'MassCarg' :['МасГруз'],
    'MassNoVal' :['МасНетЗнач'],
    'WayMachRead' :['МршМашЧит'],
    'WayTransf' :['МршПрвз'],
    'WayTxt' :['МршТекст'],
    'PropShipName' :['НадОтгНаим'],
    'NameRadionuc' :['НазРадионук'],
    'Naim' :['Наим'],
    'NameCarg' :['НаимГруз'],
    'NameDoc' :['НаимДок'],
    'NameOIV' :['НаимОИВ'],
    'NameOKV' :['НаимОКВ'],
    'NameOrg' :['НаимОрг'],
    'NamePL' :['НаимПЛ'],
    'AplExTTypeElemP' :['НалКоорТочВрВыпПрвз'],
    'AplExTTypeElemO' :['НалКоорТочВрОтмет'],
    'AplExTTypeElemTC' :['НалКоорТочВрПодТС'],
    'AplExTypeElem' :['НалКоорТочВрПолТС'],
    'SelPoint' :['НаселПункт'],
    'IDNDL' :['НомВУ'],
    'IDNDoc' :['НомДок'],
    'IDNDFix' :['НомИспр'],
    'IDNDOON' :['НомООН'],
    'IDNDSR' :['НомСР'],
    'IDNDTrust' :['НомерДовер'],
    'NumberOfDoc' :['НомерДок'],
    'NumberOfZN' :['НомерЗН'],
    'NumberOfPL' :['НомерПЛ'],
    'OGRNIP' :['ОГРНИП'],
    'TotalMassNoExplosiveCont' :['ОбМасНетВзрСод'],
    'TotalMassNoExplosiveAll' :['ОбМасНетВзрСодВсех'],
    'TotalPriceGr' :['ОбЦеннГр'],
    'CurcMark' :['ОбстОтмет'],
    'Volume' :['Объем'],
    'DescrCarg' :['ОпГруз'],
    'DescrFizChemForm' :['ОписФизХимФорм'],
    'Description' :['Описание'],
    'FixSign' :['ОпозЗнак'],
    'MarkChart' :['ОтметФт'],
    'MarkFrei' :['ОтметФщ'],
    'SecondName' :['Отчество'],
    'ParamsTransp' :['ПарТС'],
    'Density' :['Плотн'],
    'Signater' :['Подписант'],
    'FullActCarg' :['ПолнАктГр'],
    'WayDone' :['ПорядОсущ'],
    'PrecMix' :['ПроцСмеси'],
    'WaiList' :['ПутевойЛист'],
    'AmouNonPresVeh' :['РазШтрНеПрТС'],
    'AmouNonPresOtk' :['РазШтрОткПол'],
    'AmountFine' :['РазмШтр'],
    'AmountPrice': ['РазмерПлат'],
    'Area': ['Район'],
    'ExpencesToolRoads': ['РасхПлатДор'],
    'ExpencesProm': ['РасхПром'],
    'ExpencesCustDuty': ['РасхТамПош'],
    'CostFine': ['РасчШтр'],
    'TotalCost': ['Расчет'],
    'NumberOfArea': ['РегНомер'],
    'ModeWorkRest': ['РежТрОтд'],
    'DetAccStat': ['РекСопрВед'],
    'DetAct': ['СвАкт'],
    'DetActVzv': ['СвАктВзв'],
    'DetDriver': ['СвВодит'],
    'DetCarg': ['СвГруз'],
    'DetTrust': ['СвДовер'],
    'DetContain': ['СвКонтейн'],
    'DetWayVeh': ['СвМршПодТС'],
    'DetChangeFeri': ['СвОгЗамФщ'],
    'DetOPCarg': ['СвОпГруз'],
    'DetZNIsp': ['СвПринЗНИсп'],
    'DetOtherCond': ['СвПрочУсл'],
    'DetStepPay': ['СвРазПлатТС'],
    'DetSpIDSign': ['СвСпИдПодп'],
    'DetTimePay': ['СвСрокВыпПрвз'],
    'DetTimePL': ['СвСрокПЛ'],
    'DetVech': ['СвТС'],
    'DetOrdChart': ['СвУказФт'],
    'DetCondFrah': ['СвУслФрах'],
    'DetChart': ['СвФт'],
    'DetFrei': ['СвФщ'],
    'WayDetails': ['СведМрш'],
    'SystDetails': ['СведСистОтм'],
    'SerVY': ['СерВУ'],
    'ContOrdChart': ['СодЗНИнфФт'],
    'ContOrdFrei': ['СодЗНИнфФщ'],
    'AccompDocs': ['СопрДок'],
    'CargoCond': ['СостГруз'],
    'WayPack': ['СпУпак'],
    'WaysConn': ['СредСвяз'],
    'TimeSP': ['СрокСР'],
    'PriceService': ['СтУсл'],
    'PriceOfCarg': ['СтЦеннГр'],
    'StatSignater': ['СтатПодп'],
    'Countr': ['Стран'],
    'TxtInf': ['ТекстИнф'],
    'TechName': ['ТехНаим'],
    'Type': ['Тип'],
    'Nmbr': ['Тлф'],
    'TransIndex': ['ТрансИндекс'],
    'IdDocForgnFP': ['УдЛичнИнФЛ'],
    'InstrNormTrans': ['УкНормПрвз'],
    'Street': ['Улица'],
    'File': ['Файл'],
    'NSS': ['ФИО'],
    'NSSPersons': ['ФИОЛиц'],
    'ActNumbUnsMeas': ['ФактКолЕдИзм'],
    'Surname': ['Фамилия'],
    'ChartFL': ['ФтФЛ'],
    'ChartUL': ['ФтЮЛ'],
    'FreiIP': ['ФщИП'],
    'FreiUL': ['ФщЮЛ'],
    'PriceCarg': ['ЦеннГруз'],
    'WidMean': ['ШирЗнач'],
    'Width': ['Широта'],
    'ESign': ['ЭП'],
    'Email': ['ЭлПочта']
}
keyword_processor.add_keywords_from_dict(dict)

def elem_to_internal(elem, strip_ns=1, strip=1):
    d = OrderedDict()
    elem_tag = elem.tag
    #print(elem_tag)

    for key, value in list(elem.attrib.items()):
        d[key] = value
        #print(key)

    # loop over subelements to merge them
    for subelem in elem:
        v = elem_to_internal(subelem, strip_ns=strip_ns, strip=strip)
        tag = subelem.tag
        #print(tag)
        value = v[tag]
        #print(value)
        try:
            # add to existing list for this tag
            d[tag].append(value)
        except AttributeError:
            # turn existing entry into a list
            d[tag] = [d[tag], value]
        except KeyError:
            # add a new non-list entry
            d[tag] = value
    text = elem.text

    if not d:
        # text is the value if no attributes
        d = text or None
    return {elem_tag: d}


def elem2json(elem, strip_ns=1, strip=1):
    """Convert an ElementTree or Element into a JSON string."""

    if hasattr(elem, 'getroot'):
        elem = elem.getroot()
    return json.dumps(elem_to_internal(elem, strip_ns=strip_ns, strip=strip), indent=4, ensure_ascii=False,
                      separators=(',', ': '))


def xml2json(xmlstring, strip_ns=1, strip=1):
    """Convert an XML string into a JSON string."""

    elem = ET.fromstring(xmlstring)
    return elem2json(elem, strip_ns=strip_ns, strip=strip)


def main():
    strip_ns = 0
    strip = 0

    ids_f_files = []
    if len(sys.argv) != 2:  # проверка количества аргументов
        sys.stderr.write("Insufficient number of arguments")
        sys.exit(-1)

    dir_path = sys.argv[1]
    try:
        for dir in os.listdir(dir_path):
            print(dir)
            dir_a = '{0}/{1}'.format(dir_path, dir)
            os.mkdir('output/{0}'.format(dir))
            save_path = 'output/{0}'.format(dir)  # папка для вывода результатов
            for file in os.listdir(dir_a):
                print(file)
                xml_str = open(f'{dir_path}/{dir}/{file}', 'r', encoding='utf-8').read()
                out1 = xml2json(xml_str, strip_ns, strip)

                out = keyword_processor.replace_keywords(out1)

                name_outfile = os.path.join(save_path, '{0}.json'.format(file[:-4]))
                outfile = open(name_outfile, 'w', encoding='utf-8')
                outfile.write(out)
                outfile.close()
    except:  # ошибки при открытии директории
        if 'file' in locals():
            sys.stderr.write("Problem reading '{0}'\n".format(file))
        else:
            sys.stderr.write("Problem reading '{0}'\n".format(dir))
        sys.exit(-2)

if __name__ == '__main__':
    main()