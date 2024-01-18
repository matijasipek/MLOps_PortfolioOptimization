---
layout: default
nav_exclude: true
---

# Exam template for 02476 Machine Learning Operations

This is the report template for the exam. Please only remove the text formatted as with three dashes in front and behind
like:

```--- question 1 fill here ---```

where you instead should add your answers. Any other changes may have unwanted consequences when your report is auto
generated in the end of the course. For questions where you are asked to include images, start by adding the image to
the `figures` subfolder (please only use `.png`, `.jpg` or `.jpeg`) and then add the following code in your answer:

```markdown
![my_image](figures/<image>.<extension>)
```

In addition to this markdown file, we also provide the `report.py` script that provides two utility functions:

Running:

```bash
python report.py html
```

will generate an `.html` page of your report. After deadline for answering this template, we will autoscrape
everything in this `reports` folder and then use this utility to generate an `.html` page that will be your serve
as your final handin.

Running

```bash
python report.py check
```

will check your answers in this template against the constrains listed for each question e.g. is your answer too
short, too long, have you included an image when asked to.

For both functions to work it is important that you do not rename anything. The script have two dependencies that can
be installed with `pip install click markdown`.

## Overall project checklist

The checklist is *exhaustic* which means that it includes everything that you could possible do on the project in
relation the curricilum in this course. Therefore, we do not expect at all that you have checked of all boxes at the
end of the project.

### Week 1

* [ ] Create a git repository
* [ ] Make sure that all team members have write access to the github repository
* [ ] Create a dedicated environment for you project to keep track of your packages
* [ ] Create the initial file structure using cookiecutter
* [ ] Fill out the `make_dataset.py` file such that it downloads whatever data you need and
* [ ] Add a model file and a training script and get that running
* [ ] Remember to fill out the `requirements.txt` file with whatever dependencies that you are using
* [ ] Remember to comply with good coding practices (`pep8`) while doing the project
* [ ] Do a bit of code typing and remember to document essential parts of your code
* [ ] Setup version control for your data or part of your data
* [ ] Construct one or multiple docker files for your code
* [ ] Build the docker files locally and make sure they work as intended
* [ ] Write one or multiple configurations files for your experiments
* [ ] Used Hydra to load the configurations and manage your hyperparameters
* [ ] When you have something that works somewhat, remember at some point to to some profiling and see if
      you can optimize your code
* [ ] Use Weights & Biases to log training progress and other important metrics/artifacts in your code. Additionally,
      consider running a hyperparameter optimization sweep.
* [ ] Use Pytorch-lightning (if applicable) to reduce the amount of boilerplate in your code

### Week 2

* [ ] Write unit tests related to the data part of your code
* [ ] Write unit tests related to model construction and or model training
* [ ] Calculate the coverage.
* [ ] Get some continuous integration running on the github repository
* [ ] Create a data storage in GCP Bucket for you data and preferable link this with your data version control setup
* [ ] Create a trigger workflow for automatically building your docker images
* [ ] Get your model training in GCP using either the Engine or Vertex AI
* [ ] Create a FastAPI application that can do inference using your model
* [ ] If applicable, consider deploying the model locally using torchserve
* [ ] Deploy your model in GCP using either Functions or Run as the backend

### Week 3

* [ ] Check how robust your model is towards data drifting
* [ ] Setup monitoring for the system telemetry of your deployed model
* [ ] Setup monitoring for the performance of your deployed model
* [ ] If applicable, play around with distributed data loading
* [ ] If applicable, play around with distributed model training
* [ ] Play around with quantization, compilation and pruning for you trained models to increase inference speed

### Additional

* [ ] Revisit your initial project description. Did the project turn out as you wanted?
* [ ] Make sure all group members have a understanding about all parts of the project
* [ ] Uploaded all your code to github

## Group information

### Question 1
> **Enter the group number you signed up on <learn.inside.dtu.dk>**
>
> Answer:

