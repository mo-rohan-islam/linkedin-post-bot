# 🤖 AI-Powered LinkedIn Post Generator

This is a Streamlit application that uses **OpenRouter's LLaMA models** to generate high-quality LinkedIn posts from trending tech topics and publish them directly to LinkedIn via OAuth2 login.

---

## 🚀 Features

- 🔐 LinkedIn OAuth 2.0 Login
- 🧠 Generative AI via OpenRouter (LLaMA-3)
- ✍️ Unicode-formatted LinkedIn posts (bolds, styles)
- 🚀 One-click post to LinkedIn
- 📂 Postman collection for API testing

---

## 🧱 Project Structure

```text
linkedin-post-bot/
├── Login.py                  # Handles LinkedIn login & callback
├── pages/
│   └── App.py                # Main post generator UI
├── openrouter_api.py         # OpenRouter API integration (LLaMA models)
├── linkedin_api.py           # LinkedIn posting logic
├── linkedin_auth.py          # OAuth2 login flow
├── formatter.py              # Unicode formatting logic
├── exceptions.py             # Custom exception classes
├── logger.py                 # Logging setup
├── .env                      # Environment configuration (API keys, secrets)
├── .gitignore                # Git ignore rules
├── .streamlit/
│   └── config.toml           # Streamlit UI/theme config
├── etc/
│   └── postman/
│       └── linkedin-bot.postman_collection.json
├── pyproject.toml            # Python project dependencies (via uv)
├── product_roadmap.md        # Future plans and features
├── LICENSE                   # Project license
└── README.md                 # You're here!
```

---

## ⚙️ Configuration

### `.env` - Create and populate it with your API keys and secrets

```env
OPENROUTER_API_KEY=your_openrouter_api_key

LINKEDIN_CLIENT_ID=your_linkedin_client_id
LINKEDIN_CLIENT_SECRET=your_linkedin_client_secret
LINKEDIN_USER_URN=urn:li:person:abc123
LINKEDIN_REDIRECT_URI=http://localhost:8501     # Make sure this matches your LinkedIn app settings
```

> Make sure the redirect URI is **registered in your LinkedIn developer app** settings.

---

## 📦 Install & Run

### Install Dependencies (via `uv`)

```bash
uv pip install -r pyproject.toml
```

### Start the App

```bash
streamlit run Login.py
```

> 🔁 This starts the login screen first. After authentication, users are redirected to `pages/App.py`.

---

## ✨ How It Works

1. User logs in using LinkedIn OAuth2
2. App fetches an `access_token`
3. User lands on the post generator UI
4. Enters topic + context
5. Post is generated via OpenRouter LLaMA model
6. Formatted with Unicode bold/italic characters
7. Posted directly to LinkedIn with one click

---

## 🧪 API Testing

You can use the Postman collection:

```text
etc/postman/linkedIn-Post-Bot.postman_collection.json
```

> To simulate  Login flow

---

## 📈 Roadmap

See [`product_roadmap.md`](product_roadmap.md) for upcoming features and releases.

---

## ✅ To-Do (Planned Enhancements)

- [ ] Access token expiry handling
- [ ] Scheduled posting
- [ ] Prompt tone customization (e.g. Formal, Funny)

> Check the [Roadmap](#-roadmap) section for more details.

---

## 👨‍💻 Author

Built by [Rohan Islam](https://www.linkedin.com/in/rohanislam)  
🌱 Automating daily workflows with AI & cloud-first tools.

---

## 🛡 License

This project is licensed under the MIT License.
