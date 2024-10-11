# Assetfind AI- IntelliTag & IntelliSearch Tool 
~ *Databricks Hackathon*


### Description
This project automates the identification and tagging of key product attributes using prompt engineering and keyword extraction. It integrates a GenAI-based search engine for image-to-image and text-to-image searches, leveraging Azure OpenAI/ Databricks LLMs and other Databricks capabilities. Databricks Unity Catalog is used to store and manage data, while scheduled jobs handle automated runs. The output is an interactive dashboard for seamless image uploads and attribute-based search.


### Table of Contents
1. [Folder Structure](#folder-structure)
2. [Technologies Used](#)
3. [Intellitag flow Diagram](#)
4. [IntelliSearch Flow Diagram](#)
5. [Databricks Workflows](#)
6. [Streamlit UI](#)


## 1. Folder Structure
Here is the structure of the project:

```plaintext
  <Affine IntelliTag-Search>/
  │
  ├── jobs/
  │   ├── demo - Embeddings_Indexing
  │   ├── demo - Intelli Tag
  │   ├── demo - Intellisearch
  │   └── requirements.txt
  │    
  ├── notebook/   
  │   ├── LLM Registry                       # External Hugging Face LLM Registry
  │   └── Evaluation_without_and_with_agent  # custom evaluation matrix defined
  │   
  ├── streamlit ui/  
  │   ├── Dockerfile
  │   ├── requirements.txt
  │   ├── app.py
  │   ├──.dockerignore
  │   ├── pages_call/
  │   │   ├── intellisearch_page.py.py
  │   │   ├── login_page.py
  │   │   ├── upload_page.py
  │   │   ├── user_add_page.py
  │   │   └── view_tags_page.py
  │   │
  │   ├── src/
  │   │   ├── data_load.py
  │   │   ├── databricks_job_run.py
  │       ├── databricks_sql_connector.py
  │       ├── login_call.py
  │       └── processing.py
  │
  ├── .gitignore
  └── README.md
```
--------------------------------------------
## 2. Technologies Used
1. **Azure Databricks**: 

      Offers a unified platform for processing, analyzing, and generating insights from data, while facilitating the seamless integration of LLM models and automated workflows.

2. **Databricks Unity Catalog**: 

      Provides a centralized governance layer to manage and secure data across Databricks, ensuring organized storage and retrieval of image attributes and search results.

3. **Databricks Delta Table Indexing**:

      Optimizes data retrieval by enabling faster querying and efficient access to large datasets, crucial for managing image metadata.

4. **Databricks Vector Search Endpoint**: 

      Powers high-performance similarity searches for image and text embeddings, enabling efficient search functionalities.

5. **Databricks Model Registry & Serving**: 

      Manages model tracking and deployment, ensuring seamless scaling and real-time or batch inference for machine learning models.

6. **Azure OpenAI**: 

      Provides large language models (LLMs) to generate product tags and perform text-to-image searches using prompt engineering, enabling intelligent and automated search capabilities.
   
7. **Azure Blob Storage**: 

      Stores product images and metadata efficiently, serving as a scalable and secure repository for the image data used in the project.

8. **Azure Key Vault**: 

      Azure Key Vault is a cloud service used to securely store and manage sensitive information like secrets, keys, and certificates for protecting access to applications and resources.


9. **Autogen Agent**: 
              
      An automation tool that streamlines the image tagging and search processes, reducing the need for manual intervention by continuously improving search and tagging results.

10. **GitHub**: 

      Used for version control and collaboration, hosting the project's codebase, ensuring continuous integration, and managing updates to the search engine and tagging framework.


11. **Streamlit**:
  
      Python-based framework used to develop the interactive dashboard, allowing users to upload images, perform keyword-based searches, and view results in real time.

------------------------------------------------------------------------
## 3. IntelliTag Flow Diagram


------------------------------------------------------------------
## 4. IntelliSearch Flow Diagram



-----------------------------------------------------------------
## 5. Databricks Workflows

### DAG Flow Overview

##### Overview

The DAG (Directed Acyclic Graph) represents the workflow for the AffineReviewSummarization project, orchestrating various tasks in a sequential and conditional manner to achieve specific data processing and model training objectives. This DAG runs daily on a schedule basis for batch processing.

##### Task Dependencies

Tasks within the DAG are organized based on dependencies, ensuring that certain tasks are executed only after their prerequisite tasks have completed successfully. The dependencies are defined using the depends_on attribute, specifying the task keys on which each task depends.

##### Task Execution Conditions

Some tasks in the DAG are executed conditionally based on the outcome of previous tasks or external conditions. Conditional execution logic is defined using the condition_task attribute, which compares a specific value or expression with the outcome of a preceding task.

##### Task Details

  Below is a detailed breakdown of the tasks within the DAG:




-------------------------------
####  Note

This documentation provides a comprehensive overview of the DAG flow within the Databricks workflow for Intellitag, keyword indexing, and uploaded images as well as Intellisearch. Understanding this flow is essential for effectively managing and optimizing task execution to achieve project objectives efficiently.

1. IntelliTag & Indexing of Tags/Images

![image](https://github.com/user-attachments/assets/1ff08e48-fe63-4afa-940a-397119dab861)

2. IntelliSearch

![image](https://github.com/user-attachments/assets/17d91db7-18d4-4780-a576-ae5e4def8326)


## 6. How to Run the Streamlit Application

1. Clone the Repository
  Run the following command to clone the repository:
  ```bash
  git clone https://github.com/sanket-affine/D-Bricks.git
  ```
2. Navigate to the Directory
  Change the directory to the streamlit_ui folder:
```bash
cd streamlit_ui
```
3. Install Requirements
  Install the required dependencies:
```bash
pip install -r requirements.txt
```
4. Run the Application
  Start the Streamlit application with the following command:
```bash
streamlit run app.py --global.developmentMode=false
```




