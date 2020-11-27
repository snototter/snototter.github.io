---
title: "Publications"
permalink: /publications/
author_profile: true
---

TODO do we need this???? layout: archive
TODO group
## Publications (Peer-Reviewed)
{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

## Scientific Presentations
Not including workshops, teaching, etc.
