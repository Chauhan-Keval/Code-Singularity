<?php
include "connection.php";
$sql="update student set city='surat' where city='rajkot'";
if(mysqli_query($con,$sql)){
    echo "Record updated";
}
else{
    echo "Record not updated".mysqli_error($con);
}
?>