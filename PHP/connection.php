<?php
$con=mysqli_connect("localhost","root","","keval");
if(!$con)
{
    echo "Database not connected".mysqli_connect_error();
}
else
{
    echo "Database connected";
}
?>