#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:39:25 2020

@author: Aksham darian
"""

def writedown(path,data):
    with open(path, 'w') as csvfile: 
        try:
            csvfile.write(','.join(data))
        except:
            with open(path, 'x') as csvfile: 
                csvfile.write(','.join(data))
            


user_list = open("raw_list.csv","rb")
contents_raw = user_list.read()
contents_raw = contents_raw.decode("Windows-1251")
contents_raw = contents_raw.replace(" " , "").replace(";" , "\n").replace('"' , "\n").replace("," , "\n").replace(':' , "\n")
contents_raw = contents_raw.split()
print("your list have",len(contents_raw), "entries")


contents = []
for character in contents_raw:
    character_clean = character.replace(" " , "")
    contents.append(character_clean)
    

domains = []
for atsign in contents:
    domains.append(atsign.split("@")[-1])
    
domains_list = []
for domain in domains:
    if domain not in domains_list:
        domains_list.append(domain) 
writedown("domains.csv",domains_list)
print("your list has",len(domains_list),"unique domains")


gmail_temp= []
for gmail in contents:
    if "gmail.com" in gmail:
        gmail_temp.append(gmail)
        
gmails_accounts = []
for atsign in gmail_temp:
    gmail_account = atsign.replace(".", "")
    gmails_accounts.append(gmail_account.split("@")[0])
writedown("gmail_accounts.csv",gmails_accounts)
print("encluding",len(gmails_accounts),"gmail accounts")

rest_emails_temp= []
for email in contents:
    if "gmail.com" not in email:
        rest_emails_temp.append(email)

rest_accounts = []
for atsign in rest_emails_temp:
    rest_accounts.append(atsign.split("@")[0])
print("&",len(rest_accounts),"other accounts")
writedown("rest_accounts.csv",rest_accounts)







