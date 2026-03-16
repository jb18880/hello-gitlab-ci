# 🚀 hello-gitlab-ci

基于 GitLab CI/CD + Docker + Harbor 搭建的完整 DevOps 实践项目。

## 📋 项目介绍

本项目从零搭建了一套企业级 CI/CD 流水线，实现代码提交到自动构建、测试、部署的全流程自动化。

## 🏗️ 架构
```
开发机(192.168.65.100)
    │
    │  git push
    ▼
GitLab(192.168.65.101)  ──→  触发流水线
    │
    │  GitLab Runner执行
    ▼
构建Docker镜像
    │
    │  docker push
    ▼
Harbor镜像仓库(192.168.65.102)
    │
    │  docker pull + 部署
    ▼
应用服务器(192.168.65.100)
├── 测试环境 :5001
└── 生产环境 :5002
```

## 🛠️ 技术栈

| 组件 | 版本 | 用途 |
|------|------|------|
| GitLab CE | latest | 代码仓库 + CI/CD |
| GitLab Runner | latest | 流水线执行器 |
| Harbor | v2.10.0 | 私有镜像仓库 |
| Docker | 24.x | 容器化运行 |
| Python | 3.11 | 应用运行环境 |
| Flask | 3.0.0 | Web框架 |
| pytest | 7.4.0 | 单元测试 |

## 🔄 CI/CD 流水线
```
┌─────────┐   ┌──────┐   ┌────────┐   ┌─────────────┐   ┌────────┐   ┌────────┐
│  build  │──▶│ test │──▶│ deploy │──▶│ deploy-prod │──▶│ verify │──▶│ notify │
│构建&推送 │   │单元测试│   │测试环境 │   │ 生产环境(手动)│   │健康检查 │   │Telegram│
└─────────┘   └──────┘   └────────┘   └─────────────┘   └────────┘   └────────┘
```

**分支策略：**
- `dev` 分支：触发 build + test
- `main` 分支：触发全流程

**主要特性：**
- ✅ 自动构建 Docker 镜像并推送到 Harbor
- ✅ 自动运行单元测试，失败则阻断部署
- ✅ 测试环境自动部署，生产环境手动确认
- ✅ 容器健康检查
- ✅ Telegram 流水线状态通知
- ✅ 敏感信息通过 GitLab Variables 管理

## 📁 项目结构
```
hello-gitlab-ci/
├── app/
│   └── main.py          # Flask 应用
├── tests/
│   └── test_main.py     # 单元测试
├── Dockerfile           # 镜像构建配置
├── .gitlab-ci.yml       # CI/CD 流水线配置
└── requirements.txt     # Python 依赖
```

## ⚙️ 环境变量

流水线依赖以下 GitLab CI/CD Variables：

| 变量名 | 说明 |
|--------|------|
| `SSH_PRIVATE_KEY` | 部署服务器的 SSH 私钥 |
| `HARBOR_USER` | Harbor 登录用户名 |
| `HARBOR_PASS` | Harbor 登录密码 |
| `TELEGRAM_TOKEN` | Telegram Bot Token |
| `TELEGRAM_CHAT_ID` | Telegram 接收通知的 Chat ID |

## 🚀 本地运行
```bash
# 安装依赖
pip install -r requirements.txt

# 启动应用
python app/main.py

# 运行测试
python -m pytest tests/ -v
```

## 📝 踩过的坑

- Docker 容器内 `localhost` 不等于宿主机，需用宿主机 IP
- HTTP 私有镜像仓库需配置 `insecure-registries`
- GitLab CI 中 `only` 和 `rules` 不能混用
- alpine 镜像默认无 `curl`，需手动安装
- 容器内访问外网需单独配置代理

## 📌 Roadmap

- [ ] 接入 Kubernetes 部署
- [ ] 添加 Prometheus + Grafana 监控
- [ ] 代码质量检查（flake8）
- [ ] 镜像安全扫描（trivy）
