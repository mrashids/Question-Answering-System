import tkinter as tk
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer




def click(entry):
    #default questions
    Q1="What is Broadband Internet Service?"
    ANS1="Broadband is internet connectivity at high speed and without having to dial the ISP number. This results in very fast download of information from the internet as soon as you switch on your computer."

    Q2="Is SMUL Broadband Service available on Wi-Fi?"
    ANS2="Yes, SMUL broadband offers Wi-Fi services. SMUL Broadband Wi-Fi service enables multiple and simultaneousbroadband connectivity sessions using multiple devices such as Desktops, Laptops, PSP’s etc in a wire free home environment."


    Q3="How would I know SMUL Broadband Service is available in my city?"
    ANS3="SMUL offers Broadband Service in more than 2000 cities across the Pakistan including Islamabad, Rawalpindi,Lahore, Karachi, Peshawar, Hyderabad, Quetta, Faisalabad, Multan, Gujranwala, Sialkot, and Sheikhupura. New cities are updated regularly. To know Broadband Service is availablein your city? Please call at our help line 1915."

    Q4="How can I order PTCL broadband service connection?"
    ANS4="You can order PTCL Broadband connection by simply calling 1218 or order online by visiting our website at www.SMUL.com or visiting your nearest OSS"

    Q5="Can I change my package?"
    ANS5="Yes you can change your package, just call 1218"

    Q6="How many days it will take to install Broadband services at my premises?"
    ANS6="It takes 5 days for our technical staff to provide the broadband Services at your premises. You can call 1915 for the follow-up of your order in case of delay."

    Q7="Do I have to purchase a modem and pay an activation fee?"
    ANS7=" You will be provided free modem till you use our services. One time Installation charges will be charged. Modem will remain property of SMUL"

    Q8="How will I be billed for PTCL Broadband service?"
    ANS8="Your broadband charges will appear as a separate itemized charge on your monthly telephone bill."

    Q9="How is DSL installed?"
    ANS9="Our DSL installation team will visit your premises / home to evaluate the condition of your landline and then install/connect DSL modem."

    Q10="Can I shift the service to another number or location?"
    ANS10="Yes, you can request for shifting the broadband service to another number or location just by calling SMUL helpline 1915."

    Q11="What if my phone line goes down, will my DSL still work?"
    ANS11="DSL will not work if phone line goes down. DSL service is dependent on the functional connection and quality of copper phone line."

    Q12="What are the installation Internet Setup charges for new internet connection?"
    ANS12="""New Broadband over existing Landline:        Rs. 2,499 inclusive of Tax         

New Double Play (Landline+Broadband):     Rs. 3,999 inclusive of Tax
"""

    Q13="Why is my Internet speed not as fast as it should be?"
    ANS13=" Your intenet speed may varied from the advertised amount as the bandwidth is shared between several users."

    Q14="What are our internet packages and how much do they cost"
    ANS14="please visit www.smul.com/packages for suitable information."

    Q15="why is your internet not working?"
    ANS15="Please check if you have a proper connection wireless or wired with your between your device and the modem. please restart the modem. call our helpline 1915 for further assisstance."

    Q16="Why is my modem / router not working?"
    ANS16="ensure all the connections to your modem including the power switch and connection wire. Please contact our helpline 1915 for further assisstance."

    Q17="How do I reset my Internet modem?"
    ANS17="You can reset the modem by unplugging power cord from the wall or power bar, waiting 30 seconds while it resets, and then plugging it back in. Wait 2-3 more minutes for the modem to reboot, then test your connection. For further assisstance call our helpline 1915"

    Q18="How can I be sure that my Internet modem is functioning properly?"
    ANS18="If you have a laptop or PC, connect your computer to your modem with an Ethernet cable. Open a web browser (eg. Chrome, Firefox, Microsoft Edge) and try to browse to the Internet."

    Q19="How can I check my Internet speed?"
    ANS19="you can visit www.speedtest.com"

    Q20="What is WiFi?"
    ANS20="WiFi is the technology that lets you send Internet data wirelessly between devices. A WiFi connection is recommended for mobile devices like laptops, phones, and tablets."

    Q21="How do I change my WiFi network password?"
    ANS21="please visit www.SMUL.com/wifi for this information or call 1915"

    Q22="why I can’t access some websites"
    ANS22="There is a list of websites blocked by PTA, please see www.pta.gov/internet, if you can't access a website that's not on the list please call our helpline 1915."

    Q23="Does SMUL provide unlimited internet?"
    ANS23="our broadband service provides unlimited download data"

    Q24="Does SMUL provide fiber optics?"
    ANS24="YEs, our whole network is based on fiber optics that provides fast and un interrupted service to our customers."

    Q25="Do I need a telephone line too?"
    ANS25="No SMUL does not require a telephone line."

    FAQs=[Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20, Q21, Q22, Q23, Q24, Q25]
    Answers=[ANS1, ANS2, ANS3, ANS4, ANS5, ANS6, ANS7, ANS8, ANS9, ANS10, ANS11, ANS12, ANS13, ANS14, ANS15, ANS16, ANS17, ANS18, ANS19, ANS20, ANS21, ANS22, ANS23, ANS24, ANS25]

    stopwords=['into','the','is','a','to','in','be','too','of','do',] #words to be omitted

    FAQs1=[]
    for i in FAQs:
        s=[]
        for k in i.split():       
            if k not in stopwords:   
                s.append(k)    
        new_qs=" ".join(s)    
        FAQs1.append(new_qs) #pre-process: new list without stopwords

    cnt_vec=CountVectorizer() 
    cnt_vec.fit(FAQs1)         #learn on default questions

    vector=cnt_vec.transform(FAQs1).toarray()  #transform results on an array

    cs1=cosine_similarity(vector)

    user_ques=entry

    for x in user_ques:
        t=[]
        for y in x.split():
            if y not in stopwords:
                t.append(y)    
        new_qs=" ".join(t)         #pre-process

        
    response=cnt_vec.transform([user_ques])

    vector1=response.toarray()

    answer=cosine_similarity(response, vector) #compare user question with default to find similarities
    ans=answer[0]

    b=np.argmax(ans)

    label['text']= Answers[b]  #returns asnwer


    

