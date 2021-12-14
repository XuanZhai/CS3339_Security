
<?php

error_reporting(E_ALL);
ini_set('display_errors', 1);

$host="localhost"; // Host name
$username="username"; // Mysql username
$password="my_password"; // Mysql password
$db_name="test"; // Database name
$tbl_name="members"; // Table name

// Connect to server and select databse.
$link = mysqli_connect("$host", $username, $password, "test");


// Define $myusername and $mypassword
$myusername=$_POST['myusername'];
$mypassword=$_POST['mypassword'];


//$sql="SELECT * FROM $tbl_name WHERE username='$myusername' and password=" . $mypassword;


$stmt = $link->prepare("SELECT * FROM $tbl_name WHERE username= ? and password= ?");
$stmt->bind_param("ss",$_POST['myusername'],$_POST['mypassword']);
$stmt->execute();


$sresult = $stmt->get_result();
$sql = $sresult->fetch_assoc();


//echo "SQL QUERY: " .$sql;
echo "</br> \r\n";


if($sql){

	header("location:login_success.php");
}
else {
	echo "Wrong Username or Password";
}





?>


