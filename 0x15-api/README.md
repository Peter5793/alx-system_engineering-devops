# API

## General
* What Bash scripting should not be used for
* What is an API
* What is a REST API
* What are microservices
* What is the CSV format
* What is the JSON format
* Pythonic Package and module name style
* Pythonic Class name style
* Pythonic Variable name style
* Pythonic Function name style
* Pythonic Constant name style
* Significance of CapWords or CamelCase in Python

## Task
Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.

Requirements:

* You must use urllib or requests module
* The script must accept an integer as a parameter, which is the employee ID
* The script must display on the standard output the employee TODO list progress in this exact format:
	* First line: ```Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):```
		* ```EMPLOYEE_NAME:``` name of the employee
		* NUMBER_OF_DONE_TASKS: number of completed tasks
		* TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of 			completed and non-completed tasks
	* Second and N next lines display the title of completed tasks: Tab TASK_TITLE (with 1 tabulation + 1 space before)

Example
```
ubuntu$ python3 0-gather_data_from_an_API.py 2
Employee Ervin Howell is done with tasks(8/20):
     distinctio vitae autem nihil ut molestias quo
     voluptas quo tenetur perspiciatis explicabo natus
     aliquam aut quasi
     veritatis pariatur delectus
     nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis
     repellendus veritatis molestias dicta incidunt
     excepturi deleniti adipisci voluptatem et neque optio illum ad
     totam atque quo nesciunt
@ubuntu$ python3 0-gather_data_from_an_API.py 4
Employee Patricia Lebsack is done with tasks(6/20):
     odit optio omnis qui sunt
     doloremque aut dolores quidem fuga qui nulla
     sint amet quia totam corporis qui exercitationem commodi
     sequi dolorem sed
     eum ipsa maxime ut
     tempore molestias dolores rerum sequi voluptates ipsum consequatur
@ubuntu$
