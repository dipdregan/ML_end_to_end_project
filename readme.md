## House Price Prediction
```
python setup.py install
```
### upload file
```
git add .
git commit -m 'update'
git push origin main
```

#                                      `Coding flow for each and every stpes`

## 1.Data Ingetion
```
config.yaml(defineing data ingetion config in this file first)--

--> Constants(based on config file we will define some constant)--

-->entity(it's give the structure)
 
--> configration.py(we will use those entity in this file)--

--> data_ingetion.py(throgh this configration file we will perform data ingetion)-- 

--> pipeline(based on all the component we will run our pipeline)
```

## 2.Data Validation

```
config.yaml(defineing data validation config in this file first) --> Constants(based on config file we will define some constant) --> entity(it's provide the structure) --> configration.py(we will use those entity in this file) --> data_validation.py(throgh this configration file we will perform data validation) --> pipeline(based on all the component we will run our pipeline)
```

# `Project Structure`
# -------------------

```
Housing_project/
    ├── config/
    │   ├── config.yaml
    │   └── schema.yaml
    ├── jupyter_notebook/
    │   ├── EDA/
    │   │   ├── data_exploration.ipynb
    │   │   └── data_visualization.ipynb
    │   ├── feature_selection/
    │   │   └── feature_selection.ipynb
    │   ├── model_training/
    │   │   ├── model_training.ipynb
    │   │   └── hyperparameter_tuning.ipynb
    │   └── model_evaluation/
    │       ├── model_evaluation.ipynb
    │       └── model_comparison.ipynb
    ├── housing/
    │   ├── artifact/
    │   ├── components/
    │   │   ├── data_ingestion.py
    │   │   ├── data_transformation.py
    │   │   ├── data_validation.py
    │   │   ├── model_evaluation.py
    │   │   ├── model_pusher.py
    │   │   └── model_trainer.py
    │   ├── config/
    │   │   ├── __init__.py
    │   │   └── configuration.py
    │   ├── constant/
    │   │   ├── __init__.py
    │   │   └── constant.py
    │   ├── entity/
    │   │   ├── __init__.py
    │   │   ├── artifact_entity.py
    │   │   └── config_entity.py
    │   ├── exception/
    │   │   ├── __init__.py
    │   │   └── exception.py
    │   ├── logger/
    │   │   ├── __init__.py
    │   │   └── logging.py
    │   ├── pipeline/
    │   │   ├── __init__.py
    │   │   └── pipeline.py
    │   ├── utils/
    │   │   ├── __init__.py
    │   │   └── util.py
    │   └── __init__.py
    ├── logs/
    ├── .gitignore
    ├── Docker/
    ├── testing_files.py
    ├── init.sh
    ├── License
    ├── README.md
    ├── Requirements.txt
    ├── setup.py
    ├── main.py

```

## Step -1 Create the *Config.yaml* file
## -------------------------------------

### Why this this file are important 
#### ---------------------------------

The `config.yaml` file is used to store various configuration parameters for your ML project. It provides a centralized location to define and manage these parameters, making it easier to update and maintain your project.

In the provided `config.yaml` example, different sections are defined for different aspects of the ML pipeline:

- `training_pipeline_config`: Contains general configuration parameters for the training pipeline, such as the pipeline name and artifact directory.

- `data_ingestion_config`: Contains configuration parameters related to data ingestion, including the dataset download URL, directories for raw and ingested data, and train/test data splits.

- `data_validation_config`: Defines parameters for data validation, such as the directory for schema files, report filenames, and report output formats.

- `data_transformation_config`: Contains parameters for data transformation and preprocessing, including options for adding a feature, directories for transformed data, and filenames for preprocessed objects.

- `model_trainer_config`: Contains configuration parameters for model training, including the directory for trained models, the filename for the model file, and a base accuracy value.

- `model_evaluation_config`: Defines parameters for model evaluation, such as the filename for model evaluation results.

- `model_pusher_config`: Contains parameters for model deployment or pushing, including the directory for saved models.

By storing these configuration parameters in a `config.yaml` file, you can easily modify and update them without modifying your code. It also helps in maintaining consistency across different runs of your ML pipeline and allows for easy management of different configuration settings for different environments (e.g., development, production).