--- 11 ---

### Question 2
> **Enter the study number for each member in the group**
>
> Example:
>
> *sxxxx, sxxxxx, sxxxx*
>
> Answer:

--- s204704, s222736, s222660 ---

### Question 3
> **What framework did you choose to work with and did it help you complete the project?**
>
> Answer length: 100-200 words.
>
> Example:
> *We used the third-party framework ... in our project. We used functionality ... and functionality ... from the*
> *package to do ... and ... in our project*.
>
> Answer:

--- In this project we used skfolio, a Python library for portfolio optimization built on top of scikit-learn's API (https://github.com/skfolio/skfolio). The skfolio model was employed for validating the predictions and assessing portfolio performance, focusing on key metrics such as Sharpe Ratio, Conditional Value at Risk, and Calmar ratios. The framework significantly reduced the model setup and testing workload, allowing us to rely on its robust, community-tested methods. That was essential, given that the project was primarily focused on managing, deploying, and monitoring the machine learning models in a real-world operational context. ---

## Coding environment

> In the following section we are interested in learning more about you local development environment.

### Question 4

> **Explain how you managed dependencies in your project? Explain the process a new team member would have to go**
> **through to get an exact copy of your environment.**
>
> Answer length: 100-200 words
>
> Example:
> *We used ... for managing our dependencies. The list of dependencies was auto-generated using ... . To get a*
> *complete copy of our development environment, one would have to run the following commands*
>
> Answer:

--- The dependencies are managed through python3 pip for managing the required packages, and DVC for the data dependencies. The 'requirements.txt' file contains all the required packgages (and its versions) necessary to run the code, while the DVC dependencies files are stored in data.dvc and models.dvc. A new team member would need to set up the following:

- Clone the project's repository locally.
- Create a virtual environment via python3
- Activate the virtual environment (conda activate my_new_env)
- Install the dependencies listed in the project's requirements as 'pip install -r requirements.txt'.
- Pull the data from Google cloud by running 'dvc pull'. ---

### Question 5

> **We expect that you initialized your project using the cookiecutter template. Explain the overall structure of your**
> **code. Did you fill out every folder or only a subset?**
>
> Answer length: 100-200 words
>
> Example:
> *From the cookiecutter template we have filled out the ... , ... and ... folder. We have removed the ... folder*
> *because we did not use any ... in our project. We have added an ... folder that contains ... for running our*
> *experiments.*
> Answer:

--- The project is initialized using the cookiecutter template for MLOps, and follows standardized structure, where `data` folder is partitioned into `processed` for ready-to-use datasets and `raw` for untouched data. The `models` directory stores trained models and related serialization files, while the `notebooks` directory contains Jupyter notebooks for exploratory analysis and result visualization. The `src` folder was extensively used for all source code, including data processing, model training, and prediction scripts, while the `reports` directory holds generated analysis as HTML and figures for reporting. The `docs` and `dockerfiles` folders are not populated as documentation, and Dockerfiles were put in different locations.  ---

### Question 6

> **Did you implement any rules for code quality and format? Additionally, explain with your own words why these**
> **concepts matters in larger projects.**
>
> Answer length: 50-100 words.
>
> Answer:

--- For formatting, a Cookiecutter was implemented to ensure consistency across the codebase. Maintaining code quality and format is crucial in larger projects as it enhances readability, eases collaboration among team members, and improves overall efficiency in the development process. ---

## Version control

> In the following section we are interested in how version control was used in your project during development to
> corporate and increase the quality of your code.

### Question 7

> **How many tests did you implement and what are they testing in your code?**
>
> Answer length: 50-100 words.
>
> Example:
> *In total we have implemented X tests. Primarily we are testing ... and ... as these the most critical parts of our*
> *application but also ... .*
>
> Answer:

