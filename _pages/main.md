---
permalink: /me/
title: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am a first-year PhD student in machine learning, jointly at [ISIR](https://www.isir.upmc.fr/) (Sorbonne Université) and the [ARGO team](https://www.inria.fr/en/argo) at Inria and ENS-PSL, supervised by [Edouard Oyallon](https://edouardoyallon.github.io/) and [Marc Lelarge](https://www.di.ens.fr/~lelarge/).

My research focuses on the theoretical foundations of **scalable reinforcement learning**, with applications to **LLM post-training**: understanding how RL methods behave as models, data and compute grow, and how to improve these methods at scale.

Before my PhD, I studied computer science and AI at [ENS Paris-Saclay](https://ens-paris-saclay.fr/), where I completed the [MVA master's program](https://www.master-mva.com/). Along the way, I worked on quantum machine learning (an internship at [Quandela](https://www.quandela.com/) and a research year), before turning fully to classical machine learning.

**Research interests:** scalable reinforcement learning, scaling laws, asynchronous RL, LLM post-training

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