You can access these configuration parameters in your code by reading and parsing the `config.yaml` file using a YAML parsing library or framework, such as `PyYAML`. This allows you to dynamically load the configuration and use the values as needed throughout your project.

## Step-2 Create *config_entity*
## ----------------------------

### What is config_entity and why this is required for our Machine Learning Project
### -------------------------------------------------------------------------------

The `config_entity.py` file in an ML project is used to define named tuples or data classes that represent the structure of the configuration for different steps or components of the project. These entities provide a convenient and structured way to store and access the configuration parameters.

Here's an explanation of the purpose of each named tuple in the example provided:

- `DataIngestionConfig`: Represents the configuration parameters related to data ingestion, such as dataset download URL, directories for raw and ingested data, and train/test data directories.

- `DataValidationConfig`: Represents the configuration parameters for data validation, including the file paths for schema files, report files, and report pages.

- `DataTransformationConfig`: Represents the configuration parameters for data transformation, such as options for adding a feature, directories for transformed data, and file paths for preprocessed objects.

- `ModelTrainConfig`: Represents the configuration parameters for model training, including the file path for the trained model file and a base accuracy value.

- `ModelEvaluationConfig`: Represents the configuration parameters for model evaluation, including the file path for the model evaluation results and a timestamp.

- `ModelPusherConfig`: Represents the configuration parameters for model deployment or pushing, including the directory path for exporting the model.

- `TrainingPipelineConfig`: Represents the configuration parameters for the training pipeline, including the artifact directory.

By using named tuples or data classes, you can define the structure of these configuration entities once and use them throughout your codebase. This promotes code reusability, improves code readability, and makes it easier to pass and access configuration parameters in different parts of your ML project.

Additionally, using named tuples or data classes allows you to leverage the benefits of static typing and IDE autocompletion, making it easier to work with the configuration entities and reducing the chances of errors or inconsistencies in accessing configuration parameters.

## Step -3 Constant folder/__init__.py file
## -----------------------------------------

### Why it is required for our project
### ----------------------------------

The `constants folder` in an ML project is typically used to store constant values or configurations that
are used throughout the project. It helps centralize and organize such values in a single location for
easy access and maintenance.

## Step - 4 Config/configration.py
## ----------------------------------

### why we need this file
#### --------------------

The `configration.py` file is used in the ML project to provide a centralized configuration management system. It contains a `Configuartion` class that is responsible for reading the project configuration from a YAML file (`config.yaml`) and providing methods to retrieve specific configuration settings for different components of the project.

Here's a breakdown of the different components and their respective configuration retrieval methods:

1. **Data Ingestion Configuration**: The `get_data_ingestion_config` method retrieves the configuration settings for the data ingestion component. It reads the relevant section from the configuration file and constructs a `DataIngestionnConfig` object containing settings such as dataset download URL, download directories, and ingested data directories.

2. **Data Validation Configuration**: The `get_data_validation_config` method retrieves the configuration settings for the data validation component. It reads the relevant section from the configuration file and constructs a `DataValidationConfig` object containing settings such as schema file path, report file paths, and report page file paths.

3. **Data Transformation Configuration**: The `get_data_transformation_config` method is a placeholder and needs to be implemented to retrieve the configuration settings for the data transformation component. This method can be added similar to the other configuration retrieval methods.

4. **Model Trainer Configuration**: The `get_model_trainer_config` method is a placeholder and needs to be implemented to retrieve the configuration settings for the model trainer component. This method can be added similar to the other configuration retrieval methods.

5. **Model Evaluation Configuration**: The `get_model_evaluation_config` method is a placeholder and needs to be implemented to retrieve the configuration settings for the model evaluation component. This method can be added similar to the other configuration retrieval methods.

6. **Model Pusher Configuration**: The `get_model_pusher_config` method is a placeholder and needs to be implemented to retrieve the configuration settings for the model pusher component. This method can be added similar to the other configuration retrieval methods.

7. **Training Pipeline Configuration**: The `get_training_pipeline_config` method retrieves the configuration settings for the training pipeline. It reads the relevant section from the configuration file and constructs a `TrainingPipelineConfig` object containing settings such as the artifact directory.