--- In total we created **13 tests**. They were separated into 3 sections : **dataset**, **model training**, and **prediction**. In the dataset
module we tested if the columns match the expected, if there are NaN values, is type pandas, is file empty and then repeated for both test
and train data. For the model: test if model is being initialized, if parameters are being tuned, is it able to read in the data and train, and are the models saved after training. Finally, the prediction tests: are the results and figures from predictions being saved. ---


### Question 8

> **What is the total code coverage (in percentage) of your code? If you code had an code coverage of 100% (or close**
> **to), would you still trust it to be error free? Explain you reasoning.**
>
> Answer length: 100-200 words.
>
> Example:
> *The total code coverage of code is X%, which includes all our source code. We are far from 100% coverage of our **
> *code and even if we were then...*
>
> Answer:
>
---  By using framework coverage, we are able to generate the full analysis of what is covered including all the libraries and packages; and, with that we have coverage of **27%** in total. However, when we look at the source files we have written we have coverage: `/model.py`  **100%**,
`src/predict_model.py` **84%**, `src/train_model.py` **64%** which is solid. If we had code coverage of **100%** we would still not believe it
is error free. This is because tests written can also not check everything in a mindful way, or the tests can themselves have errors.
Tests can miss edge cases since we are not able to think of all possibilities which can happen during run time.
Also, when running on cloud vs running locally can give different results due to different architectures. ---

### Question 9

> **Did you workflow include using branches and pull requests? If yes, explain how. If not, explain how branches and**
> **pull request can help improve version control.**
>
> Answer length: 100-200 words.
>
> Example:
> *We made use of both branches and PRs in our project. In our group, each member had an branch that they worked on in*
> *addition to the main branch. To merge code we ...*
>
> Answer:
> 
--- The use of branches and pull requests was integrated into our GitHub workflow. When a group member is making changes on his own, every change commenced with creating a branch from the main codebase, while in a situation when all the team members were working together when implementing changes, then there was not a need to create new branches and open pull requests. Subsequently, a pull requests for merging these modifications into the main branch were initiated. These pull requests underwent a review by other team members, ensuring code quality before final approval and integration. ---

### Question 10

> **Did you use DVC for managing data in your project? If yes, then how did it improve your project to have version**
> **control of your data. If no, explain a case where it would be beneficial to have version control of your data.**
>
> Answer length: 100-200 words.
>
> Example:
> *We did make use of DVC in the following way: ... . In the end it helped us in ... for controlling ... part of our*
> *pipeline*
>
> Answer:

--- We did have **DVC** in our project; since we were working with time series data more specifically with index data, it was especially useful
since for our system to work we had to update the training data every day as the stock price changes constantly. 
Unfortunately, due to lack of time, we were not able to implement automatic subsystem which pull data everyday; however, **DVC** would be 
perfect for this. Further steps included to achieve this would be: using the new **DVC** data, pull data to the trainer docker image to 
re-train the model; and use newest data to re-predict how our model performs.
In this way, we would constantly have the newest information on our portfolio performance, and recommendation for all possible changes needed. ---

### Question 11

