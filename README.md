****___AI Cost Optimizer — Real-Time Cloud Cost Monitoring using AI & DevOps___****

***Overview***

AI Cost Optimizer is an intelligent DevOps monitoring project that uses machine learning and AWS integration to automatically track, predict, and optimize cloud costs in real time.
Built using Python, Streamlit, AWS SDK (boto3), and Prophet, it provides proactive alerts for cost anomalies and daily cost summaries through automated email notifications.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

***Features***

•Fetches real-time AWS billing data

•AI-powered cost prediction using Prophet

•Detects abnormal cost spikes with anomaly detection

•Sends automated email alerts for high spending

•Interactive Streamlit dashboard for cost visualization

•Automated daily monitoring using cron jobs

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

***TECH STACK***

**Programming Language:** Python 3.10+

**Framework:** Streamlit

**Cloud SDK:** AWS boto3

**Forecasting Library:** Prophet

**Data Handling**: Pandas, Matplotlib

**Automation:** Cron jobs

**Email Service:** SMTP (Gmail App Password)

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

│   ├── dashboard.py

│   ├── email_alert.py

│
├── data/

│   └── aws_billing_mock.csv

│
├── fetch_aws_cost.py

├── daily_monitor.py

├── anomaly_detector.py

├── cost_predictor.py

├── optimizer.py

├── requirements.txt

└── README.md

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Example Alert Message**


•Subject: Cost Spike Detected

•Body:

•Date: 2025-11-05

•Current Cost: ₹423.00

•Expected Cost: ₹220.00

•Anomaly: +92%


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------



***RESULTS AND FUTURE IMPROVEMENTS***


***Results***

•Successfully visualized real AWS cost trends and predictions

•Detected anomalies automatically using AI forecasting

•Sent email alerts for real-time cost monitoring

•Provided optimization suggestions using pattern analysis


***Future Improvements***

•Integrate Slack or Teams alerts for real-time updates.

•Add multi-cloud support (AWS, Azure, GCP).

•Containerize with Docker and deploy via GitHub Actions.

•Extend service-level cost breakdowns.

•Build AI-driven budget recommendation engine.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

***Author***

Vignesh Vellaidurai,

AI & DevOps Enthusiast,

Building intelligent automation for cloud cost optimization and monitoring.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


