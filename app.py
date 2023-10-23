import numpy as np
import urllib.request
import re

from collections.abc import Mapping

from flask import Flask, request, jsonify, render_template, send_file, send_from_directory, session

app = Flask(__name__)

app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'


def listToString(s):
 
    str1 = "" 
    for ele in s:
        str1 += ele
    return str1


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [str(x) for x in request.form.values()]


    name = list(int_features[0].replace(" ", "_"))                    # name =  "Samarth_Sudhirkumar_Bhalerao_"
    rollno = int_features[1].replace(" ", "_")                        # rollno = "B21EE060_"
    # rollno[0].upper()
    rollno = rollno.upper()
    if rollno[-1] != "_":
        rollno += "_"
    name[0] = name[0].upper()
    k=0;    
    for i in range(len(name)):
        if k==1:
            name[i] = name[i].upper()
            k=0
        if name[i] == "_":
            k=1
    if k==0:
        name += '_'

    # return render_template('index.html', prediction_text=str(listToString(name) + '  --  ' + rollno ))
    print(listToString(name) ,"  ", rollno[0:8], rollno)

    # https://oa.iitj.ac.in/All_Attachments_Upload/ACADEMIC_REGISTRATION/B21EE001/B21EE001_Photo.jpg

    s = "https://oa.iitj.ac.in/All_Attachments_Upload/ACADEMIC_REGISTRATION/"
    s += rollno[0:8] + "/" + rollno          # till now# https://oa.iitj.ac.in/All_Attachments_Upload/ACADEMIC_REGISTRATION/B21EE001/B21EE001_



    # not important 
    # https://oa.iitj.ac.in/All_Attachments_Upload/ACADEMIC_REGISTRATION/B21EE035/B21EE035_ProofofAdvanceFee.pdf
    # https://oa.iitj.ac.in/All_Attachments_Upload/ACADEMIC_REGISTRATION/B21EE035/B21EE035_CovidVaccination.pdf
    # https://oa.iitj.ac.in/All_Attachments_Upload/ACADEMIC_REGISTRATION/B21EE035/B21EE035_MedicalCertificate.pdf

    try:
        # https://oa.iitj.ac.in/All_Attachments_Upload/ACADEMIC_REGISTRATION/B21EE035/B21EE035_Photo.jpg
        end = "Photo.jpg"
        urllib.request.urlretrieve(s+end, "uploads/" + rollno +"_" + end)
    except:
        pass

    try:
        # https://oa.iitj.ac.in/All_Attachments_Upload/ACADEMIC_REGISTRATION/B21EE035/B21EE035_Signature.jpg
        end = "Signature.jpg"
        urllib.request.urlretrieve(s+end, "uploads/" + rollno +"_" + end)
    except:
        pass

    try:
        # https://oa.iitj.ac.in/All_Attachments_Upload/ACADEMIC_REGISTRATION/B21EE035/B21EE035_Aadhaar.pdf
        end = "Aadhaar.pdf"
        urllib.request.urlretrieve(s+end, "uploads/" + rollno +"_" + end)
    except:
        pass

    try:
        # https://oa.iitj.ac.in/All_Attachments_Upload/ACADEMIC_REGISTRATION/B21EE035/B21EE035_IncomeCertificate.pdf
        end = "IncomeCertificate.pdf"
        urllib.request.urlretrieve(s+end, "uploads/" + rollno +"_" + end)
    except:
        pass

    try:
        # https://oa.iitj.ac.in/All_Attachments_Upload/ACADEMIC_REGISTRATION/B21EE035/B21EE035_Fellowship.pdf
        end = "Fellowship.pdf"
        urllib.request.urlretrieve(s+end, "uploads/" + rollno +"_" + end)
    except:
        pass

    try:
        # https://oa.iitj.ac.in/All_Attachments_Upload/ACADEMIC_REGISTRATION/B21EE035/B21EE035_OfferLetter.pdf
        end = "OfferLetter.pdf"
        urllib.request.urlretrieve(s+end, "uploads/" + rollno +"_" + end)
    except:
        pass

    try:
        # https://oa.iitj.ac.in/All_Attachments_Upload/ACADEMIC_REGISTRATION/B21EE035/B21EE035_DOBCertificate.pdf
        end = "DOBCertificate.pdf"
        urllib.request.urlretrieve(s+end, "uploads/" + rollno +"_" + end)
    except:
        pass

    try:
        # https://oa.iitj.ac.in/All_Attachments_Upload/ACADEMIC_REGISTRATION/B21EE035/B21EE035_CharacterCertificate.pdf
        end = "CharacterCertificate.pdf"
        urllib.request.urlretrieve(s+end, "uploads/" + rollno +"_" + end)
    except:
        pass


    print(s, "  ", rollno)
    session["n"]=name
    session["r"]=rollno

    return render_template('test1.html')


@app.route('/download_file')      #faltu, just to understand
def download_file():     
    pat = "uploads/" + "block_diag" + ".pdf"
    return send_file(pat)
    # return send_file(pat, as_attachment=True)
    # return send_from_directory(app.config['UPLOAD_FOLDER'], 'file.pdf')


@app.route('/downloadss/<filename>')
def downloadss(filename):     
    try:
        pat = "uploads\\" + session.get("r",None) + "_" + filename
        return send_file(pat)
    except:
        pat = "uploads\\iitj.png"
        return send_file(pat)



if __name__ == "__main__":
    app.run(host='localhost',port=80)
