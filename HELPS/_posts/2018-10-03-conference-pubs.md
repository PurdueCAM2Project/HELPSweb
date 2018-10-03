---
layout: default
title: Conference Papers
permalink: /publications/conference
categories: [publication, conference]
---


# Conference Papers

These papers are protected by copyrights. The copyright owners (such as ACM and IEEE) allow authors to post own papers to the public for personal and noncommercial uses.

{% for topic in site.data.conference_pubs %}

## {{ topic[0] }}


{% for paper in topic[1] %}

- {{ paper.authors }}, *{{ paper.paper_name }}*, {{ paper.conference }}.

{% endfor %}


{% endfor %}