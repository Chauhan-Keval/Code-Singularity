<?php
Session_start();
$user = $_GET['uid'];
$pwd = $_GET['pwd'];
$_SESSION['user']=$_GET['uid'];
if($user == 'keval' && $pwd == '123'){
    header('Location: sedemo2.php');
}
else{
    echo "Stay here";
}
?>