<?php
$a=$_GET['i1'];
$b=$_GET['i2'];
if(isset($_GET['b1'])){
    echo "Add : ".( $a + $b );
}
if(isset($_GET['b2'])){
    echo "Sub : ".( $a - $b );
}
if(isset($_GET['b3'])){
    echo "Mul : ".( $a * $b );
}
if(isset($_GET['b4'])){
    echo "Div : ".( $a / $b );
}
?>