# 🎵 OvertureGPT

**The AI-Powered Geometry Dash Layout Critic.**
_Using Multimodal LLMs to judge Composition, Representation, and Player Movement in gameplay layouts._

---

## 🎮 What is this?

**OvertureGPT** is an AI that watches Geometry Dash layouts and gives harsh, honest feedback.

It doesn't just "look" at the screen—it **listens** to the music and watches the player's movement simultaneously. It can tell if your gameplay is too slow for a drop, if your clicks are off-sync, or if your structuring is unreadable.

**Why?** Because getting good feedback on a layout is hard. OvertureGPT gives you an instant second opinion based on competitive gameplay theory.

---

## ✨ Features

- **🔊 True Audio-Visual Sync:** It uses a specialized AI (Video-LLaMA 2) that can "hear" the beat and "see" the gameplay at the same time.
- **🌊 Intensity Matching:** Detects if you are using 1x speed during a dubstep drop (a major crime).
- **🤖 No Decoration Bias:** It ignores art and effects, focusing 100% on the raw layout.
- **📄 Theory-Driven:** Critiques are based on real principles of gameplay theory and layout design.

---

## 🛠️ How it Works

OvertureGPT is a **Multimodal RAG (Retrieval-Augmented Generation) Pipeline** running on a quantized Large Language Model.

### The Stack

- **Model:** `Video-LLaMA 2.1 (7B-AV)`
- **Architecture:** Qwen-2.5 Backbone + ImageBind (Audio Encoder) + SigLIP (Visual Encoder).
- **Optimization:** 8-bit quantization (BNB) to run on T4 GPUs (Colab Free Tier).
- **Input:** Raw `.mp4` video files (processed as interleaved audio/visual tokens).

### The Pipeline

1.  **Ingestion:** The user uploads a layout video.
2.  **Perception:** The `ImageBind` encoder extracts audio spectrograms, while `SigLIP` extracts visual frames.
3.  **Binding:** These modalities are projected into a shared latent space (the AI "connects" the sound of a beat to the visual of a jump).
4.  **Inference:** The LLM applies "Gameplay Theory" rules to the multimodal context to generate a critique.

---

## 🚀 Quick Start

You don't need a powerful PC. The AI runs on Google's cloud.

1.  Open the [Colab Notebook](YOUR_COLAB_LINK_HERE).
2.  Run the **Setup** cells to install the AI.
3.  Upload your layout video (`layout.mp4`).
4.  Run the **Critique** cell and get roasted.

---

## ⚠️ Limitations

- **Short Clips Only:** Currently optimized for 10-30 second clips (due to context window limits).
- **Lyric Deafness:** It hears _energy_ and _beats_, but it cannot transcribe lyrics.
- **Hallucinations:** Occasionally, it might invent "blind jumps" that aren't there. It's an assistant, not a god.

---

_Built with ❤️ by ATXM._
