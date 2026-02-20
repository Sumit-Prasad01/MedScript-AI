import os
from flask import Flask, render_template, request, session, redirect, url_for
from markupsafe import Markup
from app.components.retriever import create_qa_chain
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.secret_key = os.urandom(24)


def nl2br(value):
    return Markup(value.replace("\n"," <br>\n"))

app.jinja_env.filters['nl2br'] = nl2br


@app.route("/", methods = ["GET", "POST"])
def index():

    if "messages" not in session:
        session["messages"] = []

    if request.method == "POST":
        user_input = request.form.get("prompt")

        if user_input:
            messages = session["messages"]
            messages.append({"role" : "user", "content" : user_input})
            session["messages"] = messages

            try:
                print("Creating QA chain...")
                qa_chain = create_qa_chain()
                print("QA chain:", qa_chain)

                if qa_chain is None:
                    raise Exception("QA Chain is None")

                print("Invoking chain...")
                response = qa_chain.invoke({"query": user_input})
                print("RAW RESPONSE:", response)

                if isinstance(response, dict):
                    result = response.get("answer") or response.get("result") or str(response)
                else:
                    result = str(response)

                print("FINAL RESULT:", result)

                messages.append({"role": "assistant", "content": result})
                session["messages"] = messages

            except Exception as e:
                import traceback
                print("\n\n====== FULL ERROR ======")
                traceback.print_exc()
                print("========================\n\n")

                error_message = f"Error : {repr(e)}"
                return render_template("index.html", messages=session["messages"], error=error_message)
            
        return redirect(url_for("index"))

    return render_template("index.html", messages = session.get("messages", []))



@app.route("/clear")
def clear():

    session.pop("messages", None)

    return redirect(url_for("index"))


if __name__ == "__main__":

    app.run(host = "0.0.0.0", port = 5000, debug = False, use_reloader = False)