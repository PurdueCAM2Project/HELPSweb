---
layout: page
title: Publications
permalink: /publications/
---


{% assign papers = site.data.pubs %}

{% for paper in papers %}
<!-- {% if paper.document_type == item.type %} -->

- {{ paper.authors }}, *{{ paper.paper_name }}*, {{ paper.conference }}

<!-- {% endif %} -->
{% endfor %}
