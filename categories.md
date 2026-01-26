---
layout: page
title: "文章分类"
permalink: /categories/
---

<div class="categories-grid">
  {% for category in site.categories %}
  <div class="category-card">
    <h3>
      <i class="fas fa-folder"></i>
      {{ category[0] }}
    </h3>
    <span class="post-count">{{ category[1].size }} 篇文章</span>
    
    <ul class="category-posts">
      {% for post in category[1] limit:5 %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a>
        <span class="post-date">{{ post.date | date: "%Y-%m-%d" }}</span>
      </li>
      {% endfor %}
    </ul>
    
    <a href="/categories/{{ category[0] | slugify }}/" class="view-all">查看全部</a>
  </div>
  {% endfor %}
</div>

<style>
.categories-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
    margin-top: 30px;
}

.category-card {
    background: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    border: 1px solid #e5e7eb;
}

.category-card h3 {
    color: #3b82f6;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.post-count {
    color: #6b7280;
    font-size: 0.9rem;
}

.category-posts {
    list-style: none;
    margin: 15px 0;
}

.category-posts li {
    margin: 8px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.category-posts a {
    color: #374151;
    text-decoration: none;
    flex: 1;
}

.category-posts a:hover {
    color: #3b82f6;
}

.post-date {
    color: #9ca3af;
    font-size: 0.8rem;
}

.view-all {
    display: inline-block;
    margin-top: 10px;
    color: #3b82f6;
    text-decoration: none;
    font-size: 0.9rem;
}
</style>