

import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import numpy as np
import pandas as pd
import seaborn as sns
import re 



############ WCZYTANIE DANYCH O CZUJNIKACH ######################################################


xxx = pd.read_csv("https://raw.githubusercontent.com/RusieckiFilip/PracaInz/main/VMPA.csv", sep = ";")

for i in xxx["SN"]:
    if type(i)==int:
        i = str(i)
        
####### FUNKCJA WCZYTANIA DANYCH ###############################################################################

def wczytanie_danych(nazwa_pliku, nazwa_folderu, kanal=0):
    data = pd.read_csv("https://raw.githubusercontent.com/RusieckiFilip/PracaInz/main/"+
                       nazwa_folderu+"/H2-pow_fi1/"+nazwa_pliku, sep = ";")

    
    #### USUWANIE SZUMU ######
    if kanal != 0:
        i=0
        for j in data[kanal]:
            if data[kanal][i] > 0.45:
                data[kanal] = data[kanal].drop(labels=list(range(i,31999)), axis=0)    
                break
            i+=1
        for i in data:
            j=0
            for k in data[i]:
                if i != "time [us]" and j < 2000:
                    data[i][j]=0
                else: break
                j+=1
    return data


############# WCZYTANIE DANYCH ##########################################################################################################################


# data1 = wczytanie_danych("Exp_01.csv","testy_H2-pow_fi1_new_setup")
# text1 = wczytanie_danych("Exp_01_t.csv","testy_H2-pow_fi1_new_setup")

# data2 = wczytanie_danych("Exp_02.csv","testy_H2-pow_fi1_new_setup")
# text2 = wczytanie_danych("Exp_02_t.csv","testy_H2-pow_fi1_new_setup")

# data3 = wczytanie_danych("Exp_03.csv","testy_H2-pow_fi1_new_setup")
# text3 = wczytanie_danych("Exp_03_t.csv","testy_H2-pow_fi1_new_setup")

# data4 = wczytanie_danych("Exp_04.csv","testy_H2-pow_fi1_new_setup")
# text4 = wczytanie_danych("Exp_04_t.csv","testy_H2-pow_fi1_new_setup")

# data5 = wczytanie_danych("Exp_05.csv","testy_H2-pow_fi1_new_setup")
# text5 = wczytanie_danych("Exp_05_t.csv","testy_H2-pow_fi1_new_setup")

# data6 = wczytanie_danych("Exp_01.csv","testy_H2-pow_fi16_new_setup_16152021")
# text6 = wczytanie_danych("Exp_01_t.csv","testy_H2-pow_fi16_new_setup_16152021")

# data7 = wczytanie_danych("Exp_02.csv","testy_H2-pow_fi16_new_setup_16152021")
# text7 = wczytanie_danych("Exp_02_t.csv","testy_H2-pow_fi16_new_setup_16152021")

# data8 = wczytanie_danych("Exp_03.csv","testy_H2-pow_fi16_new_setup_16152021")
# text8 = wczytanie_danych("Exp_03_t.csv","testy_H2-pow_fi16_new_setup_16152021")

# data9 = wczytanie_danych("Exp_04.csv","testy_H2-pow_fi16_new_setup_16152021")
# text9 = wczytanie_danych("Exp_04_t.csv","testy_H2-pow_fi16_new_setup_16152021")

# data10 = wczytanie_danych("Exp_05.csv","testy_H2-pow_fi16_new_setup_16152021")
# text10 = wczytanie_danych("Exp_05_t.csv","testy_H2-pow_fi16_new_setup_16152021")

# data11 = wczytanie_danych("Exp_06.csv","testy_H2-pow_fi16_new_setup_16152021")
# text11 = wczytanie_danych("Exp_06_t.csv","testy_H2-pow_fi16_new_setup_16152021")

# data12 = wczytanie_danych("Exp_07.csv","fi16_styczen_newsetup")
# text12 = wczytanie_danych("Exp_07_t.csv","fi16_styczen_newsetup")

