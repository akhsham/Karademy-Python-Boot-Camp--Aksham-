#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:39:25 2020

@author: Aksham darian
"""


f = open("raw_list_test.csv","rb")
contents_raw = f.read()
contents_raw = contents_raw.decode("Windows-1251")
contents_raw = contents_raw.replace(" " , "").replace(";" , "\n").replace('"' , "\n").replace("," , "\n").replace(':' , "\n")
contents_raw = contents_raw.split()

contents = []
for character in contents_raw:
    character_clean = character.replace(" " , "")
    contents.append(character_clean)
    

domains = []
for atsign in contents:
    domains.append(atsign.split("@")[-1])
    
clear_domains = []
for domain in domains:
    if domain not in clear_domains:
        clear_domains.append(domain)
with open("domains.csv", 'w') as csvfile:  
    csvfile.write(','.join(clear_domains))
    


gmails= []
for gmail in contents:
    if "gmail.com" in gmail:
        gmails.append(gmail)
        
gmails_accounts = []
for atsign in gmails:
    gmail_account = atsign.replace(".", "")
    gmails_accounts.append(gmail_account.split("@")[0])
    
with open("gmail_accounts.csv", 'w') as csvfile:  
    csvfile.write(','.join(gmails_accounts))

rest_emails= []
for email in contents:
    if "gmail.com" not in email:
        rest_emails.append(email)

rest_accounts = []
for atsign in rest_emails:
    rest_accounts.append(atsign.split("@")[0])
print(len(rest_accounts))
with open("rest_accounts.csv", 'w') as csvfile:  
    csvfile.write(','.join(rest_accounts))







