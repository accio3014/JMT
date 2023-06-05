</br>

- [JMT Manual](#jmt-manual)
  - [Description](#description)
  - [Diagram](#diagram)
  - [Requirements](#requirements)
  - [Useage](#useage)
  - [How to bypass reCAPTCHA](#how-to-bypass-recaptcha)
- [Author](#author)
  - [accio](#accio)
  - [socelia](#socelia)

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

Allow Safari automation :
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
Download file :
```shell
$ git clone https://github.com/accio3014/JMT.git
```

Run JMT :
```shell
$ python3.x "Download path"/JMT/source/gui.py
```
</br>

Insert URL :</br>
<img src="https://github.com/accio3014/JMT/assets/92027143/0be08b6f-eadb-49b9-a7c3-7f256da9d457" width="50%" /></br>
</br>

Select category in GHDB :</br>
<img src="https://github.com/accio3014/JMT/assets/92027143/2613cc62-fde1-44be-b271-912e8ba15cc1" width="50%" /></br>
</br>

Waiting for result :</br>
<img src="https://github.com/accio3014/JMT/assets/92027143/35071172-4806-42bf-8555-1c98676a31aa" width="50%" /></br>
<span style='color:#FFF978'>[Exploit]</span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; : There are search results..</br>
<span style='color:#696969'>[Fail]</span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; : No search results.</br>
<span style='color:#5F87E1'>[reCAPTCHA]</span>&nbsp; &nbsp;  : Google reCAPTCHA detected.</br>
</br>

## How to bypass reCAPTCHA
Most reCAPTCHA are bypassed because they use the Safari web browser, but you can bypass them more effectively by additionally using the methods below :</br>
```plaintext
1. Use a VPN
reCAPTCHA can be bypassed by using a VPN to change your country or region.

2. Restart your MAC
reCAPTCHA can be bypassed by restarting the Mac.
```
It doesn't matter which of the above two methods you use, but we recommend restarting your Mac.</br>
</br>

# Author
## <a href="https://github.com/accio3014" target="_blank">accio</a>
## <a href="https://github.com/eey4611" target="_blank">socelia</a>