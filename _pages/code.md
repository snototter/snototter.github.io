---
permalink: /code/
title: "Code & Data"
author_profile: true
redirect_from: 
  - /data
  - /downloads
  - /tinkering
---

Here you'll find downloads for various [software libraries/utilities](#software) and [custom datasets](#datasets). For publication-related downloads, please refer to my [publication list](/publications) 

{% assign dlist = site.downloads | where: "show", "true" %}
{% assign sw_list = dlist | where: "type", "software" %}
{% assign data_list = dlist | where: "type", "dataset" %}

{% if sw_list.size > 0 %}
<h2 id="software" class="dlheader">Software{% include scroll_top %}</h2>
<table class="dltable">
  <tbody>
    {% for entry in sw_list %}
      {% include downloadentry.html %}
    {% endfor %}
  </tbody>
</table>
{% endif %}
{% if data_list.size > 0 %}
<h2 id="datasets" class="dlheader">Datasets{% include scroll_top %}</h2>
<table class="dltable">
  <tbody>
    {% for entry in data_list %}
      {% include downloadentry.html %}
    {% endfor %}
  </tbody>
</table>
{% endif %}
