---
layout: default
title: Technical Reports
permalink: /publications/reports
categories: [publication, reports]
---


# Technical Reports

{% assign reports = site.data.reports %}

{% for report in reports %}

- {{ report.authors }} **{{ report.report_name }}**, {{ report.details }} {% if report.link %}[[PDF]]({{ report.link }}){% endif %}

{% endfor %}