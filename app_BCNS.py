import pandas as pd
import numpy as np
import pickle
import streamlit as st

  
# loading in the model to predict on the data
pickle_in = open('model.pkl',  'rb')
model = pickle.load(pickle_in)
  
def welcome():
    return 'welcome all'
  
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(age,cs_v,RX_s,year,icd_b,cs_ex,first_malignant,gde,cs_c,primary_s,ss,lt):  
   
    
    #ann_pred=model.predict([[age,cs_v,RX_s,year,icd_b,cs_ex,first_malignant,gde,cs_c,primary_s,ss,lt]])
    ann_pred=model.predict_proba([[age,cs_v,RX_s,year,icd_b,cs_ex,first_malignant,gde,cs_c,primary_s,ss,lt]])

    pred=round(ann_pred[0,1]*100,2)
 

    
#    if pred == 0:
#	    value = r'Dead'
 #   elif pred == 1:
 #       value = r'Survive'
   
   
    
    

    return pred
      
  
def main():
      # giving the webpage a title
    #st.title("Iris Flower Prediction")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed

    html_temp = """
    <div style ="background-color:turquoise;padding:9px">
    <h1 style ="color:black;text-align:center;">BCNS TOOL-Utah Tech</h1>
    </div>
    """

    # this line allows us to display the front end aspects we have 

    st.markdown(html_temp, unsafe_allow_html = True)
    st.subheader("")       
     
if __name__=='__main__':
    main()
    
col1,col2 = st.columns(2)

    
    
with col1:
     age = st.slider("Age", 1, 100)
     
     
     cs_version = st.selectbox("CS-original",options=['010401','020550', '020440', '010200',  '010300', '020302', '020200', '010100', '010400', '010002'   ])
     result =""
     
       
     cs_v=0
     
     if cs_version == '010401':
	     cs_v = 10401
     elif cs_version == '020550':
	     cs_v = 20550
     elif cs_version == '020440':
	     cs_v = 20440
     elif cs_version == '010200':
	     cs_v = 10200
     elif cs_version == '010300':
 	    cs_v = 10300
     elif cs_version == '020302':
	     cs_v = 20302
     elif cs_version == '020200':
	     cs_v = 20200
     elif cs_version == '010100':
	     cs_v = 10100
     elif cs_version == '010400':
	     cs_v = 10400
    
     elif cs_version == '010002':
	     cs_v = 10002
         
         
         


     RX_Surg = st.selectbox("RX Summ-Surg Prim Site",options=['0','55', '20', '40',  '30', '21', '90', '99', '22', '10'   ])
     result =""
     
       
     RX_s=0
     
     if RX_Surg == '0':
	     RX_s = 0
     elif RX_Surg == '55':
	     RX_s = 55
     elif RX_Surg == '20':
	     RX_s = 20
     elif RX_Surg == '40':
	     RX_s = 40
     elif RX_Surg == '30':
 	    RX_s = 30
     elif RX_Surg == '21':
	     RX_s = 21
     elif RX_Surg == '90':
	     RX_s = 90
     elif RX_Surg == '99':
	     RX_s = 99
     elif RX_Surg == '22':
	     RX_s = 22
    
     elif RX_Surg == '10':
	     RX_s = 10


           
         
     year=st.number_input('Year of diagnosis',step=1.,format="%.0f")    

            
         
     ICD_behav = st.selectbox("ICD-O-3 Hist/behav",options=['Glioblastoma NOS','Astrocytoma anaplastic', 'Glioma malignant', 'Astrocytoma NOS',  'Neoplasm malignant', 'Oligodendroglioma NOS', 'Pilocytic astrocytoma',  'Mixed glioma', 'Ependymoma NOS', ' Oligodendroglioma anaplastic'])
     result =""
     
       
     icd_b=0
     
     if cs_version == 'Glioblastoma NOS':
	     icd_b = 74
     elif cs_version == 'Astrocytoma anaplastic':
	     icd_b = 67
     elif cs_version == 'Glioma malignant':
	     icd_b = 56
     elif cs_version == 'Astrocytoma NOS':
	     icd_b = 66
     elif cs_version == 'Neoplasm malignant':
 	    icd_b = 0
     elif cs_version == 'Pilocytic astrocytoma':
	     icd_b = 77
     elif cs_version == 'Mixed glioma':
	     icd_b = 71
     elif cs_version == 'Ependymoma NOS':
	     icd_b = 58
     elif cs_version == 'Mixed glioma':
	     icd_b = 62
    
     elif cs_version == 'Oligodendroglioma anaplastic':
	     icd_b = 78

     
         
     cs_ex=st.number_input('CS extension',step=1.,format="%.0f")    

     
    
   
     
 
with col2: 
     first_malignant= st.selectbox("First malignant primary indicator",options=['Yes' , 'No'])
     first_malignant = 0 if first_malignant == 'No' else 1
     
         
     grade = st.selectbox("Grade",options=['I','II', 'III', 'IV'])
     result =""
     
       
     gde=0
     
     if grade == 'I':
	     gde = 1
     elif grade == 'II':
	     gde = 2
     elif grade == 'III':
	     gde = 3
     elif grade == 'IV':
	     gde = 4
     

     cs_current = st.selectbox("CS-current",options=['020510','020550', '020540', '020520', '020530'])
     result =""
     
       
     cs_c=0
     
     if cs_current == '020510':
	     cs_c = 20510
     elif cs_current == '020550':
	     cs_c = 20550
     elif cs_current == '020540':
	     cs_c = 20540
     elif cs_current == '020520':
	     cs_c = 20520
     elif cs_current == '020530':
 	    cs_c = 20530
       

     
         
     primary_s=st.number_input('Primary site',step=1.,format="%.0f")    


     ss_seq = st.selectbox("SS seq",options=['1','2', '3'])
     result =""
     
       
     ss=0
     
     if ss_seq == '1':
	     ss = 1
     elif ss_seq == '2':
	     ss = 2
     elif ss_seq == '3':
	     ss = 3
   
     Laterity = st.selectbox("Laterality",options=['Right-origin of primary','Left-origin of primary', 'Not a paired  site', 'Bilateral', 'Paired site', 'Only one side','midline tumor' ])
     result =""
     
       
     lt=0
     
     if Laterity == 'Right-origin of primary':
	     lt = 6
     elif Laterity == 'Left-origin of primary':
	     lt = 1
     elif Laterity == 'Not a paired  site':
	     lt = 2
     elif Laterity == 'Bilateral':
	     lt = 0
     elif Laterity == 'Paired site':
 	    lt = 4
     elif Laterity == 'Only one side':
        lt= 3
        
     elif Laterity == 'midline tumor':
 	    lt = 5
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
     if st.button("Predict"):
        result = prediction(age,cs_v,RX_s,year,icd_b,cs_ex,first_malignant,gde,cs_c,primary_s,ss,lt)
     st.success('The 10-year survival probability is  --- {} %'.format(result))
st.write('_NB: This prototype (developed based on a limited number of observations) is intended only for demonstration of the proposed tool and not as a replacement for professional medical counseling, diagnosis, or treatment. The authors and the institution do not guarantee the outcome of this prototype for any particular patient._')
