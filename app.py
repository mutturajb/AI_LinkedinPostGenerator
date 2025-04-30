# app.py

import gradio as gr
from generator import generate_linkedin_post

with gr.Blocks(title="LinkedIn Post Generator") as demo:
    gr.Markdown("## 💼 LinkedIn Post Generator")
    gr.Markdown("Craft **professional, engaging**, and beautifully formatted LinkedIn posts with ease.")

    with gr.Tab("📝 Create Your Post"):
        with gr.Row():
            with gr.Column(scale=1):
                topic = gr.Textbox(
                    label="📌 Post Topic",
                    placeholder="e.g. Leadership, Remote Work, AI in Healthcare"
                )

                tone = gr.Dropdown(
                    label="🎯 Select Tone",
                    choices=[
                        "Professional", "Inspirational", "Casual",
                        "Analytical", "Humorous", "Empowering",
                        "Reflective", "Storytelling"
                    ],
                    value="Professional"
                )

                bullet_points = gr.Textbox(
                    label="🧠 Key Bullet Points (optional)",
                    lines=4,
                    placeholder="- Achieved 200% growth\n- Launched new product\n- Mentored 5 engineers"
                )

                beautify_toggle = gr.Checkbox(
                    label="✨ Beautify Post (add formatting & emojis)",
                    value=True
                )

                generate_btn = gr.Button("🚀 Generate Post")

            with gr.Column(scale=1):
                output = gr.Textbox(
                    label="✅ Generated LinkedIn Post",
                    lines=18,
                    placeholder="Your post will appear here...",
                    show_copy_button=True
                )

        generate_btn.click(
            fn=generate_linkedin_post,
            inputs=[topic, tone, bullet_points, beautify_toggle],
            outputs=output
        )

    with gr.Tab("ℹ️ About"):
        gr.Markdown("""
        ### 👋 Welcome!
        This tool helps you create impactful LinkedIn posts by:
        - ✍️ Accepting a topic and tone
        - 🔍 Optional bullet points or ideas
        - ✨ Optionally beautifying the text with emojis and formatting

        Built using:
        - 🧠 OpenAI GPT-4
        - 🖼️ Gradio UI
        - 🔐 `.env` secured API access
        """)

demo.launch()
