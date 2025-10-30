# 🎬 智能电影推荐系统

一个基于协同过滤算法的智能电影推荐系统，能够根据用户的观影偏好推荐相似的电影。本项目使用MovieLens数据集，结合机器学习算法和Streamlit Web框架，打造了一个完整的端到端数据科学项目。


## ✨ 项目特色

- 🎯 **个性化推荐**：基于用户的观影历史，提供精准的电影推荐
- 🔍 **协同过滤算法**：使用基于物品的协同过滤，确保推荐质量
- 🎨 **直观界面**：简洁美观的Streamlit Web界面，零代码操作
- 📊 **完整流程**：涵盖数据清洗、特征工程、模型构建到Web部署的全流程
- 🚀 **易于部署**：一键部署到Streamlit Cloud或其他云平台

## 📁 项目结构

```
movie-recommendation-system/
├── app.py                          # Streamlit主应用文件
├── recommendation_engine.py        # 推荐算法核心模块
├── requirements.txt                # 项目依赖包列表
├── data/
│   ├── ml-100k/                   # MovieLens 100k原始数据集
│   ├── movies.csv                 # 处理后的电影数据
│   ├── ratings.csv                # 处理后的评分数据
│   └── users.csv                  # 处理后的用户数据
├── notebooks/
│   └── movie_recommendation.ipynb # 数据探索和算法开发笔记
└── README.md                      # 项目说明文档
```

## 🛠️ 技术栈

- **编程语言**: Python 3.8+
- **Web框架**: Streamlit
- **数据处理**: Pandas, NumPy
- **机器学习**: Scikit-learn

## 🚀 快速开始

### 前置要求

- Python 3.8 或更高版本
- pip (Python包管理器)或conda

### 安装步骤

1. **克隆项目到本地**
   ```bash
   git clone https://github.com/Theicefish/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. **创建虚拟环境（推荐）**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **安装依赖包**
   ```bash
   pip install -r requirements.txt
   ```

4. **运行Streamlit应用**
   ```bash
   streamlit run app.py
   ```

5. **在浏览器中访问**
   ```
   http://localhost:8501
   ```


## 📊 数据集说明

本项目使用[MovieLens 100k数据集](https://grouplens.org/datasets/movielens/100k/)，包含：

- **1,000+** 用户
- **1,700+** 部电影  
- **100,000+** 条评分记录
- **电影基本信息**（标题、类型、上映年份等）
- **用户人口统计信息**（年龄、性别、职业等）

## 🧠 算法原理

### 基于物品的协同过滤

本系统采用基于物品的协同过滤算法，核心思想是：

> "如果很多用户同时喜欢物品A和物品B，那么物品A和物品B是相似的"

**实现步骤**：
1. 构建用户-电影评分矩阵
2. 计算电影之间的余弦相似度
3. 根据目标用户的历史评分，找到最相似的电影
4. 生成个性化推荐列表

### 核心公式

**余弦相似度计算**：
```
similarity(A, B) = (A · B) / (||A|| × ||B||)
```

其中A和B分别代表两部电影的评分向量。

## 💡 使用方法

1. **打开应用**：运行`streamlit run app.py`或在浏览器中访问部署的链接
2. **选择电影**：从下拉菜单中选择你喜欢的电影
3. **获取推荐**：点击"获取推荐"按钮
4. **查看结果**：系统将显示10部最相似的电影推荐


## 🔧 自定义开发

### 修改推荐算法

在`recommendation_engine.py`中，你可以轻松替换推荐算法：

```python
# 尝试不同的相似度计算方法
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances, manhattan_distances

# 或者实现基于用户的协同过滤
user_similarity = cosine_similarity(ratings_matrix)
```

### 添加新功能

- **实时推荐**：集成实时用户反馈
- **混合推荐**：结合内容过滤和协同过滤
- **A/B测试**：比较不同算法的效果

## 📝 更新日志

### v1.0.0 (2025-10-25)
- ✅ 实现基于物品的协同过滤算法
- ✅ 开发Streamlit Web界面
- ✅ 完成项目文档和部署

## 🙏 致谢

- [MovieLens](https://movielens.org/) - 提供高质量的电影评分数据集
- [Streamlit](https://streamlit.io/) - 优秀的Python Web应用框架
- [Scikit-learn](https://scikit-learn.org/) - 强大的机器学习库

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 📧 联系方式

- 作者：Theicefish
- 邮箱：3157944478@qq.com
- GitHub: [@Theicefish](https://github.com/Theicefish)

  
