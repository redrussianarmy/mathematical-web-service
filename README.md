# Mathematical Web Service

This is a web service which calculates and provides results for the following algorithms via a REST API:

- The n:th Fibonacci number F(n) with the value of n provided by the user.
- The Ackermann function A(m,n) with values of m and n provided by the user.
- The factorial n! of a non-negative integer n provided by the user.

---

- [Tasks](#tasks)
  - [Environment Preparation](#environment-preparation)
  - [Unit Tests and Coverage](#unit-tests-and-coverage)
- [Launch](#launch)
  - [Run Server](#run-server)
  - [Run Unit Tests](#run-unit-tests)
- [Query Examples](#query-examples)
  - [Fibonacci Algorithm](#fibonacci-algorithm)
  - [Ackermann Algorithm](#ackermann-algorithm)
  - [Factorial Algorithm](#factorial-algorithm)
- [How to Deploy the Application to AWS Elastic Beanstalk](#how-to-deploy-the-application-to-aws-elastic-beanstalk)

---

## Tasks

If you are using VSCode, the tasks config file was created in the **.vscode** file. When you press ```CTRL+SHIFT+B```, you will see the following options.

- ### Environment Preparation

  The necessary environment can be created by selecting the ```Prepare Environment``` option.

  ![Untitled](https://user-images.githubusercontent.com/24498747/160241473-4c582291-1cb8-4cbb-99f3-03ec6c1c9715.png)


- ### Unit Tests and Coverage

  A report that shows how much of the written code is covered by the unit tests can be created by selecting the ```Unit Tests and Coverage``` option.

  ![image](https://user-images.githubusercontent.com/24498747/160241801-88889260-7d83-443e-a0cc-113ea8cfc3e4.png)
  
  When the task is completed, you can find coverage rates by opening ```index.html``` in the ```coverage-report``` folder.
  
  <img src="https://user-images.githubusercontent.com/24498747/160244757-454c962f-acab-4f31-88c7-2ef3e9bcffb4.png" height="500"/> 
  <img src="https://user-images.githubusercontent.com/24498747/160245049-fb8e12c6-b825-4fd1-bd63-eda5dbe35845.png" width="600"/> 

---

## Launch

- ### Run Server

  - **[OPT1]** If you have docker installed on your computer, run the following commands in order.
    ```
    docker build -t web-service:1.0 .
    ```
    
    ```
    docker run -p 8000:8000 web-service:1.0
    ```

  - **[OPT2]** If you are using VSCode, the application can be started if you select the ```Run Web Service``` option from the ```Run and Debug``` menu.

    ![image](https://user-images.githubusercontent.com/24498747/160242849-c7c03010-c008-40f3-bd9a-8534cd350ffb.png)

  - **[OPT3]** If you are going to run the application from the terminal, you can type the following command. Make sure you are on the same path as the manage.py file.

    ```
    py manage.py runserver
    ```
  
- ### Run Unit Tests

  - If you are using VSCode, the unit tests can be run if you select the ```Run UT Web Service``` option from the ```Run and Debug``` menu.

    ![image](https://user-images.githubusercontent.com/24498747/160243119-a15ef52c-cbed-4841-87aa-54aa50ff3b9e.png)

  - If you are going to run the unit tests from the terminal, you can type the following command. Make sure you are on the same path as the manage.py file.

    ```
    py manage.py test algorithms.tests
    ```

---

## Query Examples

- ### Fibonacci Algorithm

    **GET** query string request:

      http://127.0.0.1:8000/api/fibonacci/?n=6

    Response:

      {
        "result": 8
      }
    

- ### Ackermann Algorithm

    **GET** query string request:

      http://127.0.0.1:8000/api/ackermann/?m=1&n=3

    Response:

      {
        "result": 5
      }
    

- ### Factorial Algorithm

    **GET** query string request:

      http://127.0.0.1:8000/api/factorial/?n=6

    Response:

      {
        "result": 720
      }
    
---

## How to Deploy the Application to AWS Elastic Beanstalk

You can reach the official article on how to deploy this application to Elastic Beanstalk by clicking the link below.

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html#python-django-configure-for-eb