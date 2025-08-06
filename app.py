from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def redirect_to_store():
    user_agent = request.headers.get('User-Agent', '').lower()
    
    if 'iphone' in user_agent or 'ipad' in user_agent:
        return redirect("https://apps.apple.com")
    elif 'android' in user_agent:
        return redirect("https://play.google.com")
    else:
        return redirect("https://google.com")  # Fallback

@app.route("/health")  # Render necesita esto
def health_check():
    return "OK", 200
