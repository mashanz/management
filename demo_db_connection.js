var mysql = require('mysql');

var con = mysql.createConnection({
  host: "127.0.0.1",
  user: "root",
  password: "op3nk3y",
  database: "prima"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");

  // CREATE DATABASE
  // con.query("CREATE DATABASE prima", function (err, result) {
  //   if (err) throw err;
  //   console.log("Database created");
  // });

  // CREATE TABLE
  // var sql = "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))";
  // con.query(sql, function (err, result) {
  //   if (err) throw err;
  //   console.log("Table created");
  // });

  // INSERT INTO TABLE
  var sql = "INSERT INTO customers (name, address) VALUES ('Company Inc', 'Highway 37')";
  con.query(sql, function (err, result) {
    if (err) throw err;
    console.log("1 record inserted");
  });

});