# data13 = wczytanie_danych("Exp_08.csv","fi16_styczen_newsetup")
# text13 = wczytanie_danych("Exp_08_t.csv","fi16_styczen_newsetup")

# data14 = wczytanie_danych("Exp_09.csv","fi16_styczen_newsetup")
# text14 = wczytanie_danych("Exp_09_t.csv","fi16_styczen_newsetup")

# data15 = wczytanie_danych("Exp_010.csv","fi16_styczen_newsetup")
# text15 = wczytanie_danych("Exp_010_t.csv","fi16_styczen_newsetup")

# data16 = wczytanie_danych("Exp_011.csv","fi16_styczen_newsetup")
# text16 = wczytanie_danych("Exp_011_t.csv","fi16_styczen_newsetup")

# data17 = wczytanie_danych("Exp_012.csv","fi16_styczen_newsetup")
# text17 = wczytanie_danych("Exp_012_t.csv","fi16_styczen_newsetup") 

data18 = wczytanie_danych("Exp_01.csv","testy_H2-pow_fi128_new_setup_11012022")
text18 = wczytanie_danych("Exp_01_t.csv","testy_H2-pow_fi128_new_setup_11012022")

data19 = wczytanie_danych("Exp_02.csv","testy_H2-pow_fi128_new_setup_11012022")
text19 = wczytanie_danych("Exp_02_t.csv","testy_H2-pow_fi128_new_setup_11012022")

data20 = wczytanie_danych("Exp_03.csv","testy_H2-pow_fi128_new_setup_11012022")
text20 = wczytanie_danych("Exp_03_t.csv","testy_H2-pow_fi128_new_setup_11012022")

data21 = wczytanie_danych("Exp_04.csv","testy_H2-pow_fi128_new_setup_11012022")
text21 = wczytanie_danych("Exp_04_t.csv","testy_H2-pow_fi128_new_setup_11012022")

data22 = wczytanie_danych("Exp_05.csv","testy_H2-pow_fi128_new_setup_11012022")
text22 = wczytanie_danych("Exp_05_t.csv","testy_H2-pow_fi128_new_setup_11012022")

data23 = wczytanie_danych("Exp_06.csv","testy_H2-pow_fi128_new_setup_11012022")
text23 = wczytanie_danych("Exp_06_t.csv","testy_H2-pow_fi128_new_setup_11012022")


############ FUNKCJA TWORZACA WYKRESY ######################################################

####### Funkcja(dane z czujnikow, opis, numer exp, trigger dla SN, trigger dla SN powrotna fala, 
####### trigger dla SJ, trig dla 2 pierwszych SN, czas po ktorym mierzymy trigger powrotnej fali,
####### max dopusz predkosc fizyczna, V_CJ,aP, czas data, usrednianie predkosci) 

