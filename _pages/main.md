---
permalink: /me/
title: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am a first-year PhD student at [ISIR](https://www.isir.upmc.fr/) (Sorbonne Université) and [INRIA](https://www.inria.fr/en/argo) (ENS). I am under the supervision of [Edouard Oyallon](https://edouardoyallon.github.io/) and [Marc Lelarge](https://www.di.ens.fr/~lelarge/).

I am working on the theoretical foundations of scalable reinforcement learning. Before that, I studied at ENS Paris-Saclay about computer science and AI.

**Research interests:** scalable reinforcement learning, scaling laws

## News
{% for item in site.data.news limit:6 %}
- **{{ item.date }}**: {{ item.text | markdownify | remove: '<p>' | remove: '</p>' }}
{% endfor %}

{% comment %}
## Selected publications
{% for post in site.publications reversed %}{% if post.selected %}
  {% include archive-single.html %}
{% endif %}{% endfor %}
{% endcomment %}