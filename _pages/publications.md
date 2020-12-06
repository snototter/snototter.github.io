---
title: "Publications"
permalink: /publications/
author_profile: true
---

Here you'll find a (mostly) up-to-date list of my publications.

{% include base_path %}
{% assign author = site.author %}

Still to be filled with actual content!

<h2 class="pubheader">Conference Proceedings &amp; Journal Articles</h2>
<table class="pubtable">
  <tbody>
    {% for pub in site.pubs reversed %}
      {% include pubentry.html %}
    {% endfor %}
  </tbody>
</table>

<h2 class="pubheader">Workshops &amp; Challenges</h2>
<table class="pubtable">
  <tbody>
    {% for pub in site.pubs_workshops reversed %}
      {% include pubentry.html %}
    {% endfor %}
  </tbody>
</table>


<h2 class="pubheader">Theses</h2>
<table class="pubtable">
  <tbody>
    {% for pub in site.theses reversed %}
      {% include pubentry.html %}
    {% endfor %}
  </tbody>
</table>



{% comment %}
## Publications (Peer-Reviewed)


## Scientific Presentations
Not including workshops, teaching, etc.


## Other Media
ORF, Pro7, ...
{% endcomment %}
