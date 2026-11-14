# Animated Component Picker

Choose one animation approach or ready-made component for a web interface. The [skill](SKILL.md) first checks the project's stack and existing design system, then opens the [comparison catalog](references/catalog.md) only when a component choice is needed. This keeps routine UI tasks from loading an entire animation library catalog.

The catalog distinguishes product controls, subtle local motion, marketing decoration, expressive effects, premium Motion UI, and scroll-driven timelines. It records compatibility, visual character, and access limits with links to the providers' current documentation. Those descriptions are selection guidance, not measured performance rankings; check the chosen component's current version and dependencies before installing it.

The original selector instructions and catalog are maintained here under this repository's MIT license. [Motion's official AI Kit skill](https://motion.dev/docs/ai-kit-install) is an independent upstream project and is **not** redistributed. Its MCP and Motion+ features are optional and subject to Motion's access terms.

Use `$animated-component-picker` with a concrete task, for example: “Choose a restrained animation for our existing shadcn dialog” or “Pick a creative hero effect that works with our React and Tailwind versions.” For a plain CSS transition, the skill does not require an extra component library.

<a name="chinese-version"></a>

## 中文版

此 skill 为网页选择一个合适的动效方案或现成组件。它先检查项目技术栈和已有设计体系；只有确实需要现成组件时，才读取[组件选型表](references/catalog.md)，降低日常调用的上下文开销。

选型表按产品控件、局部低调动效、营销展示、创意效果、付费 Motion UI 和滚动叙事区分适用场景、兼容性、风格与授权。表中判断不是实测性能排名；安装前仍需检查目标组件的当前文档和依赖。

调用示例：`$animated-component-picker 为现有 shadcn 对话框选择克制的动效`。Motion 官方 [AI Kit skill](https://motion.dev/docs/ai-kit-install) 是独立上游项目，本仓库只链接，不重新发布。
