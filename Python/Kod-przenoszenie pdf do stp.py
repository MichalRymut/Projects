#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# from os import walk
import shutil
import os
# Zakładam strukturę dokumentacji folder główny, w nim foldery fasad, następnie foldery listw oraz słupów + rygli
# Maksymalnie jedno podzłożenie w słupie
# Ścieżka podstawowa dla dokumentacji:

mypath = 'C:\\Users\\m.rymut\\Desktop\\Dokumentacja'
Ściezka_PDF = 'C:\\Users\\m.rymut\\Desktop\\PDF 3D'

# Określenie list itd. do czwartego stopnia
Sciezka_Plikow_Pierwszego_Stopnia = mypath
Nazwa_Plikow_Pierwszego_Stopnia = []
Nazwa_Folderow_Pierwszego_Stopnia = []
Sciezka_Folderow_Pierwszego_Stopnia = ""

Nazwa_Plikow_Drugiego_Stopnia = []
Nazwa_Folderow_Drugiego_Stopnia = []

Nazwa_Plikow_Trzeciego_Stopnia = []
Nazwa_Folderow_Trzeciego_Stopnia = []

Nazwa_Plikow_Czwartego_Stopnia = []
Nazwa_Folderow_Czwartego_Stopnia = []


# pobranie ścieżek folderów pierwszego stopnia, nazw folderów oraz plików w 3 osobnych listach
for (dirpath, dirnames, filenames) in walk(mypath):
    Nazwa_Plikow_Pierwszego_Stopnia.extend(filenames)
    Nazwa_Folderow_Pierwszego_Stopnia.extend(dirnames)
    Sciezka_Folderow_Pierwszego_Stopnia = dirpath
    break
    
# Sprawdzenie czy w folderze głównym występują pliki

if len(Nazwa_Plikow_Pierwszego_Stopnia) > 0:
    print("We wskazanym folderze umieszczone są pliki")
    print("Sprawdź ścieżkę początkową lub usuń pliki")
    
# Sprawdzenie czy w folderze głównym są foldery

elif len(Nazwa_Folderow_Pierwszego_Stopnia) == 0:
    print("Brak folderów")
    
# Jeżeli w folderze głównym występują foldery - pobranie ścieżek i nazw dla folderów i plików drugiego stopnia.
    
elif len(Nazwa_Plikow_Pierwszego_Stopnia) == 0:
    print('Zaczęto działanie kodu')

    
    
