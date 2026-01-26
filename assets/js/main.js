// 创建 assets/js/main.js
document.addEventListener('DOMContentLoaded', function() {
  // 文章卡片悬停效果
  const postItems = document.querySelectorAll('.post-item');
  postItems.forEach(item => {
    item.addEventListener('mouseenter', () => {
      item.style.transform = 'translateY(-5px)';
    });
    item.addEventListener('mouseleave', () => {
      item.style.transform = 'translateY(0)';
    });
  });
});