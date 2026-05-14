import os

from flask import Flask, render_template, request
import markdown
from agents import generate_plan

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    goal = request.form.get("goal", "").strip()
    level = request.form.get("level", "beginner")

    if not goal:
        return render_template(
            "result.html",
            output="<p style='color:red'>Please enter a fitness goal.</p>"
        )

    try:
        # generate_plan now returns a plain string (no JSON wrapping needed)
        plan_text = generate_plan(goal, level)
    except ValueError as e:
        return render_template("result.html", output=f"<p style='color:red'>{e}</p>")
    except RuntimeError as e:
        return render_template("result.html", output=f"<p style='color:red'>{e}</p>")
    except Exception as e:
        return render_template(
            "result.html",
            output=f"<p style='color:red'>Unexpected error: {e}</p>"
        )

    # Convert Markdown → HTML for nice rendering
    formatted_output = markdown.markdown(plan_text)

    return render_template("result.html", output=formatted_output)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
