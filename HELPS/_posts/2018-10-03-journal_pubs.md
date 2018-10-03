---
layout: default
title: Journal Papers
permalink: /publications/journal
categories: [publication, journal]
---

# Journal Papers

These papers are protected by copyrights. The copyright owners (such as ACM and IEEE) allow authors to post own papers to the public for personal and noncommercial uses.

{% assign papers = site.data.journal_pubs %}

{% for paper in papers %}

- {{ paper.authors }}, *{{ paper.paper_name }}*, {{ paper.conference }}.

{% endfor %}