> **Discuss you continues integration setup. What kind of CI are you running (unittesting, linting, etc.)? Do you test**
> **multiple operating systems, python version etc. Do you make use of caching? Feel free to insert a link to one of**
> **your github actions workflow.**
>
> Answer length: 200-300 words.
>
> Example:
> *We have organized our CI into 3 separate files: one for doing ..., one for running ... testing and one for running*
> *... . In particular for our ..., we used ... .An example of a triggered workflow can be seen here: <weblink>*
>
> Answer:
>
--- The CI was setup in a single file through **GitHub Actions**. The CI pipeline is triggered on every push and pull requests event to the main 
branch; tests are run only on the latest version of Ubuntu since we are running everything within docker images; the pipeline uses **Python 3.
10** version to accommodate all the dependencies. They are installed via `requirements.txt` in the portfolio directory. We had some problems 
with `skfolio` since there is no image for this library (as it is completely new v0.9), thus we had to install it directly from GitHub repo; 
we made use of `—no-cache-dir` to prevent pip from caching packages. **DVC** is installed and data is pulled for the tests from Google Cloud 
Storage (GCS) bucket. Unit tests are all developed and ran using **pytest**. *
The CI pipeline does not include linting, testing on multiple operating system and Python versions. We are not using caching as the build 
process was getting an error (same with mounting). With mounting, BuildKit which enhances the speed of builds was not enabled in Google Cloud,
so this also had to be removed. 
Build : [Link to Build](https://github.com/matijasipek/MLOps_PortfolioOptimization/actions/runs/7541775834/job/20529189656)
One of the main issues we had was pulling the data from the **DVC**; first our approach was using a service key which connected our GitHub 
repo with but this resulted in `Anonymous caller does not have storage.objects.list access` to the Google Cloud Storage bucket, no matter 
which permissions were given to the object as can be seen from 
[Link to Issue](https://github.com/matijasipek/MLOps_PortfolioOptimization/actions/runs/7502864007/job/20426370496). Unfortunately, to make it work, I gave the full public access permission to the bucket. ---

## Running code and tracking experiments

> In the following section we are interested in learning more about the experimental setup for running your code and
> especially the reproducibility of your experiments.

### Question 12

> **How did you configure experiments? Did you make use of config files? Explain with coding examples of how you would**
> **run a experiment.**
>
> Answer length: 50-100 words.
>
> Example:
> *We used a simple argparser, that worked in the following way: python my_script.py --lr 1e-3 --batch_size 25*
>
> Answer:

--- The hyperparameters are by default loaded from the configuration file src/config/params.yaml, when training the model. The configuration file (.yaml) contains the evaluation metric, n_jobs(computation is dispatched on all machine's CPUs), walk forward train and test size. The configuration file is passed to the wandb.init() function, through which hyperparameters are loaded into the training script, together with w&b project name and entity. When using the src/models/predict_model.py, a simple argparser is used to give the input string to be translated along with the checkpoint file containing the trained model weights. ---

### Question 13

> **Reproducibility of experiments are important. Related to the last question, how did you secure that no information**
> **is lost when running experiments and that your experiments are reproducible?**
>
> Answer length: 100-200 words.
>
> Example:
> *We made use of config files. Whenever an experiment is run the following happens: ... . To reproduce an experiment*
> *one would have to do ...*
>
> Answer:

--- When loading the configuration file the hyperparameters of the model are set to the default values provided in the file. Then, the user can track which parameters are used to train the model. The reproduciblity of results is ensured, since the data is static and experiments don't include any random state. Hereby, the experiment result will always be the same, which can also be confirmed when observing results of different runs displayed in chart within w&b project. Furthermore docker images are created, to ensure that model can be run on any machine.  ---

### Question 14

> **Upload 1 to 3 screenshots that show the experiments that you have done in W&B (or another experiment tracking**
> **service of your choice). This may include loss graphs, logged images, hyperparameter sweeps etc. You can take**
> **inspiration from [this figure](figures/wandb.png). Explain what metrics you are tracking and why they are**
> **important.**
>
> Answer length: 200-300 words + 1 to 3 screenshots.
>
> Example:
> *As seen in the first image when have tracked ... and ... which both inform us about ... in our experiments.*
> *As seen in the second image we are also tracking ... and ...*
>
> Answer:

--- The first figure tracks the value of Calmar Ratio for the selected model. As seen in the **[figure](figures/Q14_W&B-1.png)**, all the runs have the same Calmar Ratio throughout the training, since the data does not change between the runs.

The second **[figure](figures/Q14_W&B%20-2.png)** shows the highest obtained Calmar Ratio, which will also not change, as the data is static.

The **[table](figures/Q14.jpg)** displays the cumulative returns (daily) over period between 2013-2023.---

### Question 15

> **Docker is an important tool for creating containerized applications. Explain how you used docker in your**
> **experiments? Include how you would run your docker images and include a link to one of your docker files.**
>
> Answer length: 100-200 words.
>
> Example:
> *For our project we developed several images: one for training, inference and deployment. For example to run the*
> *training docker image: `docker run trainer:latest lr=1e-3 batch_size=64`. Link to docker file: <weblink>*
>
> Answer:

--- Docker was utilized to execute the model's prediction script in a controlled environment, where a Docker image was built using a Dockerfile that outlined all the necessary dependencies and code. The image could then be run with the command: `docker run -it --rm -v "C:\path_to_data:/data" image-test /data/processed/X_test.csv`, where `image-test` is the name of the Docker image, and `C:\path_to_data` is the path to the dataset on the host machine. This ensured that the `X_test.csv` file was used as an argument for the prediction script within the container. The Dockerfile for this image is available via [Link to Dockerfile](https://github.com/AndroCrunch/MLOps_PortfolioOptimization/blob/main/portfolio/trainer.dockerfile), showcasing the steps taken to set up the environment, install dependencies, and define the entry point for running the prediction script. ---

### Question 16

> **When running into bugs while trying to run your experiments, how did you perform debugging? Additionally, did you**
> **try to profile your code or do you think it is already perfect?**
>
> Answer length: 100-200 words.
>
> Example:
> *Debugging method was dependent on group member. Some just used ... and others used ... . We did a single profiling*
> *run of our main code at some point that showed ...*
>
> Answer:


--- When running the code locally, the built-in debugger in Visual Studio code was used. Additionally, simple print statements were added to code blocks, which was sufficient enough, as the code itself was not very complex.
The profiling was implemented through cProfile module, and visualized with SnakeViz. The profiling run was conducted on the train_model.py script and the results can be visible **[here](figures/Q16profiling.jpg)**. ---

## Working in the cloud

> In the following section we would like to know more about your experience when developing in the cloud.

### Question 17

> **List all the GCP services that you made use of in your project and shortly explain what each service does?**
>
> Answer length: 50-200 words.
>
> Example:
> *We used the following two services: Engine and Bucket. Engine is used for... and Bucket is used for...*
>
> *Answer:*

--- We used: Bucket, Artifact Registry, Cloud Build, Vertex AI and Cloud Run
Bucket : We set up our DVC in the bucket and connected it to our GitHub repo
Cloud Build: We are building and pushing our images in using this service
Artefact Registry: In the artifact registry, after building our images are being saved here
Vertex AI: We are creating custom jobs for each of our images (train and predict) and testing them with this service.
Cloud Run: Used for deploying containers in “production” version so that it can be called from user side via URL / API requests ---

### Question 18

> **The backbone of GCP is the Compute engine. Explained how you made use of this service and what type of VMs**
> **you used?**
>
> Answer length: 100-200 words.
>
> Example:
> *We used the compute engine to run our ... . We used instances with the following hardware: ... and we started the*
> *using a custom container: ...*
>
> Answer:

--- We used this for testing that our project works in an new environment, but also through CloudBuild, VertexAI and Cloud Run as they all use VMs
in the background. 
By using Cloud Build which uses VMs to build and push images, and then used compute engine VMs to run Vertex AI for our machine learning tasks
such that it runs jobs of containers and serves predictions. We used n1-standard-4 type VM, it has 4vCPUs and 15GB of memory, we used 1 
replica count. As I have Mac M2 CPU we had a big problem when building images since the architecture in the google cloud is different.
Further, if we had time to develop continuous new data integration with the compute engine, we could know the training and inference
time on specific hardware specifications. And, this process can be setup in parallel in background. ---

### Question 19

> **Insert 1-2 images of your GCP bucket, such that we can see what data you have stored in it.**
> **You can take inspiration from [this figure](figures/bucket.png).**
>
> Answer:

**[Bucket 1](figures/Q19%20-%20Bucket.png)**

**[Bucket 2](figures/Q19%20-%20Bucket%202.png)**


### Question 20

> **Upload one image of your GCP container registry, such that we can see the different images that you have stored.**
> **You can take inspiration from [this figure](figures/registry.png).**
>
> Answer:
>

**[Artifact Registry 1](figures/Q20%20-%20Artifact%20Registry%20.png)**

**[Artifact Registry 2](figures/Q20%20-%20Artifact%20Registry%202.png)**


### Question 21

> **Upload one image of your GCP cloud build history, so we can see the history of the images that have been build in**
> **your project. You can take inspiration from [this figure](figures/build.png).**
>
> Answer:
>

**[Build history](figures/Q21%20-%20Build.png)**


### Question 22

> **Did you manage to deploy your model, either in locally or cloud? If not, describe why. If yes, describe how and**
> **preferably how you invoke your deployed service?**
>
> Answer length: 100-200 words.
>
> Example:
> *For deployment we wrapped our model into application using ... . We first tried locally serving the model, which*
> *worked. Afterwards we deployed it in the cloud, using ... . To invoke the service an user would call*
> *`curl -X POST -F "file=@file.json"<weburl>`*
>
> Answer:

--- We successfully implemented local monitoring of our deployed model using FastAPI, which tracks performance metrics and generates alerts for quick issue resolution. The sucessful run can be visible **[here](figures/Q22fastapi.jpg)**:

However, we haven't extended this monitoring to Google Cloud, a crucial step for scalability and reliability in a distributed environment, due time constraint. ---

### Question 23

> **Did you manage to implement monitoring of your deployed model? If yes, explain how it works. If not, explain how**
> **monitoring would help the longevity of your application.**
>
> Answer length: 100-200 words.
>
> Example:
> *We did not manage to implement monitoring. We would like to have monitoring implemented such that over time we could*
> *measure ... and ... that would inform us about this ... behaviour of our application.*
>
> Answer:

**[Metrics](figures/Q23%20-%20Metrics.png)**

--- Yes, we successfully implemented model monitoring via Prometheus, which runs locally alongside our application.
You should run the predictor.dockerfile locally which is then going to give you the localhost url where you'll be
able to see the metrics update in realtime as docker image is being ran. The metrics displayed in the screenshot
indicate that Prometheus is actively scraping and recording data. Our configuration tracks several important indicators:
- Memory Usage: Measures the virtual and resident memory of the application to prevent leaks and optimize resource allocation.
- CPU Utilization: Monitors the CPU time consumed by the application, enabling us to assess and improve processing efficiency.
- File Descriptors: Keeps count of open file descriptors to avoid reaching system limits that could lead to failures.
- Model-Specific Metrics:
   - Total Predictions Made: Shows us the demand on the model and its throughput.
   - Prediction Errors: Used for detecting anomalies in the model's performance which might indicate data drift or model degradation.
   - Model Load Time: Helps ensure the model is loaded efficiently and remains responsive to prediction requests. ---

### Question 24

> **How many credits did you end up using during the project and what service was most expensive?**
>
> Answer length: 25-100 words.
>
> Example:
> *Group member 1 used ..., Group member 2 used ..., in total ... credits was spend during development. The service*
> *costing the most was ... due to ...*
>
> Answer:

---  S222736 - google cloud  32$, in GitHub action I had 0 minutes which is unclear to me as I had more than 40 calls push/pull with CI
- Artifact registry most expensive wth 28.79$
S222660 - google cloud 0$ since monitoring was ran locally, in GitHub action I had 0 also unsure as to why.
S204704 - google cloud 0$, W&B 0$ desite having more that 100 runs, GitHub Actions 0$, which is also unexplanable. ---

## Overall discussion of project

> In the following section we would like you to think about the general structure of your project.

### Question 25

> **Include a figure that describes the overall architecture of your system and what services that you make use of.**
> **You can take inspiration from [this figure](figures/overview.png). Additionally in your own words, explain the**
> **overall steps in figure.**
>
> Answer length: 200-400 words
>
> Example:
>
> *The starting point of the diagram is our local setup, where we integrated ... and ... and ... into our code.*
> *Whenever we commit code and puch to github, it auto triggers ... and ... . From there the diagram shows ...*
>
> Answer:

**[Architecture](figures/Q25%20-%20Architecture.png)**

--- First off all we have the profiler which is running on train_model.py and shows us performance of the code,
and cookiecuter that encompass the whole project. When training the model, the
first entry point is the W&B. It shows us the relevant
model parameters which can be seen in set up charts.
All of our data is stored in a google bucket via DVC
that is being referenced through GitHub. Every time
we make a change to the code i.e commit/push, we trigger
GitHub Actions. This triggers the unittesting module and
if it's sucesessfull it will trigger the google cloud build.
Through the build process we monitor it using Prometheus
and when it finishes it creates a docker image which is
saved in the Artifact Registry. Here we have several different images: The training image, the predict image
and the prometheus monitoring image. Then we are using VertexAI
to grab the models from the artifact registry and then do
inference. Unfortunantly we weren't able to deploy the model
in the cloud, but when testing locally we were able to get
metric results. In the local version we have a designated folder called visualisations which saves the final
results in addition to printing. We do however have everything set up
including a prometheus sidecontainer, which would store
this metrics. ---



### Question 26

> **Discuss the overall struggles of the project. Where did you spend most time and what did you do to overcome these**
> **challenges?**
>
> Answer length: 200-400 words.
>
> Example:
> *The biggest challenges in the project was using ... tool to do ... . The reason for this was ...*
>
> Answer:

--- During implementation of GitHub Actions Cil most of the time we lost was on the connection.
between the DVC and Github. First we tried with creating a service key in the bucket and adding it to 
the GH secrets, but it did not work; so we had to give public permission to the bucket and we were
able to pass the tests in the CI. Next, during the build phase, we had a problem with the architecture
due to the difference between the architecture of Mac M2 and the Cloud Build system, and it was
fixed after giving it explicit architecture on which to build on (--platform=linux/amd64).
Unfortunately, the Cloud Run was not able to deploy the model and we could not make it work.
Due to not being able to make the cloud run work, it left us with only being able to setup local
monitoring which was sucsesfull. However this isn't really optimal and we believe that given more
more time we could've made it work with clour run and we have even made a setup using a prometheus
image conteiner that was supposed to be used for scrapping and storing the metrics in an image so
we can have a track history of the apps metrics while it was running. The challenge with W&B stemmed 
from how the code was structured: the grid search was designed in a way that it returns only the best 
performing model out of four. As a result, only this top-performing model's metrics were monitored 
and logged, limiting visibility into the performance of the other three models during the grid search 
process. This made it difficult to analyze and compare the performance of all models side by side, 
together with different metrics. ---



### Question 27

> **State the individual contributions of each team member. This is required information from DTU, because we need to**
> **make sure all members contributed actively to the project**
>
> Answer length: 50-200 words.
>
> Example:
> *Student sXXXXXX was in charge of developing of setting up the initial cookie cutter project and developing of the*
> *docker containers for training our applications.*
> *Student sXXXXXX was in charge of training our models in the cloud and deploying them afterwards.*
> *All members contributed to code by...*
>
> Answer:


--- Student s222736 did git, data version control, docker, unit testing, cloud
Student s204704 did W&B, cookiecuter, profiler, fastAPI
Studnet s222660 did system monitoring, docker, cloud
All members contributed equally when running into errors or issues that they themselfs couldn't resolve.
For example like when running docker images, git actions, general environment issues and setups etc. ---
