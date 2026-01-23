// 学习数据统计
const learningStats = {
  totalDays: 0,
  totalModels: 0,
  categories: {},
  updateStats: function() {
    // 从文章计数
    this.totalDays = document.querySelectorAll('.post').length;
    // 更多统计...
  }
};