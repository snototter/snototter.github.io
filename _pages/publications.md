---
title: "Publications"
permalink: /publications/
author_profile: true
---

<!--TODO do we need this???? layout: archive
TODO group
-->

{% include base_path %}
{% assign author = site.author %}
# Publications
{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{ author.googlescholar }}">my Google Scholar profile</a>.</u>
{% endif %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}


## Publications (Peer-Reviewed)


## Scientific Presentations
Not including workshops, teaching, etc.


## Other Media
ORF, Pro7, ...