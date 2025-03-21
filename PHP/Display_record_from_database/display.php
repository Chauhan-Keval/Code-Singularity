<?php
include "connection.php";
$sql ="select * from pro1";
$result = mysqli_query($con,$sql);
while($row=mysqli_fetch_array($result)){
    echo $row['Rollno']."-".$row['Name']."<br>";
}
?>