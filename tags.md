---
layout: page
title: 标签
permalink: /tags/
nav_order: 3
icon: tags
---

<div class="tags-page">
  <div class="tags-cloud">
    {% for tag in site.tags %}
    {% assign tag_size = tag[1].size %}
    {% assign font_size = tag_size | times: 2 | plus: 14 %}
    <a href="/tags/{{ tag[0] | slugify }}/" 
       class="tag-link" 
       style="font-size: {{ font_size }}px;">
      {{ tag[0] }} ({{ tag_size }})
    </a>
    {% endfor %}
  </div>
  
  <div class="tags-list">
    {% for tag in site.tags %}
    <div class="tag-section">
      <h2 id="{{ tag[0] | slugify }}">
        <i class="fas fa-tag"></i>
        {{ tag[0] }}
        <span class="post-count">({{ tag[1].size }} 篇)</span>
      </h2>
      
      <div class="tag-posts">
        {% for post in tag[1] %}
        <article class="post-item">
          <time class="post-date">{{ post.date | date: "%Y-%m-%d" }}</time>
          <a href="{{ post.url }}" class="post-title">{{ post.title }}</a>
        </article>
        {% endfor %}
      </div>
    </div>
    {% endfor %}
  </div>
</div>

<style>
.tags-cloud {
  text-align: center;
  margin: 40px 0;
  padding: 30px;
  background: white;
  border-radius: 15px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.tag-link {
  display: inline-block;
  margin: 8px 12px;
  padding: 8px 16px;
  background: linear-gradient(135deg, #3b82f6, #8b5cf6);
  color: white;
  text-decoration: none;
  border-radius: 20px;
  transition: all 0.3s ease;
  font-weight: 500;
}

.tag-link:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(59, 130, 246, 0.4);
}

.tags-list {
  margin-top: 50px;
}

.tag-section {
  margin-bottom: 40px;
  padding-bottom: 30px;
  border-bottom: 1px solid #e5e7eb;
}

.tag-section h2 {
  color: #374151;
  font-size: 1.5rem;
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.tag-section h2 i {
  color: #3b82f6;
}

.post-count {
  font-size: 1rem;
  color: #6b7280;
  font-weight: normal;
}

.tag-posts {
  display: grid;
  gap: 15px;
}

.post-item {
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 15px;
  background: #f8fafc;
  border-radius: 10px;
  transition: all 0.3s ease;
}

.post-item:hover {
  background: #e0e7ff;
  transform: translateX(5px);
}

.post-date {
  color: #6b7280;
  min-width: 100px;
  font-family: 'Courier New', monospace;
}

.post-title {
  color: #374151;
  text-decoration: none;
  font-weight: 500;
  flex: 1;
}

.post-title:hover {
  color: #3b82f6;
}

@media (max-width: 768px) {
  .post-item {
    flex-direction: column;
    align-items: flex-start;
    gap: 5px;
  }
  
  .post-date {
    min-width: auto;
  }
}
</style>