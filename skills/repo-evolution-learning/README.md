# Repo Evolution Learning

[English](#english) | [中文版](#chinese-version)

<a name="english"></a>

Learn an existing repository by connecting its **current architecture** to the changes that shaped it. The output is a staged reading path with commit-linked explanations and short exercises, rather than a chronological list of every diff.

## Choose a lens

| Lens | Main question |
| --- | --- |
| Architecture evolution | How did the system's modules and interfaces change? |
| Feature evolution | How did one feature or code path develop, including fixes and replacements? |
| Own-project lessons | What did our iterations teach us, and which conclusions are supported by evidence? |

The lenses can be combined. The learner's starting knowledge determines the order and depth of lessons.

## Workflow and files

1. Inventory the accessible scoped Git history, including relevant refs and visibility limits.
2. Use commit metadata to identify candidate changes, then inspect decisive patches, code, tests, logs, and later reversions.
3. Map prior behavior → problem or goal → change → observed outcome or unknown → later fate.
4. Teach prerequisites first, then exact code paths and historical decisions. Add an exercise and self-check for each key lesson.

[SKILL.md](SKILL.md) contains the agent workflow. [Learning-output guide](references/learning-output.md) gives a report structure. [history_index.py](scripts/history_index.py) is an optional, read-only metadata index:

```sh
python3 skills/repo-evolution-learning/scripts/history_index.py \
  --repo /absolute/path/to/repo --path trainer --max-candidates 30
```

The script needs Python 3 and Git. It does not fetch missing history or inspect patch meaning. Its ranking is a search aid, not evidence that a commit improved quality. To save the complete index, pass `--json-out` with a path **outside** the analyzed repository.

## Use

Install through the [collection instructions](../../README.md#install-and-use), then ask:

```text
$repo-evolution-learning
I am new to this repository. Give me a five-minute architecture map, then
trace the key changes behind the training pipeline. Link each claim to code
or commits, separate observations from inferences, and teach me the
prerequisites in the fastest useful order with short exercises.
```

Use [Software History Lessons](../software-history-lessons/README.md) when the primary goal is a full engineering retrospective or transferring lessons to another product. This skill focuses on helping someone learn the repository.

## Limits

Commit messages alone cannot establish motivation or performance. Shallow clones, missing branches, unavailable experiments, and unverified tests limit conclusions. The entrypoint passed the local skill validator; the index was checked on a small synthetic repository and a shallow local repository. Learning quality has not been benchmarked.

---

<a name="chinese-version"></a>

## 中文版

[返回英文版](#english)

沿着**当前架构与真实提交历史**学习一个仓库，得到按基础到细节排序的阅读路径、带提交依据的解释和短练习，而不是逐条罗列 Diff。

### 三种学习视角

| 视角 | 核心问题 |
| --- | --- |
| 架构演进 | 模块与接口是怎样逐步改变的？ |
| 功能演进 | 某个功能经历了哪些引入、修复、替换和回退？ |
| 自己项目的经验 | 每轮迭代教会了我们什么，哪些结论有证据？ |

可以组合视角，并根据学习者已有知识安排顺序。

### 工作方式与文件

先清点可访问的 Git 历史，再用元数据寻找候选提交；只细读关键补丁，并结合代码、测试、日志及后续变更核对结论。最终按“原行为 → 问题或目标 → 修改 → 已观察结果或未知 → 后续变化”梳理，再组织成先修知识、代码阅读和练习。

[SKILL.md](SKILL.md) 定义执行流程；[输出结构](references/learning-output.md) 用于较长的学习报告；[history_index.py](scripts/history_index.py) 是可选的只读 Git 元数据索引。运行命令见上方。它需要 Python 3 和 Git，不会补全缺失历史，也无法仅凭提交信息证明优化效果。需要保存完整索引时，将 `--json-out` 指向被分析仓库以外的位置。

### 调用示例

```text
$repo-evolution-learning
我刚接触这个仓库。先给我五分钟的整体架构图，再追踪训练流程的
关键变更。重要结论请链接到代码或提交，区分观察和推断，并按照
最快上手的顺序安排先修知识、阅读位置和短练习。
```

如需完整工程复盘或将经验迁移到其他产品，可使用 [Software History Lessons](../software-history-lessons/README.md)。本 skill 的重点是帮助学习者理解当前仓库。

### 能力边界

提交说明不能单独证明动机或性能；浅克隆、缺失分支或无法取得的实验会限制结论。入口文件已通过本地验证器，索引脚本在临时仓库和浅克隆仓库上完成基础检查；学习效果尚未经过基准测试。