def funkcja(data1,text1,numer,tr_SN, tr_SN_f2, tr_SJ, tr_SN2, czas_zbior, V_max, V_CJ, aP, t_d, usrednianie = "nie"):
    
    ######## TWORZENIE KOPII #########
    data = data1[:]

    
    
    
    list1=[]
    for i in text1["Tabela"]:
        l=0
        for j in xxx["SN"]:
            if j in i:
                print("Czujnik: ", j)
                list1.append(xxx["VMPA"][l])
            l+=1
   
    ############## Pobieranie wspolrzednych i opisow ######################################
    pattern = "\](.*?)\["
    list2=[]
    print("\n")
    l=0
    
    # Zczytanie pozycji z czujnika
    for i in text1["Tabela"]:
        if  i != "time [us]":
            if "POS" in i:
                substring = re.search(pattern, i).group(1)
                list2.append(float(substring))
    
    # Zczytanie opisu eksperymentu
    for i in text1["Tabela"]:
        if  i != "time [us]":
            if "[EXP_DESC_s]" in i:
                opis = i
                break
            
    for i in text1["Tabela"]:
        if  i != "time [us]":
            if "/EXP_DESC_s" in i:
                opis = opis + " " + i
                break
    opis = re.search(pattern, opis).group(1)
        
    ############ TWORZENIE DATAFRAME Z DANYMI CZUJNIKOW ####################################
    d = {'Kanal': range(1,6), 'VPMA': list1, "Odleglosc": list2[:5]}
    df1 = pd.DataFrame(data=d)
    
    l=-1
    
    ########## PRZELICZENIE NA MPa CZUJNIKOW ###########
    for i in data1:
        if  i != "time [us]" and l < 5:
            data1[i] = data1[i]/df1["VPMA"][l]+0.1
        l+=1
    #####################################################
    

    
    ########################## WYKRES ODCZYTÓW CZUJNIKÓW #################################
        
        
    fig1 = plt.figure("data" + numer,figsize=(16, 9), dpi=150)
    plt.clf()
    
    fig1.suptitle(opis, fontsize=20)
    
    ax1=plt.subplot(211)
    plt.style.use('seaborn-deep')
    plt.xlabel("Czas [us]", fontsize=15)
    plt.ylabel("P [MPa]", fontsize=15)
    plt.grid(color='#717171', linestyle='--', linewidth=0.3)
    #
    plt.xlim(2000,t_d)
    #color = cm.rainbow(np.linspace(0, 1, 8))
    for i in range(1,6):
        plt.plot(data1["time [us]"],data1["ch "+ str(i)], linewidth=1.5, label =  "ch"+ str(i) + " SN")
    plt.legend(loc="upper left")
    plt.tick_params(axis='both', labelsize=14)
        
    ax1=plt.subplot(212)
    plt.style.use('seaborn-deep')
    plt.xlabel("Czas [us]", fontsize=15)
    plt.ylabel("U [V]", fontsize=15)
    plt.grid(color='#717171', linestyle='--', linewidth=0.3)
    plt.ylim(0,1)
    plt.xlim(2000,t_d)
    for i in range(1,11):
        if i > 5:
            plt.plot(data1["time [us]"],data1["ch "+ str(i)], linewidth=1.5, label =  "ch"+ str(i) + " SJ" )
    plt.legend(loc="upper left")
    plt.tick_params(axis='both', labelsize=14)
    
    plt.tight_layout()
    

    
        ################ WYKRES ZBIORCZY ####################
    
    fig4 = plt.figure("Zbiorczy" + numer,figsize=(16, 9), dpi=150)
    plt.clf()
    
    fig4.suptitle(opis, fontsize=20)
    zbiorczy = plt.subplot(111)
    
    plt.style.use('seaborn-deep')
    plt.xlabel("Czas [us]", fontsize=15)
    plt.ylabel("P[MPa] + x[m]", fontsize=15)
    plt.grid(color='#717171', linestyle='--', linewidth=0.3)
    #plt.ylim(0,2.5)
    plt.xlim(2000,t_d)
    color = cm.rainbow(np.linspace(0, 1, 5))
    for i, c in zip(range(1,6),color):
        plt.plot(data1["time [us]"],data1["ch "+ str(i)] + df1["Odleglosc"][i-1], 
                 linewidth=1, label = "ch"+ str(i) + " SN, " + str(df1["Odleglosc"][i-1])+" m", c=c)
    plt.legend(loc="upper left",  fontsize=13)
    plt.tick_params(axis='both', labelsize=14)
    plt.tight_layout()
    
    
    
    ################### USTALENIE KIEDY DOTARL PLOMIEN I FALA DO CZUJNIKOW  ###################
    
    list3=[]
    list4=[]
    l=-1
    
    for i in data1:
        if  i != "time [us]" and l <= 5  and  i != "ch 6":
            k=-1
            for j in data1[i]:
                k+=1
                if data1[i][k] > tr_SN:
                    list3.append(data1["time [us]"][k]/1000)
                    break
        elif i != "time [us]":
            k=-1
            for j in data1[i]:
                k+=1
                if data1[i][k] > tr_SJ:
                    list4.append(data1["time [us]"][k]/1000)
                    break
        l+=1
    print("List 3:", list3)
    print("List 4:", list4)
    #list4[1]=list4[2]*list2[1]/list2[2]
    df1["TOA_P [ms]"]=list3
    df1["TOA_V [ms]"]=list4
    
    ######################### WYKRES TOA ####################################################
    
    fig2 = plt.figure("TOA" + str(numer),figsize=(16, 9), dpi=150)
    plt.clf()
    
    fig2.suptitle('ToA\n' + opis, fontsize=17)
    
    plt.style.use('seaborn-deep')
    plt.xlabel("Dystans [m]", fontsize=15)
    plt.ylabel("Czas [ms]", fontsize=15)
    plt.grid(color='#717171', linestyle='--', linewidth=0.3)
    plt.xlim(0,2)
    
    
    plt.plot([0,df1["Odleglosc"][0]],[0,df1["TOA_P [ms]"][0]], linestyle='--', color="g")
    plt.plot([0,df1["Odleglosc"][0]],[0,df1["TOA_V [ms]"][0]], linestyle='--', color="b")
    
    
    plt.plot(df1["Odleglosc"],df1["TOA_P [ms]"], color="g", label="Fala cisnieniowa",marker="o")
    plt.plot(df1["Odleglosc"],df1["TOA_V [ms]"], color="b", label="Front plomienia",marker="o")
    plt.legend(loc="upper left",  fontsize=15)
    plt.tick_params(axis='both', labelsize=14)
    plt.tight_layout()
    
    
    ################ SREDNIA ODLEGLOSC POMIEDZY CZUJNIKAMI #########################
    
    list5=[0]
    l=1
    for i in df1["Odleglosc"]:
        if l<5:
            list5.append((df1["Odleglosc"][l]+df1["Odleglosc"][l-1])/2)
        l+=1
    df1["Srednia odleglosc"]=list5
    
    
    ################### PREDKOSC FALI CISNIENIOWEJ ###########################
    
    list6=[0]
    l=1
    print("Eksperyment: "+numer)
    for i in df1["TOA_P [ms]"]:
        if l<5:
            if (df1["Odleglosc"][l]-df1["Odleglosc"][l-1])/(df1["TOA_P [ms]"][l]-df1["TOA_P [ms]"][l-1])>100:
                list6.append(0)
            else: 
                list6.append((df1["Odleglosc"][l]-df1["Odleglosc"][l-1])*1000/(df1["TOA_P [ms]"][l]-df1["TOA_P [ms]"][l-1]))
                print("Odleglosc "+str(l+1)+" i", str(l),":", df1["Odleglosc"][l],",", df1["Odleglosc"][l-1], ";TOAP1-2:",
                      round(abs(df1["TOA_P [ms]"][l]-df1["TOA_P [ms]"][l-1]),3), ", droga: ", round((df1["Odleglosc"][l]-df1["Odleglosc"][l-1]), 3))
            l+=1 
    df1["Predkosc P"]=list6
    
    
    
    ############# PREDKOSC PLOMIENIA #############################
    list7=[0]
    l=1
    for i in df1["TOA_V [ms]"]:
        if l<5:
            if (df1["Odleglosc"][l]-df1["Odleglosc"][l-1])/(df1["TOA_V [ms]"][l]-df1["TOA_V [ms]"][l-1])>100:
                list7.append(0)
            else: 
                list7.append((df1["Odleglosc"][l]-df1["Odleglosc"][l-1])*1000/(df1["TOA_V [ms]"][l]-df1["TOA_V [ms]"][l-1]))
                print("Odleglosc "+str(l+1)+" i", str(l),":",df1["Odleglosc"][l],",",df1["Odleglosc"][l-1], ",TOAV1-2:",
                      round(abs(df1["TOA_V [ms]"][l]-df1["TOA_V [ms]"][l-1]),3), ", droga: ", round((df1["Odleglosc"][l]-df1["Odleglosc"][l-1]), 3))
            l+=1
    df1["Predkosc V"]=list7
    
    if usrednianie == "tak":
        ########## USREDNIANIE ZA DUZYCH WARTOSCI PREDKOSCI ########################
        ########## Error gdy pierwsza lub ostatnia wartosc predkosci wieksza od 1950 lub ujemna
        j=-1
        for p,v in zip(list6,list7):
            j+=1
            if abs(p) > 2400:
                list6[j]=1000
            if abs(v) > 2400:
                list7[j]=1000
            if j < 4 and (abs(p) > V_max or (list6[j-1]>0 and list6[j+1]>0 and p < 0) 
                          or (p > 2*(list6[j-1]+list6[j+1])/2 and list6[j-1]>0 and list6[j+1] > 0)  
                          or (p > 2*(abs(list6[j-1])+abs(list6[j+1]))/2) ):
                
                if (list6[j-1]<0 and list6[j+1]<0 and p < 0): list6[j] = ((list6[j-1])+(list6[j+1]))/2
                else: list6[j] = (abs(list6[j-1])+abs(list6[j+1]))/2 
            elif j < 4 and (abs(v) > V_max or (list7[j-1]>0 and list7[j+1]>0 and v < 0) 
                            or (v > 2*(list7[j-1]+list7[j+1])/2 and list7[j-1]>0 and list7[j+1] > 0)  
                            or (v > 2*(abs(list7[j-1])+abs(list7[j+1]))/2) ):
                
                if (list7[j-1]<0 and list7[j+1]<0 and v < 0): list7[j] = ((list7[j-1])+(list7[j+1]))/2 
                else: list7[j] = list7[j] = (abs(list7[j-1])+abs(list7[j+1]))/2
           
            #################
        
            else: ########### USUWAM UJEMNE WARTOSCI ALE CZY POPRAWNIE  ???????   ###########
                list6[j]=abs(list6[j])
                list7[j]=abs(list7[j])
              
                ################
        j=-1
        for p,v in zip(list6,list7):
            j+=1
            if abs(p) > 2400:
                list6[j]=1000
            if abs(v) > 2400:
                list7[j]=1000
            if j < 4 and (abs(p) > V_max or (list6[j-1]>0 and list6[j+1]>0 and p < 0) 
                          or (p > 2*(list6[j-1]+list6[j+1])/2 and list6[j-1]>0 and list6[j+1] > 0)  
                          or (p > 2*(abs(list6[j-1])+abs(list6[j+1]))/2) ):
                
                if (list6[j-1]<0 and list6[j+1]<0 and p < 0): list6[j] = ((list6[j-1])+(list6[j+1]))/2
                else: list6[j] = (abs(list6[j-1])+abs(list6[j+1]))/2 
            elif j < 4 and (abs(v) > V_max or (list7[j-1]>0 and list7[j+1]>0 and v < 0) 
                            or (v > 2*(list7[j-1]+list7[j+1])/2 and list7[j-1]>0 and list7[j+1] > 0)  
                            or (v > 2*(abs(list7[j-1])+abs(list7[j+1]))/2) ):
                
                if (list7[j-1]<0 and list7[j+1]<0 and v < 0): list7[j] = ((list7[j-1])+(list7[j+1]))/2 
                else: list7[j] = list7[j] = (abs(list7[j-1])+abs(list7[j+1]))/2
           
            #################
        
            ########### USUWAM UJEMNE WARTOSCI ALE CZY POPRAWNIE  ???????   ###########
            list6[j]=abs(list6[j])
            list7[j]=abs(list7[j])
                
                ################
    
    list7 =  [abs(i) for i in list7]
    
    
    fig3 = plt.figure("V" + numer,figsize=(16, 9), dpi=150)
    plt.clf()
    
    fig3.suptitle('dx/dt\n' + opis, fontsize=17)
    
    plt.style.use('seaborn-deep')
    plt.xlabel("Dystans [m]", fontsize=15)
    plt.ylabel("Predkosc [m/s]", fontsize=15)
    plt.grid(color='#717171', linestyle='--', linewidth=0.3)
    
    plt.plot([0,list5[1]],[0,df1["Predkosc P"][1]], linestyle='--', color="g")
    plt.plot([0,list5[1]],[0,list7[1]], linestyle='--', color="b")
    
    plt.plot([list5[1],list5[2]],[df1["Predkosc P"][1],list6[2]], color="g",marker="o")
    plt.plot(list5[2:],list6[2:], label="Fala cisnieniowa", color="g",marker="o")
    plt.plot(list5[1:],list7[1:], label="Front plomienia",  color="b",marker="o")
    plt.ylim(0,V_CJ+200)
    plt.tick_params(axis='both', labelsize=14)
    
    V_CJ_t = str(V_CJ)
    aP_t = str(aP)
    plt.plot([0,3.5], [V_CJ,V_CJ], linestyle='-.', color = "r", linewidth=1.5, alpha=0.6)
    plt.plot([0,3.5], [aP,aP], linestyle='-.', color = "r", linewidth=1.5, alpha=0.6)
    plt.xlim(0,2)
    plt.text(0.1, V_CJ+30, r'$V_{CJ}=\ $'+V_CJ_t+'[m/s]', fontsize=15)
    plt.text(0.1, aP+30, r'$a_{p}=\ $'+aP_t+'[m/s]', fontsize=15)
    
    plt.legend(loc="upper right", fontsize=15)
    plt.tight_layout()
    
    
    
    
    

    
    ###### CIAG DALSZY WYKRESU ZBIORCZEGO #####
    
    df_temp = df1
    
    df_temp=df_temp.drop(df_temp.index[2])
    
    
    print("DF TEMP ", df_temp['Odleglosc'])
    
    ##### Linia pochyla reprezentujaca predkosc pierwszej fali #####
    zbiorczy.plot(df_temp["TOA_P [ms]"]*1000, df_temp["Odleglosc"]+0.08,
                  linewidth=2, color='k')
    
    
    ########## NIEDOKONCZONE  ##############################
    
     
    ###### USUWANIE kanału zanieczyszczonego i urwanego #################################
    
    data.drop('ch 3',
      axis='columns', inplace=True)
    
    ################### USTALENIE KIEDY DOTARLA FALA DO CZUJNIKOW  ###################
    l=-1
    list_zbior = []
    list_czas = []
    
    ##### CZAS DOTARCIA POWROTNEJ FALI #######
    for i, o in zip(data,df_temp["Odleglosc"]):
        if  i != "time [us]" and l < 6:
            k=czas_zbior
            print("Kanal ",i)
            for j in data[i]:
                k+=1
                if data[i][k] > tr_SN_f2:
                    list_czas.append(data["time [us]"][k])
                    if data[i][k]> 1.2: list_zbior.append(o+0.3)  #Gdy za duza wartosc
                    else: list_zbior.append(data[i][k-100]+o-0.3)
                    break
        l+=1
     
    list_czas.append(df1["TOA_P [ms]"][4]*1000)
    list_zbior.append(df_temp["Odleglosc"][4]+0.08)
    list_czas = list_czas[:4]
    
    list_czas = list_czas[::-1]

    """
    ####### Wartosci cisnien ToA powrotnej fali #######
    j=0
    for i in df_temp["Odleglosc"]:
        if j < 7: list_zbior.append(i+tr_SN_f2)
        j+=1
    
    """
    list_zbior = list_zbior[::-1]
   
    
    print("List zbior",  list_zbior)
    print("List czas",  list_czas)
   
    ###### Linia pochyla reprezentujaca fale powrotna ########
    
    zbiorczy.plot(list_czas, df_temp["Odleglosc"][::-1]+0.08,
                  linewidth=2, color='k')
    
    ##### OPOZNIONY ZAPLON ########
    predkosc_powrotn = (1000000*(df_temp["Odleglosc"][4]-df_temp["Odleglosc"][3]))/(list_czas[1]-list_czas[0])
     
    opoz_zapl = (df1['TOA_V [ms]'][4]-df1['TOA_P [ms]'][4])*1000
    print("\nOPOZNIENIE ZAPLONU:",opoz_zapl,"[us]\n")
    print("OSTATNIA PREDKOSC:", round(list6[4],1),"[m/s]\n")
    print("PREDKOSC POWROTNA", round(predkosc_powrotn,1), "[m/s]\n")
    
    return df1
    
    




