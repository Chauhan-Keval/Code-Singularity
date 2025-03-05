<?php
Session_start();
echo "You have been logged out".$_SESSION['user'];
session_destroy();
?>