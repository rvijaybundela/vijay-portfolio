from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def portfolio():
    data = {
        "name": "Vijay Bundela",
        "title": "Agentic AI & ML Engineer",
        "profile_image": "https://ui-avatars.com/api/?name=Vijay+Bundela&background=10b981&color=fff&size=150", 
        "profile_overview": "AI/ML Developer specializing in building, deploying, and scaling functional AI applications and automated workflows. Proven expertise in integrating Large Language Models (LLMs) such as Gemini and GPT to drive operational efficiency. Proficient in Python, cloud environments (GCP), and MLOps methodologies.",
        "links": [
            {"url": "mailto:ranvjbundela48@gmail.com", "icon": "fas fa-envelope"},
            {"url": "https://www.linkedin.com/in/rvjbundela", "icon": "fab fa-linkedin"},
            {"url": "https://github.com/rvijaybundela", "icon": "fab fa-github"}
        ],
        "experience": [
            {
                "title": "Data Science Intern",
                "company": "Cognifyz Technologies (Remote)",
                "duration": "2 months",
                "details": [
                    "Streamlined data preprocessing by architecting ETL pipelines using Pandas and NumPy, reducing data preparation time for large-scale datasets by 30%.",
                    "Optimized predictive model performance through advanced feature engineering and automated hyperparameter tuning in Scikit-learn, achieving a 15% improvement in accuracy.",
                    "Applied data science tools and operations for project workflows and implemented ML models within defined timelines."
                ]
            },
            {
                "title": "Flutter Development (Internship & Self-initiated)",
                "company": "Digiblinkit & Independent",
                "duration": "3 months",
                "details": [
                    "Built IoT-based app for sensor data capture and analysis.",
                    "Contributed to Digiblinkit internship developing basic mobile applications and UI components."
                ]
            },
            {
                "title": "Freelancing & Projects",
                "company": "Independent Consultant",
                "duration": "Various",
                "details": [
                    "Designed and deployed a location tagging solution for the Maharashtra Government.",
                    "Developed a fitness tracking app with real-time monitoring and e-book website integration."
                ]
            }
        ],
        "skills": {
            "Programming": ["Python", "NumPy", "Pandas"],
            "Gen AI & Agentic AI": ["LangChain", "LangGraph", "AutoGPT", "CrewAI", "Prompt Engineering", "LLM Integration"],
            "ML/AI": ["Scikit-Learn", "TensorFlow", "PyTorch"],
            "Databases": ["MySQL/SQL", "Chroma DB", "Pinecone", "PostgreSQL"],
            "Visualization": ["Seaborn", "Matplotlib", "Power BI"],
            "Tools & Cloud": ["FastAPI", "ETL", "GCP", "Docker", "Git/GitHub"]
        },
        "projects": [
            {
                "title": "Automated Admissions Enquiry System",
                "desc": "Automated lead management system using Google Apps Script processing 5,000+ monthly records. Utilized Gemini API for automated emails and real-time report generation, improving conversion speed by 60%.",
                "link": "https://github.com/rvijaybundela/admissions-system",
                "github": "https://github.com/rvijaybundela/admissions-system"
            },
            {
                "title": "Conversational AI Support Bot",
                "desc": "Created a text-response chatbot to answer queries using foundational AI model integration, reducing support ticket volume by an estimated 40% and enhancing knowledge retrieval.",
                "link": "https://github.com/rvijaybundela/ai-support-bot",
                "github": "https://github.com/rvijaybundela/ai-support-bot"
            },
            {
                "title": "Fitness Tracking Application",
                "desc": "Developed a comprehensive mobile application featuring real-time health metric monitoring and seamless integration with external e-book platforms.",
                "link": "https://github.com/rvijaybundela/fitness-tracker",
                "github": "https://github.com/rvijaybundela/fitness-tracker"
            }
        ]
    }
    return render_template('index.html', user=data)

if __name__ == '__main__':
    app.run(debug=True)