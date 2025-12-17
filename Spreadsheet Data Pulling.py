import os
import sys
import csv
import pandas as pd
import numpy as np
import processing

folder = (r'E:\\Grassland Mapping files\\Code\\')
text = str('End File')
spreadsheet = "Site Validation Spreadsheet" #Name of spreadsheet being pulled from
alphanumericList = []

#alphanumeric list
x = 1
for x in range(101)[1:]:
    if x < 11:
        let = 'A'
        t = f'{let}{x}'
        alphanumericList.append(t)

    elif x < 21:
        let = 'B'
        t = f'{let}{x-10}'
        alphanumericList.append(t)
        
    elif x < 31:
        let = 'C'
        t = f'{let}{x-20}'
        alphanumericList.append(t)
        
    elif x < 41:
        let = 'D'
        t = f'{let}{x-30}'
        alphanumericList.append(t)
        
    elif x < 51:
        let = 'E'
        t = f'{let}{x-40}'
        alphanumericList.append(t)
        
    elif x < 61:
        let = 'F'
        t = f'{let}{x-50}'
        alphanumericList.append(t)
        
    elif x < 71:
        let = 'G'
        t = f'{let}{x-60}'
        alphanumericList.append(t)
        
    elif x < 81:
        let = 'H'
        t = f'{let}{x-70}'
        alphanumericList.append(t)
        
    elif x < 91:
        let = 'I'
        t = f'{let}{x-80}'
        alphanumericList.append(t)
        
    elif x < 101:
        let = 'J'
        t = f'{let}{x-90}'
        alphanumericList.append(t)
        
print(alphanumericList)