##########################################################################################################

###### WYSWIETLENIE WYKRESOW #############################################################################


####### Funkcja(dane z czujnikow, opis, numer exp, trigger dla SN, trigger dla SN powrotna fala, 
####### trigger dla SJ, trig dla 2 pierwszych SN, czas po ktorym mierzymy trigger powrotnej fali,
####### max dopusz predkosc fizyczna, V_CJ,aP, czas data, usrednianie predkosci) 

####### TESTY_H2-pow_fi1_091121 #############

##### CZAS = LICZBA / 2 bo kazda proba byla liczona co 0.5 us
  
# df1=funkcja(data1,text1,"1",0.25,0.35,0.13,0.15,9000,1750,1979.24,1009.8,8000,"tak")
# df2=funkcja(data2,text2,"2",0.25,1.1,0.225,0.25,9000,1750,1979.24,1009.8,5500)
# df3=funkcja(data3,text3,"3",0.25,1.1,0.225,0.25,8000,1750,1979.24,1009.8,6500,"tak")
# ##df4=funkcja(data4,text4,"4",0.19,0.4,0.158,0.19,10000,1750,1979.24,1130.1,1000)
# df5=funkcja(data5,text5,"5",0.25,0.5,0.156,0.15,10000,1750,1979.24,1009.8,7600)

