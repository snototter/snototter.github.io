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

To be filled with actual content!


{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}


{% comment %}
## Publications (Peer-Reviewed)


## Scientific Presentations
Not including workshops, teaching, etc.


## Other Media
ORF, Pro7, ...
{% endcomment %}