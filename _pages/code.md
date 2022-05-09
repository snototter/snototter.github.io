---
permalink: /code/
title: "Code & Data"
author_profile: true
redirect_from: 
  - /data
  - /downloads
  - /tinkering
---

Here you'll find downloads for various [software libraries/utilities](#software-utils), as well as [software accompanying our publications](#software-pubs) and [custom datasets](#datasets). Publication-related downloads can also be accessed from my [publication list](/publications).

{% assign dlist = site.downloads | where: "show", "true" %}
{% assign sw_list = dlist | where: "type", "software" %}
{% assign pub_list = dlist | where: "type", "publication-software" %}
{% assign data_list = dlist | where: "type", "dataset" %}

{% if sw_list.size > 0 %}
<h2 id="software-utils" class="dlheader">Software Utilities{% include scroll_top %}</h2>
<table class="dltable">
  <tbody>
    {% for entry in sw_list %}
      {% include downloadentry.html %}
    {% endfor %}
  </tbody>
</table>
{% endif %}
{% if pub_list.size > 0 %}
<h2 id="software-pubs" class="dlheader">Software from Publications{% include scroll_top %}</h2>
<table class="dltable">
  <tbody>
    {% for entry in pub_list %}
      {% include downloadentry.html %}
    {% endfor %}
  </tbody>
</table>
{% endif %}
{% if data_list.size > 0 %}
<h2 id="datasets" class="dlheader">Published Datasets{% include scroll_top %}</h2>
<table class="dltable">
  <tbody>
    {% for entry in data_list %}
      {% include downloadentry.html %}
    {% endfor %}
  </tbody>
</table>
{% endif %}
