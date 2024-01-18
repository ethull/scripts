# convert docx files to pdf

for i in * ; do 
    libreoffice --convert-to pdf $i
    #sleep 60
done
