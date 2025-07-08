# AI Trip Planner

**AI Trip Planner** is an intelligent travel assistant built using FastAPI. It leverages agentic workflows and large language models (LLMs) to generate personalized travel itineraries and visualize planning logic using graphs.


<img width="500" alt="trip 1 2" src="https://github.com/user-attachments/assets/07528e58-ec9c-4687-a2d9-9cbdaf4cd529" />
<img width="500" alt="trip 2" src="https://github.com/user-attachments/assets/42bdc925-430b-4aca-a17e-1a15a04b9d0e" />
<img width="500" alt="trip 3" src="https://github.com/user-attachments/assets/82746ec1-5107-4de2-b314-44d4b83bba38" />

---

## 🚀 Features

* **FastAPI Backend** – Lightweight, scalable API server.
* **Agentic Workflow** – Dynamically builds task execution graphs using `GraphBuilder`.
* **Graph Visualization** – Generates and saves a `.png` representation of the travel planning workflow.
* **Document Generation** – Supports saving results to documents.
* **Modular Codebase** – Organized into tools, agents, utils, and configuration modules.

---

## 🧩 Project Structure

```
ai_trip_planner/
│
├── main.py                     # Entry point for the FastAPI server
├── requirements.txt            # Python dependencies
├── pyproject.toml              # Project metadata and build info
├── .env                        # Environment variables
├── my_graph.png                # Auto-generated graph of the planning workflow
│
├── agent/
│   └── agentic_workflow.py     # Core logic for agent workflow and graph creation
│
├── tools/                      # External tools or helper functions used by agents
├── utils/
│   └── save_to_document.py     # Utilities to persist results
├── config/                     # Configuration files or helpers
├── exception/                  # Custom exception classes or handling
├── logger/                     # Logging utilities
├── notebook/                   # Jupyter notebooks for experimentation
├── prompt_library/             # Prompt templates and LLM interactions
│
├── ai_trip_planner.egg-info/   # Packaging info for installation (if needed)
├── __pycache__/                # Cached Python files
├── .gitignore                  # Git ignore rules
└── README.md                   # Project overview (this file)
```

---

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone <repo_url>
   cd ai_trip_planner
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   Create a `.env` file and populate necessary API keys or configuration:

   ```
   MODEL_PROVIDER=groq
   ```

4. **Run the server**

   ```bash
   uvicorn main:app --reload
   ```

---

## 📬 API Endpoint

### `POST /query`

Send a question or travel request.

**Request Body:**

```json
{
  "question": "Plan me a 7-day trip to Japan"
}
```

**Response:**

* Saves a visual `.png` graph of the task flow.
* Generates a structured plan using LLM-based reasoning.

---

## 🧠 Technologies Used

* **FastAPI** – Modern API framework
* **Python** – Main programming language
* **Pydantic** – Request validation
* **Dotenv** – Environment config
* **Custom Agent Framework** – For decision graph planning
* **Mermaid / Graphviz** – For visualizing graphs

---

## 🛠 Work Done

* Built a modular FastAPI backend.
* Integrated agentic planning logic via `GraphBuilder`.
* Enabled CORS for external frontend usage.
* Created support for visualizing planning logic.
* Structured project for future extensibility with tools, prompts, and notebooks.

---

## 📌 Future Enhancements

* Integrate a frontend interface (React or Streamlit).
* Add support for multiple model providers.
* Improve graph interpretation and explainability.
* Export plans as PDFs or calendar integrations.