# ####### TESTY_H2-pow_fi16_newsetup

# df6=funkcja(data6,text6,"6",0.25,0.3,0.13,0.15,5000,1750,2102.29,1056.6,7500)
# df7=funkcja(data7,text7,"7",0.25,0.33,0.225,0.25,11000,1750,2102.29,1056.6,7500,"tak")
# df8=funkcja(data8,text8,"8",0.25,0.4,0.225,0.25,11000,1750,2102.29,1056.6,6800,"tak")
# df9=funkcja(data9,text9,"9",0.19,0.4,0.158,0.19,10000,1750,2102.29,1056.6,7000,"tak")
# df10=funkcja(data10,text10,"10",0.25,0.4,0.156,0.15,10000,1750,2102.29,1056.6,6600,"tak")
# df11=funkcja(data11,text11,"11",0.25,0.35,0.156,0.15,10000,1750,2102.29,1056.6,7000)

# # # # ################## fi16_styczen_newsetup  (40%) #######################

# df12=funkcja(data12,text12,"12",0.25,0.35,0.156,0.15,10000,1750,2102.29,1056.6,7000,"tak")
# df13=funkcja(data13,text13,"13",0.25,0.35,0.156,0.15,10000,1750,2102.29,1056.6,7000)
# df14=funkcja(data14,text14,"14",0.25,0.35,0.156,0.15,10000,1750,2102.29,1056.6,7300)
# df15=funkcja(data15,text15,"15",0.25,0.35,0.156,0.15,10000,1750,2102.29,1056.6,6900,"tak")
# df16=funkcja(data16,text16,"16",0.25,0.32,0.156,0.15,10000,1750,2102.29,1056.6,7200,"tak")
# df17=funkcja(data17,text17,"17",0.25,0.35,0.156,0.15,10000,1750,2102.29,1056.6,6700)

################# testy_H2-pow_fi128_new_setup_11012022 ###############

df18=funkcja(data18,text18,"18",0.25,0.5,0.156,0.15,10000,1750,2056.51,1039.5,6000)
df19=funkcja(data19,text19,"19",0.25,0.35,0.156,0.15,10000,1750,2056.51,1039.5,7000)
df20=funkcja(data20,text20,"20",0.25,0.35,0.156,0.15,10000,1750,2056.51,1039.5,7000)
df21=funkcja(data21,text21,"21",0.25,0.5,0.156,0.15,10000,1750,2056.51,1039.5,6000,"tak")
df22=funkcja(data22,text22,"22",0.25,0.8,0.156,0.15,8000,1750,2056.51,1039.5,5300,"tak")
df23=funkcja(data23,text23,"23",0.25,0.5,0.156,0.15,10000,1750,2056.51,1039.5,5800,"tak")