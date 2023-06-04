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
<img src="https://github.com/accio3014/JMT/assets/92027143/5342f05b-6e0e-48ba-8eff-f5ca66618c04" width="50%" /></br>


## Requirements
| **Check list** | **Requirements**     |
|----------------|----------------------|
| OS             | MacOS X              |
| Safari         | latest version       |
| Python         | python3.10 or higher |
</br>

Python module installation list:
```shell
$ pip3.x install PyQt5
$ pip3.x install fake-useragent
$ pip3.x install 
$ pip3.x install
```
</br>

## Useage
There are two ways to use the tool, and the "git clone" is recommended.</br>

### #1 git clone
Download file:
```shell
$ git clone https://github.com/accio3014/JMT.git
```

Run JMT:
```shell
$ python3 "Download path"/JMT/source/gui.py
```

### #2 Download zip

## How to bypass google robot?