for folder_1_stopnia in Nazwa_Folderow_Pierwszego_Stopnia:
    Sciezka_Fasady = mypath + "\\" + folder_1_stopnia
    
    for (dirpath, dirnames, filenames) in walk(Sciezka_Fasady):
        Nazwa_Plikow_Drugiego_Stopnia = []
        Nazwa_Folderow_Drugiego_Stopnia = []
        Pliki_bez_rozszerzen = []
        Nazwa_Plikow_Drugiego_Stopnia.extend(filenames)
        Nazwa_Folderow_Drugiego_Stopnia.extend(dirnames)
        Sciezka_Folderow_Drugiego_Stopnia = dirpath
        
        for i in  Nazwa_Plikow_Drugiego_Stopnia:
            Pliki_bez_rozszerzen.append(i.replace('.stp', ''))
        
        
        #tutaj kopiowanie blach
        for a in Pliki_bez_rozszerzen:
          
            
            Sciezka_pliku_PDF = Ściezka_PDF + "\\" + a + ".pdf"
            Sciezka_Docelowa  = Sciezka_Folderow_Drugiego_Stopnia + "\\" + a + ".pdf"
            try:
                shutil.copy(Sciezka_pliku_PDF, Sciezka_Docelowa)
            except:
                print("Plik - " + a + ".PDF nie istnieje")
                print(Sciezka_pliku_PDF)
                print(Sciezka_Docelowa)
            
        for folder_2_stopnia in Nazwa_Folderow_Drugiego_Stopnia:
            Sciezka_PodZlozenia = Sciezka_Fasady + "\\" + folder_2_stopnia
            
            
            Sciezka_Folderu_Zlozenie = Sciezka_PodZlozenia + "\\Zlozenie"
            Sciezka_Folderu_Elementy = Sciezka_PodZlozenia + "\\Elementy"
            
            try:
                os.mkdir(Sciezka_Folderu_Zlozenie)
            except OSError as error: 
                Sciezka_Folderu_Zlozenie = Sciezka_Folderu_Zlozenie 
           
            try:
                os.mkdir(Sciezka_Folderu_Elementy)
            except OSError as error: 
                Sciezka_Folderu_Elementy = Sciezka_Folderu_Elementy 
                
            # przelozenie zlozenia
            Sciezka_Wstawienia_Zlozenia = Sciezka_Folderu_Zlozenie + "\\" + folder_2_stopnia + ".stp"
            Sciezka_Pobrania_Zlozenia = Sciezka_PodZlozenia + "\\" + folder_2_stopnia + ".stp"
            
            try:
                shutil.move(Sciezka_Pobrania_Zlozenia, Sciezka_Wstawienia_Zlozenia)
                
            except:
                Sciezka_Pobrania_Zlozenia = Sciezka_Pobrania_Zlozenia
                
                
            for (dirpath, dirnames, filenames) in walk(Sciezka_PodZlozenia):
                Nazwa_Plikow_Trzeciego_Stopnia = []
                Nazwa_Folderow_Trzeciego_Stopnia = []
                Pliki_bez_rozszerzen_2 = []
                Nazwa_Plikow_Trzeciego_Stopnia.extend(filenames)
                Nazwa_Folderow_Trzeciego_Stopnia.extend(dirnames)
                Sciezka_Folderow_Trzeciego_Stopnia = dirpath
                
                for b in  Nazwa_Plikow_Trzeciego_Stopnia:
                    Pliki_bez_rozszerzen_2.append(b.replace('.stp', ''))
                
                for c in Pliki_bez_rozszerzen_2:
                    
                    Sciezka_Wstawienia_Czesci = Sciezka_Folderu_Elementy + "\\" + c + ".stp"
                    Sciezka_Pobrania_Czesci = Sciezka_PodZlozenia + "\\" + c + ".stp"
                    
                    try:
                        shutil.move(Sciezka_Pobrania_Czesci, Sciezka_Wstawienia_Czesci)
                    except:
                        Sciezka_Pobrania_Zlozenia = Sciezka_Pobrania_Zlozenia
                
                
                for folder_3_stopnia in Nazwa_Folderow_Trzeciego_Stopnia:
                    Sciezka_Ostatnich_Folderow = Sciezka_PodZlozenia + "\\" + folder_3_stopnia
                    
                    for (dirpath, dirnames, filenames) in walk(Sciezka_Ostatnich_Folderow):
                        Nazwa_Plikow_Czwartego_Stopnia = []
                        Nazwa_Folderow_Czwartego_Stopnia = []
                        Pliki_bez_rozszerzen_3 = []
                        Nazwa_Plikow_Czwartego_Stopnia.extend(filenames)
                        Nazwa_Folderow_Czwartego_Stopnia.extend(dirnames)
                        Sciezka_Folderow_Czwartego_Stopnia = dirpath
        
                        for d in  Nazwa_Plikow_Czwartego_Stopnia:
                            Pliki_bez_rozszerzen_3.append(d.replace('.stp', ''))
        
        
                        #tutaj kopiowanie elementów 
                        for d in Pliki_bez_rozszerzen_3:
                    
                    
                            Sciezka_pliku_PDF_2 = Ściezka_PDF + "\\" + d + ".pdf"
                            Sciezka_Docelowa_2  = Sciezka_Folderow_Czwartego_Stopnia + "\\" + d + ".pdf"
                            try:
                                shutil.copy(Sciezka_pliku_PDF_2, Sciezka_Docelowa_2)
                            except:
                                print("plik - " + d + ".PDF nie istnieje")
                                print(Sciezka_pliku_PDF_2)
                                print(Sciezka_Docelowa_2)
                
                        break
                break
        break
        
        
print('Zakończono działanie kodu')

