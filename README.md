# 🧠 Multi-LLM Routing Platform

A production-grade orchestration platform that dynamically routes user prompts across multiple Large Language Models (LLMs) based on prompt complexity, priority, cost, and performance — with benchmarking, evaluation scoring, and real-time UI visualization.

---

## 🚀 Live System Capabilities

* 🔀 Intelligent prompt routing
* 🧭 Priority-aware model selection
* 🧪 Multi-model benchmark execution
* 📊 Cost vs latency comparison
* 🧮 Response quality evaluation
* 🛟 Automatic fallback handling
* ⚡ Streaming response rendering
* 🖥️ FastAPI dashboard UI
* 🧩 Local + API model orchestration

---

## 🏗️ Architecture Overview

```
User Prompt
     ↓
FastAPI UI Layer
     ↓
Routing Engine
     ↓
Model Selection Logic
     ↓
LLM Execution Layer
   ↙        ↓        ↘
OpenAI   Mistral   Ollama (Local)
     ↓
Evaluation Engine
     ↓
Cost + Latency Metrics
     ↓
Benchmark Comparator
     ↓
Streaming Dashboard Output
```

---

## 🧠 Routing Intelligence

The router selects the optimal model based on:

| Factor              | Description                |
| ------------------- | -------------------------- |
| Prompt complexity   | Coding vs general queries  |
| Priority mode       | Quality / Speed / Balanced |
| Latency sensitivity | Faster model routing       |
| Cost awareness      | Token pricing              |
| Benchmark toggle    | Multi-model execution      |

---

## 🎯 Priority Modes

| Mode         | Behavior                                    |
| ------------ | ------------------------------------------- |
| **Quality**  | Routes to highest reasoning model (OpenAI)  |
| **Speed**    | Routes to fastest inference model (Mistral) |
| **Balanced** | Smart heuristic routing                     |

---

## 🤖 Supported Models

### Cloud Providers

* OpenAI (GPT-4o)
* Mistral Large

### Local Models (via Ollama)

* LLaMA3
* Mistral
* Phi

Hybrid orchestration supported.

---

## 📊 Benchmark Mode

Executes all models in parallel and compares:

| Metric  | Measured         |
| ------- | ---------------- |
| Latency | Execution time   |
| Cost    | Token pricing    |
| Score   | Response quality |
| Output  | Model answer     |

Best model selected automatically.

---

## 🧮 Evaluation Engine

Responses are scored heuristically on:

* Length adequacy
* Structural completeness
* Code presence
* Clarity indicators

Score range:

```
0 → 10
```

Used for benchmark ranking & fallback triggers.

---

## 🛟 Fallback Logic

If a model:

* Fails execution
* Times out
* Produces low score

System falls back:

```
OpenAI → Mistral → Ollama
```

Ensures reliability.

---

## 🖥️ UI Dashboard Features

* Prompt playground
* Priority selector
* Benchmark toggle
* Streaming response rendering
* Model selection badge
* Cost / latency / score tiles
* Benchmark comparison table
* Cost vs latency chart

Server-rendered via FastAPI + Jinja.

---

## 📁 Project Structure

```
backend/
│
├── main.py                # FastAPI entrypoint
├── ui_routes.py           # UI + execution routes
├── config.py              # Environment config
│
├── router/
│   └── model_router.py
│
├── providers/
│   ├── openai_provider.py
│   ├── mistral_provider.py
│   └── ollama_provider.py
│
├── evaluation/
│   └── evaluator.py
│
├── cost/
│   └── cost_calculator.py
│
├── fallback/
│   └── fallback_engine.py
│
├── utils/
│   └── latency.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    ├── styles.css
    └── icons/
```

---

## ⚙️ Installation

```bash
git clone https://github.com/nishithraj14/multi-llm-routing-platform.git
cd multi-llm-routing-platform

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create `.env`:

```
OPENAI_API_KEY=your_key
MISTRAL_API_KEY=your_key
OLLAMA_BASE_URL=http://localhost:11434
```

---

## ▶️ Run Platform

```bash
uvicorn backend.main:app --reload
```

Open:

```
http://127.0.0.1:8000
```

---

## 🧪 Example Workflows

### Single Routing

Prompt → Routed to best model → Evaluated → Displayed

---

### Benchmark Execution

Prompt → All models run → Compared → Best selected

---

## 📊 Sample Metrics Output

| Model   | Latency | Cost    | Score |
| ------- | ------- | ------- | ----- |
| OpenAI  | 8.5s    | $0.0029 | 7     |
| Mistral | 4.1s    | $0.0012 | 6     |
| Ollama  | 111s    | $0.00   | 7     |

---

## 🛠️ Tech Stack

**Backend**

* FastAPI
* LiteLLM
* Python
* Requests

**LLM Providers**

* OpenAI API
* Mistral API
* Ollama Local

**UI**

* Jinja2 Templates
* Chart.js
* Streaming JS Renderer

---

## 📌 Use Cases

* Cost-aware LLM routing
* Multi-vendor orchestration
* Model benchmarking
* Latency optimization
* Prompt complexity classification

---

## 🧑‍💻 Author

**Nishith Raj**

AI Engineering • LLM Systems • Model Orchestration

GitHub:
[https://github.com/nishithraj14](https://github.com/nishithraj14)

---

## ⭐ Project Value

This project demonstrates:

* LLM infra orchestration design
* Multi-provider abstraction
* Evaluation pipelines
* Cost optimization routing
* Hybrid local + API inference
* Production UI exposure

---

## 📜 License

MIT License
