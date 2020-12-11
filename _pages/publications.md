---
title: "Publications"
permalink: /publications/
author_profile: true
---

Here you'll find a list of my publications, including [conference & journal papers](#cjproc), contributions to [tracking challenges](#chg), and [my theses](#theses).

{% include base_path %}
{% assign author = site.author %}

<h2 id="cjproc" class="pubheader">Conferences &amp; Journals <a href="#main"><i class="totopnav fas fa-arrow-up"></i></a></h2>
<table class="pubtable">
  <tbody>
    {% for pub in site.pubs reversed %}
      {% include pubentry.html %}
    {% endfor %}
  </tbody>
</table>

<h2 id="chg" class="pubheader">Tracking Challenges <a href="#main"><i class="totopnav fas fa-arrow-up"></i></a></h2>
<table class="pubtable">
  <tbody>
    {% for pub in site.pubs_workshops reversed %}
      {% include pubentry.html %}
    {% endfor %}
  </tbody>
</table>


<h2 id="theses" class="pubheader">Theses <a href="#main"><i class="totopnav fas fa-arrow-up"></i></a></h2>
<table class="pubtable">
  <tbody>
    {% for pub in site.theses reversed %}
      {% include pubentry.html %}
    {% endfor %}
  </tbody>
</table>

{% comment %}
TODO potential bibtex popup solution
<div class="bibpopup" onclick="toggleBibPopup()">Toggle Popup
  <span class="bibpopuptext" id="bib-somekey">
  <p>
      border: 1px dashed #B3B2B2;
    margin-left: 1em;
    margin-right: 1em;
    margin-bottom: 2em;
    padding: 1em;
    background-color: #F8F8F8;
    font-family: monospace;
    font-size: 13px;
    </p>
  </span>
</div>

<script>
// When the user clicks on div, open the popup
function toggleBibPopup() {
  var popup = document.getElementById("bib-somekey");
  popup.classList.toggle("show");
}
</script>
{% endcomment %}
