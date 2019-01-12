import glob
import pydicom
file_list = glob.glob(r'C:\Users\Nachiketh Atawale\Downloads\*.dcm')
for files in file_list:
    print ("DICOM File", files) # For indicating the file being processed. 
    Patient = pydicom.dcmread(files)
    with open(r"C:\Users\Nachiketh Atawale\Downloads\Output.txt", 'a') as output: 
        print ("DICOM File : ",files,"\n\n\t","Tags present in the file : \n\n\t\t",Patient.dir(),"\n\n\t","Patient Information :","\n\n", Patient,"\n\n\n", file = output)
        print ("\n")
output.close()      
