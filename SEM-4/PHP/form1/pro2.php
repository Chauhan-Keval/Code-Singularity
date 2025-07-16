<?php
Session_start();
$user = $_GET['uid'];
$pwd = $_GET['id'];
$SESSION = $_GET['user'];
if($user=='keval' && $pwd=='123'){
    header('Location :pro3.php');
}else{
    echo "Stay here !";
}
?>