The `Configuartion` class also includes an `__init__` method that initializes the configuration object by reading the YAML file and storing it in the `config_info` attribute. It sets the `training_pipeline_config` attribute by calling the `get_training_pipeline_config` method and sets the `time_stamp` attribute with the current timestamp.

Overall, the purpose of the `configration.py` file is to provide a structured and centralized way to access and retrieve configuration settings for different components of the ML project. It helps in managing and organizing the configuration, making it easier to modify and customize the project's behavior without changing the code.


## Step - 5 Components
## -------------------

### Why we are using this

The `components` folder in an ML project is typically used to store reusable components or modules that encapsulate specific functionalities or tasks. It helps in organizing the codebase and promoting modularity. Here are some reasons why the `components` folder is commonly used:

1. **Code Reusability**: ML projects often involve multiple tasks such as data preprocessing, feature engineering, model training, and evaluation. Each of these tasks can be implemented as separate components that can be reused across different projects or experiments. Placing these reusable components in the `components` folder allows easy access and promotes code reuse.

2. **Modularity**: ML projects can become complex, involving multiple steps and dependencies. Organizing the code into modular components makes it easier to understand, maintain, and test individual parts of the project. Each component can focus on a specific task, and the dependencies between components can be managed effectively.

3. **Encapsulation**: By encapsulating specific functionalities within components, the overall project structure becomes more organized and easier to navigate. Each component can have a well-defined purpose and encapsulate the necessary code, making it easier to understand and work with.

4. **Separation of Concerns**: Separating different parts of the ML pipeline into components allows for better separation of concerns. For example, you can have separate components for data preprocessing, model training, and evaluation. This separation makes it easier to modify or update specific parts of the pipeline without affecting other components.

5. **Testing and Debugging**: When components are designed with clear inputs and outputs, it becomes easier to test and debug them independently. You can create unit tests for each component and ensure that they work correctly before integrating them into the overall pipeline.

6. **Scalability**: ML projects often involve experimentation and iterative development. Having a modular structure with reusable components allows you to easily add, modify, or replace components as needed, making the project more scalable and adaptable to changes.


#### what are all the file inside the components
#### ---------------------------------------------

1. **Data Ingestion**: The `data_ingestion.py` component is responsible for downloading or accessing the raw data required for the ML project. It handles tasks such as data retrieval, data loading, and data preprocessing to prepare the data for further processing.

2. **Data Transformation**: The `data_transformation.py` component focuses on transforming the raw data into a suitable format for ML modeling. It may involve tasks such as feature engineering, data cleaning, normalization, scaling, or any other data preprocessing steps required to prepare the data for training a machine learning model.

3. **Data Validation**: The `data_validation.py` component performs data validation tasks to ensure the quality and integrity of the dataset. It checks for data consistency, completeness, and correctness based on predefined schema or validation rules. It may generate reports or metrics to identify any issues or anomalies in the dataset.

4. **Model Evaluation**: The `model_evaluation.py` component is responsible for evaluating the performance of the trained ML model. It calculates various evaluation metrics, such as accuracy, precision, recall, F1 score, etc., to assess how well the model performs on unseen data or a validation dataset. It helps in understanding the model's strengths and weaknesses and guides further model improvement.

5. **Model Pusher**: The `model_pusher.py` component handles the deployment or saving of the trained ML model for future use or integration with other systems. It exports or saves the trained model in a suitable format, such as pickle, TensorFlow SavedModel, ONNX, etc., to be consumed by other applications or services.

6. **Model Trainer**: The `model_trainer.py` component focuses on the training of the ML model using the prepared data. It defines the model architecture, trains the model on the training dataset, and optimizes the model's parameters based on a specified loss function and optimization algorithm. It may also include tasks such as model selection, hyperparameter tuning, and cross-validation.

These components represent the different stages or tasks within an ML pipeline, each with a specific purpose and functionality. By separating these tasks into individual components, you can achieve better code organization, modularity, reusability, and easier maintenance. It also allows you to test and modify each component independently, facilitating iterative development and experimentation in your ML project.

Overall, the `components` folder in an ML project promotes code organization, reusability, modularity, and separation of concerns. It helps in building robust and maintainable ML pipelines by encapsulating specific functionalities into reusable modules.
