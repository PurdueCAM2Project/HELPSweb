---
layout: page
title: Projects
permalink: /projects/
---

<ul>
  {% for post in site.tags.project_sec %}
    <li>
        <big><a href="{{ post.url }}">{{ post.title }}</a></big>
    </li>
  {% endfor %}
</ul>


