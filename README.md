# AbuseIPDB-python3-GUI

[![Build Status](https://travis-ci.org/growmaster420/AbuseIPDB-python3-GUI.svg?branch=master)](https://travis-ci.org/growmaster420/AbuseIPDB-python3-GUI)

https://www.abuseipdb.com/

https://www.abuseipdb.com/categories

## requirements 
* python3 python3-requests python3-tkinter
* a computer(windows or linux)
* an API key
* a keyboard(and maybe a mouse)
## setup
change variable

    API_KEY = 'place_your_apikey_here'

# Usage of API
## Report Categories
```
D	Title	Description
3 	Fraud Orders 	Fraudulent orders.
4 	DDoS Attack 	Participating in distributed denial-of-service (usually part of botnet).
9 	Open Proxy 	Open proxy, open relay, or Tor exit node.
10 	Web Spam 	Comment/forum spam, HTTP referer spam, or other CMS spam.
11 	Email Spam 	Spam email content, infected attachments, phishing emails, and spoofed senders (typically via exploited host or SMTP server abuse). Note: Limit comments to only relevent information (instead of log dumps) and be sure to remove PII if you want to remain anonymous.
14 	Port Scan 	Scanning for open ports and vulnerable services.
18 	Brute-Force 	Credential brute-force attacks on webpage logins and services like SSH, FTP, SIP, SMTP, RDP, etc. This category is seperate from DDoS attacks.
19 	Bad Web Bot 	Webpage scraping (for email addresses, content, etc) and crawlers that do not honor robots.txt. Excessive requests and user agent spoofing can also be reported here.
20 	Exploited Host 	Host is likely infected with malware and being used for other attacks or to host malicious content. The host owner may not be aware of the compromise. This category is often used in combination with other attack categories.
21 	Web App Attack 	Attempts to probe for or exploit installed web applications such as a CMS like WordPress/Drupal, e-commerce solutions, forum software, phpMyAdmin and various other software plugins/solutions.
22 	SSH 	Secure Shell (SSH) abuse. Use this category in combination with more specific categories.
23 	IoT Targeted 	Abuse was targeted at an "Internet of Things" type device. Include information about what type of device was targeted in the comments. 
```

## Your final str would be somthing like:
```
https://www.abuseipdb.com/report/json?key=YOUAPIKEY&category=18&comment=80.82.66.60&ip=80.82.66.60
```
