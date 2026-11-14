# 动效组件选型表

以下“风格”是基于组件示例的选型判断，不是库的硬性限制。版本、组件依赖和价格会变化；安装前查看所选组件的官方页面。

| 方案 | 适用场景 | 兼容性与接入 | 风格 / 取舍 |
| --- | --- | --- | --- |
| [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animations) / [Web Animations API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API) | 单个元素的状态反馈、低成本过渡 | 框架无关；无额外运行时 | 最容易融入现有设计；复杂状态或布局编排需自己维护 |
| [Motion](https://motion.dev/docs) + 本地 `$motion` | React 状态、布局、手势；也有 JS、Vue 文档 | React 版要求 React ≥18.2；按平台选入口 | 风格完全由项目决定；是动画引擎，不是组件目录 |
| [Animate UI](https://animate-ui.com/docs) | 已有 shadcn/ui、Radix UI、Base UI 或 React Aria 的产品控件 | 当前 v2 为 React 19 + Motion；现有组件可换 primitive import，CLI 可批量处理 | 克制、频繁交互友好；批量改动前审查 diff，React 18 项目先排除 |
| [Motion Primitives](https://motion-primitives.com/docs) | 产品与营销页中的局部交互、文本、对话框 | React + Tailwind CSS + Motion；按组件复制/安装源码 | 轻巧、可改造；需核对每个组件的语义和额外依赖 |
| [Magic UI](https://magicui.design/docs/installation) | 营销页、logo 展示、视觉点缀 | React、Tailwind、shadcn 注册表；组件逐个安装 | 装饰性较强；避免把持续运动放进高频工作界面；Pro 另需授权 |
| [Aceternity UI](https://ui.aceternity.com/installation) | 强视觉 hero、3D、背景、展示区块 | 当前安装指南要求 React 19 + Tailwind v4；组件逐个检查 | 大胆、沉浸；部分效果依赖较重，Pro 区块另需授权 |
| [React Bits](https://reactbits.dev/) | 创意文本、背景、微交互 | React；JS/TS × CSS/Tailwind，复制源码或 CLI | 表现力强；逐个核对依赖、移动端性能及可读性；Pro 另需授权 |
| [Motion UI](https://motion.dev/ui) | 复杂 gallery、carousel、ticker 等现成组件 | React；`motion-plus` 与免费 `motion` 是不同包 | 工程化、headless、可定制；属于 Motion+ 付费内容 |
| [GSAP ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/) | 多段滚动时间线、pin、scrub | 框架无关；需处理组件生命周期 | 叙事性强；增加实现与维护成本，不当作普通控件库 |

快速筛选：高频业务控件 → 现有体系 / Animate UI；低调可复用局部动效 → Motion Primitives；营销展示 → Magic UI；强视觉创意 → Aceternity UI / React Bits；复杂现成轮播或图库且有授权 → Motion UI。若候选不适配当前技术栈，就使用现有组件加 Motion/CSS 实现所需反馈。

Motion 官方公开 [AI Kit skill 与安装指南](https://motion.dev/docs/ai-kit-install)；本地 `$motion` 是该官方 skill。官方免费 MCP 可搜索最新文档，Motion+ 源码和性能审计需要对应授权。Animate UI 也有 [官方 skill](https://animate-ui.com/docs/skills)，仅在确定使用该库时按其当前安装说明启用，以免平常加载额外上下文。
