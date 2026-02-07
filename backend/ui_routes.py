from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from backend.router.model_router import select_model
from backend.providers.openai_provider import call_openai
from backend.providers.mistral_provider import call_mistral
from backend.providers.ollama_provider import call_ollama
from backend.evaluation.evaluator import evaluate_response
from backend.cost.cost_calculator import estimate_cost
from backend.utils.latency import measure_latency

router = APIRouter()

templates = Jinja2Templates(directory="backend/templates")


# -----------------------------
# UI HOME PAGE
# -----------------------------
@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


# -----------------------------
# EXECUTION HANDLER
# -----------------------------
@router.post("/run", response_class=HTMLResponse)
def run_prompt(
    request: Request,
    prompt: str = Form(...),
    priority: str = Form("balanced"),
    benchmark: str = Form(None)
):

    benchmark_mode = benchmark == "on"

    if benchmark_mode:
        results = run_benchmark(prompt)

        best = max(results, key=lambda x: x["score"])

        return templates.TemplateResponse(
            "result.html",
            {
                "request": request,
                "selected_model": best["model"],
                "response": best["output"],
                "metrics": best,
                "benchmark_results": results,
                "benchmark": True
            }
        )

    model = select_model(prompt, priority)

    result = execute_model(model, prompt)

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "selected_model": result["model"],
            "response": result["output"],
            "metrics": result,
            "benchmark": False
        }
    )


# -----------------------------
# EXECUTION ENGINE
# -----------------------------
def execute_model(model, prompt):

    if model == "openai":
        (output, tokens), latency = measure_latency(call_openai, prompt)

    elif model == "mistral":
        (output, tokens), latency = measure_latency(call_mistral, prompt)

    else:
        (output, tokens), latency = measure_latency(call_ollama, prompt)

    cost = estimate_cost(model, tokens)
    score = evaluate_response(output)

    return {
        "model": model,
        "output": output,
        "latency": latency,
        "cost": cost,
        "score": score
    }


# -----------------------------
# BENCHMARK ENGINE
# -----------------------------
def run_benchmark(prompt):

    models = ["openai", "mistral", "ollama"]

    results = []

    for m in models:
        try:
            results.append(execute_model(m, prompt))
        except:
            pass

    return results
