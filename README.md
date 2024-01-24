# Reddit_To_BigQuery_Airflow:
### Description:
Reddit_To_BigQuery_Airflow, a streamlined data pipeline that extracts valuable insights from Reddit using the Reddit API. Orchestrated by Apache Airflow, the process seamlessly uploads data to Google Cloud Storage, processes it with Dataproc, and deposits it into a BigQuery table. This automated workflow ensures efficient data analysis, making it easy to explore and leverage Reddit data at scale. Dive into the power of automation and scalability.

### Project Architecture:
![redshifttobigquery](https://github.com/AfzalAliSolangi/Reddit_To_BigQuery_Airflow/assets/100179604/d9c6f4da-6c47-450b-ab6e-f41b13d144c6)

### Services Used in Reddit_To_BigQuery_Airflow:

1. **Reddit API:**
   - Utilized for extracting valuable data and insights from the Reddit platform.

2. **Apache Airflow:**
   - Orchestrates the entire workflow, automating the extraction, processing, and storage of Reddit data.

3. **Google Cloud Storage:**
   - Serves as the initial repository for Reddit data before further processing in the pipeline.

4. **Google Cloud Dataproc:**
   - Employs Dataproc for efficient data processing, enhancing scalability, and executing complex tasks seamlessly.

5. **Google BigQuery:**
   - The final destination for processed data, enabling powerful and scalable analytics and insights.

### Steps to Set Up:
1. **Reddit API**
   - Create an application by visiting, https://www.reddit.com/prefs/apps.
   - Make sure to select script and fill other fields with you information.
     ![image](https://github.com/AfzalAliSolangi/Reddit_To_BigQuery_Airflow/assets/100179604/7b1c88e9-996d-4b78-a52c-70475dc72d03)
   - After clicking on create app button, the app will be created.
     ![image](https://github.com/AfzalAliSolangi/Reddit_To_BigQuery_Airflow/assets/100179604/66e76b4d-ca0b-47d8-909c-1b843a7360ae)
   - The app will give you CLIENT_ID and CLIENT_SECRET.
2. **Setting Python Files**
   - In *reddit_pipeline.py* put the CLIENT_ID and CLIENT_SECRET.
     ![image](https://github.com/AfzalAliSolangi/Reddit_To_BigQuery_Airflow/assets/100179604/203c7300-7968-46cc-95a2-2cc56e7d2d4a)
3. **Setting the DAG**
   - In *Reddit_dag.py*, fill the green fields with the respective configuration.
     ![image](https://github.com/AfzalAliSolangi/Reddit_To_BigQuery_Airflow/assets/100179604/d9444986-4ffd-4787-9438-4e52282586d6)
   - The DAG should look like this:
     ![image](https://github.com/AfzalAliSolangi/Reddit_To_BigQuery_Airflow/assets/100179604/e9506526-b52d-4af6-bac9-6b66c49efd51)



