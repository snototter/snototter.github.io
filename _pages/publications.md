---
title: "Publications"
permalink: /publications/
redirect_from: 
  - /papers
author_profile: true
---
{% include base_path %}
{% assign author = site.author %}

Here you'll find a list of my publications, including [conference & journal papers](#cjproc), contributions to [tracking challenges](#chg), and [my theses](#theses).


<table class="iconsummary" align="center">
  <tr>
    <td class="isicon"><i class="fa fa-file-pdf withpuburl"></i></td><td class="istxt">Author's preprint</td>
    <td class="isicon"><i class="fa fa-book-open withpuburl"></i></td><td class="istxt">Publisher's version</td>
    <td class="isicon"><i class="fa fa-file-alt withpuburl"></i></td><td class="istxt">Supplemental material</td>
  </tr>
  <tr>
    <td class="isicon"><i class="fa fa-desktop withpuburl"></i></td><td class="istxt">Presentation</td>
    <td class="isicon"><i class="fa fa-video withpuburl"></i></td><td class="istxt">Video</td>
    <td class="isicon"><i class="fa fa-link withpuburl"></i></td><td class="istxt">BibTeX</td>
  </tr>
  <tr>
    <td class="isicon"><i class="fa fa-database withpuburl"></i></td><td class="istxt">Data</td>
    <td class="isicon"><i class="fa fa-code withpuburl"></i></td><td class="istxt">Software</td>
    <td class="isicon"><i class="fa fa-globe-americas withpuburl"></i></td><td class="istxt">External URL</td>
  </tr>
</table>

<h2 id="cjproc" class="pubheader">Conferences &amp; Journals{% include scroll_top %}</h2>
<table class="pubtable">
  <tbody>
    {% for pub in site.pubs reversed %}
      {% include pubentry.html %}
    {% endfor %}
  </tbody>
</table>

<h2 id="chg" class="pubheader">Visual Object Tracking Challenges{% include scroll_top %}</h2>
<table class="pubtable">
  <tbody>
    {% for pub in site.pubs_workshops reversed %}
      {% include pubentry.html %}
    {% endfor %}
  </tbody>
</table>


<h2 id="theses" class="pubheader">Theses{% include scroll_top %}</h2>
<table class="pubtable" id="thesistable">
  <tbody>
    {% for pub in site.theses reversed %}
      {% include pubentry.html %}
    {% endfor %}
  </tbody>
</table>


<script>
  function toggle_bib(id) {
    var bib_span = document.getElementById(id);
    var tcell = document.getElementById(id + '-pubinfo')

    if (bib_span.style.display == 'block') {
      bib_span.style.display = 'none';
      tcell.onclick = function() { toggle_bib(id); };
    } else {
      bib_span.style.display = 'block';
      tcell.onclick = null; // Disable toggle via cell-click (so you can copy the bibentry)
    }
  }
</script>
