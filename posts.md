---
layout: page
title: 所有文章
permalink: /posts/
nav_order: 2
icon: newspaper
---

<div class="all-posts">
  {% assign posts_by_year = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}
  
  {% for year in posts_by_year %}
  <div class="year-section">
    <h2 class="year-title">
      <i class="fas fa-calendar-alt"></i>
      {{ year.name }} 年
      <span class="post-count">({{ year.items.size }} 篇)</span>
    </h2>
    
    <div class="posts-grid">
      {% for post in year.items %}
      <article class="post-card">
        <div class="post-header">
          <h3 class="post-title">
            <a href="{{ post.url }}">{{ post.title }}</a>
          </h3>
          <time class="post-date">
            <i class="far fa-calendar"></i>
            {{ post.date | date: "%Y-%m-%d" }}
          </time>
        </div>
        
        {% if post.excerpt %}
        <div class="post-excerpt">
          {{ post.excerpt | strip_html | truncate: 150 }}
        </div>
        {% endif %}
        
        {% if post.tags %}
        <div class="post-tags">
          {% for tag in post.tags %}
          <span class="tag">{{ tag }}</span>
          {% endfor %}
        </div>
        {% endif %}
        
        {% if post.categories %}
        <div class="post-categories">
          <i class="far fa-folder"></i>
          {% for category in post.categories %}
          <span class="category">{{ category }}</span>{% unless forloop.last %}, {% endunless %}
          {% endfor %}
        </div>
        {% endif %}
      </article>
      {% endfor %}
    </div>
  </div>
  {% endfor %}
</div>

<style>
.all-posts {
  max-width: 1200px;
  margin: 0 auto;
}

.year-section {
  margin-bottom: 50px;
  padding-bottom: 30px;
  border-bottom: 2px solid #e5e7eb;
}

.year-section:last-child {
  border-bottom: none;
}

.year-title {
  font-size: 1.8rem;
  color: #374151;
  margin-bottom: 25px;
  padding-bottom: 10px;
  border-bottom: 2px solid #3b82f6;
  display: flex;
  align-items: center;
  gap: 10px;
}

.year-title i {
  color: #3b82f6;
}

.post-count {
  font-size: 1rem;
  color: #6b7280;
  font-weight: normal;
  margin-left: auto;
}

.posts-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 20px;
}

.post-card {
  background: white;
  border-radius: 12px;
  padding: 25px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  border: 1px solid #e5e7eb;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.post-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  border-color: #3b82f6;
}

.post-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 15px;
}

.post-title {
  font-size: 1.3rem;
  font-weight: 600;
  margin: 0;
  flex: 1;
}

.post-title a {
  color: #1f2937;
  text-decoration: none;
  transition: color 0.3s ease;
}

.post-title a:hover {
  color: #3b82f6;
}

.post-date {
  color: #6b7280;
  font-size: 0.9rem;
  white-space: nowrap;
  display: flex;
  align-items: center;
  gap: 5px;
}

.post-excerpt {
  color: #4b5563;
  line-height: 1.6;
  font-size: 0.95rem;
  margin: 5px 0;
}

.post-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 5px;
}

.tag {
  background: rgba(59, 130, 246, 0.1);
  color: #3b82f6;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 500;
}

.post-categories {
  color: #6b7280;
  font-size: 0.9rem;
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 5px;
}

.category {
  color: #8b5cf6;
  font-weight: 500;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .posts-grid {
    grid-template-columns: 1fr;
  }
  
  .post-header {
    flex-direction: column;
    gap: 8px;
  }
  
  .post-date {
    align-self: flex-start;
  }
  
  .year-title {
    font-size: 1.5rem;
  }
}
</style>