"""
Author: Kody Moodley
Date: 4 May 2022
License: Apache 2.0 - https://www.apache.org/licenses/LICENSE-2.0.txt
Description: a Python script to extract all verses, translations and purports
from A.C. Bhaktivedanta Swami Prabhupada's Bhagavad Gita as it is, Srimad Bhagavatam and Caitanya Caritamrta
from the vedabase.io website
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
import argparse

cccantos = ["adi", "madhya", "antya"]
df = pd.DataFrame(columns=["id","sanskrit","english","purport"])

def extract_main(book, canto):
    global df    
    canto_page = requests.get("https://vedabase.io/en/library/"+book+"/"+str(canto))
    canto_soup = BeautifulSoup(canto_page.content, 'html.parser')
    chapters = canto_soup.select("div.r-chapter a")
    for chapter in chapters:
        chapnum = chapter.get("href").split('/')[-2]
        if chapnum.isnumeric():
            chap_page = requests.get("https://vedabase.io"+chapter.get("href")+"advanced-view")
            chap_soup = BeautifulSoup(chap_page.content, 'html.parser')
            texts = chap_soup.select("div.bb.r-verse h1 a")
            for text in texts:       
                text_page = requests.get("https://vedabase.io"+text.get("href"))
                text_soup = BeautifulSoup(text_page.content, 'html.parser')
                para = text_soup.select("div.wrapper-verse-text")[0]
                purp = ""

                parap = text_soup.select("div.wrapper-puport") if len(text_soup.select("div.wrapper-puport")) > 0 else text_soup.select("div.wrapper-purport")

                if (len(parap) > 0):
                    paraPurp = parap[0]
                    for div in paraPurp.findChildren("div"):
                        purp += " " + div.get_text()

                sans = ""
                for div in para.findChildren("div"):
                    sans += " " + div.get_text()
                        
                english = text_soup.select("div.r.r-lang-en.r-translation p")[0].get_text()
                print(text.get("href")[15:])
                df.loc[len(df)]=[text.get("href")[15:],sans,english,purp]

def extract(book):
    if book not in ["bg", "sb", "cc"]:
        print("Error: a valid book is either 'bg' (Bhagavad Gita as it is), 'sb' (Srimad Bhagavatam) or 'cc' Caitanya Caritamrta.")
    else:
        # SB has 12 cantos
        if (book == 'sb'):
            for canto in range(1,13):
                extract_main(book, canto)
            df.to_csv('output-sb.csv',index=False)
        elif (book == 'cc'):
            # Adi, Madhya and Antya lila cantos
            for canto in cccantos:
                extract_main(book, canto)
            df.to_csv('output-cc.csv',index=False)
        else:
            # BG has 18 Chapters
            extract_main(book, "")
            df.to_csv('output-bg.csv',index=False)

parser = argparse.ArgumentParser(description=
'Extracts transliterated sanskrit verses, english translations and purports from A.C. Bhaktivedanta Swami Prabhupada''s Bhagavad Gita as it is, Srimad Bhagavatam and Caitanya Caritamrta from the vedabase.io website.')
parser.add_argument('--extract', default="bg", choices=["bg", "sb", "cc"], help='extracts text from vedabase.io for the specific book given (bg - Bhagavad Gita, sb - Srimad Bhagavatam or cc - Caitanya Caritamrta)')
parser.add_argument('-extract', default="bg", choices=["bg", "sb", "cc"], help='extracts text from vedabase.io for the specific book given (bg - Bhagavad Gita, sb - Srimad Bhagavatam or cc - Caitanya Caritamrta)')

args = parser.parse_args()

if (len(sys.argv) != 3):
    print("Error: exactly 2 arguments are required in order to run this script. Type '-h' to get help about how to use this script.")
else:
    if sys.argv[2] == "bg":
        extract("bg")
    elif sys.argv[2] == "sb":
        extract("sb")
    else:
        extract("cc")


