<?php
include "connection.php";
$sql = "insert into student values('keval','Rajkot')";
if(mysqli_query($con,$sql)){
    echo "Record inserted";
}
else{
    echo "Rcord not inserted".mysqli_errno($con);
}
?>