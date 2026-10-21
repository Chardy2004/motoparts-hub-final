import json
from html import escape
from pyscript import document, when
from js import localStorage

feedback = json.loads(localStorage.getItem("feedback") or "[]")


def render_list():
    if feedback:
        document.querySelector("#list").innerHTML = "".join(
            f'<div class="row" style="display:block"><b>{escape(f["name"])}</b> '
            f'<span class="tag">({escape(f["interest"])}, wants: {escape(f["wish"])})</span>'
            f'<br>{escape(f["message"])}</div>'
            for f in reversed(feedback[-5:])
        )


@when("input", "#message")         # live character counter
def on_typing(event):
    left = 200 - len(document.querySelector("#message").value)
    document.querySelector("#counter").innerText = f"{left} characters left"


@when("submit", "#feedback")       # form submission
def on_submit(event):
    event.preventDefault()
    name = document.querySelector("#name").value.strip()
    message = document.querySelector("#message").value.strip()
    out = document.querySelector("#form-msg")
    if not name or not message:
        out.innerText = "Please fill in your name and message."
        return
    feedback.append({
        "name": name,
        "interest": document.querySelector("#interest").value,
        "wish": document.querySelector("#wish").value,
        "message": message,
    })
    localStorage.setItem("feedback", json.dumps(feedback))
    document.querySelector("#feedback").reset()
    document.querySelector("#counter").innerText = "200 characters left"
    out.innerText = f"Thanks, {name}! Your feedback was saved."
    render_list()


@when("click", "#clear-fb")        # clear all saved feedback
def on_clear_feedback(event):
    feedback.clear()
    localStorage.setItem("feedback", json.dumps(feedback))
    document.querySelector("#list").innerHTML = '<p class="mute">No feedback yet.</p>'
    document.querySelector("#form-msg").innerText = "Feedback cleared."


render_list()
