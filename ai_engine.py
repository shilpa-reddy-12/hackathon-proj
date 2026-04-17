def ai_review(code, filename, past_failures=""):
    prompt = f"""
You are a strict senior reviewer.

ONLY return like:
Line <number>: <issue>

CODE:
{code}
"""
    return call_ai(prompt)
