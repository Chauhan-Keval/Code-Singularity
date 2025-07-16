<?php
include "connection.php";
$sql = "create database E2";
if(mysqli_query($con,$sql)){
    echo "Database Created";
}
else{
    echo "Database not created".mysqli_error($con);
}
mysqli_selected_db($con,"E2");
echo "Database Selected";
?>