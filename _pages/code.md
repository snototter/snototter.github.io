---
permalink: /code/
title: "Code & Data"
author_profile: true
redirect_from: 
  - /data
  - /downloads
  - /tinkering
---

Still rather incomplete!

{% assign dlist = site.downloads | where: "show", "true" %}
{% assign sw_list = dlist | where: "type", "software" %}
{% assign data_list = dlist | where: "type", "dataset" %}


{% if sw_list.size > 0 %}
<h2 id="software" class="dlheader">Software <a href="#main"><i class="totopnav fas fa-arrow-up"></i></a></h2>
<table class="dltable">
  <tbody>
    {% for entry in sw_list %}
      {% include downloadentry.html %}
    {% endfor %}
  </tbody>
</table>
{% endif %}
{% if data_list.size > 0 %}
<h2 id="datasets" class="dlheader">Datasets <a href="#main"><i class="totopnav fas fa-arrow-up"></i></a></h2>
<table class="dltable">
  <tbody>
    {% for entry in data_list %}
      {% include downloadentry.html %}
    {% endfor %}
  </tbody>
</table>
{% endif %}