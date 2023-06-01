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

## Check list
| **Check list**    | **Detail**                                           | **Required** | **Optional** |
|-------------------|------------------------------------------------------|:------------:|:------------:|
| OS                | MacOS X                                              |       O      |       -      |
| Python            | python3.10 or higher                                 |       O      |       -      |
| Chrome            | latest release version                               |       -      |       O      |
| Chromedriver      | Install the one that matches your version of Chrome. |       -      |       O      |
| Chrome extensions | Buster: Captcha Solver for Humans                    |       -      |       O      |
| Firefox           | latest release version                               |       -      |       O      |

The checklist for Chrome and Firefox are optional. If you install the option, you can bypass robot detection in Google search a little more.</br></br>

Python module installation list:
```python
$ pip3 install PyQt5
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
$ python3 "download path"/JMT/source/gui.py
```

### #2 Download zip

## How to bypass google robot?