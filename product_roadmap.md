# 🛠 Product Roadmap & Backlog

This document outlines planned features, improvements, and future directions for the **AI-Powered LinkedIn Post Generator**.

---

## 📌 Backlog Tasks

### 🔐 Authentication & Session Management

1. **Persistent Access Token**
   - Store LinkedIn `access_token` in `.env` after the first login.
   - Reuse stored token if valid.
   - Fetch a new token automatically if expired.

2. **Dynamic LinkedIn User URN**
   - Replace the hardcoded `LINKEDIN_USER_URN` from `.env` with dynamic retrieval after successful login.
   - Make the app usable by any authenticated LinkedIn user.

---

### 🧱 Architecture & Refactoring

3. **Separate Frontend and Backend**
   - Decouple Streamlit frontend from backend logic.
   - Use a RESTful API (e.g., FastAPI or Flask) for communication.
   - Implement proper routing and remove Streamlit’s `pages/` structure.

4. **Service Bootstrap**
   - Create a shell script to start Streamlit, backend API server, DB, and any dependent services.

5. **Centralised Configuration**
   - Load all environment variables only once during app startup.

6. **Post Confirmation Step**
   - Before posting, prompt user with a preview and confirmation dialog.
   - Schedule the post for a specific time or allow immediate posting.

---

### 🧠 AI Enhancements

7. **Multimodal Post Generation**
   - Update the AI model and prompt structure to support image generation alongside text (e.g., via OpenRouter or Stability AI).

8. **Model Customization**
   - Let users choose the tone of the post (e.g., Formal, Friendly, Technical, Humorous) via UI dropdown.
   - Adjust the temperature, top_p, frequency_penalty, and other parameters to generate the optimal post style.

---

### 💾 Data Management

9. **Post History & Analytics**
   - Store all generated posts in a local or cloud database (e.g., SQLite, Supabase, Firebase).
   - Include metadata: topic, context, generation timestamp, and success/failure status.
   - Allow viewing previously generated posts in a dashboard.

---

## 🧪 Developer Notes

- When switching models (e.g., from LLaMA to multimodal), consider how image generation impacts token limits.
- LinkedIn posting might still fail even with a valid token due to static or mismatched `user_urn`. Analyze API limitations for fully dynamic posting.

---

## 🔮 Product Insight – Vision

Build an **automated AI system** to:

1. 🔍 Crawl the web daily for **trending tech topics** in CS, AI, and Software Engineering.
2. 🧠 Rank topics based on virality using a custom **ML model**.
3. 📝 Feed best topics into the current **AI post generator**.
4. 🕓 Schedule the pipeline to run **once daily**.
5. 🚀 Automatically post content on LinkedIn with high visibility and relevance.

---

✅ **Goal**: Deliver high-quality, automated, AI-generated technical content daily — with minimal human input.
