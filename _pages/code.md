---
permalink: /code/
title: "Code & Data"
author_profile: true
redirect_from: 
  - /data
  - /downloads
  - /tinkering
---

Still to be filled with additional content!


<h2 id="vito" class="cd-header">[Python] vito<a href="#main"><i class="totopnav fas fa-arrow-up"></i></a></h2>
<div class="cd-detail">
<p>
<a href="https://pypi.org/project/vito"><img src="https://badge.fury.io/py/vito.svg" alt="View on PyPI"/></a>
<a href="https://pypi.org/project/vito"><img src="https://img.shields.io/pypi/dm/vito.svg" alt="PyPI - Downloads"/></a>
<a href="https://travis-ci.com/snototter/vito"><img src="https://travis-ci.com/snototter/vito.svg?branch=master" alt="Build Status"/></a>
<a href="https://coveralls.io/github/snototter/vito?branch=master"><img src="https://coveralls.io/repos/github/snototter/vito/badge.svg?branch=master" alt="Coverage Status"/></a>
<a href="https://github.com/snototter/vito/blob/master/LICENSE?raw=true"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"/></a>
</p>
<p>
A light-weight Python utility package for common computer vision &amp; image manipulation tasks.
</p>
</div>


<ul>
{% for dl in site.downloads %}
<li>dl.title
{%for ic in dl.icons %}
({{ic}})
{% endfor %}
</li>
{% endfor %}
</ul>

<h2 id="iminspect" class="cd-header">[Python] iminspect<a href="#main"><i class="totopnav fas fa-arrow-up"></i></a></h2>
<div class="cd-detail">
TODO
</div>


<h2 id="basictinkering" class="cd-header">[Arduino] BasicTinkering<a href="#main"><i class="totopnav fas fa-arrow-up"></i></a></h2>
<div class="cd-detail">
TODO
</div>
{% comment %}

# Software
## vitocpp
# Data
## ICG Lab6
## vPTZ
{% endcomment %}