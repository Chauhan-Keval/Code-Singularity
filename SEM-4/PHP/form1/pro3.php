<?php
Session_start();
echo "Welcome to our site ".$_SESSION['user'];
echo "<br><a href='sedemo3.php'>Logout</a>";
?>