<?php
include "connection.php";
$sql="delete from student where name='keval'";
if(mysqli_query($con,$sql)){
    echo "Record Deleted";
}
else{
    echo "Record not Deleted".mysqli_error($con);
}
?>