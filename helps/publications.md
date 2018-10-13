---
layout: page
title: Publications
permalink: /publications/
---

# {{ site.baseurl }}

{% for pub_type in site.categories.publication %}
    
- [{{ pub_type.title }}](/{{ site.baseurl }}{{ pub_type.url }})

{% endfor %}

