****___AI Cost Optimizer — Real-Time Cloud Cost Monitoring using AI & DevOps___****

***Overview***

The AI-Powered Cloud Cost Predictor and Optimizer is a Streamlit-based application designed to help users analyze, predict, and optimize their cloud infrastructure costs.
It uses AI and data analytics to forecast expenses, detect anomalies, and suggest cost-saving actions for improved financial efficiency.
This project serves as a learning and practical demonstration of integrating AI + DevOps + Cloud cost management

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

***Key Features***


•**AI Forecasting:** Uses the Facebook Prophet time-series model to predict future AWS spending trends.

•**Anomaly Detection:** Automatically detects unusual spikes in cloud costs using statistical analysis.

•**Optimization Suggestions:** Provides actionable cost-saving recommendations based on usage data.

•**Email Alerts:** Sends automated alerts when cost anomalies are detected.

•**Interactive Dashboard:** Displays visual insights using Streamlit and Plotly.

•**Mock Data Support:** Can run without connecting to AWS using a sample dataset for testing.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

***TECH STACK***

| Layer                   | Tools / Technologies               |
| ----------------------- | ---------------------------------- |
| **Frontend**            | Streamlit, Plotly, Matplotlib      |
| **Backend / AI**        | Python, Prophet, Pandas            |
| **Automation / Alerts** | SMTP (Email), Custom alert scripts |
| **Data Handling**       | CSV files (AWS mock data)          |
| **Version Control**     | Git & GitHub                       |




****AI Usage***


**AI is utilized in two main areas of this project:**

**Predictive Analysis (Prophet Model):**

The Prophet model learns from historical billing data to predict future costs for the next 7–30 days.

This allows early detection of potential overages and improved budget planning.

**Anomaly Detection:**

AI-based anomaly detection identifies abnormal cost spikes or spending patterns using statistical z-score analysis.

When an anomaly is detected, the system triggers an automated email alert to notify the user.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

***INSTALLATION***


***Step 1*: Clone the repository**

git clone https://github.com/<your-username>/ai-cost-optimizer.git
cd ai-cost-optimizer


***Step 2*: Install dependencies**

pip install -r requirements.txt


***Step 3*: Configure environment variables**
Create a .env file in the project root:

•AWS_ACCESS_KEY_ID=your_access_key
•AWS_SECRET_ACCESS_KEY=your_secret_key
•AWS_REGION=us-east-1
•EMAIL_ADDRESS=your_email@gmail.com
•EMAIL_PASSWORD=your_app_password


**Run the Dashboard**

To start the dashboard, run

streamlit run app/dashboard.py

Then open the displayed URL in your browser, typically:

http://localhost:8501

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Automate Daily Alerts**

Set up a cron job for automatic daily cost monitoring and alerts:

*crontab -e*

**Add this line:**

0 9 * * * /usr/bin/python3 /home/vicky/ai-cost-optimizer/daily_monitor.py >> /home/vicky/ai-cost-optimizer/logs.txt 2>&1

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Folder Structure**

ai-cost-optimizer/
│
├── app/
│   ├── dashboard.py              # Main Streamlit application
│   ├── cost_predictor.py         # AI forecasting logic
│   ├── anomaly_detector.py       # Anomaly detection module
│   ├── optimizer.py              # Cost optimization recommendations
│   ├── email_alert.py            # Email alert function
│   └── data/
│       └── aws_billing_mock.csv  # Sample cost data
│
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
└── .gitignore                    # Git ignore rules

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Example Alert Message**


•Subject: Cost Spike Detected

•Body:

•Date: 2025-11-05

•Current Cost: ₹423.00

•Expected Cost: ₹220.00

•Anomaly: +92%


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


****File Descriptions****


| File                     | Description                                                                               |
| ------------------------ | ----------------------------------------------------------------------------------------- |
| **dashboard.py**         | The main Streamlit dashboard integrating AI models, anomaly detection, and visualization. |
| **cost_predictor.py**    | Implements Prophet-based time-series forecasting.                                         |
| **optimizer.py**         | Suggests cost-saving measures based on usage trends.                                      |
| **anomaly_detector.py**  | Detects and flags unusual cost fluctuations.                                              |
| **email_alert.py**       | Handles automated email notifications for cost alerts.                                    |
| **aws_billing_mock.csv** | Example dataset used for local testing and AI training.                                   |


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

***RESULTS AND FUTURE IMPROVEMENTS***


***Results***

•Understanding of AI in cost optimization using Prophet.

•Exposure to Streamlit for interactive data visualization.

•Hands-on experience in Python-based DevOps automation.

•Implementation of alerting mechanisms for anomaly detection.

•Knowledge of integrating AI models into dashboards.


***Future Improvements***

•Integration with AWS Cost Explorer API for real-time data.

•Adding multi-cloud cost comparison (AWS, Azure, GCP).

•Deploying the Streamlit app using Docker + GitHub Actions + AWS ECS.

•Enhancing email automation with scheduled reports.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

***Author***

**Developed by:** Vignesh V
**Role:** AI + DevOps Enthusiast
**Focus Areas:** Streamlit, Prophet AI, Cloud Cost Management, DevOps Automation.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

***License***

This project is licensed under the MIT License.
You are free to use, modify, and distribute it for educational or non-commercial purposes.


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