root=tk.Tk()    #defines root
canvas=tk.Canvas(root,height=1080,width=1920)
canvas.pack()    #defines the working area

bground_image = tk.PhotoImage(file='landscape.png')  # import bg image from the same folder as the python file
bground_label = tk.Label(root, image=bground_image)
bground_label.place(relwidth=1,relheight=1.2)  #background image

frame=tk.Frame(root,bg='#8de8fd',bd=5)
frame.place(relx=0.55,rely=0.3,relwidth=0.75,relheight=0.1, anchor='n')   # defines the working frame of question

entry=tk.Entry(frame,font=40)
entry.place(relwidth=0.69,relheight=1)  #user input space

button=tk.Button(frame, text="Ask ",font=40,command=lambda: click(entry.get()))
button.place(relx=0.73,relheight=1,relwidth=0.3)
button.bind("<Return>", (lambda event: click(entry.get())))   #Ask utton

answer_frame=tk.Frame(root,bg='#8de8fd',bd=10)
answer_frame.place(relx=0.53,rely=0.45,relwidth=0.75,relheight=0.3, anchor='n')

label=tk.Label(answer_frame,font=40,justify='left',anchor='nw',bd=4,wraplength=800)
label.place( relwidth=1,relheight=1)   #answer space

qs_label=tk.Label(root,font=40,text='Question:',bg='#8de8fd')
qs_label.place(relx=0.085,rely=0.3,relwidth=0.09,relheight=0.1)   

ans_label=tk.Label(root,font=40,text='Answer:',anchor='ne',bg='#8de8fd')
ans_label.place(relx=0.087,rely=0.45,relwidth=0.07,relheight=0.3)

heading="""SMUL INTERNET SERVICE PROVIDER
          CHATBOT"""


#head_label=tk.Label(root,font=("Times", 25, "bold"),text=heading,bg='#7da6c2',anchor='n',justify='center')
#head_label.place(relx=0.1,relwidth=0.8,relheight=0.15)

root.mainloop()  # operation
