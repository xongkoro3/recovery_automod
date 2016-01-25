import csv

f = open ('final_data.csv')
csv_f = csv.reader(f)
i=0
a="FINISHED_1.arff"
text_file = open (a,"w")
var1 = 'drug use'
x=0
text_file.write("@relation 'Correlation'\n\n")
for row in csv_f:

    if (i==0):
        for col in row:
            if (col=="Filename"):
                text_file.write("@attribute "+col+" string\n")
            elif(col=="drugs" or col=="recovery" or col=="nothing"):
                text_file.write("@attribute "+col+" {TRUE,FALSE}\n")
            else:
                text_file.write ("@attribute "+col+" numeric\n")
    elif (x==0):
        text_file.write("\n\n@data\n\n")
        x=x+1
    elif (i>0):
        #print(row)
        for col1 in row:
            text_file.write(col1+",")
        text_file.write("\n")

    i=i+1




print (x)
text_file.close()
#f1.close()
f.close()
