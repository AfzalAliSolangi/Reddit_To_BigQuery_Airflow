### Reddit_To_BigQuery_Airflow

## Description:
Reddit_To_BigQuery_Airflow, a streamlined data pipeline that extracts valuable insights from any subreddit of the Reddit using the Reddit API. Orchestrated by Apache Airflow, the process seamlessly uploads data to Google Cloud Storage, processes it with Dataproc, deposits it into a BigQuery table, and destory all the resouces created in GCP in the end after the process is completed. This automated workflow ensures efficient data analysis, making it easy to explore and leverage Reddit data at scale.

## Project Architecture:
![redshifttobigquery](https://github.com/AfzalAliSolangi/Reddit_To_BigQuery_Airflow/assets/100179604/d9c6f4da-6c47-450b-ab6e-f41b13d144c6)

## Services Used in Reddit_To_BigQuery_Airflow:

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

## Steps to Set Up:
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
4. **Creating Table in the BigQuery**
   - In your desired dataset create the Table using create table script from from *Create_Table.txt*.
     ![image](https://github.com/AfzalAliSolangi/Reddit_To_BigQuery_Airflow/assets/100179604/625d34f1-15f8-4d83-90ae-79570ebfe89c)
     
## Running The ETL:
   - Manually trigger the *etl_reddit_pipeline* or configure it to trigger at desired time.
     ![image](https://github.com/AfzalAliSolangi/Reddit_To_BigQuery_Airflow/assets/100179604/35f7303d-80da-4e9e-a570-30ec262bf58f)
   - After execution the result DAG graph should look like this:
     ![image](https://github.com/AfzalAliSolangi/Reddit_To_BigQuery_Airflow/assets/100179604/f2b08bd5-9088-4c72-b9ff-969055d5cd75)
   - The DAG is capable of uploading the file from local Ubuntu WSL to the cloud storage, the airflow sensor checks if the file is exists in the bucket. Then the DataProc cluster is creaeted dynamically in the GCP using airflow, after the reddit file from the bucket is processed and the data is inserted into the BigQuery table, all the resources created for this ETL task are destroyed dynamically.
     
## Result:
   - After the ETL is completed the Table gets populated with the entries, verfiy it by querying on the Reddit4 table in the BigQuery.
     ![image](https://github.com/AfzalAliSolangi/Reddit_To_BigQuery_Airflow/assets/100179604/68194750-3c5e-4c93-8db4-2f368db80d7f)

## Usage:
   - I have used r/GTA6 subrettid for this project. It can be used for any subreddit to extract out all the posts of a single day. Further the data can be explored within the BigQuery or using tools like Tableau or PowerBI to build interactive dashboard.



     


