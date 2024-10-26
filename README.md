# Employee_management_system

<h1>Instruction</h1>

<p>
  Here are some curl commands for testing the api calls
  
  For inserting employee info to the database: <br>
  <code> curl -X POST 127.0.0.1:5000/create_employee -H "Content-Type: application/json" -d "{\"name\":\"<name>\",\"gender\":\"<gender>\",\"age\":<age>,\"email\":\"<username@example.com>\",\"date\":\"<date>\"}"</code>

  For display employee info in the database by their email:<br>
  <code>curl -X POST 127.0.0.1:5000/dete_employee -H "Content-Type: application/json" -d "{\"email\":\"<username@example.com>\"}"
  </code>
  or just<br>
  <code>curl -X POST 127.0.0.1:5000/dete_employee -H "Content-Type: application/json" 
  </code>

  To sucessfully insert employee info data to the database, please follow by the format: {name (String), gender (male. female), age (number), email ([A-Za-z0-9\.]+@[A-Za-z0-9].com), and date (String)}

  Send help please :(
</p>
