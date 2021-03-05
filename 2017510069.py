import csv
import sys


def csvtoxml (args,argv):
    with open(args, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        f = open(argv, "w", encoding='utf-8')


        f.write("<Departments>\n")
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                f.write(f'\t<ÜNİVERSİTE_TÜRÜ>{row[0]}</ÜNİVERSİTE_TÜRÜ>\n')
                f.write(f'\t  <ÜNİVERSİTE>{row[1]}</ÜNİVERSİTE>\n')
                f.write(f'\t      <FAKÜLTE>{row[2]}</FAKÜLTE>\n')
                f.write(f'\t      <PROGRAM_KODU>{row[3]}</PROGRAM_KODU>\n')
                f.write(f'\t      <PROGRAM>{row[4]}</PROGRAM>\n')
                f.write(f'\t      <DİL>{row[5]}</DİL>\n')
                f.write(f'\t      <ÖĞRENİM_TÜRÜ>{row[6]}</ÖĞRENİM_TÜRÜ>\n')
                f.write(f'\t      <BURS>{row[7]}</BURS>\n')
                f.write(f'\t      <ÖĞRENİM_SÜRESİ>{row[8]}</ÖĞRENİM_SÜRESİ>\n')
                f.write(f'\t      <PUAN_TÜRÜ>{row[9]}</PUAN_TÜRÜ>\n')
                f.write(f'\t      <KONTENJAN>{row[10]}</KONTENJAN>\n')
                f.write(f'\t      <OKUL_BİRİNCİSİ_KONTENJANI>{row[11]}</OKUL_BİRİNCİSİ_KONTENJANI>\n')
                f.write(f'\t      <GEÇEN_YIL_MİN_SIRALAMA>{row[12]}</GEÇEN_YIL_MİN_SIRALAMA>\n')
                f.write(f'\t      <GEÇEN_YIL_MİN_PUAN>{row[13]}</GEÇEN_YIL_MİN_PUAN>\n')
                line_count += 1
        f.write("</Departments>")
        print(f'Processed {line_count} lines.')

        f.close()

def csvtojson(argc,argv):
    with open(argc, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        f = open(argv, "w", encoding='utf-8')

        f.write('[\n')
        f.write('   {\n')
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                f.write(f'\t       "university name": "{row[1]}",\n')
                f.write(f'\t           "uType": "{row[0]}",\n')
                f.write(f'\t           "items":\n')
                f.write(f'\t           [\n')
                f.write('\t              { \n')
                f.write(f'\t                   "faculty":"{row[2]}",\n')
                f.write(f'\t                   "department":\n')
                f.write(f'\t                   [\n')
                f.write('\t                         { \n')
                f.write(f'\t                               "id":"{row[3]}",\n')
                f.write(f'\t                               "name":"{row[4]}",\n')
                f.write(f'\t                               "lang":"{row[5]}",\n')
                f.write(f'\t                               "second":"{row[6]}",\n')
                f.write(f'\t                               "period":"{row[7]}",\n')
                f.write(f'\t                               "spec":"{row[8]}",\n')
                f.write(f'\t                               "quota":"{row[10]}",\n')
                f.write(f'\t                               "field":"{row[9]}"\n')
                f.write('\t                         } \n')
                f.write(f'\t                   ]\n')
                f.write('\t              } \n')
                if(line_count==105):
                    f.write(f'\t           ]\n')
                else:
                    f.write(f'\t           ],\n')
                line_count += 1
        f.write('   }\n')
        f.write(']\n')
        f.close()

def xmltocsv(argc, argv):
    from xml.etree import ElementTree
    tree = ElementTree.parse(argc)
    root = tree.getroot()

    for att in root:
        first = att.find('attval').text
        for subatt in att.find('children'):
            second = subatt.find('attval').text
            print('{},{}'.format(first, second))

# (1=CSV to XML, 2=XML to CSV, 3=XML to JSON, 4=JSON to XML, 5=CSV to JSON, 6=JSON to CSV,7=XML validates with XSD)

if(sys.argv[3]=='1'):
    csvtoxml(sys.argv[1], sys.argv[2])  # WORKS LIKE THIS -> "python converter.py DEPARTMENTS.csv DEPARTMENTS.xml 1"
elif(sys.argv[3]=='2'):
    xmltocsv(sys.argv[1], sys.argv[2])
elif(sys.argv[3]=='3'):
    print()
elif(sys.argv[3]=='4'):
    print()
elif(sys.argv[3]=='5'):
    csvtojson(sys.argv[1], sys.argv[2])   # WORKS LIKE THIS -> "python converter.py DEPARTMENTS.csv DEPARTMENTS.json 5"
elif(sys.argv[3]=='6'):
    print()
elif(sys.argv[3]=='7'):
    print()