#names
namesList = []
line_count = 0  
with open (r'E://Grassland Mapping files//Code//' +spreadsheet+'.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter =',')

        for row in csv_reader:
            
            if line_count == 3:
                name1 = row[1]
                name1 = name1.replace('Name of site image: ', '')
                name1 = name1.replace('Name of site image:', '')
                namesList.append(name1)
                line_count = line_count + 1
            elif line_count == 14:
                name2 = row[1]
                name2 = name2.replace('Name of site image: ', '')
                name2 = name2.replace('Name of site image:', '')
                namesList.append(name2)
                line_count = line_count + 1
            elif line_count == 25:
                name3 = row[1]
                name3 = name3.replace('Name of site image: ', '')
                name3 = name3.replace('Name of site image:', '')
                namesList.append(name3)
                line_count = line_count + 1
            elif line_count == 36:
                name4 = row[1]
                name4 = name4.replace('Name of site image: ', '')
                name4 = name4.replace('Name of site image:', '')
                namesList.append(name4)
                line_count = line_count + 1
            elif line_count == 47:
                name5 = row[1]
                name5 = name5.replace('Name of site image: ', '')
                name5 = name5.replace('Name of site image:', '')
                namesList.append(name5)
                line_count = line_count + 1
            elif line_count == 58:
                name6 = row[1]
                name6 = name6.replace('Name of site image: ', '')
                name6 = name6.replace('Name of site image:', '')
                namesList.append(name6)
                line_count = line_count + 1
            elif line_count == 69:
                name7 = row[1]
                name7 = name7.replace('Name of site image: ', '')
                name7 = name7.replace('Name of site image:', '')
                namesList.append(name7)
                line_count = line_count + 1
            elif line_count == 80:
                name8 = row[1]
                name8 = name8.replace('Name of site image: ', '')
                name8 = name8.replace('Name of site image:', '')
                namesList.append(name8)
                line_count = line_count + 1
            elif line_count == 91:
                name9 = row[1]
                name9 = name9.replace('Name of site image: ', '')
                name9 = name9.replace('Name of site image:', '')
                namesList.append(name9)
                line_count = line_count + 1
            elif line_count == 102:
                name10 = row[1]
                name10 = name10.replace('Name of site image: ', '')
                name10 = name10.replace('Name of site image:', '')
                namesList.append(name10)
                line_count = line_count + 1
            elif line_count == 113:
                name11 = row[1]
                name11 = name11.replace('Name of site image: ', '')
                name11 = name11.replace('Name of site image:', '')
                namesList.append(name11)
                line_count = line_count + 1
            else:
                line_count = line_count + 1

print(namesList)

def temp1():
    print("Stage 1 start...")
    #opens the spreadhsheet with filled in values
    with open(r'E://Work files//Code//' +spreadsheet+'.csv')as csv_file:
        csv_reader = csv.reader(csv_file, delimiter =',')
        with open (r'D:\\Work files\\Code\\temp.csv', 'w') as output_csv:
            writer = csv.writer(output_csv, delimiter='\t',lineterminator='\n')
    #set the spreadsheed to be gone through line by line
            line = 0  
            for row in csv_reader:        
                if line == 0 or line == 1 or line == 2 or line == 13 or line == 24 or line == 35 or line == 46 or line == 57 or line == 68 or line == 79 or line == 90 or line == 101 or line == 112:
                    line = line + 1

                elif line <124:
                    writer.writerow(row[3])
                    writer.writerow(row[4])
                    writer.writerow(row[5])
                    writer.writerow(row[6])
                    writer.writerow(row[7])
                    writer.writerow(row[8])
                    writer.writerow(row[9])
                    writer.writerow(row[10])
                    writer.writerow(row[11])
                    writer.writerow(row[12])
            
                    line = line + 1

                
                elif line <125:
                    writer.writerow(row[3])
                    writer.writerow(row[4])
                    writer.writerow(row[5])
                    writer.writerow(row[6])
                    writer.writerow(row[7])
                    writer.writerow(row[8])
                    writer.writerow(row[9])
                    writer.writerow(row[10])
                    writer.writerow(row[11])
                    writer.writerow(row[12])
                    writer.writerow([text])
                    
                    #calls the next step in the process
                    print("Stage 1 done")
                    tempfiles()
                    

def tempfiles():
    print("Stage 2 start...")
    with open ('D:\\Work files\\Code\\temp.csv', 'r') as csv_temp:
        csv_reader2 = csv.reader(csv_temp, delimiter = ',')
        print('opened')
        
        line_count = 0
        for row in csv_reader2:
            if line_count == 1100:

                print("File Done!")
                print(row[0])
                
                join()

            elif line_count == 0:
                with open ('D:\\Work files\\Code\\temp0.csv', 'a', newline='') as output_csv:
                    writer = csv.writer(output_csv, delimiter=',',lineterminator='\n',)
                    
                    writer.writerow(('Value', 'newID'))
                    writer.writerow((row[0], alphanumericList[line_count]))
                    line_count = line_count + 1
                
            elif line_count < 100:
                with open ('D:\\Work files\\Code\\temp0.csv', 'a', newline='') as output_csv:
                    writer = csv.writer(output_csv, delimiter=',',lineterminator='\n',)
                    
                    writer.writerow((row[0], alphanumericList[line_count]))
                    line_count = line_count + 1

            elif line_count == 100:
                with open ('D:\\Work files\\Code\\temp1.csv', 'a', newline='') as output_csv:
                    writer = csv.writer(output_csv, delimiter=',',lineterminator='\n',)

                    print("File Done!")
                    writer.writerow(('Value', 'newID'))
                    writer.writerow((row[0], alphanumericList[line_count-100]))
                    line_count = line_count + 1
                        
            elif line_count < 200:
                with open ('D:\\Work files\\Code\\temp1.csv', 'a', newline='') as output_csv:
                    writer = csv.writer(output_csv, delimiter=',',lineterminator='\n',)
                    
                    writer.writerow((row[0], alphanumericList[line_count -100]))
                    line_count = line_count + 1

            elif line_count == 200:
                with open ('D:\\Work files\\Code\\temp2.csv', 'a', newline='') as output_csv:
                    writer = csv.writer(output_csv, delimiter=',',lineterminator='\n',)

                    print("File Done!")
                    writer.writerow(('Value', 'newID'))
                    writer.writerow((row[0], alphanumericList[line_count-200]))
                    line_count = line_count + 1
                    
            elif line_count < 300:
                with open ('D:\\Work files\\Code\\temp2.csv', 'a', newline='') as output_csv:
                    writer = csv.writer(output_csv, delimiter=',',lineterminator='\n',)
                    
                    writer.writerow((row[0], alphanumericList[line_count-200]))
                    line_count = line_count + 1

            elif line_count == 300:
                with open ('D:\\Work files\\Code\\temp3.csv', 'a', newline='') as output_csv:
                    writer = csv.writer(output_csv, delimiter=',',lineterminator='\n',)

                    print("File Done!")
                    writer.writerow(('Value', 'newID'))
                    writer.writerow((row[0], alphanumericList[line_count-300]))
                    line_count = line_count + 1
                    
            elif line_count < 400:
                with open ('D:\\Work files\\Code\\temp3.csv', 'a', newline='') as output_csv:
                    writer = csv.writer(output_csv, delimiter=',',lineterminator='\n',)
                    
                    writer.writerow((row[0], alphanumericList[line_count-300]))
                    line_count = line_count + 1

            elif line_count == 400:
                with open ('D:\\Work files\\Code\\temp4.csv', 'a', newline='') as output_csv:
                    writer = csv.writer(output_csv, delimiter=',',lineterminator='\n',)

                    print("File Done!")
                    writer.writerow(('Value', 'newID'))
                    writer.writerow((row[0], alphanumericList[line_count-400]))
                    line_count = line_count + 1
                    
            elif line_count < 500:
                with open ('D:\\Work files\\Code\\temp4.csv', 'a', newline='') as output_csv:
                    writer2 = csv.writer(output_csv, delimiter=',',lineterminator='\n',)
                    
                    writer2.writerow((row[0], alphanumericList[line_count-400]))
                    line_count = line_count + 1

            elif line_count == 500:
                with open ('D:\\Work files\\Code\\temp5.csv', 'a', newline='') as output_csv:
                    writer = csv.writer(output_csv, delimiter=',',lineterminator='\n',)

                    print("File Done!")
                    writer.writerow(('Value', 'newID'))
                    writer.writerow((row[0], alphanumericList[line_count-500]))
                    line_count = line_count + 1
                    
            elif line_count < 600:
                with open ('D:\\Work files\\Code\\temp5.csv', 'a', newline='') as output_csv:
                    writer = csv.writer(output_csv, delimiter=',',lineterminator='\n',)
                    
                    writer.writerow((row[0], alphanumericList[line_count-500])) 
                    line_count = line_count + 1

            elif line_count == 600:
                with open ('D:\\Work files\\Code\\temp6.csv', 'a', newline='') as output_csv:
                    writer = csv.writer(output_csv, delimiter=',',lineterminator='\n',)

                    print("File Done!")
                    writer.writerow(('Value', 'newID'))
                    writer.writerow((row[0], alphanumericList[line_count-600]))
                    line_count = line_count + 1
            
            elif line_count < 700:
                with open ('D:\\Work files\\Code\\temp6.csv', 'a', newline='') as output_csv:
                    writer = csv.writer(output_csv, delimiter=',',lineterminator='\n',)
                    
                    writer.writerow((row[0], alphanumericList[line_count-600]))
                    line_count = line_count + 1

            elif line_count == 700:
                with open ('D:\\Work files\\Code\\temp7.csv', 'a', newline='') as output_csv:
                    writer = csv.writer(output_csv, delimiter=',',lineterminator='\n',)

                    print("File Done!")
                    writer.writerow(('Value', 'newID'))
                    writer.writerow((row[0], alphanumericList[line_count-700]))
                    line_count = line_count + 1
                    
            elif line_count < 800:
                with open ('D:\\Work files\\Code\\temp7.csv', 'a', newline='') as output_csv:
                    writer = csv.writer(output_csv, delimiter=',',lineterminator='\n',)
                    
                    writer.writerow((row[0], alphanumericList[line_count-700]))
                    line_count = line_count + 1

            elif line_count == 800:
                with open ('D:\\Work files\\Code\\temp8.csv', 'a', newline='') as output_csv:
                    writer = csv.writer(output_csv, delimiter=',',lineterminator='\n',)

                    print("File Done!")
                    writer.writerow(('Value', 'newID'))
                    writer.writerow((row[0], alphanumericList[line_count-800]))
                    line_count = line_count + 1
                    
            elif line_count < 900:
                with open ('D:\\Work files\\Code\\temp8.csv', 'a', newline='') as output_csv:
                    writer = csv.writer(output_csv, delimiter=',',lineterminator='\n',)
                    
                    writer.writerow((row[0], alphanumericList[line_count-800]))
                    line_count = line_count + 1

            elif line_count == 900:
                with open ('D:\\Work files\\Code\\temp9.csv', 'a', newline='') as output_csv:
                    writer = csv.writer(output_csv, delimiter=',',lineterminator='\n',)

                    print("File Done!")
                    writer.writerow(('Value', 'newID'))
                    writer.writerow((row[0], alphanumericList[line_count-900]))
                    line_count = line_count + 1
                    
            elif line_count < 1000:
                with open ('D:\\Work files\\Code\\temp9.csv', 'a', newline='') as output_csv:
                    writer = csv.writer(output_csv, delimiter=',',lineterminator='\n',)
                    
                    writer.writerow((row[0], alphanumericList[line_count-900]))
                    line_count = line_count + 1

            elif line_count == 1000:
                with open ('D:\\Work files\\Code\\temp10.csv', 'a', newline='') as output_csv:
                    writer = csv.writer(output_csv, delimiter=',',lineterminator='\n',)

                    print("File Done!")
                    writer.writerow(('Value', 'newID'))
                    writer.writerow((row[0], alphanumericList[line_count-1000]))
                    line_count = line_count + 1
                    
            elif line_count < 1100:
                with open ('D:\\Work files\\Code\\temp10.csv', 'a', newline='') as output_csv:
                    writer = csv.writer(output_csv, delimiter=',',lineterminator='\n',)
                    
                    writer.writerow((row[0], alphanumericList[line_count-1000]))
                    line_count = line_count + 1

def join():
    
    i = 0
    for i in range (11):
        print('temp'+str(i)+'.csv, ' + namesList[i])
        processing.run("native:joinattributestable", {'INPUT':'E:\\Grassland Mapping files\\Code\\FILES WITH GRID\\'+namesList[i]+'.geojson','FIELD':'newID','INPUT_2':'D:/Work files/Code/temp'+str(i)+'.csv','FIELD_2':'newID','FIELDS_TO_COPY':['Value'],'METHOD':1,'DISCARD_NONMATCHING':False,'PREFIX':'','OUTPUT':'E:\\Grassland Mapping files\\Code\\FINISHED IMPORTANT FILES (joined)\\Joined '+namesList[i]+'.geojson'})
    
    finished()
    
def finished():
    print("done")
    
temp1()
