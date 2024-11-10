# Employee_management_system

### Overview
A basic backend sturcture of employee management system written in Flask and Mysql. This project is still in development. 
### Instruction
You can use curl command or Postman to test these API calls. Here are some curl commands for each of the API call. 

##### For inserting employee information:
<code> curl -X POST 127.0.0.1:5000/createEmployee -H "Content-Type: application/json" -d "{\"name\":\"<name>\",\"gender\":\"<gender>\",\"age\":<age>,\"email\":\"<username@example.com>\"}"</code>
Please replace each parameter values by the following:
- name: String type
- gender: male, m, female, f, not case sensitive
- age: integer value
- email: must have @ symbol. Before the symbol is the collection of alphabets, numbers, and hyphens (the first character must be alphabets), and after the symbol must include a collection of alphabets and numbers and ends with .com. 

##### For deleting employee information:
<code> curl -X DELETE 127.0.0.1:5000/deleteEmployee -H "Content-Type: application/json" -d "{\"employee\":\"<username@example.com>\"}"</code>


##### For showing all employee information:
<code> curl -X GET 127.0.0.1:5000/employee </code>