from flask import Flask, render_template, redirect, request, session, url_for

app = Flask(__name__)
app.secret_key = "vynox_secret_key_change_me"

# Replace these with your actual Discord Application credentials from discord.com/developers
CLIENT_ID = "1551418931984732240"
CLIENT_SECRET = "i3klsFmGW3xMPzm8JioWqXEU8z22uDHC"
REDIRECT_URI = "http://127.0.0.1:5000/callback"

@app.route('/')
def home():
    # Check if user is logged in via session
    user = session.get('user')
    return render_template('index.html', user=user)

@app.route('/login')
def login():
    # Redirects to real Discord OAuth2 Login page
    discord_login_url = f"https://discord.com/api/oauth2/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope=identify+guilds"
    return redirect(discord_login_url)

@app.route('/callback')
def callback():
    # This handles the return from Discord after login
    code = request.args.get('code')
    if code:
        # Simulate a logged-in user profile for demonstration purposes
        # (In production, you would exchange this code for an access token via Discord API)
        session['user'] = {
            "username": "VyroxAdmin",
            "discriminator": "0001",
            "avatar": "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f916.png"
        }
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

@app.route('/invite')
def invite():
    # Discord Bot Invite Link with permissions (8 = Administrator, or choose specific music permissions)
    bot_invite_url = f"https://discord.com/oauth2/authorize?client_id={CLIENT_ID}&permissions=8&scope=bot+applications.commands"
    return redirect(bot_invite_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)