---
permalink: /research
title: "Research"
excerpt: "Research Overview"
author_profile: true
redirect_from: 
  - /
  - /index.html
---
{% include base_path %}
{% assign author = site.author %}

## Research Overview
I'm a senior scientist coordinating the __Learning, Recognition & Surveillance__ workgroup at the __Institut of Computer Graphics & Vision__.
My PhD research focused on....
Currently, my research interests are...

# Publications
{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{ author.googlescholar }}">my Google Scholar profile</a>.</u>
{% endif %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}


## Awards & Honors
* Winner of the **Austrian Road Safety Board Research Award** (Forschungspreis des Kuratoriums f&uuml;r Verkehrssicherheit, KfV), 2020
* **Outstanding Reviewer**, European Conference on Computer Vision (ECCV), 2020
* **Outstanding Reviewer**, Elsevier Pattern Recognition (PR), 2017
* **OCG Best Paper Award** by the Austrian Computer Society (&Ouml;sterreichische Computer Gesellschaft), 2013


## Professional Services
Reviewing for conferences (since 2015), including:
* IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
* European Conference on Computer Vision (ECCV)
* International Conference on Computer Vision (ICCV)
* IEEE Winter Conference on Applications of Computer Vision (WACV)
* Visual Object Tracking challenge (VOT) Workshop
* IEEE International Conference on Robotics and Automation (ICRA)
* International Symposium on Image and Signal Processing and Analysis (ISPA)
* Computer Vision Winter Workshop (CVWW)
* Joint OAGM and ARW Workshop (OAGM/ARW)
* ACM SIGGRAPH Asia

Reviewing for journals (since 2014), including:
* [IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=34)
* [IEEE Transactions on Image Processing (TIP)](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=83)
* [IEEE Transactions on Neural Networks and Learning Systems (TNNLS)](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=5962385)
* IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)
* IEEE Signal Processing Letters (SP LETTERS)
* IEEE Transactions on Multimedia (TMM)
* Elsevier Computer Vision and Image Understanding (CVIU)
* Elsevier Pattern Recognition (PR)
* Elsevier Pattern Recognition Letters (PR LETTERS)
* Elseview Image and Vision Computing (IMAVIS)
* Elsevier Journal of Visual Communication and Image Representation (JVCI)
* International Journal of Distributed Sensor Networks (IJDSN)
* Systems Science and Control Engineering (SSCE)
* Computational Intelligence and Neuroscience (CIN)
* IET Computer Vision
