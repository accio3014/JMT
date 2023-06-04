# JMT Manual

## Description
"JMT" stands for "Jonna Michine Tool" and is a tool for  diagnosing vulnerabilities in websites. Most web vulnerability diagnosis tools perform analysis by scanning URLs, but JMT is different from other tools because it uses the Google search engine to check open information on the web.</br>
The reason why the vulnerability diagnosis tool was created using the Google search engine is that by combining individual email addresses and other information, you can get a larger amount of personal information than you think just by searching Google, and the search for websites is the same.  Using the JMT tool prevents malicious users from collecting vulnerable information when gathering information about a website as a preliminary step to attacking a particular website.</br>

Target : 
```
- Information Security Manager
- Web Developer
```
</br>


## Diagram
<img src="https://github.com/accio3014/JMT/assets/92027143/f8a67c3b-f162-4926-880c-e1f8ec52c4c7" width="100%" /></br>
</br>


## Requirements
| **Check list** | **Requirements**     |
|----------------|----------------------|
| OS             | MacOS X              |
| Safari         | latest version       |
| Python         | python3.10 or higher |
</br>

Allow Safari automation:
```plaintext
Safari → Develop → Allow Remote Automation
```
Python module installation list:
```shell
$ pip3.x install PyQt5
$ pip3.x install bs4
$ pip3.x install selenium
```
</br>

## Useage
Download file:
```shell
$ git clone https://github.com/accio3014/JMT.git
```

Run JMT:
```shell
$ python3.x "Download path"/JMT/source/gui.py
```
</br>

Insert URL:</br>
<img src="https://github.com/accio3014/JMT/assets/92027143/0be08b6f-eadb-49b9-a7c3-7f256da9d457" width="40%" /></br>
</br>

Select category in GHDB:</br>
<img src="https://github.com/accio3014/JMT/assets/92027143/2613cc62-fde1-44be-b271-912e8ba15cc1" width="40%" /></br>
</br>