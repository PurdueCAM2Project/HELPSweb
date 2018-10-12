---
layout: page
title: Publications
permalink: /publications/
---

{% for pub_type in site.categories.publication %}
    
- [{{ pub_type.title }}]({{ pub_type.url }})

{% endfor %}

